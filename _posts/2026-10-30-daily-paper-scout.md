---
layout: post
title: "每日論文雷達｜2026-10-30"
date: 2026-10-30 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-30
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 1,431 篇論文，經過去重與篩選後共取得 858 篇新候選文，其中評估並接受 132 篇，精選出 18 篇最具代表性的研究成果深入解析。

---

## Must-Read

### SimRetract: Zero-Shot Sim-to-Real Robotic Assistance for Retractor Take-Over in Open Surgery
- **作者**：Xucheng Wang, Zhizhou Yang, Sung Eun Kim, Romain Hardy, Michael P. Sampson
- **連結**：[arXiv:2610.38234](https://arxiv.org/abs/2610.38234)
- **來源**：`arxiv_cs.RO`
- **技術突破與啟發**：
  本篇論文實現了手術機器人與外科醫生在開放式手術中協作任務（如牽開器交接）的首個零樣本 (zero-shot) 模擬到真實世界轉移（Sim-to-Real）。透過僅在模擬演示中訓練的策略，機器人手臂能夠在交接時接手牽開器並維持穩定牽引，完全無需真實世界的微調或昂貴的人類示範。其關鍵創新在於 SimRetract 框架設計了專為轉移優化的模擬演示，讓策略觀察帶有遮罩的動態。這項研究為高精度、高風險醫療機器人領域提供了突破性的範例，證明透過精巧的模擬環境設計，能有效避開真實世界標註成本高昂的瓶頸。

---

## Highly Relevant

### CAPTURER: A Dexterous Aerial Manipulator for Dynamic and Precise Grasping across Diverse Environments
- **作者**：Meng Wang, Jindou Jia, Sicheng Zhou, Zeshuai Chen, Kexin Guo
- **連結**：[arXiv:2610.39119](https://arxiv.org/abs/2610.39119)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：提出具備公分級抓取能力的靈巧空中操作器，克服動態目標運動、定位飄移與動態耦合等挑戰，推進多元環境下的空中動態抓取。

### Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand
- **作者**：Arth Shukla, Kehlani Fay, Huaze Liu, Darin Djapri, Alexiy Buynitsky
- **連結**：[arXiv:2610.39044](https://arxiv.org/abs/2610.39044)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：針對人形機器人提出能夠透過單一自我中心相機進行動態物件接球的 Sim-to-Real 框架，能泛化至未見過、具備不同幾何與物理屬性的物體。

### SimTO-Robust: Automated Design of Soft Grippers Robust to Grasp Pose and Object Geometry
- **作者**：Kurt Enkera, Joshua Pinskier, Marcus Gallagher, David Howard
- **連結**：[arXiv:2610.39560](https://arxiv.org/abs/2610.39560)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：結合模擬驅動拓樸最佳化（SimTO），自動化設計對抓取姿態與物件幾何具備高強健性的軟性夾爪機械結構。

### Humanoid Dodgeball: Learning Fast Dynamic Obstacle Avoidance Motions for Humanoids
- **作者**：Aoqian Zhang, Chunzheng Wang, Haoran Chen, Annan Tang, Cheng Xiang
- **連結**：[arXiv:2610.40003](https://arxiv.org/abs/2610.40003)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：透過強化學習（RL）框架實現人形機器人的敏捷躲避球動作，兼顧快速動態障礙物規避、全身穩定性與自然動態。

### ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation
- **作者**：Shiqi Liu, Radu Corcodel, Ding Zhao
- **連結**：[arXiv:2610.38388](https://arxiv.org/abs/2610.38388)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：利用四足操作任務中的持續失敗作為觸發點，透過編碼代理（Coding Agent）自動識別並獲取缺失的全身控制能力與強化學習策略。

### Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory
- **作者**：Kai Sheng, Liuyi Wang, Jinlong Li, Haojie Dai, Chengju Liu
- **連結**：[arXiv:2610.39446](https://arxiv.org/abs/2610.39446)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：提出 EvoLife 導航框架，結合混合動作空間與持續記憶，賦予多模態具備自主互動與終身學習能力的導航代理。

### Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling
- **作者**：Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li
- **連結**：[arXiv:2610.39232](https://arxiv.org/abs/2610.39232)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
- **核心亮點**：GenSight 透過預訓練影片擴散 Transformer，將未來影片生成與密集 4D 感知整合至單一架構中，作為具備強大世界模型的基礎。

### OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation
- **作者**：Junli Liu, Zhongrui You, Chenhui Li, Zhen Li, Yuyang Tian
- **連結**：[arXiv:2610.39287](https://arxiv.org/abs/2610.39287)
- **來源**：`arxiv_cs.RO`, `arxiv_keyword`
- **核心亮點**：設計一體化的機載視覺-語言-動作（VLA）模型，使飛行機器人能在資源受限的平台上執行端到端的語意理解與導航。

### OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels
- **作者**：Francesco Iotti, Alok Ranjan, Franco Angelini, Manolo Garabini
- **連結**：[arXiv:2610.38502](https://arxiv.org/abs/2610.38502)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：整合輪式與腿式優勢，提出配備全向輪的混合型機器人，兼具室內高效移動與地形適應能力。

### METATRON: A Promptable Whole-Body Execution Layer for Humanoids
- **作者**：Chen Tessler, Yifeng Jiang, Alec Otto, Yi Shi, Umar Iqbal
- **連結**：[arXiv:2610.38027](https://arxiv.org/abs/2610.38027)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
- **核心亮點**：Metatron 提供可提示（Promptable）的全身執行層，結合生成式基礎策略與可編程式技能層，統一管理人形機器人的動態行為。

### SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing
- **作者**：Yunchu Zhang, Ray Song, Junhan Jiao, Liyiming Ke, Yuchen Yang
- **連結**：[arXiv:2610.40646](https://arxiv.org/abs/2610.40646)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：以工具為中心發展模組化末端執行器系統，結合低成本轉接器與觸覺感知，實現日常生活中複雜工具的自主切換與操作。

### LLM-guided Planar Loco-Manipulation for Quadruped Robots
- **作者**：Georges Jetti, Michael Khayyat, Jean-Pierre Sleiman, Stefano Arrigoni, Francesco Braghin
- **連結**：[arXiv:2610.40248](https://arxiv.org/abs/2610.40248)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`
- **核心亮點**：利用大語言模型（LLM）引導四足機器人在雜亂環境中進行平面定位與基於物理互動的操縱規劃。

### Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection
- **作者**：Li Guan, Rachael Granberry, Sahar Aseeri, Sahar Rostami, Taylor Niehues
- **連結**：[arXiv:2610.39076](https://arxiv.org/abs/2610.39076)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.LG`
- **核心亮點**：開發超薄 3D 針織觸覺與姿態感測手套，兼顧指尖力回饋與抗遮擋手部追蹤，解決靈巧操作數據收集的痛點。

### Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors
- **作者**：Liangyu Li, Qingwen Liu
- **連結**：[arXiv:2610.40401](https://arxiv.org/abs/2610.40401)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`, `arxiv_cs.LG`
- **核心亮點**：提出連續動作世界模型（CoAWM），透過跨本體（Cross-Embodiment）函數預訓練學習通用的時空動態先驗。

### Self-Supervised Doppler-Guided RF Odometry
- **作者**：Kunzhe Song, Jialuo Du, Jingkai Lin, Huacheng Zeng
- **連結**：[arXiv:2610.39005](https://arxiv.org/abs/2610.39005)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`
- **核心亮點**：RFWalk 實現了自監督、純無線電頻率（RF）的里程計估測，在黑暗或煙霧等惡劣環境下利用都卜勒效應提供穩健的自我動態定位。

### PhysVLMM: Interaction-Conditioned Physical Belief Maps for Articulated Objects in Robot Scene Maps
- **作者**：Dibyendu Ghosh
- **連結**：[arXiv:2610.40539](https://arxiv.org/abs/2610.40539)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：在視覺-語言-動作地圖中引入基於互動的物理信念圖，使移動機器人能針對關節型物件（如門、抽屜）維持機率式的動力學後驗估計。

### DAWN: Diffusion-based Alignment and unfastening Workflow Network
- **作者**：Hemant Kumar, Piyush Goenka, Nikhil Chopra
- **連結**：[arXiv:2610.40537](https://arxiv.org/abs/2610.40537)
- **來源**：`arxiv_cs.RO`
- **核心亮點**：DAWN 是一個基於擴散模型的階層式機器人框架，專門用於處理回收與拆卸場景中高精度的螺絲鬆開等接觸密集型任務。

---

## Interesting

*(本期無納入評分較低或關聯間接之邊際論文)*

---

## Idea Sparks

1. **跨本體世界模型的函數空間對齊**
   - **觀察**：從 `Continuous-Action World Models` 等研究顯示，將不同硬體本體與採樣頻率的動作軌跡對齊至共享函數空間，能有效提取通用的動態先驗。
   - **具體後續問題**：當引入形態學差異極大的新本體（例如從四足轉換到仿生靈巧手）時，此共享函數空間的零樣本泛化極限在哪裡？如何設計動態擴充機制來避免負遷移？
2. **從任務失敗中自主生成控制策略（Agentic Controller Acquisition）**
   - **觀察**：`ELEVATE` 提出在任務執行失敗時，透過編碼代理自動構建與最佳化強化學習環境以補足缺失技能的思路，展現了具備自我演化能力的軟體架構。
   - **具體後續問題**：這種由高層語言代理自動發起並驗證底層控制器的機制，能否即時應用於動態且具安全critical的真實世界互動任務中，而不導致機器人硬體損壞？
3. **多模態感知與物理信念地圖的融合**
   - **觀察**：結合視覺-語言-動作與物理信念（如 `PhysVLMM`）顯示，機器人地圖正從單純的語意標記轉向對物體動態互動行為的機率推論。
   - **具體後續問題**：如何在具備高自由度的連續互動過程中，即時更新並壓縮這些物理信念，以符合即時路徑規劃與操作控制的運算頻寬需求？
