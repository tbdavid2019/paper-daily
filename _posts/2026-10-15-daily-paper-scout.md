---
layout: post
title: "每日論文雷達｜2026-10-15"
date: 2026-10-15 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-10-15
- **主題**：具身智慧 (Embodied Intelligence)
- **資料統計**：本次爬取總計 1,487 篇論文，經去重與候選篩選後共有 640 篇新候選論文，其中 250 篇經過深度決策評估（`decision_evaluated`），最終收錄 60 篇高質量研究。

## Must-Read
本區收錄今日最具突破性、跨領域影響力的前 4 篇關鍵論文：

1. **FACT: A Multimodal Force-Action-Track Foundation Model for Human-to-Robot Dexterity**
   - **作者**：Zhi Cao, Yining Hong, Jiaolong Yang, Yejin Choi, Li Fei-Fei
   - **來源與連結**：[arXiv:2610.19155](https://arxiv.org/abs/2610.19155)
   - **技術突破與啟發**：針對靈巧操作（Dexterous Manipulation）中人類資料集普遍缺乏力感測（force measurement）的痛點，作者群推出了大規模人類觸覺資料集 EgoForce，並結合機器人示範進行預訓練，提出能串接視覺規劃與力回饋的基礎模型 FACT。這對研究「觸覺與多模態感知」及「靈巧操作」的研究者是一大啟發，展示了如何透過大規模多模態對齊來解決真實世界互動中的力量調節問題。

2. **FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs**
   - **作者**：Bingao Chen, Lihan Zha, C. Karen Liu, Guy Tevet
   - **來源與連結**：[arXiv:2610.20064](https://arxiv.org/abs/2610.20064)
   - **技術突破與啟發**：傳統視覺語言動作模型（VLA）常依賴腕部相機（wrist camera）來獲取微距細節，但往往犧牲了整體全景視野。FoveaVLA 提出以「學習式注視動作（foveation actions）」取代腕部相機，在每次策略查詢時預測互動區域，並自動截取原始高解析度影像與全景圖像結合。這項創新大幅優化了 VLA 在面對精細操作時的視覺感知架構。

3. **AutoRSR: Automated Real-to-Sim-to-Real Data Generation for Scalable Robot Learning**
   - **作者**：Jiawei Zhang, Chang Liu, Litao Deng, Tao Zhang, Qin Jin
   - **來源與連結**：[arXiv:2610.20336](https://arxiv.org/abs/2610.20336)
   - **技術突破與啟發**：為了解決真實世界資料收集昂貴、模擬環境建置手續繁雜的瓶頸，AutoRSR 提供了一套高度自動化的真實-模擬-真實（Real-to-Sim-to-Real）工作流程，能將掃描的真實工作區自動轉換為可重複使用的模擬資產與資料。這對降低 Sim-to-Real 轉移門檻、實現具身智慧的大規模資料擴展提供了解決方案。

4. **Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control**
   - **作者**：Nolan Fey, Khai Nguyen, Yash Prabhu, Gabriel B. Margolis, Pulkit Agrawal
   - **來源與連結**：[arXiv:2610.18991](https://arxiv.org/abs/2610.18991)
   - **技術突破與啟發**：人形機器人在模擬器中訓練的策略轉移至硬體時，常因力矩與接觸動態不匹配而失效。Contact-UAN 提出一個非監督執行器網路作為殘差世界模型，在保留模擬器物理先驗的同時校正執行器動態，完美對齊硬體 rollouts。這對未來人形機器人的強健控制與 sim-to-real 具有極高的實用價值。

## Highly Relevant
本區收錄扎實且高度相關的核心研究，涵蓋 VLA、機器人操作與人形機器人 locomotion：

- **E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots** (Cheng Fan et al.) - [arXiv:2610.19627](https://arxiv.org/abs/2610.19627)：提出軟可微分障礙物互動公式，突破四足機器人端到端視覺避障的梯度最佳化瓶頸。
- **A Mode-Unified, Continuous, and Biomimetic Control Strategy of a Robotic Lower Limb Prosthesis** (Hanjun Kim et al.) - [arXiv:2610.19183](https://arxiv.org/abs/2610.19183)：運用徑向基函數（RBF）插值統一機器人下肢義肢的連續地形步態控制策略。
- **TacClaw-Infinity: A Large-Scale Vision-Tactile-Language-Action Dataset for Dexterous Manipulation** (Fucai Zhu et al.) - [arXiv:2610.20320](https://arxiv.org/abs/2610.20320)：推出基於 TacClaw 手持介面的大規模結構化視觸覺語言動作資料集。
- **PolyMorph: Learning Locomotion Policy for Cross-Embodiment Adaptation** (Hyunsik Oh et al.) - [arXiv:2610.19615](https://arxiv.org/abs/2610.19615)：透過模組化 URDF 解析與圖形 Transformer，實現異質四足/多足機器人的跨本體單一策略學習。
- **AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents** (Peidong Wang et al.) - [arXiv:2610.20474](https://arxiv.org/abs/2610.20474)：針對長序列任務中 VLA 之中途失敗，提出隨需遞迴自我改進（RSI）框架。
- **Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution** (Yunze Liu et al.) - [arXiv:2610.19495](https://arxiv.org/abs/2610.19495)：首創聯合編碼當前狀態與未來演進的 VLA 嵌入模型，支援機器人上下文學習。
- **Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training** (Liqian Ma et al.) - [arXiv:2610.19479](https://arxiv.org/abs/2610.19479)：以元學習輔助模擬器資料生成分佈，最大化下游真實世界效能。
- **Learning from Demonstrations meets Symbolic Control - A Supervisory Control Architecture for Formal Certification of Learned Motion** (Ashok Kumar et al.) - [arXiv:2610.19815](https://arxiv.org/abs/2610.19815)：結合示範學習與符號監督控制架構，為機器人動態系統運動提供形式化安全保證。
- **RoboSpan: Learning Modular Coordination Policies for High-DoF Whole-Body Mobile Manipulation with Teleoperation** (Keqiang Ren et al.) - [arXiv:2610.19594](https://arxiv.org/abs/2610.19594)：透過階層模組化框架（HMF）解耦 29-DoF 的全身體移動操作。
- **MUCO: A Mani-Unit-Structured Manipulation Framework for Compositional Long-Horizon Robot Tasks** (Xiangyi Wei et al.) - [arXiv:2610.19913](https://arxiv.org/abs/2610.19913)：引入操作單元（MUs）與編排機制，解決長序列組合任務中的誤差累積。
- **PingpongDuo: Agile Humanoid Table Tennis Doubles with Safe Team Coordination** (Haoran Jiang et al.) - [arXiv:2610.20579](https://arxiv.org/abs/2610.20579)：探討人形機器人在桌球雙打中的層級化團隊安全協調策略。
- **DD-GBP: Anytime Multi-Arm Planning and Continuous Execution via Distributed Dynamic Gaussian Belief Propagation** (Zhao Jin et al.) - [arXiv:2610.20460](https://arxiv.org/abs/2610.20460)：透過分散式動態高斯信念傳播實現即時多手臂路徑規劃。
- **Human Demonstrations as Post-Training Data for Any Robot Body: Retargeting the Object, Not the Hand** (Nagasrikanth Kallakuri) - [arXiv:2610.20351](https://arxiv.org/abs/2610.20351)：提出不重定向手部、改為重定向物件的跨本體示範後訓練方法。
- **MorphAct: Robot Policies Morphing with the Worlds They Act In** (Ziyan Liu et al.) - [arXiv:2610.20019](https://arxiv.org/abs/2610.20019)：針對跨環境操作中互斥參數更新的衝突，提出上下文參數調節機制。

## Interesting
- 資料未提供更多低關聯或邊緣創新論文，今日收錄皆聚焦於具身智慧的核心突破。

## Idea Sparks
1. **多模態基底模型的「感測器去蕪存菁」趨勢**：從 FoveaVLA（以動態注視取代腕部相機）與 FACT/TacClaw（結合觸覺與力回饋資料集）的密集出現，顯示具身智慧模型正從盲目堆疊感測器，轉向「依任務需求動態擷取高解析細節與物理互動特徵」的智慧化感知架構。
   - *後續問題*：當動態注視與區域裁剪成為主流，VLA 模型在處理高速動態或突發遮蔽（Occlusion）時的延遲與穩定性該如何兼顧？
2. **跨本體（Cross-Embodiment）資料重定向與模組化適應**：PolyMorph 與「Retargeting the Object, Not the Hand」這類研究顯示，學界正逐漸擺脫對特定機器人本體硬體的強烈依賴，改以 URDF 模組化或本體無關（Body-free）的物件軌跡來擴充後訓練資料。
   - *後續問題*：如何將物件級別的重定向資料與底層高自由度靈巧手的動力學限制進行端到端的無縫對齊？
3. **模擬與現實的閉環優化（AutoRSR 與 Active Generative Simulation）**：自動化工作區掃描與元學習模擬資料生成（MetaGenSim）的結合，標誌著 Sim-to-Real 正在從「手動調整領域隨機化參數」邁入「依據下游效能自動演化模擬分佈」的新階段。
   - *後續問題*：這種自動生成的模擬資料分佈，是否會引入人類專家未曾預期的物理偏差（Sim-to-Real Artifacts），進而對極端控制策略造成負面影響？
