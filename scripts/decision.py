#!/usr/bin/env python3
"""
decision.py — SystemOne 決策模型客戶端（Jev 主力 + Clef 備援）
=============================================================
支援以 TypeSafe AI 的 Jev 決策模型為主力（極速、低延遲），
並在網路異常、額度超額或服務離線時，自動無縫 Fallback 至自 Host 的 Clef-Flash。

特性：
- 零第三方依賴（純 Python 標準函式庫 urllib / concurrent.futures）
- 支援多執行緒並行推論（ThreadPoolExecutor）
- 結構化題目組定義（針對具身智能與通用 AI 定義專屬 Prompt）
- 依據決策機率與新穎度自動重新計算優先級（Reranking）
"""

from __future__ import annotations

import json
import logging
import os
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

logger = logging.getLogger("decision")
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

DEFAULT_JEV_URL = "https://api.typesafe.ai/v1/systemone"
DEFAULT_JEV_MODEL = "jev-latest"
DEFAULT_CLEF_URL = "https://clef.aiurl.tw/v1/systemone"
DEFAULT_CLEF_MODEL = "clef-flash"
USER_AGENT = "DailyPaperScout/1.0 (github.com/tbdavid2019/paper-daily)"


def get_topic_questions(topic_name: str) -> dict[str, Any]:
    """針對不同主題產出最適切的決策題目組。"""
    if topic_name == "embodied_ai":
        return {
            "is_embodied_ai": {
                "type": "noul",
                "instructions": "判斷這篇論文是否直接涉及具身智能 (Embodied AI)、機器人實體控制/操作/導航，而非純文字或非實體虛擬任務？",
            },
            "primary_category": {
                "type": "choice",
                "instructions": "將該研究歸納至最適切的核心技術子領域",
                "criteria": {
                    "robot_manipulation": "機械手臂操控、靈巧手、物體抓取與裝配、接觸任務",
                    "vla_foundation_model": "視覺-語言-動作 (VLA) 多模態模型、通用機器人策略、具身大腦",
                    "autonomous_driving_navigation": "自動駕駛、移動機器人導航、路徑規劃與避障",
                    "locomotion_humanoid": "雙足人形、四足足式機器人步態平衡與動態控制",
                    "simulation_sim2real": "物理模擬器、Domain Randomization、模擬向真實世界遷移",
                    "tactile_sensing": "觸覺感知、多模態感官融合、本體感受",
                    "non_embodied": "純語言模型、純 2D 電腦視覺、機器翻譯、非具身任務",
                },
            },
            "impact_and_novelty": {
                "type": "score",
                "instructions": "評估該論文的新穎性與架構突破程度",
                "criteria": [
                    "0: 漸進式小幅改進、既有技術應用或調參",
                    "1: 具備扎實實驗與明確創新概念的高品質研究",
                    "2: 提出全新架構範式、里程碑突破",
                ],
            },
            "recommendation": {
                "type": "choice",
                "instructions": "對具身智能研究者的閱讀優先級推薦",
                "criteria": {
                    "must_read": "必讀亮點論文，方法新穎且影響重大",
                    "highly_relevant": "高度相關，具體細節值得參考",
                    "interesting": "視角有趣但關聯較間接或小眾",
                    "skip": "與實體具身智能關聯弱或偏離核心主題",
                },
            },
        }

    # 通用 AI 題目組
    return {
        "is_relevant": {
            "type": "noul",
            "instructions": "判斷這篇論文是否對人工智慧前沿、基礎模型或機器學習具有高度實質相關性？",
        },
        "primary_category": {
            "type": "choice",
            "instructions": "將該研究歸納至最適切的領域",
            "criteria": {
                "foundation_models": "大語言模型、多模態基礎模型、預訓練與架構",
                "reasoning_alignment": "推理邏輯、RLHF/DPO、對齊、自我反思與思考",
                "agents_tool_use": "AI Agent、工具調用、工作流與自主執行系統",
                "vision_diffusion": "生成擴散模型、影像生成、多模態感知",
                "other": "理論、邊緣優化或其他次領域",
            },
        },
        "impact_and_novelty": {
            "type": "score",
            "instructions": "評估該論文的新穎性與架構突破程度",
            "criteria": [
                "0: 漸進式小幅改進、常規應用或調參",
                "1: 具備扎實實驗與明確創新概念的高品質研究",
                "2: 提出全新架構範式、里程碑突破",
            ],
        },
        "recommendation": {
            "type": "choice",
            "instructions": "對 AI 研究者的閱讀優先級推薦",
            "criteria": {
                "must_read": "必讀亮點論文，方法新穎且影響重大",
                "highly_relevant": "高度相關，具體細節值得參考",
                "interesting": "視角有趣但關聯較間接或小眾",
                "skip": "品質平庸或偏離核心研究興趣",
            },
        },
    }


class DecisionClient:
    """雙軌決策模型客戶端（Jev 主力 + Clef 備援）。"""

    def __init__(
        self,
        jev_api_key: str | None = None,
        jev_url: str = DEFAULT_JEV_URL,
        jev_model: str = DEFAULT_JEV_MODEL,
        clef_url: str = DEFAULT_CLEF_URL,
        clef_model: str = DEFAULT_CLEF_MODEL,
        timeout: float = 12.0,
        clef_timeout: float = 60.0,
    ):
        self.jev_api_key = jev_api_key or os.environ.get("JEV_API_KEY", "").strip()
        self.jev_url = os.environ.get("JEV_BASE_URL", "").strip() or jev_url
        self.jev_model = os.environ.get("JEV_MODEL", "").strip() or jev_model
        self.clef_url = os.environ.get("CLEF_BASE_URL", "").strip() or clef_url
        self.clef_model = os.environ.get("CLEF_MODEL", "").strip() or clef_model
        self.timeout = float(os.environ.get("DECISION_TIMEOUT", timeout))
        self.clef_timeout = float(os.environ.get("DECISION_CLEF_TIMEOUT", clef_timeout))

    @property
    def is_available(self) -> bool:
        """只要有 Jev 金鑰或 Clef 端點任一可用即可。"""
        return bool(self.jev_api_key or self.clef_url)

    def _call_systemone(
        self,
        url: str,
        model: str,
        state: str,
        questions: dict[str, Any],
        headers: dict[str, str],
        timeout: float,
    ) -> dict[str, Any]:
        payload = json.dumps(
            {
                "model": model,
                "state": state,
                "questions": questions,
            },
            ensure_ascii=False,
        ).encode("utf-8")

        req_headers = {
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        }
        req_headers.update(headers)

        req = urllib.request.Request(url, data=payload, headers=req_headers, method="POST")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if not isinstance(data, dict):
                raise ValueError(f"Expected dict response from {url}")
            return data

    def decide(self, state: str, questions: dict[str, Any]) -> dict[str, Any]:
        """執行單次決策判定，若 Jev 失敗則自動 fallback 至 Clef。"""
        # 1. 優先嘗試 Jev
        if self.jev_api_key:
            t0 = time.time()
            try:
                result = self._call_systemone(
                    url=self.jev_url,
                    model=self.jev_model,
                    state=state,
                    questions=questions,
                    headers={"Authorization": f"Bearer {self.jev_api_key}"},
                    timeout=self.timeout,
                )
                answers = result.get("answers", {})
                latency = (time.time() - t0) * 1000
                return {
                    "answers": answers,
                    "provider": "jev",
                    "model": result.get("model", self.jev_model),
                    "latency_ms": round(latency, 1),
                }
            except Exception as exc:
                logger.warning(
                    "Jev decision call failed (%s). Falling back to Clef endpoint %s...",
                    exc,
                    self.clef_url,
                )

        # 2. Fallback 至 Clef
        if self.clef_url:
            t0 = time.time()
            try:
                result = self._call_systemone(
                    url=self.clef_url,
                    model=self.clef_model,
                    state=state,
                    questions=questions,
                    headers={},
                    timeout=self.clef_timeout,
                )
                answers = result.get("answers", {})
                latency = (time.time() - t0) * 1000
                return {
                    "answers": answers,
                    "provider": "clef",
                    "model": result.get("model", self.clef_model),
                    "latency_ms": round(latency, 1),
                }
            except Exception as exc:
                logger.error("Clef decision fallback also failed (%s)", exc)
                raise RuntimeError(f"All decision model backends failed (Clef error: {exc})") from exc

        raise RuntimeError("No decision model configured (neither JEV_API_KEY nor CLEF_BASE_URL available)")


def format_paper_state(paper: dict[str, Any]) -> str:
    """將論文轉換為 SystemOne state 字串。"""
    title = str(paper.get("title", "")).strip()
    abstract = str(paper.get("abstract", "")).strip()
    authors = paper.get("authors", [])
    author_str = ", ".join(authors[:5]) if isinstance(authors, list) else str(authors)
    parts = [f"Title: {title}"]
    if author_str:
        parts.append(f"Authors: {author_str}")
    if abstract:
        parts.append(f"Abstract: {abstract[:2500]}")
    return "\n\n".join(parts)


def parse_decision_summary(answers: dict[str, Any], provider: str) -> dict[str, Any]:
    """提煉精簡決策指標，方便存入論文 metadata。"""
    summary: dict[str, Any] = {"provider": provider}

    # 相關度 (noul)
    noul_ans = answers.get("is_embodied_ai") or answers.get("is_relevant")
    if isinstance(noul_ans, dict) and "noul" in noul_ans:
        summary["relevance_prob"] = round(float(noul_ans["noul"]), 4)

    # 主領域 (choice)
    cat_ans = answers.get("primary_category")
    if isinstance(cat_ans, dict) and "choice" in cat_ans:
        summary["primary_category"] = cat_ans["choice"]
        summary["category_confidence"] = round(float(cat_ans.get("confidence", 0)), 3)

    # 突破度評分 (score)
    score_ans = answers.get("impact_and_novelty")
    if isinstance(score_ans, dict) and "score" in score_ans:
        summary["novelty_score"] = round(float(score_ans["score"]), 3)

    # 推薦等級 (choice)
    rec_ans = answers.get("recommendation")
    if isinstance(rec_ans, dict) and "choice" in rec_ans:
        summary["recommendation"] = rec_ans["choice"]

    return summary


def calculate_decision_score(decision: dict[str, Any]) -> float:
    """依據決策結果計算單一量化分數 (0.0 ~ 100.0)，用於重排序。"""
    if not decision:
        return 0.0

    # 基礎分：相關度 (0 ~ 40 分)
    rel_prob = float(decision.get("relevance_prob", 0.5))
    base_score = rel_prob * 40.0

    # 突破度 (0 ~ 30 分，score 範圍通常 0 ~ 2)
    novelty = float(decision.get("novelty_score", 0.0))
    novelty_score = min(30.0, novelty * 15.0)

    # 推薦權重 (0 ~ 30 分)
    rec = decision.get("recommendation", "interesting")
    rec_weights = {
        "must_read": 30.0,
        "highly_relevant": 20.0,
        "interesting": 10.0,
        "skip": -30.0,
    }
    rec_bonus = rec_weights.get(rec, 5.0)

    # 類別懲罰（若分類為 non_embodied 則大幅扣分）
    if decision.get("primary_category") in ("non_embodied", "other_irrelevant"):
        return max(0.0, base_score * 0.1)

    return max(0.0, min(100.0, base_score + novelty_score + rec_bonus))


def evaluate_papers(
    papers: list[dict[str, Any]],
    topic_name: str = "embodied_ai",
    client: DecisionClient | None = None,
    max_workers: int | None = None,
    candidate_limit: int = 35,
) -> list[dict[str, Any]]:
    """並行評估一組論文，並將決策結果附加至各 paper 物件。

    回傳附加了 `decision` 與 `decision_score` 的論文列表。
    """
    if client is None:
        client = DecisionClient()

    if not client.is_available:
        logger.info("Decision client is not configured; skipping decision evaluation.")
        return papers

    questions = get_topic_questions(topic_name)
    eval_candidates = papers[:candidate_limit]
    remaining = papers[candidate_limit:]

    # 如果走 Jev 則可開多個 worker 並行加速；若走 Clef（自 Host CPU），預設以 1~2 worker 避免機器過載
    if max_workers is None:
        max_workers = 4 if client.jev_api_key else 1

    logger.info(
        "Evaluating %d candidate papers with Decision Model (topic=%s, workers=%d)...",
        len(eval_candidates),
        topic_name,
        max_workers,
    )

    def _eval_one(paper: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        state = format_paper_state(paper)
        try:
            res = client.decide(state, questions)
            summary = parse_decision_summary(res.get("answers", {}), res.get("provider", "unknown"))
            summary["latency_ms"] = res.get("latency_ms")
            summary["model"] = res.get("model")
            return paper, summary
        except Exception as err:
            logger.warning("Failed to evaluate paper '%s': %s", paper.get("id"), err)
            return paper, None

    start_time = time.time()
    evaluated_papers: list[dict[str, Any]] = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {executor.submit(_eval_one, p): p for p in eval_candidates}
        for future in as_completed(future_map):
            paper, decision = future.result()
            if decision:
                paper["decision"] = decision
                paper["decision_score"] = calculate_decision_score(decision)
            evaluated_papers.append(paper)

    elapsed = time.time() - start_time
    logger.info("Completed decision evaluation for %d papers in %.2fs", len(evaluated_papers), elapsed)

    # 組合回到完整列表
    all_papers = evaluated_papers + remaining
    return all_papers


def rerank_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """根據決策分數與既有優先級重新排序論文。

    排序權重：
    1. decision_score (0~100)
    2. priority (爬蟲原始權重)
    3. keyword_hits
    4. published_at
    """
    def _rank_key(paper: dict[str, Any]) -> tuple[float, float, int, str]:
        dec_score = float(paper.get("decision_score", 0.0) or 0.0)
        prio = float(paper.get("priority", 0.0) or 0.0)
        kw = int(paper.get("keyword_hits", 0) or 0)
        pub = str(paper.get("published_at", "") or "")
        return (dec_score, prio, kw, pub)

    return sorted(papers, key=_rank_key, reverse=True)
