---
layout: post
title: "每日論文雷達｜2026-10-29"
date: 2026-10-29 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-10-29
- **主題**：具身智能（Embodied Intelligence）
- **收錄數量**：本次爬取總計 1312 篇論文，經去重與候選篩選後，評估 250 篇，最終採納 91 篇高度相關研究，涵蓋 VLA 模型、人形機器人控制、靈巧手與模擬到真實（Sim-to-Real）轉移等核心領域。

## Must-Read
本期選出 3 篇最具突破性與技術代表性的 Must-Read 論文，分別在 3D 原生世界模型、統一代理模型以及跨本體控制展現重要進展：

1. **[E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling](https://arxiv.org/abs/2610.36011)**
   - **作者**：X-Era AI Lab Team 等
   - **來源**：arxiv_cs.RO
   - **技術突破點**：現有的世界行動模型（WAMs）多數基於視訊或視覺語言模型（VLM），常將 3D 幾何特徵作為輔助輸入。該研究提出了 E0.5，一個直接建立在 3D 基礎模型之上的「幾何原生」世界行動模型，將幾何特徵提升為未來預測的核心基礎。
   - **研究啟示**：這項工作提醒研究者，擺脫 2D 影片模型的侷限、擁抱幾何原生的 3D 預測架構，可能是實現高空間智慧具身代理的關鍵路徑。

2. **[OmniBrain-0: A Unified Agentic Model for Embodied Intelligence](https://arxiv.org/abs/2610.36013)**
   - **作者**：Xiaomi Embodied Intelligence Team, Yuechen Luo, Chong He, Fang Li, Shaoqing Xu 等
   - **來源**：arxiv_cs.CV
   - **技術突破點**：為解決通用具身智能在長時序任務中協調多樣化技能與錯誤恢復的難題，本篇論文推出了 OmniBrain-0，一個輕量化的統一具身代理模型。它透過共享的高階決策模型，將任務理解、規劃、進度追蹤與反饋驅動的恢復機制無縫整合。
   - **研究啟示**：證明了透過輕量化架構將高階決策與具體操作（導航與操作）結合，能夠在不依賴高成本多模態推理的情況下，兼顧任務層級的可靠性。

3. **[ActiveAlign: Aligning Egocentric Manipulation via Active Perception](https://arxiv.org/abs/2610.36859)**
   - **作者**：Ri-Zhao Qiu, Bowen Wen, Yifeng Jiang, Chen Tessler, Eric Heiden 等
   - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_cs.CV
   - **技術突破點**：針對 Real2Sim2Real 轉換中因被動感知產生的真實落差（Real2Sim gap），該研究借鏡人類主動探索的精神，提出 ActiveAlign。透過 ActiveAlign-Waving 進行主動手眼校準（結合主動手部運動與可微分渲染），有效提升第一人稱視角下的操作對齊能力。
   - **研究啟示**：將主動感知（Active Perception）與可微分渲染整合至資料對齊流程，為減少 Sim-to-Real 差距提供了一個強大且具互動性的解方。

## Highly Relevant
以下為高度相關且架構扎實的核心論文：

- **[Whole-Body Humanoid Control via Stochastic Motion Tokenization](https://arxiv.org/abs/2610.36452)**：探討人形機器人全身控制，利用隨機動作標記化解決速度指令 RL 政策在複雜行為轉換時的資訊不足問題。
- **[A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation](https://arxiv.org/abs/2610.36789)**：提出 Torch-Hand，具備 21 個自由度與連桿驅動的人形靈巧手，兼顧解剖學結構與機械負載能力。
- **[REACH: An RL-based Hierarchical Humanoid Crawling Framework for Adaptable Confined Space Traversal](https://arxiv.org/abs/2610.36546)**：實現 Unitree G1 人形機器人在狹窄空間中的高矮適應與爬行穿越。
- **[Learning Visuomotor Quadrotor Flight Through Dynamic Narrow Gaps via Differentiable Simulation](https://arxiv.org/abs/2610.37557)**：利用可微分模擬訓練四軸飛行器，直接透過車載視覺與慣性量測穿過動態狹窄縫隙。
- **[A Bi-level Co-design Framework for Lunar Monoped with 2D Jump and Landing Control](https://arxiv.org/abs/2610.37199)**：研究月球低重力環境下的單足機器人雙層共設計（Co-design）框架。
- **[Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization](https://arxiv.org/abs/2610.36270)**：擴展 PPO 以訓練單一政策，執行包含蹲伏、抓取與 locomotion 的多階段全身協同操作任務。
- **[HC2Robot: Hyper-Connection Transformers with Predicted Foresight for Multi-Terrain Humanoid Parkour](https://arxiv.org/abs/2610.36825)**：提出部署型具備預測能力的非對稱 actor-critic 架構，支援人形機器人進行多地形跑酷。
- **[EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance](https://arxiv.org/abs/2610.37582)**：開發視覺驅動的超額具身機械拇指（Supernumerary Robotic Thumb），擴充人類單手操作能力。
- **[RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty](https://arxiv.org/abs/2610.37111)**：針對空拍機器人在定位不確定性下的快速主動視覺探索與 SLAM 系統。
- **[Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos](https://arxiv.org/abs/2610.36615)**：提出 HumiTransfer 框架，將野外人與人互動影片轉化為具身人形的真實互動。
- **[RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning](https://arxiv.org/abs/2610.36685)**：利用矢狀面鏡像（Sagittal Mirroring）實現單臂到雙臂學習的零樣本（Zero-Shot）資料轉換。
- **[RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](https://arxiv.org/abs/2610.36533)**：透過多層次物理理解引導 LLM 進行自主機器人程式碼搜尋與生成。
- **[From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement](https://arxiv.org/abs/2610.36681)**：結合不確定性引導優化的軟體模組化機器人學習式逆向設計。
- **[Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction](https://arxiv.org/abs/2610.37441)**：透過多代理人強化學習共同調適髖關節外骨骼，以降低使用者步行代謝消耗。
- **[When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate](https://arxiv.org/abs/2610.36852)**：探討黑盒子機器人政策失效時，如何透過透明代理模型在線診斷與修復受損感測器輸入。

## Interesting
此區收錄構想獨特但關聯較間接的研究，提供跳脫傳統框架的思考角度：
- **資料未提供**（註：本期篩選結果中所有被收錄之論文皆具備高相關性與實證導向，故暫無歸類於邊緣或小眾但低支撐的條目）。

## Idea Sparks
1. **幾何原生 3D 世界模型與傳統視訊模型的融合**：
   - *觀察*：如 E0.5 等研究顯示，將 3D 幾何特徵提升至模型底座核心（而非單純作為視訊或 VLM 的輔助）能更準確地進行未來預測。這挑戰了現今高度依賴 2D 影片生成作為世界模型的趨勢。
   - *後續問題*：當 3D 幾何特徵作為原生基礎時，模型在面對動態光影變化或未見過材質的物體表面時，其泛化能力是否會優於純視覺基礎模型？
2. **主動感知作為 Sim-to-Real 的橋樑**：
   - *觀察*：ActiveAlign 等研究強調「主動互動」能有效修正感測與校準誤差。這意味著傳統被動等待模擬器完美的思路正在轉變為讓代理主動去探測環境不確定性。
   - *後續問題*：這種主動校準機制的計算開銷（如可微分渲染的耗時）是否能在高頻率的實體機器人控制迴圈中實現即時線上（Online）部署？
3. **從單臂資料零樣本遷移至雙臂與複雜本體**：
   - *觀察*：RoboSTD 利用矢狀面鏡像解決單雙臂之間的資料鴻溝，顯示出利用幾何對稱性擴充訓練資料庫的高效性。
   - *後續問題*：這種幾何對稱性假設在面對非對稱任務（如非平衡負載或異質雙臂協同）時，應如何設計自適應修正機制？
