---
layout: post
title: "每日論文雷達｜2026-10-07"
date: 2026-10-07 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-07
- **主題**：具身智慧（Embodied Intelligence）
- **收錄數量**：本次爬取總計 868 篇論文，經過重複刪除與篩選後，取得 30 篇候選文，並精選出 10 篇與具身智慧、視覺語言動作模型（VLA）、模擬到真實轉移（Sim-to-Real）及靈巧操作高度相關的研究進行深度追蹤與分析。

## Must-Read

### 1. VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation
- **作者**：Yutian Zhang, Xingrui Xiong, Siyuan Ma, Yang Li, Jiawen Wen
- **連結**：[arXiv:2610.08220](https://arxiv.org/abs/2610.08220)
- **來源**：arxiv_cs.RO, arxiv_cs.AI
- **重點與關聯**：
  這篇論文針對行動操作（mobile manipulation）中資料稀缺的問題，提出名為 VOMMI（Visual-Odometry-Conditioned Mobile Manipulation Interface）的可攜式示範收集方法。研究指出，直接使用視覺里程計（VO）軌跡容易因累積漂移與不完美的動作監督而產生不一致性。VOMMI 旨在透過 RGB 觀察提供可靠且具成本效益、無須依賴額外感測硬體的動作監督。對於研究行動操作與真實世界資料收集的學者而言，這項工作提供了克服硬體限制、擴展資料集規模的實用方案。

### 2. ReDex: Repairing Sim-to-Real Dexterous Policies by Finger-Level Compliant Interaction
- **作者**：Jinzhou Li, Hadi Tabatabaee, Kelin Yu, Yuyin Sun, Cheng-Hao Kuo
- **連結**：[arXiv:2610.07525](https://arxiv.org/abs/2610.07525)
- **來源**：arxiv_cs.RO
- **重點與關聯**：
  靈巧操作（dexterous manipulation）政策在模擬環境中訓練後，常因接觸時機與力道調節的誤差而在真實世界中失效。ReDex 提出了一個修復框架，允許基於本體感覺（proprioception-only）的基礎政策在真實部署時，透過人類操作員在具備順應性控制（compliant control）的手指層級進行互動與糾錯，並納入觸覺回饋。此研究直接切中模擬到真實轉移（Sim-to-Real transfer）與多指協調的核心痛點。

### 3. DepthWorld: 3D World Model for Robot Manipulation
- **作者**：Jai Bardhan, Josef Sivic, Vladimir Petrik
- **連結**：[arXiv:2610.08780](https://arxiv.org/abs/2610.08780)
- **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_cs.CV
- **重點與關聯**：
  世界模型（world models）為機器人操作提供了一種資料驅動的模擬器替代方案。然而，現有的影片基底世界模型多數僅在 RGB 影像上訓練，雖然能產生逐幀看似合理的影片，卻無法組成具有一致性的 3D 世界。DepthWorld 結合了大規模 3D 操縱監督與能夠吸收該監督而不破壞強大預訓練影片先驗的架構，並透過校正管線來推進 3D 空間智慧在機器人任務中的應用。

### 4. VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models
- **作者**：Owen Du, Yang Yue, Jie Zhang, Jiaqi Pi, Chi Bene Chen
- **連結**：[arXiv:2610.08133](https://arxiv.org/abs/2610.08133)
- **來源**：arxiv_cs.RO, arxiv_cs.CV, arxiv_keyword
- **重點與關聯**：
  視覺語言動作（VLA）模型在機器人操作上表現優異，但每個控制步驟需處理長序列視覺 Token，導致運算成本高昂、難以即時部署。VLA-ACL（Action Consistency Learning）學習一個輕量化的視覺 Token 剪枝機制，直接針對動作一致性進行優化，避免了過去依賴啟發式評分或需對基礎 VLA 模型進行昂貴微調的缺點，對提升 VLA 模型推論效率具備高度參考價值。

## Highly Relevant

### 1. SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining
- **作者**：Jicong Ao, Shuhan Jiang, Yuling Zhong, Yanwen Liu, Yuhan Gao
- **連結**：[arXiv:2610.07652](https://arxiv.org/abs/2610.07652)
- **來源**：arxiv_cs.RO, arxiv_cs.AI
- **重點與關聯**：聚焦於具身智慧系統中對關節物件（articulated objects）的互動與零樣本模擬到真實轉移，透過大規模合成預training彌補實體資料收集的困難。

### 2. MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation
- **作者**：Suzannah Wistreich, Stephen Tian, Isabella Huang, Vitor Campagnolo Guizilini, Sergey Zakharov
- **連結**：[arXiv:2610.07511](https://arxiv.org/abs/2610.07511)
- **來源**：arxiv_cs.RO, arxiv_cs.CV
- **重點與關聯**：針對人形機器人等行動操作器在動態環境中，因機器人姿態微小偏差導致策略失效的問題，提出生成式資料增強框架以增強姿態泛化能力。

### 3. Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution
- **作者**：Ahin Lee, Jinwoo Seo, Youngsoo Jang, Taesik Gong
- **連結**：[arXiv:2610.07946](https://arxiv.org/abs/2610.07946)
- **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_keyword
- **重點與關聯**：提出自監督適應方法（SALT），利用動作區塊重疊產生的剩餘軌跡作為測試時適應（test-time adaptation）的監督信號，以應對 VLA 模型執行時遭遇的未知視覺干擾。

### 4. VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning
- **作者**：Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng
- **連結**：[arXiv:2610.08761](https://arxiv.org/abs/2610.08761)
- **來源**：huggingface, arxiv_cs.RO, arxiv_cs.AI
- **重點與關聯**：探討具身推理中的自我提升（self-improvement），透過策略、訓練課程與評判機制的共同演化（co-evolution）來擴展驗證能力。

## Interesting

### 1. ViDAL: A Visual Dynamics-Grounded Action Latent Space for Vision-Language-Action Models
- **作者**：Yuan Xu, Yixiang Chen, Qisen Ma, Jiabing Yang, Peiyan Li
- **連結**：[arXiv:2610.08150](https://arxiv.org/abs/2610.08150)
- **來源**：arxiv_cs.RO, arxiv_keyword
- **重點與關聯**：提出將 VLA 模型中的連續動作潛在空間（action latents）與場景未來的視覺動態進行錨定（grounding），超越單純模型化動作軌跡的傳統作法。

### 2. EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors
- **作者**：Harsh Gupta, Tyler Ga Wei Lum, Changhao Wang, Chuer Pan, C. Karen Liu
- **連結**：[arXiv:2610.07681](https://arxiv.org/abs/2610.07681)
- **來源**：arxiv_cs.RO, arxiv_cs.AI
- **重點與關聯**：探討靈巧操作的高維最佳化與強化學習中的探索難題，結合人類手部資料先驗以設計結構化探索策略。

## Idea Sparks

1. **視覺動態潛在空間與 3D 世界模型的結合**：
   - 觀察：`ViDAL` 將動作潛在空間錨定於未來視覺動態，而 `DepthWorld` 則強調世界模型需要具備一致的 3D 幾何結構。
   - 後續問題：若將 3D 幾何一致的世界模型（DepthWorld）與視覺動態動作潛在空間（ViDAL）整合，是否能進一步提升 VLA 模型在長序日、具空間互動任務中的長期預測與規劃穩定性？

2. **自我監督適應與手指層級順應性控制的互補性**：
   - 觀察：`Adapting VLA to Unknown Visual Disruptions` 利用剩餘軌跡進行測試時適應以應對視覺干擾，而 `ReDex` 透過手指層級的順應性互動修復實體接觸失敗。
   - 後續問題：能否將基於軌跡的視覺適應機制與實體接觸的觸覺順應控制（ReDex）結合，建構出能同時應對視覺環境突變與動態接觸誤差的閉環具身代理系統？
