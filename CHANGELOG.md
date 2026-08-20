# Changelog

本檔案記錄 Daily Paper Scout 的重要變更。

## 2026-08-20

### LLM 研究摘要 Blog

- 新增 `scripts/generate_blog.py`，讀取每日論文 JSON、研究者設定與 topic profile，使用 OpenAI-compatible LLM endpoint 產生繁體中文研究摘要。
- 摘要固定包含「今日概況」、「Must-Read」、「Highly Relevant」、「Interesting」與「Idea Sparks」段落；模型漏段落時啟動修復流程，資料不足的段落標示「資料未提供」。
- 新增 `_posts/`、Jekyll layout、首頁與 responsive CSS，輸出成 `888每日論文雷達 -- Embodied AI` Blog。

### GitHub Pages 自動部署

- `daily-crawl.yml` 現在會依序執行爬蟲、LLM 摘要、Jekyll build 與 GitHub Pages deploy。
- 新增 `pages-deploy.yml`，品牌或網站樣式變更時由獨立 workflow 直接重新部署 Pages。
- GitHub Pages 採用官方 workflow artifact，部署步驟由 `configure-pages`、`jekyll-build-pages`、`upload-pages-artifact` 與 `deploy-pages` 組成。
- 公開網址：[888每日論文雷達 -- Embodied AI](https://tbdavid2019.github.io/paper-daily/)。

### 品牌與技術提供

- Blog 名稱改為 `888每日論文雷達 -- Embodied AI`。
- Footer 中央新增 [https://david888.com](https://david888.com) 技術提供連結。

### 測試與安全

- 新增手動 `LLM Connection Test` workflow，驗證 LLM 連線但不輸出 API key 或完整回應。
- 新增摘要產生器的排序、回應格式、Markdown 與必要段落測試。

## 2026-07-18

### First-seen 增量雷達

- 收錄條件由 `published_at == 目標日期` 改為本 topic 第一次發現的候選論文。
- 新增 `data/seen.json` 記錄 first-seen state；同日重跑可重現，後續日期依 state 完成去重。
- arXiv 查詢回看 4 天，週一可接住週末累積後才公開的投稿。
- GitHub Actions 改為台灣時間週一至週五 10:00（UTC 02:00），週六、週日不排程。

### 项目重置

- 删除 2026-07-18 以前由旧爬虫产生的 93 份历史 JSON，只保留当前日期资料。
- 将默认主题改为 `embodied_ai`，新增具身智能关键词、arXiv 分类与选择门槛。
- 移除原始 `audio_speech` topic 與所有語音關鍵字，只保留 `embodied_ai` 與 `general_ai`。
- 報告語言改為 `auto`，由 Agent 跟隨提問者語言，並支援明確指定輸出語言。
- 新增 `config/README.md` 與可執行的資料庫、研究者及限定學者 demo，方便 clone 後改成其他研究方向。
- arXiv 分類改為依 `topics.json` 動態建立，主題 profile 由設定檔定義研究範圍。
- 新增 `source_limits`，限制 arXiv 回傳數、Semantic Scholar 作者數、每位作者論文數與請求間隔。
- 預設具身智能採主題雷達模式，作者追蹤設定維持空集合，Semantic Scholar 作者查詢額度設為 0，每日輸出上限 30 篇。
- 将软件授权改为 `AGPL-3.0-or-later`，并保留原作者的 MIT notice。

### 研究者追蹤名單

- 感謝原作者 [voidful](https://github.com/voidful) 建立本專案的多來源論文爬蟲與自動化基礎。
- 所有內建 topic 預設採主題條件聚合，人物雷達可於自訂 profile 加入作者設定，並由 priority 提供排序加分。

### 日期與資料品質

- arXiv 查詢使用可設定的 `submittedDate` 回看範圍，收錄判斷則採 first-seen state。
- 來源整體回傳空集合時保留既有 JSON 與 seen state；個別 best-effort 來源失敗時，其他來源持續完成當日資料。
- 索引的 `latest` 取所有日期中的最大值，歷史重跑維持索引日期順序。

### 可配置主題

- 新增 `config/topics.json`，可調整 arXiv categories、keywords、keyword searches、追蹤作者與收錄門檻。
- 新增 `config/researcher.json`，將研究者背景與報告偏好從 prompt 中分離。
- 新增 `general_ai` 範例 profile，示範跨領域 AI 主題切換。
- `selection.min_keyword_hits`、`include_tracked_authors`、`max_papers` 可控制每日輸出範圍。

### LLM 報告

- 重寫 `grok-task-prompt.md`，研究者、學校與研究專案改由 `researcher.json` 提供。
- LLM 報告改依 `researcher.json` 與當日 `topic` 個人化產生。

### 已知限制

- Semantic Scholar 公開 API 有速率限制，作者追蹤數量過多時可能暫時失敗。
- alphaXiv trending endpoint 採 best-effort；遇到 404 時，流程沿用其他來源完成當日資料。
