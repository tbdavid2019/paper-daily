---
layout: post
title: "每日論文雷達｜2026-08-20"
date: 2026-08-20 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

* **日期**：2026-08-20
* **主題**：具身智慧（Embodied Intelligence / Embodied AI）
* **收錄數量**：精選 10 篇論文（候選集共 22 篇）
* **資料檢索與過濾統計**：
  * 爬取總數：760 篇
    * Hugging Face：100 篇
    * arXiv cs.RO：148 篇
    * arXiv cs.AI：250 篇
    * arXiv cs.CV：250 篇
    * arXiv 關鍵字檢索：12 篇
    * Papers with Code / AlphaXiv：0 篇
  * 去重後總數：665 篇
  * 時間窗口內候選（2026-08-16 起）：623 篇
  * 已見過項目：384 篇
  * 新候選論文：239 篇
  * 關鍵字命中與入選：22 篇

---

## Must-Read

### [The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433)
* **作者**：Yukiyasu Domae, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Tomohiro Motoda
* **來源**：arXiv (cs.RO, arxiv_keyword)
* **重點與關聯**：
  * 本篇綜述論文深入探討機器人基礎模型（RFMs）與視覺-語言-動作（VLA）策略在規模化架構下所忽視的實體落地問題。
  * 論文明確提出並定義了「實體落差（Embodiment Gap）」——即通用預訓練模型、特徵表徵或跨機體資料，與部署至特定機器人本體執行控制之間存在的適配差距。
  * 對於研究機器人基礎模型與泛化策略的研究者而言，該文有助於重新審視純粹依賴資料規模化的局限性，並指出實體部署所需的系統化橋接方法。

### [SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation](https://arxiv.org/abs/2608.18701)
* **作者**：Bowen Jing, Mingxin Wang, Ruiyang Hao, Chenchen Ge, Hanwen Shen
* **來源**：Hugging Face / arXiv (cs.RO)
* **重點與關聯**：
  * 現有可形變物體操作評測多僅以「任務成功率」為單一指標，忽略了滑動或過度擠壓等物理交互品質問題。
  * 該研究提出了 SoftVTBench，一個具備形變感知的視覺-觸覺數據集與基準，提供 4,000 條專家演示數據與超過 50 種資產（涵蓋體積可形變物體等），將策略可見的接觸觀測與物理真實標註（ground truth）配對。
  * 對於專注於多模態感知（視觸覺整合）與柔性/非剛體物體操作的研究者而言，此基準填補了完整任務交互評估的空白。

### [ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](https://arxiv.org/abs/2608.19182)
* **作者**：Jayjun Lee, Jessica Yin, Asif Rana, Nicholas Blauch, Sam Mady
* **來源**：arXiv (cs.RO, cs.AI)
* **重點與關聯**：
  * 針對高自由度（High-DoF）多指機器人本體在原始視覺-觸覺感知下難以從頭學習長時程任務的問題，論文提出 ADEPT 大規模強化學習框架。
  * 該方法先在通用物體姿態重定位（object reposing）任務上預訓練靈巧操作先驗，再於下游長時程任務進行後訓練，實現 Sim-to-Real 遷移並加速新行為探索。
  * 此框架對從事靈巧手操作（Dexterous Manipulation）、強化學習先驗設計及模擬到真實遷移的研究者具備直接參考價值。

---

## Highly Relevant

### [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](https://arxiv.org/abs/2608.19066)
* **作者**：Yechan Park, HyunJin Kim
* **來源**：arXiv (cs.AI, cs.CV)
* **重點與關聯**：
  * 探討 VLA 策略在相機視角偏移時性能大幅衰退的脆弱性（例如在 LIBERO 基準上輕微相機偏移即導致成功率驟降）。
  * 提出利用 3D Gaussian Splatting（3DGS）進行新視角合成的即插即用框架，在不微調或重新訓練已凍結的 VLA 策略權重下，直接在觀測空間中進行視角標準化校正。

### [DA-WAM: Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085)
* **作者**：Ruiguo Zhong, Benshan Ma, Xiaolong Chen, Lang Zhang, Mingyue Feng
* **來源**：arXiv (cs.RO, cs.AI)
* **重點與關聯**：
  * 聚焦於自駕世界模型中未來預測與規劃決策脫節的問題（現有方法常解耦預測與規劃，或在不同軌跡候選間共享狀態，稀釋了動作特定後果）。
  * 提出 DA-WAM 框架，使預測的未來潛在空間具備決策導向性（decision-informative），讓未來的狀態演變直接引導軌跡選擇。

### [LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding](https://arxiv.org/abs/2608.19059)
* **作者**：Yumin Lee, Hyoseok Ju, Giseop Kim
* **來源**：arXiv (cs.RO, cs.CV)
* **重點與關聯**：
  * 為解決長期自主運行中機器人對物體歷史狀態遺忘（temporal amnesia）的問題，論文提出 LT-Mem 記憶演化架構。
  * 結合空間對齊的實例級 3D 感知與基於變動性感知（volatility-conditioned）的時空記憶更新機制，支援跨會話的物體歷史檢索與持續場景理解。

### [Beyond Placement and Articulation: Usage-Driven Code Scenes for Embodied Interaction](https://arxiv.org/abs/2608.18840)
* **作者**：Zijian Xiao, Zipeng Ye, Jinkun Hao, Xiong Yang, Yuchen Xie
* **來源**：arXiv (cs.RO, cs.CV)
* **重點與關聯**：
  * 針對室內場景合成多偏重幾何外觀與物體關節度而忽視功能性使用的局限，提出 RoomWright 框架。
  * 透過代理導向的使用驅動推理，將 3D 場景完全表示為可執行的代碼形式，專門為具身交互與策略學習建構具備功能合理性的模擬環境。

---

## Interesting

### [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227)
* **作者**：Shuangyu Xie, Kaiyuan Chen, Ken Goldberg
* **來源**：arXiv (cs.RO)
* **觀點摘要**：
  * 重新評估經典 Push-T 操縱基準，探索利用 LLM 編程代理（Claude Code 結合 Fable 5）直接生成演算法策略代碼（Code-as-Policy）的可行性。
  * 該方法完全無需人類示範數據，並將生成代碼與傳統基於示範的視覺運動模仿學習策略進行對比（具體實驗數值摘要未提供）。

### [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484)
* **作者**：Pardis Taghavi, Reza Langari, Gaurav Pandey
* **來源**：arXiv (cs.AI, cs.CV)
* **觀點摘要**：
  * 探討影片生成與世界模型中 Transformer 的加速瓶頸，分析區塊稀疏注意力（block-sparse attention）在分區幾何結構上的誤差來源。
  * 提出免訓練的 SparsePR 機制（結合響應耦合分區與殘差重建），為大型世界模型的計算效率優化提供了底層架構改良思路。

### [GrabVG: Graph-Attentive Binding for Visual Grounding in UAV Imagery](https://arxiv.org/abs/2608.18996)
*
