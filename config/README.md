# Configuration Guide

這個目錄有兩個正式設定檔，職責不同：

| 檔案 | 控制內容 | 是否影響爬蟲 |
|------|----------|--------------|
| `topics.json` | 資料來源、分類、關鍵字、作者追蹤、候選與篇數上限 | 是 |
| `researcher.json` | LLM 閱讀者背景、研究興趣、報告篇數、門檻與語言 | 否 |

目前正式預設是 `embodied_ai`。`general_ai` 只是內建的切換示範；原始語音 profile 已移除。

## 修改目前研究方向

在 `topics.json` 的 `topics` 新增 profile，並將 `default_topic` 改成它的名稱：

```json
{
  "default_topic": "database_systems",
  "topics": {
    "database_systems": {
      "name": "Database Systems",
      "description": "Database engines, query optimization and data systems.",
      "arxiv_categories": ["cs.DB", "cs.DC"],
      "keywords": ["query optimization", "database system", "vector database"],
      "keyword_searches": ["learned query optimizer", "LLM for databases"],
      "tracked_authors": {},
      "source_limits": {
        "lookback_days": 4,
        "arxiv_category_max_results": 250,
        "arxiv_keyword_max_results": 100,
        "semantic_scholar_max_authors": 0,
        "semantic_scholar_papers_per_author": 5,
        "semantic_scholar_delay_seconds": 3
      },
      "selection": {
        "min_keyword_hits": 1,
        "include_tracked_authors": true,
        "max_papers": 30
      }
    }
  }
}
```

主要欄位：

| 欄位 | 說明 |
|------|------|
| `arxiv_categories` | 每個分類產生一次 arXiv 查詢 |
| `keywords` | 在標題與摘要中計算 `keyword_hits` |
| `keyword_searches` | 跨分類補抓；每個搜尋詞產生一次 arXiv 查詢 |
| `tracked_authors` | Semantic Scholar 作者名稱與 ID；可留空 |
| `lookback_days` | 回看窗口，避免漏掉延後公開的投稿 |
| `arxiv_*_max_results` | 每次請求的候選回傳上限，不等於 API 呼叫次數 |
| `semantic_scholar_max_authors` | `0` 停用作者 API；正整數限制每日作者請求數 |
| `min_keyword_hits` | 至少命中幾個關鍵字才保留 |
| `include_tracked_authors` | 追蹤作者未命中關鍵字時是否仍保留 |
| `max_papers` | 每份每日 JSON 最多保存幾篇 |

候選收集可以稍微寬鬆；LLM 會再依 `researcher.json` 做第二階段相關性判讀。

## 啟用限定學者

預設不指定學者，也不呼叫 Semantic Scholar 作者 API。要啟用時，同時設定作者 ID 與數量上限：

```json
"tracked_authors": {
  "Sergey Levine": "1736651",
  "Chelsea Finn": "46881670",
  "Pieter Abbeel": "1689992",
  "Deepak Pathak": "38236002"
},
"source_limits": {
  "semantic_scholar_max_authors": 4,
  "semantic_scholar_papers_per_author": 5,
  "semantic_scholar_delay_seconds": 3
},
"selection": {
  "include_tracked_authors": true
}
```

作者 ID 取自 Semantic Scholar 作者頁。每位作者通常需要一次請求，失敗時爬蟲可能重試；公開 API 容易限流，建議先從 4–8 位開始。追蹤作者的論文會帶有 `tracked_author`，並獲得 priority 加分。

完整可執行範例見 [`examples/topics-embodied-authors.json`](examples/topics-embodied-authors.json)。此檔只是 demo，不會被預設排程載入。

## 設定 LLM 研究者

`researcher.json` 不改變抓取來源，只決定 Agent 如何解讀候選：

```json
{
  "profile_name": "Database Systems Researcher",
  "background": "Researcher working on database engines and data systems.",
  "research_interests": ["query optimization", "vector databases"],
  "current_projects": [],
  "report": {
    "target_papers": 10,
    "must_read_threshold": 80,
    "highly_relevant_threshold": 60,
    "language": "auto"
  }
}
```

`language: "auto"` 表示跟隨提問者語言；也可以明確指定語言。

## 執行 demo

資料庫主題：

```bash
PAPER_CONFIG=config/examples/topics-database.json \
PAPER_TOPIC=database_systems \
python scripts/crawl.py
```

具身智能限定學者：

```bash
PAPER_CONFIG=config/examples/topics-embodied-authors.json \
PAPER_TOPIC=embodied_ai_people \
python scripts/crawl.py
```

若要讓 GitHub Actions 長期使用 demo，將所需 profile 複製進正式 `topics.json`，並修改 `default_topic`。不要直接修改 demo 後期待排程自動讀取它。

每個 topic 在 `data/seen.json` 有獨立 first-seen state。大幅改變研究方向時，建議使用新的 topic 名稱，避免舊 state 影響新主題的首次發現結果。
