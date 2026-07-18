# Changelog

本檔案記錄 Daily Paper Scout 的重要變更。

## 2026-07-18

### 项目重置

- 删除 2026-07-18 以前由旧爬虫产生的 93 份历史 JSON，只保留当前日期资料。
- 将默认主题改为 `embodied_ai`，新增具身智能关键词、arXiv 分类与选择门槛。
- arXiv 分類改為依 `topics.json` 動態建立，不再寫死語音分類。
- 新增 `source_limits`，限制 arXiv 回傳數、Semantic Scholar 作者數、每位作者論文數與請求間隔。
- 預設具身智能採主題雷達模式，不綁定特定學者、不呼叫 Semantic Scholar 作者 API，每日輸出上限 30 篇。
- 将软件授权改为 `AGPL-3.0-or-later`，并保留原作者的 MIT notice。

### 研究者追蹤名單

- 感謝原作者 [voidful](https://github.com/voidful) 建立本專案的多來源論文爬蟲與自動化基礎。
- 所有內建 topic 預設不追蹤指定作者，避免主題偏向與不必要的 API 請求；需要人物雷達時再於自訂 profile 啟用。

### 日期與資料品質

- arXiv 查詢改用指定 `submittedDate` 範圍。
- 輸出只保留正式發布日符合目標日期的論文。
- 自動排程改抓前一個完整 UTC 日，避免 00:30 執行時漏掉當天稍後發布的論文。
- 週末或沒有發布資料的日期允許正常輸出 0 篇。
- 索引的 `latest` 改為所有日期中的最大值，歷史重跑不會讓索引倒退。

### 可配置主題

- 新增 `config/topics.json`，可調整 arXiv categories、keywords、keyword searches、追蹤作者與收錄門檻。
- 新增 `config/researcher.json`，將研究者背景與報告偏好從 prompt 中分離。
- 新增 `general_ai` 範例 profile，示範跨領域 AI 主題切換。
- `selection.min_keyword_hits`、`include_tracked_authors`、`max_papers` 可控制每日輸出範圍。

### LLM 報告

- 重寫 `grok-task-prompt.md`，不再寫死特定研究者、學校或研究專案。
- LLM 報告改依 `researcher.json` 與當日 `topic` 個人化產生。

### 資料

- 依新發布日規則重新產生 `data/2026-07-16.json`：由原本快照的 358 篇改為 156 篇正式發布論文。

### 已知限制

- Semantic Scholar 公開 API 有速率限制，作者追蹤數量過多時可能暫時失敗。
- alphaXiv trending endpoint 目前可能回傳 404；該來源屬 best-effort，不影響其他來源。
