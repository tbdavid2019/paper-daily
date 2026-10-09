---
layout: post
title: "每日論文雷達｜2026-10-09"
date: 2026-10-09 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-10-09
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 1524 篇論文，經過去重與候選篩選後，評估 250 篇，最終收錄 18 篇高相關與最具突破性之研究成果。

## Must-Read

1. **Autonomous thermodynamic cycles via robotic mobility and sensing**
   - **作者**：Sofia Kuperman, Ezra Ben-Abu, Yaron Veksler, Anna Zigelman, Sefi Givli
   - **來源與連結**：[arXiv:2610.11667](https://arxiv.org/abs/2610.11667)
   - **技術突破與啟發**：傳統熱力學循環受限於固定熱源與空間，本篇研究突破性地結合「機器人移動性與感知能力」，使機器人能主動在空間變化的溫度場中穿梭並自主執行熱力學循環。實驗上透過可循環系統的多穩態氣體填充膠囊來實現此概念，為具身智慧跨足能源轉換與物理環境互動開創了全新維度，啟發研究者思考具身機器人如何利用自身動態直接進行環境能量採集與熱力學運算。

2. **Cross-Embodiment Robot Foundation World Models with Latent Actions**
   - **作者**：Huang Huang, Sriram Yenamandra, Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan
   - **來源與連結**：[arXiv:2610.10846](https://arxiv.org/abs/2610.10846)
   - **技術突破與啟發**：針對不同機器人本體（Embodiments）與動作空間多樣性所帶來的模型泛化瓶頸，本篇提出潛在動作條件機器人世界模型（LAC-WM），透過在跨本體共學的統一潛在動作空間中運作，顯著提升世界模型適應未見過的新機器人本體之效能，超越傳統明確動作條件模型（EAC-WM），為跨本體基礎模型提供了強而有力的架構典範。

3. **UNITAS: A 3D-Native World Action Model for Embodied Manipulation**
   - **作者**：Ruixiang Wang, Yongyi Su, Wenlve Zhou, Bo Yue, Hengyan Liu
   - **來源與連結**：[arXiv:2610.12109](https://arxiv.org/abs/2610.12109)
   - **技術突破與啟發**：現有世界動作模型多建基於預訓練影片生成器，透過 2D 影像特徵來捕捉世界演化；然而機器人互動發生在度量 3D 空間中。本篇提出 `UNITAS`，作為首個 3D 原生的世界動作模型，成功將觀測、幾何與動作在 3D 空間中統一，解決了 2D 投影無法真實反映物理距離的痛點，為具身操作的空間智慧與長期預測提供扎實基礎。

4. **SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation**
   - **作者**：Kyoungin Baik, Youngwoon Lee
   - **來源與連結**：[arXiv:2610.11248](https://arxiv.org/abs/2610.11248)
   - **技術突破與啟發**：針對移動操作（Mobile Manipulation）中真實世界資料收集成本高昂的痛點，`SimVLA` 提出完全在合成模擬資料上進行端對端 VLA 訓練的框架，且無需任何遙操作（teleoperation）。透過預訓練於包含 35 種多樣化情境的 SimAction 等模擬資料集，實現了零樣本的 Sim-to-Real 遷移，大幅降低資料瓶頸，對具身基礎模型的規模化發展具重大啟發。

## Highly Relevant

1. **DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training**
   - **作者**：Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun
   - **來源與連結**：[arXiv:2610.12468](https://arxiv.org/abs/2610.12468)
   - **核心亮點**：結合影像空間條件與離線幾何校準，並導入反事實後訓練（Counterfactual Post-Training），解決世界模型在動作依從性與失敗互動覆蓋率不足的問題。

2. **REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models**
   - **作者**：Houlong Xiong, Zhenqi Qiu, Zechen Wang, Suohang Zhang, Yiyu Ren
   - **來源與連結**：[arXiv:2610.12007](https://arxiv.org/abs/2610.12007)
   - **核心亮點**：提出滾動去噪框架（Rolling Denoising），透過交錯流動時間步長（staggered flow timesteps）維持持久動作緩衝區，完美平衡了流動式 VLA 的長序列平滑性與高頻反應性。

3. **TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning**
   - **作者**：Bo Chen, Huanzhang Hu, Junyang Ma, Bo Yue, Fangdi Yu
   - **來源與連結**：[arXiv:2610.11945](https://arxiv.org/abs/2610.11945)
   - **核心亮點**：針對人類觸覺手套與機器人觸覺感測器在轉導原理與空間解析度上的異質性，提出以「接觸事件（contact events）」為層級的對齊系統，實現低成本且可擴展的觸覺示範轉移。

4. **CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding**
   - **作者**：Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan
   - **來源與連結**：[arXiv:2610.11971](https://arxiv.org/abs/2610.11971)
   - **核心亮點**：整合自監督能力推論與殘差強化學習，在無需特權資訊或任務特定重新訓練的情況下，讓凍結的 VLA 政策能夠適應關節故障等本體變異。

5. **PIER: An Evidence-Gated Execution Interface for Robotic Manipulation**
   - **作者**：Zoe Li, Anze Wang, Zhongyu Chen, Jingran Hu
   - **來源與連結**：[arXiv:2610.12123](https://arxiv.org/abs/2610.12123)
   - **核心亮點**：提出執行授權介面，將視覺／觸覺證據檢查與硬體控制分離，透過決定性閘門過濾高信心但受嚴重遮蔽的高風險動作輸出。

6. **SkillWeave: Weaving Heterogeneous Demonstrations into Long-Horizon Manipulation Skills**
   - **作者**：Ryosei Tamura, Xiaoxiang Dong, Uksang Yoo, Yuemin Mao, Romina Mir
   - **來源與連結**：[arXiv:2610.12046](https://arxiv.org/abs/2610.12046)
   - **核心亮點**：結合巨集遙操作與具身動覺教學（kinesthetic teaching），並透過物件遮罩條件擴散政策消除示範者存在帶來的視覺不匹配，實現長序列精確操作。

7. **VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation**
   - **作者**：Boyao Han, Chen Shi, Jingjing Qian, ZhuoTan Tian, Li Jiang
   - **來源與連結**：[arXiv:2610.12451](https://arxiv.org/abs/2610.12451)
   - **核心亮點**：解耦相機設置與動作學習，透過多信號目標視角預測將任意變動的 RGB 視角對齊至固定大小的潛在場景符元（scene tokens）。

8. **PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies**
   - **作者**：Qing Huang, Yifei Yang, Ziqing Zou, Anzhe Chen, Zhenjie Zhu
   - **來源與連結**：[arXiv:2610.11771](https://arxiv.org/abs/2610.11771)
   - **核心亮點**：借鏡傳統運動規劃的路徑-時間解耦思想，將 VLA 動作表示為進度索引互動路徑與正區間時間剖面，簡化遙操作資料後訓練的時序對齊。

9. **TAPNAV: Humanoid Navigation through Tactile Active Perception**
   - **作者**：Huaze Liu, Zhenyu Wu, Jaehwi Jang, Junjie Sheng, Andrew Collins
   - **來源與連結**：[arXiv:2610.10748](https://arxiv.org/abs/2610.10748)
   - **核心亮點**：針對無視覺環境（vision-denied environments），讓人形機器人透過觸覺主動探測周遭結構並結合資訊增益導向的局部探查，解決導航定位飄移問題。

10. **Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection**
    - **作者**：Lemon Foxmere, Anthony Furman, Yizheng Du, Oliver Chang, Leilani Gilpin
    - **來源與連結**：[arXiv:2610.10601](https://arxiv.org/abs/2610.10601)
    - **核心亮點**：提出三階段訓練方法，結合強化學習與模仿學習，透過對抗式任務選擇在四足機器人上合成多樣化技能（如行走、挖掘與跳躍）。

11. **Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement**
    - **作者**：Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
    - **來源與連結**：[arXiv:2610.12369](https://arxiv.org/abs/2610.12369)
    - **核心亮點**：將具身世界視為圖靈機（COAP），以程式碼直接測量、追蹤並實現機器人決策，跳脫傳統 VLA 迴圈，提供具身遞歸自我改進的新視角。

12. **Instance-anchored interaction evidence: Grounding robot plans in human pointing and handling**
    - **作者**：Xinliang Xiao, Bowen Yang, Wenjing Zhang, Li Yang, Wei Zhou
    - **來源與連結**：[arXiv:2610.12157](https://arxiv.org/abs/2610.12157)
    - **核心亮點**：透過實例錨定互動證據（IAE），利用背景遮罩傳播將最終場景物件與先前人類的指向／操作行為進行幾何對齊。

## Interesting

1. **A Reconfigurable Fabric Based Pneumatic Actuator with Button Fastened Constraint Modules for Multi Mode Actuation**
   - **作者**：Kentaro Kimura, Hiroki Ishizuka, Yusuke Sakaue, Sei Ikeda, Osamu Oshiro
   - **來源與連結**：[arXiv:2610.11054](https://arxiv.org/abs/2610.11054)
   - **亮點**：利用鈕扣固定的約束織物模組，在單一軟式氣動致動器上實現等向膨脹、收縮、彎曲等多種模式快速切換，提供軟體機器人硬體重構的新穎輕量作法。

2. **From Language to Motion: Task-Conditioned Focal-Stack Trajectory Integration for Microscopic Robots**
   - **作者**：Junjie Xie, Chuxuan He, Junkai Huang, Heng Zhang, Angen Ye
   - **來源與連結**：[arXiv:2610.12441](https://arxiv.org/abs/2610.12441)
   - **亮點**：探索微觀機器人（Microscopic Robots）領域，將語言指令映射至受限幾何算子，結合焦疊堆軌跡積分，實現零標註的微型物件語意導向操作。

## Idea Sparks

1. **跨本體與 3D 空間原生世界模型的融合**
   - **觀察**：近期研究如 `LAC-WM` 聚焦於透過潛在動作空間實現跨本體泛化，而 `UNITAS` 則強調 3D 空間原生（3D-native）的物理世界模擬。兩者分別解決了「跨不同機器人結構」與「解決 2D 投影失真」的痛點。
   - **具體後續問題**：如何將 3D 原生世界動作模型與跨本體潛在動作空間結合，打造一個既能適應任意機器人型態、又能精確在 3D 物理度量空間進行反事實預測的通用世界模型？

2. **從動作緩衝區優化到即時安全性驗證**
   - **觀察**：諸如 `REACT` 透過滾動去噪平衡了流動式 VLA 的長序列平滑與反應性，而 `PIER` 則透過證據閘門在執行前強制進行視覺／觸覺的證據檢查。這反映出學界正從「盲目預測流暢動作」轉向「具備動態修正與安全防線的閉環控制」。
   - **具體後續問題**：能否將即時滾動去噪的動作生成與證據閘門的驗證邏輯融合，設計出能在高頻反應過程中自動攔截並修正幻覺動作的防禦性 VLA 架構？

3. **由異質示範到自我改進的程式化具身智能**
   - **觀察**：`SkillWeave` 探討了將遙操作與動覺教學等異質示範進行編織的技術，而 `Embodied Turing Machines (COAP)` 則嘗試將具身狀態轉化為狀態碼（Code-Only-as-Policy）以達成遞歸自我改進。這顯示具身智能正逐步擺脫對單一大型黑盒子端到端網路的絕對依賴。
   - **具體後續問題**：如何利用異質示範所捕捉的細緻接觸資料，引導具身圖靈機（COAP）自動產生並最佳化長序列任務的程式碼策略？
