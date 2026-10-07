---
layout: post
title: "每日論文雷達｜2026-10-07"
date: 2026-10-07 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-07
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總數計 868 篇（經去重後為 770 篇），在時間窗內篩選出 30 篇候選論文，並針對具身模型與機器人控制完成評估。

## Must-Read

1. **EgoLAP: Learning from Egocentric Human Data through Language-Action Reasoning**
   - **作者**：Lihan Zha, Shresth Grover, Tenny Yin, Samuel M. Bateman, Hengkai Pan
   - **來源**：[arXiv:2610.08726](https://arxiv.org/abs/2610.08726)
   - **重點與關聯**：該研究探討如何利用第一人稱（egocentric）人類資料來擴展機器人學習，繞過直接將人類動作做為控制目標所面臨的具身落差（embodiment gap）。其核心見解在於將動作意圖透過語言動作思維鏈（language-based action chain-of-thought）進行結構化與時間抽象化，藉此捕捉跨人類與機器人的任務相關結構。這對研究視覺-語言-動作模型（VLA）跨本體遷移的學者具備高度參考價值。

2. **DepthWorld: 3D World Model for Robot Manipulation**
   - **作者**：Jai Bardhan, Josef Sivic, Vladimir Petrik
   - **來源**：[arXiv:2610.08780](https://arxiv.org/abs/2610.08780)
   - **重點與關聯**：針對機器人操作所提出的 3D 世界模型。現今以影片為基礎的世界模型多半僅以 RGB 訓練，雖能逐格生成看似合理的畫面，卻無法組合成一致的 3D 世界。該論文引入校準管線，在結合大規模 3D 監督的同時不破壞預訓練影片先驗，為策略評估與規劃提供更具幾何一致性的資料驅動替代方案。

3. **ReDex: Repairing Sim-to-Real Dexterous Policies by Finger-Level Compliant Interaction**
   - **作者**：Jinzhou Li, Hadi Tabatabaee, Kelin Yu, Yuyin Sun, Cheng-Hao Kuo
   - **來源**：[arXiv:2610.07525](https://arxiv.org/abs/2610.07525)
   - **重點與關聯**：針對靈巧手操作（dexterous manipulation）模擬到真實世界（sim-to-real）轉移時，常因接觸時機與力道調節誤差而失敗的問題。ReDex 允許操作員在真實世界執行時，透過順應控制（compliant control）對特定手指的接觸失敗進行實體修正並結合觸覺回饋，保留原本模擬訓練策略的多指協調能力。

## Highly Relevant

1. **WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses**
   - **作者**：Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen, Dung D. Le, Ngo Anh Vien
   - **來源**：[arXiv:2610.08526](https://arxiv.org/abs/2610.08526)
   - **摘要重點**：提出適用於智慧倉庫中無人機（UAV）導航與人員追蹤的視覺-語言-動作框架及擬真資料集，填補了語言條件化控制無人機連續低階飛行動作的基準缺口。

2. **SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining**
   - **作者**：Jicong Ao, Shuhan Jiang, Yuling Zhong, Yanwen Liu, Yuhan Gao
   - **來源**：[arXiv:2610.07652](https://arxiv.org/abs/2610.07652)
   - **摘要重點**：關注具身智慧系統與關節式物件（articulated objects）的互動，透過大規模合成預 training 來實現零樣本（zero-shot）的 Sim-to-Real 關節物件操作，解決真實世界示範資料收集不易的問題。

3. **ViDAL: A Visual Dynamics-Grounded Action Latent Space for Vision-Language-Action Models**
   - **作者**：Yuan Xu, Yixiang Chen, Qisen Ma, Jiabing Yang, Peiyan Li
   - **來源**：[arXiv:2610.08150](https://arxiv.org/abs/2610.08150)
   - **摘要重點**：指出現有 VLA 模型在動作表徵上較少考慮動作引起的視覺動態，因而提出 ViDAL，將連續動作潛在空間錨定在場景未來的視覺動態中。

4. **RoboCap: A New Platform for Egocentric Robot Learning**
   - **作者**：Grounded Superintelligence, BitRobot
   - **來源**：[arXiv:2610.07217](https://arxiv.org/abs/2610.07217)
   - **摘要重點**：為野外第一人稱資料收集設計了 250g 的六鏡頭雙 IMU 帽子硬體，並搭配專屬 3D 演算法，解決大規模收集具身操作資料時硬體與精確度的落差。

5. **Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution**
   - **作者**：Ahin Lee, Jinwoo Seo, Youngsoo Jang, Taesik Gong
   - **來源**：[arXiv:2610.07946](https://arxiv.org/abs/2610.07946)
   - **摘要重點**：提出自我監督適應方法 SALT，利用 VLA 動作切片中未執行的剩餘軌跡（leftover trajectory）作為測試時適應（test-time adaptation）的監督信號，應對執行時未知的視覺干擾。

6. **MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation**
   - **作者**：Suzannah Wistreich, Stephen Tian, Isabella Huang, Vitor Campagnolo Guizilini, Sergey Zakharov
   - **來源**：[arXiv:2610.07511](https://arxiv.org/abs/2610.07511)
   - **摘要重點**：針對移動操作（mobile manipulation）提出生成式資料增強框架，將單一機器人姿態下收集的示範轉換為多樣化視角與姿態，改善部署時因公分數偏差導致的效能下降。

7. **BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation**
   - **作者**：Zexi Zhang, Zecheng Zhu, Zidong Chen, Zulkhuu Tuya, Stephen James
   - **來源**：[arXiv:2610.07594](https://arxiv.org/abs/2610.07594)
   - **摘要重點**：將 BiGym 適應至 Unitree G1 人形機器人，涵蓋 20 個家務任務並提供 VR 示範，用於基準測試 VLA 微調、模仿學習與強化學習等演算法。

## Interesting

1. **WareFly-VLA 的無人機語意控制**：將 VLA 模型從常見的地面移動與機械臂操作擴展至無人機的連續低階飛行控制，顯示出多模態動作生成框架在空中載具應用的可行性，但實際載重與即時性限制資料未提供進一步說明。
2. **RoboCap 的穿戴式硬體整合**：透過輕量化硬體（250g 內建六鏡頭與雙 IMU）嘗試解決野外第一人稱資料收集的瓶頸，其工程實作為資料擴展提供了另一種硬體層面的思考方向。

## Idea Sparks

1. **跨模態意圖與視覺動態的結合**：
   - 觀察：EgoLAP 透過語言動作思維鏈捕捉跨本體的運動意圖，而 ViDAL 則是將動作潛在空間與未來的視覺動態對齊。
   - 後續問題：若將 EgoLAP 的「語言化動作意圖」與 ViDAL 的「視覺動態基礎潛在空間」進行架構上的融合，是否能進一步提升 VLA 模型在面對未見環境或動態干擾時的零樣本泛化能力？

2. **Sim-to-Real 互動修正與資料擴增的互補**：
   - 觀察：ReDex 依賴人類在真實世界互動中進行手指層級的順應性修正，而 MobileVISTA 則透過生成式資料增強來解決姿態泛化問題。
   - 後續問題：能否利用 ReDex 在真實世界中透過互動修正所收集到的少量實體接觸與力回饋失敗案例，作為 MobileVISTA 這類生成式資料擴增框架的引導目標，以自動化合成更具接觸魯棒性的模擬資料集？
