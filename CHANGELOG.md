# Changelog

本檔案記錄 Daily Paper Scout 的重要變更。

## 2026-07-18

### First-seen 增量雷達

- 收錄條件由 `published_at == 目標日期` 改為本 topic 第一次發現的候選論文。
- 新增 `data/seen.json` 記錄 first-seen state；同日重跑可重現，後續日期不會重複收錄。
- arXiv 查詢回看 4 天，週一可接住週末累積後才公開的投稿。
- GitHub Actions 改為台灣時間週一至週五 10:00（UTC 02:00），週六、週日不排程。

### 项目重置

- 删除 2026-07-18 以前由旧爬虫产生的 93 份历史 JSON，只保留当前日期资料。
- 将默认主题改为 `embodied_ai`，新增具身智能关键词、arXiv 分类与选择门槛。
- 移除原始 `audio_speech` topic 與所有語音關鍵字，只保留 `embodied_ai` 與 `general_ai`。
- 報告語言改為 `auto`，由 Agent 跟隨提問者語言，不再寫死繁體中文。
- 新增 `config/README.md` 與可執行的資料庫、研究者及限定學者 demo，方便 clone 後改成其他研究方向。
- arXiv 分類改為依 `topics.json` 動態建立，不再寫死語音分類。
- 新增 `source_limits`，限制 arXiv 回傳數、Semantic Scholar 作者數、每位作者論文數與請求間隔。
- 預設具身智能採主題雷達模式，不綁定特定學者、不呼叫 Semantic Scholar 作者 API，每日輸出上限 30 篇。
- 将软件授权改为 `AGPL-3.0-or-later`，并保留原作者的 MIT notice。

### 研究者追蹤名單

- 感謝原作者 [voidful](https://github.com/voidful) 建立本專案的多來源論文爬蟲與自動化基礎。
- 所有內建 topic 預設不追蹤指定作者，避免主題偏向與不必要的 API 請求；需要人物雷達時再於自訂 profile 啟用。

### 日期與資料品質

- arXiv 查詢使用可設定的 `submittedDate` 回看範圍，收錄判斷則採 first-seen state。
- 來源完全無資料時不覆寫 JSON 與 seen state；個別 best-effort 來源失敗不影響其他來源。
- 索引的 `latest` 改為所有日期中的最大值，歷史重跑不會讓索引倒退。

### 可配置主題

- 新增 `config/topics.json`，可調整 arXiv categories、keywords、keyword searches、追蹤作者與收錄門檻。
- 新增 `config/researcher.json`，將研究者背景與報告偏好從 prompt 中分離。
- 新增 `general_ai` 範例 profile，示範跨領域 AI 主題切換。
- `selection.min_keyword_hits`、`include_tracked_authors`、`max_papers` 可控制每日輸出範圍。

### LLM 報告

- 重寫 `grok-task-prompt.md`，不再寫死特定研究者、學校或研究專案。
- LLM 報告改依 `researcher.json` 與當日 `topic` 個人化產生。

### 已知限制

- Semantic Scholar 公開 API 有速率限制，作者追蹤數量過多時可能暫時失敗。
- alphaXiv trending endpoint 目前可能回傳 404；該來源屬 best-effort，不影響其他來源。
