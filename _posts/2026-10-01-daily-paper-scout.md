---
layout: post
title: "每日論文雷達｜2026-10-01"
date: 2026-10-01 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-01
- **主題**：具身智能（Embodied Intelligence）
- **收錄數量**：本次爬取總數 878 篇，去重後 757 篇，新候選 574 篇，經過篩選與主題高度相關並納入本次報告共 30 篇。
- **資料統計**：涵蓋 Hugging Face、arXiv (`cs.RO`、`cs.AI`、`cs.CV`) 以及關鍵字命中論文。

## Must-Read

- **[GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)**
  - **作者**：Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
  - **摘要證據與關聯**：針對現今視覺語言動作（VLA）與世界動作模型（WAMs）在複雜或微小物件定位上容易失敗、無法滿足閉環控制速度的問題，作者提出 4B 大小的基礎定位模型 GroundingPI。該模型透過共享詞彙表將點與邊界框生成為量化座標，並結合多模態與空間預訓練、監督微調及強化學習。對研究 VLA 模型與空間智能的研究者而言，這提供了提升實體環境物體辨識與定位精確度的重要基礎架構。

- **[RoboCoach: World Models as Active Coaches for Compositional Robot Skills](https://arxiv.org/abs/2609.39685)**
  - **作者**：Jiajun Liu, Yifan Chen, Yichao Liu, Jiayi Zhang, Ruoqu Chen
  - **來源**：`huggingface`, `arxiv_cs.RO`, `arxiv_cs.AI`
  - **摘要證據與關聯**：長序列機器人操作（long-horizon manipulation）重組技能成本高昂。本文提出 ROBOCOACH，一個由世界模型引導的教練框架，利用想像中的失敗來指導示範請求與專家更新。其 RIDI（Route-Imagine-Diagnose-Improve）迴圈在共享動作條件世界模型 COACHWORLD 中執行可重用的技能專家，並透過進度判定器記錄。此研究對於探索世界模型與主動自我改進機制的具身智能研究者深具參考價值。

- **[IronMind: Scaling Humanoid Dexterous Manipulation via Camera-Space Ego-Centric Pretraining](https://arxiv.org/abs/2609.39403)**
  - **作者**：Huimin Pan, Yufan Ren, Kunpeng Song, Siyang Wang, Xiwen Zhang
  - **來源**：`arxiv_cs.RO`
  - **摘要證據與關聯**：人形機器人靈巧操作常面臨人類與機器人肢體結構差異的「具身鴻溝（embodiment gap）」及低成本第一人稱（egocentric）錄影缺乏軀幹運動學的挑戰。IronMind 透過相機空間的第一人稱預訓練，結合人類與異質機器人資料，預訓練人形靈巧操作策略。這對研究人形靈巧操作與利用大規模人類影片資料的學者提供了直接的解法。

## Highly Relevant

- **[Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2609.39178)**
  - **作者**：Songhua Yang, Ziyu Liu, Yuanwei Liu, Xuetao Li, Xuanye Fei
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`, `arxiv_keyword`
  - **摘要證據與關聯**：探討 VLA 模型在機器人操作中的安全性，提出通用對抗物件（Universal Adversarial Object，一種具有優化表面紋理的球體），放置於機器人視野內即會顯著降低任務成功率。對於重視 VLA 模型強健性與安全防禦的研究者是重要的實證警訊。

- **[Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies](https://arxiv.org/abs/2609.38537)**
  - **作者**：Galbot Team, Xuchuan Chen, Xiaoqian Cheng, Yu Deng, Lihe Ding
  - **來源**：`huggingface`, `arxiv_cs.RO`
  - **摘要證據與關聯**：評估 GPT-6 Astra 作為通用具身策略的能力，涵蓋直接控制、與學習策略合作及回饋自適應等六大領域。在夾爪與靈巧操作的混合控制實驗中展現特定成功率。對於探索通用基礎模型（Foundation Models）直接進行數值動作生成的具身研究者具參考價值。

- **[Spike-driven Vision-Language-Action Model](https://arxiv.org/abs/2609.39514)**
  - **作者**：Shuai Wang, Malu Zhang, Mingquan Liu, Weihui Dai, Dehao Zhang
  - **來源**：`arxiv_keyword`
  - **摘要證據與關聯**：為解決傳統大型 Transformer 基底 VLA 模型在高資源限制平台上的延遲與能耗問題，提出首個支援機器人操作端到端直接訓練的脈衝驅動 VLA 框架（Spike-driven VLA）。這為具身智能在邊緣計算與能效優化方向開啟了新的可能。

- **[Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models](https://arxiv.org/abs/2609.39820)**
  - **作者**：Mingyue Cui, Zheyuan Liu, Yihan Zhu, Zheyuan Zhang, Meng Jiang
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_keyword`
  - **摘要證據與關聯**：針對 VLA 模型在複雜環境中常面臨策略與執行防護（safety shield）不匹配的問題，提出 FailBank 四階段自進化框架，將運行時的回饋轉換為持續的策略改進。

- **[Inline Memory Meets Reusable Skills: Memory-centric Framework for Vision-Language-Action Model](https://arxiv.org/abs/2609.39794)**
  - **作者**：Zaijing Li, Rui Shao, Bing Hu, Haoyu Zhang, Dongmei Jiang
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`, `arxiv_keyword`
  - **摘要證據與關聯**：提出 Optimus-R 記憶導向 VLA 框架，透過插入可學習的記憶 Token 進行顯式查詢-技能記憶微調，藉此解決 VLA 模型適應新任務時的高成本與災難性遺忘問題。

## Interesting

- **[Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38537)** (註：原文 ID 為 `2609.38401`)
  - **作者**：Ke Zhang, Danica J. Sutherland, Chao Liu
  - **來源**：`arxiv_cs.RO`
  - **摘要證據與關聯**：透過系統性案例研究（如 ManiSkill 中的 RL 任務），探討在訓練資料變化（如物體尺寸、顏色、光照與語言提示的網域隨機化）下，機器人學習機制的底層運作模式。雖然關聯較為基礎科學性質，但有助於理解泛化機制的黑盒子。

- **[WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents](https://arxiv.org/abs/2609.40325)**
  - **作者**：Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu
  - **來源**：`huggingface`, `arxiv_cs.AI`, `arxiv_keyword`
  - **摘要證據與關聯**：針對互動式 3D 世界中的異常檢測（如漂浮物件、可穿行牆壁等），推出 WorldAuditBench 評估管道，考驗多模態代理在 3D 空間中的導航與異常檢索能力。

## Idea Sparks

- **觀點一：從靜態感知到精確點箱量化（Grounding Foundations）**
  - 觀察：傳統 VLA 模型依賴通用視覺語言骨幹，在處理閉環控制中的微小或遮擋物件時表現不足。GroundingPI 透過將點與邊界框作為共享詞彙表的量化座標來改善定位。
  - 後續問題：這種將空間定位融入詞彙表的做法，能否無縫擴展到多機器人異質動作空間，並保持即時控制所需的低延遲？

- **觀點二：透過世界模型與執行回饋實現自我進化（Self-Evolution & World Models）**
  - 觀察：多篇論文（如 ROBOCOACH 與 FailBank）探討利用世界模型進行「想像中的失敗」模擬，或是將運行時防護回饋轉換為長效策略更新。
  - 後續問題：當世界模型的模擬環境與真實物理世界存在未建模的動態誤差（Sim-to-Real 鴻溝）時，基於想像失敗所做的策略更新是否會放大安全風險？
