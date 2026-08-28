---
layout: post
title: "每日論文雷達｜2026-08-28"
date: 2026-08-28 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

* **日期**：2026 年 8 月 28 日
* **主題**：具身智能（Embodied Intelligence）
* **文獻統計**：本期雷達共檢索 779 篇文獻（去重後 663 篇，時間窗口內候選 638 篇，新進候選 267 篇，關鍵字匹配 27 篇）。來源分佈包含 arXiv cs.RO (164)、arXiv cs.AI (250)、arXiv cs.CV (250)、arXiv keyword (15) 及 Hugging Face (100)。本期精選 10 篇代表性論文進行結構化分析。

---

## Must-Read

### [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)
* **作者**：Jun-Hui Liu, Kun-Yu Lin, Yi-Lin Wei, Xu-Han Chen, Yinghao Li
* **來源**：arXiv (`cs.RO`, `cs.CV`, `arxiv_keyword`)
* **重點與研究關聯**：本研究提出了針對視覺-語言-動作（Vision-Language-Action, VLA）模型的新型後門攻擊任務「配置失敗誘捕」（Configured Failure Trapping）。不同於以往將任意任務失敗皆視為攻擊成功的後門方法，該任務旨在透過隱蔽的文本觸發詞，精準誘導機器人產生特定配置的失敗模式（例如使機器人以指定的位置偏移進行抓取），大幅增加了隱蔽性與偵測難度；文中並提出用於合成訓練資料的資料引擎。對於具身智慧安全防禦與策略可靠性評估的研究者而言，此文揭示了精確動作控制下的新型安全漏洞。

### [PredVLA: A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation](https://arxiv.org/abs/2608.26673)
* **作者**：Hiroki Sawada, Shunichi Kasahara
* **來源**：arXiv (`cs.RO`, `arxiv_keyword`)
* **重點與研究關聯**：現行機器人操作基準多由大型預訓練 VLA 模型主導，此論文探討語言條件控制所需的最小模型規模。作者提出名為 PredVLA 的預測編碼策略，僅包含 68 萬（0.68M）個可訓練網路參數且無須機器人資料預訓練。其架構利用分層生成式遞迴動態來預測視覺特徵與本體感覺，且環境觀察僅透過特定機制影響潛在狀態。該工作為研究輕量化具身控制架構與邊緣端運算提供了具體實證。

### [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406)
* **作者**：Kechen Liu, Ola Shorinwa
* **來源**：arXiv (`cs.RO`, `cs.AI`, `cs.CV`)
* **重點與研究關聯**：現有動作條件視訊模型多受限於單一機器人實體。本文提出跨實體動作條件視訊生成框架 CLAP，能夠在涵蓋人類與多種機器人代理的異質視訊資料上進行訓練。該方法基於時空動態遵循通用物理定律的假設，將跨實體視訊世界模型作為零樣本物理模擬器。這對致力於跨實體資料利用與基底世界模型構建的研究者具備高度參考價值。

---

## Highly Relevant

### [PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](https://arxiv.org/abs/2608.27345)
* **作者**：Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević
* **來源**：Hugging Face, arXiv (`cs.AI`, `cs.CV`)
* **重點摘要**：針對視訊生成式世界模型提出基準測試 PAWBench。論文指出許多物理過程具有多種可能走向，世界模型除了生成單一合理軌跡外，更應在相同初始條件與動作下重現可能行為的分佈（即機率對齊，probabilistic alignment），並針對現有模型的分佈一致性進行評估。

### [Riemann-1.0: An Embodied World Action Model for Physical AI](https://arxiv.org/abs/2608.27033)
* **作者**：Haofeng Sun, Jiangbo Pei, Fei Kang, Zexiang Liu, Yaokun Li
* **來源**：arXiv (`cs.RO`)
* **重點摘要**：提出名為 Riemann-1.0 的全因果自回歸世界動作模型（World Action Model），在單一因果序列中統一建模多視角視覺觀察、機器人狀態與實體動作，將機器人線上策略執行與動作條件世界模擬整合至單一

## Interesting

資料未提供

## Idea Sparks

資料未提供
