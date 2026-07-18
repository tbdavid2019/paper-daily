---
name: daily-paper-scout
description: Fetch the latest first-seen paper-daily JSON and researcher profile, then produce a source-grounded research report. Use when a user asks for newly discovered papers, today's research radar, paper recommendations, or analysis of this repository's daily dataset.
---

# Daily Paper Scout

Use this skill when working with the `tbdavid2019/paper-daily` dataset or a deployment of the same schema. It is a discovery and ranking workflow: the JSON is a curated metadata feed, not a replacement for reading the paper.

## Data endpoints

Default repository:

```text
https://raw.githubusercontent.com/tbdavid2019/paper-daily/main/
```

Read these resources:

1. `data/index.json` — dates, topic, file names and counts.
2. `data/{date}.json` — the selected papers for a date.
3. `config/researcher.json` — the reader's background, interests, projects and report preferences.
4. `config/topics.json` — topic profiles and their selection rules.

If the user gives another repository or base URL, use it instead of the default. If they give a date, use that date. Otherwise read `index.json` and use its `latest` entry. Do not assume that the machine's calendar date is the dataset date.

## Retrieval workflow

1. Fetch `index.json`.
2. Select the requested date and, when relevant, confirm the file's `topic` matches the requested profile.
3. Fetch the date JSON, `researcher.json`, and `topics.json`.
4. Validate that the date JSON has `date`, `topic`, `stats`, and `papers`.
5. Report the dataset facts before interpreting it: `window_start`, `window_candidates`, `already_seen`, `new_candidates`, `selected_papers`, `keyword_matched`, source counts, and any missing-date count.
6. Rank papers using the researcher's interests and projects first, then use `priority`, `keyword_hits`, multiple sources, and tracked-author metadata as supporting signals.

Tool-neutral retrieval example:

```text
BASE=https://raw.githubusercontent.com/tbdavid2019/paper-daily/main
GET $BASE/data/index.json
GET $BASE/data/{selected-date}.json
GET $BASE/config/researcher.json
GET $BASE/config/topics.json
```

Use the host's normal HTTP, web, or file-reading tool. Do not clone the repository just to read a daily JSON unless the user asks for local development.

## Interpretation rules

- The file `date` is the discovery report date, not every paper's submission date.
- `first_seen_at` is when this crawler first observed the paper for this topic. On the initial bootstrap it may include papers that became public earlier within the lookback window.
- `published_at` is upstream publication/submission metadata. It does not mean peer review or acceptance and is not the daily inclusion key.
- `priority` is a crawler pre-ranking, not a human relevance score. Re-score against the current researcher profile.
- `keyword_hits` is a literal profile-keyword signal. A high count can still be a false positive; inspect the title and abstract.
- `abstract` may be truncated. Never invent experiments, numbers, conclusions, or claims not present in the fetched material.
- A paper appearing in multiple sources is a discovery signal, not proof of quality.
- `tracked_author` can be wrong because author-name disambiguation services sometimes merge homonyms. Verify the paper's author list before calling it an author's work.
- Distinguish clearly between **paper evidence**, **metadata**, and **your inference**.
- If the date has zero selected papers, say so plainly. Do not fill the report with older papers unless the user asks for a broader window.

## Report workflow

Use the language and thresholds in `researcher.json`. If they are absent, use Traditional Chinese and these neutral sections:

1. **今日概況** — date, topic, counts, and dominant themes.
2. **Must-Read** — strongest direct matches; include title, authors, link, score, evidence, and why it matters to this researcher.
3. **Highly Relevant** — useful but less central papers.
4. **Interesting** — plausible ideas with weaker direct fit; do not inflate the score.
5. **Idea Sparks** — two or three cross-paper observations, each with a concrete follow-up question.

For every selected paper:

- Link to its `url`.
- State the authors and source list.
- Give a one-sentence evidence-based summary from the supplied abstract.
- Explain the connection to a specific interest or project, or say that the connection is indirect.
- Include an actionable next step only when it follows from the available evidence.

When more detail is needed, follow the paper URL and read the full arXiv abstract, paper, code repository, or discussion. Label these as supplemental sources and do not silently merge them with the daily JSON.

## Failure handling

- If `index.json` cannot be fetched, report the URL and stop; do not guess a date.
- If the selected date file is missing, report the available dates from the index.
- If a source count is zero, treat it as a source outage or best-effort limitation, not evidence that no papers exist globally.
- If JSON is malformed or its `date` disagrees with the requested date, flag the mismatch before analysis.

## Example requests this skill should handle

- “Read the latest paper-daily JSON and give me the five most important papers for this researcher.”
- “Compare the last three discovery dates and identify a trend.”
- “Use the `general_ai` topic and find papers related to agents.”
- “Explain whether today's dataset is empty because there were no papers or because a source failed.”

Do not modify repository data, topic profiles, or researcher profiles during analysis unless the user explicitly asks for a code or configuration change.
