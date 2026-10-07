---
layout: post
title: "每日論文雷達｜2026-10-07"
date: 2026-10-07 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-07
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 868 篇論文，經去重與候選篩選後，涵蓋 77 篇關鍵字吻合論文，本次選出 10 篇最具代表性之研究進行深度追蹤。
- **資料統計**：來源包含 Hugging Face (100)、arXiv cs.RO (250)、cs.AI (250)、cs.CV (250) 與額外關鍵字檢索 (18)。

## Must-Read

本日未有論文跨越 80 分的 Must-Read 門檻，所有選出之優秀研究皆落於 Highly Relevant 區段。

## Highly Relevant

- **EgoLAP: Learning from Egocentric Human Data through Language-Action Reasoning**
  - **作者**：Lihan Zha, Shresth Grover, Tenny Yin, Samuel M. Bateman, Hengkai Pan
  - **連結**：[arXiv:2610.08726](https://arxiv.org/abs/2610.08726)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
  - **摘要證據**：本篇探討利用第一人稱（Egocentric）人類資料來擴展機器人學習，繞過高昂的機器人實體示範成本。透過引入基於語言的動作思維鏈（language-action chain-of-thought），將動作意圖表示為結構化且時間上抽象的型態，以跨越人類與機器人之間的具身落差（embodiment gap）。

- **ReDex: Repairing Sim-to-Real Dexterous Policies by Finger-Level Compliant Interaction**
  - **作者**：Jinzhou Li, Hadi Tabatabaee, Kelin Yu, Yuyin Sun, Cheng-Hao Kuo
  - **連結**：[arXiv:2610.07525](https://arxiv.org/abs/2610.07525)
  - **來源**：`arxiv_cs.RO`
  - **摘要證據**：針對靈巧操作政策在模擬訓練後因接觸時機與施力調節誤差而難以轉移到真實世界的痛點，ReDex 提出在真實世界滾動期間透過人為操作員進行基於順應控制（compliant control）的手指層級修正，以修復局部接觸失敗並納入觸覺回饋。

- **WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses**
  - **作者**：Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, Dung D. Le, Ngo Anh Vien
  - **連結**：[arXiv:2610.08526](https://arxiv.org/abs/2610.08526)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
  - **摘要證據**：提出適用於無人機（UAV）在智慧倉庫中進行語言導引人類搜尋、定位與追蹤的視覺-語言-動作（VLA）框架與擬真資料集，結合了連續低階飛行動作與細粒度自然語言目標描述。

- **DepthWorld: 3D World Model for Robot Manipulation**
  - **作者**：Jai Bardhan, Josef Sivic, Vladimir Petrik
  - **連結**：[arXiv:2610.08780](https://arxiv.org/abs/2610.08780)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
  - **摘要證據**：指出當前基於 RGB 的影片世界模型在機械操作中無法組成一致 3D 世界的問題。作者導入校準管線與大規模 3D 監督架構，在不破壞強大預訓練影片先驗的情況下提升世界模型的 3D 幾何忠實度。

- **SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining**
  - **作者**：Jicong Ao, Shuhan Jiang, Yuling Zhong, Yanwen Liu, Yuhan Gao
  - **連結**：[arXiv:2610.07652](https://arxiv.org/abs/2610.07652)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
  - **摘要證據**：針對具身智慧系統中互動關節物件（articulated objects）缺乏大規模真實資料的挑戰，透過具備部分層級語意（part-level semantics）與關節限制設計的大規模合成資料與預訓練，實現零樣本（zero-shot）模擬到真實世界的轉移。

- **MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation**
  - **作者**：Suzannah Wistreich, Stephen Tian, Isabella Huang, Vitor Campagnolo Guizilini, Sergey Zakharov
  - **連結**：[arXiv:2610.07511](https://arxiv.org/abs/2610.07511)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
  - **摘要證據**：為了解決移動操作器（如人形機器人）在單一機器人姿態收集示範資料時，因部署時微小姿態偏差導致策略脆化的問題，提出 MobileVISTA 資料生成框架，將典型姿態下的示範轉化為多樣化的姿態分佈。

- **ViDAL: A Visual Dynamics-Grounded Action Latent Space for Vision-Language-Action Models**
  - **作者**：Yuan Xu, Yixiang Chen, Qisen Ma, Jiabing Yang, Peiyan Li
  - **連結**：[arXiv:2610.08150](https://arxiv.org/abs/2610.08150)
  - **來源**：`arxiv_cs.RO`, `arxiv_keyword`
  - **摘要證據**：指出現有 VLA 模型在動作表徵上較少考慮視覺動態，因此引入 ViDAL（Visual Dynamics-Grounded Action Latent Space），透過動作變分自動編碼器（Action VAE）將連續動作潛在空間錨定在場景未來的視覺動態中。

- **RoboCap: A New Platform for Egocentric Robot Learning**
  - **作者**：Grounded Superintelligence, BitRobot
  - **連結**：[arXiv:2610.07217](https://arxiv.org/abs/2610.07217)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
  - **摘要證據**：為了解決第一人稱操作資料稀缺的問題，推出重 250g、具備 6 個相機與雙 IMU 的穿戴式硬體帽子 RoboCap，並搭配 Grounded API 這套針對該硬體微調的設備無關 3D 演算法。

- **Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution**
  - **作者**：Ahin Lee, Jinwoo Seo, Youngsoo Jang, Taesik Gong
  - **連結**：[arXiv:2610.07946](https://arxiv.org/abs/2610.07946)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_keyword`
  - **摘要證據**：提出「Self-supervised Adaptation from Leftover Trajectories (SALT)」方法，利用先前動作區塊中未執行的剩餘軌跡（leftover trajectory）作為測試期適應的自監督信號，以應對機器人執行任務時遭遇未知視覺干擾的問題。

- **BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation**
  - **作者**：Zexi Zhang, Zecheng Zhu, Zidong Chen, Zulkhuu Tuya, Stephen James
  - **連結**：[arXiv:2610.07594](https://arxiv.org/abs/2610.07594)
  - **來源**：`arxiv_cs.RO`
  - **摘要證據**：推出適用於 Unitree G1 的 BiGym 2.0 模擬與基準測試套件，涵蓋 20 個跨家庭任務的統一全身控制器示範與評估，並提供 60 個原生人類虛擬實境示範及多視角記錄。

## Interesting

- **WareFly-VLA** 與 **BiGym 2.0** 分別將 VLA 應用於無人機（UAV）與人形機器人家庭環境，展現出具身智慧正快速跨足非典型地面移動載具與複雜全身協調控制。然而，此類模擬與專用硬體基準的實際泛化能力仍需更多真實世界資料驗證。

## Idea Sparks

1. **跨模態動作與視覺動態的對齊**：
   - 觀察：`EgoLAP` 利用語言動作思維鏈橋接人類與機器人意圖，而 `ViDAL` 則透過未來視覺動態來錨定動作潛在空間。兩者皆試圖解耦單純的低階控制訊號。
   - 後續問題：若將 `ViDAL` 的視覺動態基礎動作潛在空間與 `EgoLAP` 的語言化動作思維鏈結合，是否能進一步提升 VLA 模型在無標記第一人稱人類示範上的遷移效率？

2. **動態干擾適應與 Sim-to-Real 的互補**：
   - 觀察：`ReDex` 透過人機協同的實體順應互動來修復真實世界的接觸失敗，而 `SALT` 則利用動作區塊的殘留軌跡進行測試期適應。
   - 後續問題：是否能將 `SALT` 的自我監督殘留軌跡機制引入 `ReDex` 的觸覺與手指層級微調中，以減少對人類即時介入修正的依賴？
