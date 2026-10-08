#!/usr/bin/env python3
"""
decision.py — SystemOne 決策模型客戶端（Jev 雲端 + Clef 主力 + Clef 備援）
=============================================================================
支援：
1. Jev 雲端推論（若配置 JEV_API_KEY，百毫秒級高速評估）
2. Clef 主力端點：https://clef.create360.ai/v1/systemone（高速邊緣推論）
3. Clef 備援端點：https://clef.aiurl.tw/v1/systemone（自 Host 實體保底備援）

特性：
- 零第三方依賴（純 Python 標準函式庫 urllib / concurrent.futures）
- 支援多執行緒並行推論（ThreadPoolExecutor）
- 自動控管 Token 長度，確保不超出伺服器 batch size / context 限制
- 三重容錯 Fallback 鏈路，保證管線高可用不中斷
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
DEFAULT_CLEF_URL = "https://clef.create360.ai/v1/systemone"
DEFAULT_CLEF_FALLBACK_URL = "https://clef.aiurl.tw/v1/systemone"
DEFAULT_CLEF_MODEL = "clef-flash"
USER_AGENT = "DailyPaperScout/1.0 (github.com/tbdavid2019/paper-daily)"


def get_topic_questions(topic_name: str) -> dict[str, Any]:
    """針對不同主題產出最適切且精簡的決策題目組。

    精簡題組確保在 clef.create360.ai (512 physical batch size) 內穩定執行，
    同時維持 Jev 與 Clef-Flash 高精度輸出。
    """
    if topic_name == "embodied_ai":
        return {
            "is_embodied_ai": {
                "type": "noul",
                "instructions": "Is this paper relevant to Embodied AI or physical robotics?",
            },
            "primary_category": {
                "type": "choice",
                "instructions": "Select the primary domain",
                "criteria": {
                    "robot_manipulation": "Robot manipulation, grasping, dexterity",
                    "vla_foundation_model": "VLA, robot foundation model",
                    "locomotion_humanoid": "Humanoid, quadruped, navigation",
                    "simulation_sim2real": "Simulation, sim-to-real",
                    "non_embodied": "Pure NLP, 2D vision, non-embodied",
                },
            },
            "impact_and_novelty": {
                "type": "score",
                "instructions": "Rate innovation level",
                "criteria": ["Incremental", "Notable", "Breakthrough"],
            },
        }

    # 通用 AI 題目組
    return {
        "is_relevant": {
            "type": "noul",
            "instructions": "Is this paper significant to general AI, foundation models, or machine learning?",
        },
        "primary_category": {
            "type": "choice",
            "instructions": "Select primary domain",
            "criteria": {
                "foundation_models": "LLM, multimodal foundation model",
                "reasoning_alignment": "Reasoning, RLHF, alignment",
                "agents_tool_use": "AI Agent, tool use, workflow",
                "vision_diffusion": "Diffusion models, generation",
                "other": "Theory, optimization, other",
            },
        },
        "impact_and_novelty": {
            "type": "score",
            "instructions": "Rate innovation level",
            "criteria": ["Incremental", "Notable", "Breakthrough"],
        },
    }


class DecisionClient:
    """決策模型客戶端（支援 Jev 雲端 + Clef 主力 clef.create360.ai + Clef 備援 clef.aiurl.tw）。"""

    def __init__(
        self,
        jev_api_key: str | None = None,
        jev_url: str = DEFAULT_JEV_URL,
        jev_model: str = DEFAULT_JEV_MODEL,
        clef_url: str = DEFAULT_CLEF_URL,
        clef_fallback_url: str = DEFAULT_CLEF_FALLBACK_URL,
        clef_model: str = DEFAULT_CLEF_MODEL,
        timeout: float = 12.0,
        clef_timeout: float = 15.0,
        clef_fallback_timeout: float = 60.0,
    ):
        self.jev_api_key = jev_api_key if jev_api_key is not None else os.environ.get("JEV_API_KEY", "").strip()
        self.jev_url = os.environ.get("JEV_BASE_URL", "").strip() or jev_url
        self.jev_model = os.environ.get("JEV_MODEL", "").strip() or jev_model
        self.clef_url = os.environ.get("CLEF_BASE_URL", "").strip() or clef_url
        self.clef_fallback_url = os.environ.get("CLEF_FALLBACK_URL", "").strip() or clef_fallback_url
        self.clef_model = os.environ.get("CLEF_MODEL", "").strip() or clef_model
        self.timeout = float(os.environ.get("DECISION_TIMEOUT", timeout))
        self.clef_timeout = float(os.environ.get("DECISION_CLEF_TIMEOUT", clef_timeout))
        self.clef_fallback_timeout = float(os.environ.get("DECISION_CLEF_FALLBACK_TIMEOUT", clef_fallback_timeout))

    @property
    def is_available(self) -> bool:
        """只要有 Jev 金鑰或 Clef 端點任一可用即可。"""
        return bool(self.jev_api_key or self.clef_url or self.clef_fallback_url)

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
        """執行單次決策判定：Jev (若有金鑰) ➔ Clef (clef.create360.ai) ➔ Clef Fallback (clef.aiurl.tw)。"""
        # 1. 優先嘗試 Jev（若提供 API Key）
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
                    "endpoint": self.jev_url,
                    "latency_ms": round(latency, 1),
                }
            except Exception as exc:
                logger.warning(
                    "Jev decision call failed (%s). Falling back to primary Clef endpoint %s...",
                    exc,
                    self.clef_url,
                )

        # 2. 嘗試 Clef 主力端點 (clef.create360.ai)
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
                    "endpoint": self.clef_url,
                    "latency_ms": round(latency, 1),
                }
            except Exception as exc:
                logger.warning(
                    "Primary Clef (%s) call failed (%s). Falling back to backup Clef (%s)...",
                    self.clef_url,
                    exc,
                    self.clef_fallback_url,
                )

        # 3. Fallback 至 Clef 備援端點 (clef.aiurl.tw)
        if self.clef_fallback_url:
            t0 = time.time()
            try:
                result = self._call_systemone(
                    url=self.clef_fallback_url,
                    model=self.clef_model,
                    state=state,
                    questions=questions,
                    headers={},
                    timeout=self.clef_fallback_timeout,
                )
                answers = result.get("answers", {})
                latency = (time.time() - t0) * 1000
                return {
                    "answers": answers,
                    "provider": "clef-fallback",
                    "model": result.get("model", self.clef_model),
                    "endpoint": self.clef_fallback_url,
                    "latency_ms": round(latency, 1),
                }
            except Exception as exc:
                logger.error("Clef backup fallback also failed (%s)", exc)
                raise RuntimeError(f"All decision model backends failed (Clef backup error: {exc})") from exc

        raise RuntimeError("No decision model configured (neither JEV_API_KEY nor CLEF endpoints available)")


def format_paper_state(paper: dict[str, Any], max_abstract_chars: int = 350) -> str:
    """將論文轉換為 SystemOne state 字串。

    限制摘要長度（預設 350 字元 / 約 70-80 tokens），
    確保整體輸入在 clef.create360.ai 512 batch size 限制下仍具備安全緩衝區。
    """
    title = str(paper.get("title", "")).strip()
    abstract = str(paper.get("abstract", "")).strip()
    authors = paper.get("authors", [])
    author_str = ", ".join(authors[:3]) if isinstance(authors, list) else str(authors)
    parts = [f"Title: {title}"]
    if author_str:
        parts.append(f"Authors: {author_str}")
    if abstract:
        parts.append(f"Abstract: {abstract[:max_abstract_chars]}")
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

    # 推薦等級 (若模型回傳則使用，若無則依相關度與新穎度客觀計算)
    rec_ans = answers.get("recommendation")
    if isinstance(rec_ans, dict) and "choice" in rec_ans:
        summary["recommendation"] = rec_ans["choice"]
    else:
        rel = summary.get("relevance_prob", 0.0)
        nov = summary.get("novelty_score", 0.0)
        cat = summary.get("primary_category", "")
        if cat in ("non_embodied", "other") or rel < 0.4:
            summary["recommendation"] = "skip"
        elif rel >= 0.88 and nov >= 1.2:
            summary["recommendation"] = "must_read"
        elif rel >= 0.70:
            summary["recommendation"] = "highly_relevant"
        else:
            summary["recommendation"] = "interesting"

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
    candidate_limit: int = 250,
    batch_size: int = 25,
) -> list[dict[str, Any]]:
    """分批並行評估一組論文，並將決策結果附加至各 paper 物件。

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

    if max_workers is None:
        max_workers = int(os.environ.get("DECISION_MAX_WORKERS", "5"))

    batch_size = int(os.environ.get("DECISION_BATCH_SIZE", str(batch_size)))
    num_batches = (len(eval_candidates) + batch_size - 1) // batch_size if eval_candidates else 0

    logger.info(
        "Evaluating %d candidate papers in %d batches (batch_size=%d, topic=%s, workers=%d)...",
        len(eval_candidates),
        num_batches,
        batch_size,
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
            summary["endpoint"] = res.get("endpoint")
            return paper, summary
        except Exception as err:
            logger.warning("Failed to evaluate paper '%s': %s", paper.get("id"), err)
            return paper, None

    start_time = time.time()
    evaluated_papers: list[dict[str, Any]] = []

    for b_idx in range(num_batches):
        batch = eval_candidates[b_idx * batch_size : (b_idx + 1) * batch_size]
        b_start = time.time()
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map = {executor.submit(_eval_one, p): p for p in batch}
            for future in as_completed(future_map):
                paper, decision = future.result()
                if decision:
                    paper["decision"] = decision
                    paper["decision_score"] = calculate_decision_score(decision)
                evaluated_papers.append(paper)
        b_elapsed = time.time() - b_start
        embodied_count = sum(
            1 for p in batch
            if p.get("decision", {}).get("primary_category") in (
                "robot_manipulation", "vla_foundation_model", "locomotion_humanoid", "simulation_sim2real"
            ) or p.get("decision", {}).get("relevance_prob", 0.0) >= 0.45
        )
        logger.info(
            "Batch %d/%d (%d papers) completed in %.2fs (Identified %d Embodied AI papers)",
            b_idx + 1,
            num_batches,
            len(batch),
            b_elapsed,
            embodied_count,
        )

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
