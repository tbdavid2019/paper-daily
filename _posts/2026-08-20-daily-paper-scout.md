---
layout: post
title: "每日論文雷達｜2026-08-20"
date: 2026-08-20 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

* **日期**：2026-08-20
* **研究主題**：具身智能（Embodied Intelligence / Embodied AI）
* **收錄與篩選統計**：
  * 總爬取篇數：760 篇（來源涵蓋 arXiv cs.RO 148 篇、cs.AI 250 篇、cs.CV 250 篇、Hugging Face 100 篇、arXiv keyword 12 篇，其餘來源 0 篇）
  * 去重後候選：665 篇
  * 時間窗口內候選：623 篇（排除已處理 384 篇後，新增候選 239 篇）
  * 關鍵字匹配與精選收錄：22 篇中精選 10 篇代表性論文

---

## Must-Read

### The Embodiment Gap in Robot Foundation Models
* **作者**：Yukiyasu Domae, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Tomohiro Motoda
* **來源**：arXiv (cs.RO, arxiv_keyword)
* **論文連結**：[https://arxiv.org/abs/2608.18433](https://arxiv.org/abs/2608.18433)
* **重點與研究關聯**：
  * **摘要核心**：論文探討機器人基礎模型（Robot Foundation Models, RFM）與視覺-語言-動作（VLA）策略中的「具身差距（Embodiment Gap）」。儘管模型可透過擴展資料與模型規模展現泛化能力，但在實際部署至特定機械本體時仍需大量適配工作。本篇回顧分析了可重用模型/表示與具體機器人執行之間的差距成因與影響。
  * **對具身智能研究者的價值**：對於研究跨本體控制、泛化策略與 VLA 實際落地的研究者而言，該文釐清了純資料擴展與本體物理限制之間的落差，有助於重新審視跨平台部署的挑戰。

### SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation
* **作者**：Bowen Jing, Mingxin Wang, Ruiyang Hao, Chenchen Ge, Hanwen Shen
* **來源**：Hugging Face, arXiv (cs.RO)
* **論文連結**：[https://arxiv.org/abs/2608.18701](https://arxiv.org/abs/2608.18701)
* **重點與研究關聯**：
  * **摘要核心**：現有可變形物體操作基準多僅評估任務成功率，忽略了滑動或過度擠壓等物理接觸品質。論文提出 SoftVTBench 視觸覺數據集與基準，包含 4,000 筆專家示範與超過 50 種資產（含體積可變形物體），將策略可見的接觸觀測與物理真實基準配對。
  * **對具身智能研究者的價值**：為多模態感知、觸覺回饋控制以及軟質/可變形物體操作研究提供了具備物理形變感知的評測環境與資料基礎。

### GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting
* **作者**：Yechan Park, HyunJin Kim
* **來源**：arXiv (cs.AI, cs.CV)
* **論文連結**：[https://arxiv.org/abs/2608.19066](https://arxiv.org/abs/2608.19066)
* **重點與研究關聯**：
  * **摘要核心**：針對 VLA 策略對視角偏移極度敏感的問題（實驗指出相機安裝的微小位移可使 LIBERO 基準成功率從約 90% 下降至約 10%），提出利用 3D Gaussian Splatting（3DGS）進行新視角合成的即插即用框架，在不重新訓練凍結策略的情況下進行觀測空間標準化。
  * **對具身智能研究者的價值**：展示了將 3D 空間表示（3DGS）作為預處理管道以提升既有凍結 VLA 策略視角強健性的有效途徑。

---

## Highly Relevant

### ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning
* **作者**：Jayjun Lee, Jessica Yin, Asif Rana, Nicholas Blauch, Sam Mady
* **來源**：arXiv (cs.RO, cs.AI)
* **論文連結**：[https://arxiv.org/abs/2608.19182](https://arxiv.org/abs/2608.19182)
* **重點評析**：提出大規模強化學習框架，先在泛化物體姿態重置（reposing）任務上預訓練靈巧手策略，再作為先驗微調至下游任務。該框架支援高自由度機械手從原始視觸覺感知中直接學習長時程任務，並具備 Sim-to-Real 遷移能力。

### DA-WAM: Decision-Aligned Future Latents for Driving World Models
* **作者**：Ruiguo Zhong, Benshan Ma, Xiaolong Chen, Lang Zhang, Mingyue Feng
* **來源**：arXiv (cs.RO, cs.AI)
* **論文連結**：[https://arxiv.org/abs/2608.19085](https://arxiv.org/abs/2608.19085)
* **重點評析**：針對自動駕駛世界模型中未來預測與決策優化脫節的問題，提出決策對齊（Decision-Aligned）的未來潛在空間學習方法，使預測的未來狀態能直接反映動作特異性結果，進而引導軌跡選擇。

### LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding
* **作者**：Yumin Lee, Hyoseok Ju, Giseop Kim
* **來源**：arXiv (cs.RO, cs.CV)
* **論文連結**：[https://arxiv.org/abs/2608.19059](https://arxiv.org/abs/2608.19059)
* **重點評析**：為解決機器人在長期運行中因覆蓋歷史地圖而產生的「時間失憶」問題，LT-Mem 結合空間對齊的實例級 3D 感知與動態揮發性（volatility）條件化記憶機制，維持跨 session 的物件身份一致性。

### Beyond Placement and Articulation: Usage-Driven Code Scenes for Embodied Interaction
* **作者**：Zijian Xiao, Zipeng Ye, Jinkun Hao, Xiong Yang, Yuchen Xie
* **來源**：arXiv (cs.RO, cs.CV)
* **論文連結**：[https://arxiv.org/abs/2608.18840](https://arxiv.org/abs/2608.18840)
* **重點評析**：提出 RoomWright 框架，將 3D 場景完全表示為程式碼，並聚焦於場景的「功能性使用」而非僅限於物件擺放與關節鉸接，透過以用途為驅動的物件推理生成可供具身互動的模擬環境。

---

## Interesting

### Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics
* **作者**：Shuangyu Xie, Kaiyuan Chen, Ken Goldberg
* **來源**：arXiv (cs.RO)
* **論文連結**：[https://arxiv.org/abs/2608.18227](https://arxiv.org/abs/2608.18227)
* **簡要筆記**：重新審視經典的 Push-T 基準，探討使用 LLM 寫程式代理（Claude Code 搭配 Fable 5）在無示範資料下直接生成演算法策略（Code as Policy）的可行性，並與傳統視動模仿學習策略進行對比。

### Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models
* **作者**：Pardis Taghavi, Reza Langari, Gaurav Pandey
* **來源**：arXiv (cs.AI, cs.CV)
* **論文連結**：[https://arxiv.org/abs/2608.18484](https://arxiv.org/abs/2608.18484)
* **簡要筆記**：針對影片生成與世界模型提出名為 SparsePR 的免訓練區塊稀疏注意力機制，透過耦合響應分割與殘差重構來加速注意力計算，對於世界模型的推論加速具潛在參考價值。

### GrabVG: Graph-Attentive Binding for Visual Grounding in UAV Imagery
* **作者**：Chaowei Wang, Yan Di, Jingjun Sun, Baozhe Liu, Jiaxu Tian
* **來源**：arXiv (cs.AI, cs.CV)
* **論文連結**：[https://arxiv.org/abs/2608.18996](https://arxiv.org/abs/2608.18996)
* **簡要筆記**：針對無人機鳥瞰視角下的微小密集物件與拓撲模糊性，提出圖注意力綁定機制以提升視覺定位精確度，主要針對無人機領域，但其空間拓撲建模想法具借鑑性。

---

## Idea Sparks

### 1. 3D 空間標準化與本體差距（Embodiment Gap）的解耦
* **跨論文觀察**：*The Embodiment Gap in Robot Foundation Models* 指出 RFM/VLA 在不同機器人載體部署時存在顯著鴻溝；而 *GS-VLA* 則示範了利用 3DGS 進行視角標準化，無需重新訓練策略即可顯著緩解感測器幾何位移造成的性能崩塌。
* **後續研究問題**：能否將 3DGS 或顯式 3D 幾何表徵進一步擴展至機械手臂本體配置與工作空間的標準化，將「觀測空間適配」與「動作空間映射」完全解耦，以系統性縮小 RFM 的具身差距？

### 2. 視觸覺融合在接觸豐富型任務中的物理約束評估
* **跨論文觀察**：*SoftVTBench* 強調傳統成功率無法反映形變與接觸品質（如滑動、過度擠壓），而 *ADEPT* 證明了透過通用姿態調整預訓練可加速多指靈巧手從原始視觸覺中學習策略。
* **後續研究問題**：在靈巧操作與軟質物件互動中，若將 SoftVTBench 所定義的物理接觸約束（如接觸應力、滑移懲罰）整合為 ADEPT 等強化學習框架的輔助獎勵或安全約束，是否能在提升 Sim-to-Real 遷移成功率的同時
