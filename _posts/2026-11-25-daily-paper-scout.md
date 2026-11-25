---
layout: post
title: "每日論文雷達｜2026-11-25"
date: 2026-11-25 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-11-25
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次檢索共爬取 1,466 篇論文，去重複後剩餘 1,140 篇候選，經過決定性評估（Decision Evaluated）共 250 篇，其中 234 篇被納入評分追蹤。本日嚴選出最具突破性的 3 篇 Must-Read 論文、15 篇 Highly Relevant 核心論文，涵蓋世界模型與代理協同設計、跨具體型操作、具身安全防護與模擬環境擴展等前沿方向。

## Must-Read

### 1. Innata-0: A Native Embodied World System with Model-Agent Co-Design
- **作者**：Innata Team, Yu Bai, Ziyi Bai, Yuxuan Cai, Chenrui He
- **連結**：[arXiv:2611.30254](https://arxiv.org/abs/2611.30254)
- **來源**：huggingface, arxiv_cs.RO
- **技術突破與啟發**：
  獨立的基礎模型在處理長序列（long-horizon）任務時往往會面臨複合誤差，而簡單地將模型與代理（agent）拼接又容易導致高階規劃與底層實體控制脫節。本文提出原生具身世界系統 Innata-0，透過共同設計（co-design）具身世界動作模型與代理，結合彼此互補優勢。其採用的 Innata-0-WAM 核心架構引入了三塔混合變壓器（tri-tower Mixture-of-Transformers）架構，為世界模型的動態預測與長跨度動作對齊提供了極佳的解法，對具身基礎模型的架構設計具有高度啟發性。

### 2. MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model
- **作者**：Rongze Tang, Chenyu Zhou, Jianjie Fang, Ziming Liu, Zhaolu Wang
- **連結**：[arXiv:2611.29501](https://arxiv.org/abs/2611.29501)
- **來源**：arxiv_cs.RO
- **技術突破與啟發**：
  世界動作模型（WAMs）在單一機器人操作任務中表現亮眼，但面對需要跨非交錯工作空間、耦合時序以及異質具體型（heterogeneous embodiments）的多機器人協作時往往無所適從。MAWAM 創新性地提出了多代理世界動作模型，實現了「聯合想像（joint imagination）」。它透過對未來互動進行時空對齊，同時保有各機器人個體與角色身分的感知，解決了過去分散式政策、扁平集中式模型與多機器人 VLA 無法兼顧全域協調與獨立本體特徵的痛點。

### 3. DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models
- **作者**：Sichen Wu, Qian Sun, Mengfan Liu, Weikai Qin, Bike Zhu
- **連結**：[arXiv:2611.32665](https://arxiv.org/abs/2611.32665)
- **來源**：arxiv_cs.RO, arxiv_keyword
- **技術突破與啟發**：
  人形機器人的全身控制（WBC）需要極高的動態平衡與全身協調，然而現有的階層式人形 VLA 通常將動態生成與物理執行切斷，使得追蹤與平衡誤差無法直接回饋優化 VLA 生成器。DiffGR00T 提出了一種端到端的可微分訓練框架，將 GR00T N1.7 與預訓練全身行為基礎模型 SONIC 緊密耦合。透過替換傳統不可微分的控制環路，實現了執行感知（execution-aware）的可微分訓練，為全身 VLA 的閉環最佳化開啟了新路徑。

## Highly Relevant

### 1. EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution
- **作者**：Zehao Liu, Huashuo Lei, Xi Lin, Haoang Li, Yuliang Chen
- **連結**：[arXiv:2611.30004](https://arxiv.org/abs/2611.30004)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：探討具身 AI 在不更改指令或模型情況下，僅透過環境中物體重新配置（environment-only object rearrangements）所帶來的安全隱患，提出診斷性框架 EnvTrap。

### 2. RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments
- **作者**：Jinkun Liu, Yingze Wang, Situ Wang, Deyao Hong, Mingju Gao
- **連結**：[arXiv:2611.31002](https://arxiv.org/abs/2611.31002)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：為了解決代理機器人（Agentic Robotics）缺乏大規模可執行環境的痛點，推出包含 10,807 個互動、可重置與可驗證物理環境的 RoboUniverse-10K 資料集與 Real2Sim 管線。

### 3. OmniAct: One Policy, One Million Embodiments
- **作者**：Xiang Fan, Yuheng Wang, Jiayuan Yan, Bohan Fang, Wisdom Oluchi Ikezogwo
- **連結**：[arXiv:2611.33158](https://arxiv.org/abs/2611.33158)
- **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_cs.CV, arxiv_cs.LG
- **摘要與亮點**：引入直接以每個機器人在特定場景中的運動學圖（kinematic graph）進行條件 conditioning 的跨具體型操作政策，將關節位置納入策略生成的依據。

### 4. BARE: Body-Aware Reflexive Evasion for Humanoid Robots
- **作者**：Zihao Li, Tong Chen, Hua Song, Zitong Ding, Zihao Xu
- **連結**：[arXiv:2611.32642](https://arxiv.org/abs/2611.32642)
- **來源**：arxiv_cs.RO, arxiv_cs.AI
- **摘要與亮點**：針對人形機器人動態避障需求，提出利用豐富關節進行局部身體調整（localized body adjustments）的反射式躲避策略，減少執行時間與所需空間。

### 5. EmboEagle: An Efficient Agentic Embodied Framework for Long-horizon Robotic Manipulation
- **作者**：Fan Xu, Zhongtao Wang, Hao Wu, Yitong Zhu, Wenzhuo Ma
- **連結**：[arXiv:2611.31173](https://arxiv.org/abs/2611.31173)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：結合子任務條件化 WAM 控制、潛在空間自適應監督與記憶引導幾何恢復，解決長序列機器人操作中的複合物理誤差。

### 6. MoMa-NMP: Scene-Scale Neural Motion Planning for Mobile Manipulators
- **作者**：Adam Kan, Jason Jingzhou Liu, Jiahui Yang, Kenneth Shaw, Deepak Pathak
- **連結**：[arXiv:2611.29913](https://arxiv.org/abs/2611.29913)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：提出 MoMa-DemoSmith 示範生成管線，解決移動機械臂（mobile manipulators）在房間規模環境中進行場景級神經運動規劃的示範資料匱乏問題。

### 7. PushMimic: Learning Adaptive Humanoid Box Pushing via Dynamic Motion Augmentation and Reference Distillation
- **作者**：Yulun Zhuang, Hanyu Zhang, Jingyu Liu, Yanran Ding
- **連結**：[arXiv:2611.30077](https://arxiv.org/abs/2611.30077)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：提出透過動態運動擴增與參考蒸餾，讓人形機器人在未知箱體質量與坡度下，自適應調整推箱姿勢的 PushMimic 框架。

### 8. CHAMP: Coordinated Humanoid Loco-Manipulation with Whole-Body Motion Priors
- **作者**：Lijun Han, Muyuan Ma, Zichen Wang, Siyuan Liu, Yuxi Liu
- **連結**：[arXiv:2611.30449](https://arxiv.org/abs/2611.30449)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：結合全身運動預訓練與自適應特徵提取，利用約 2,298 小時的異質人類與機器人資料達成協調式移動操作。

### 9. EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI
- **作者**：Erfei Cui, Shengjia Zhao, Yan Qin, Kaixuan Wang, Junming Chen
- **連結**：[arXiv:2611.33054](https://arxiv.org/abs/2611.33054)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：推出包含 1,092 個快照任務與 540 個軌跡任務的 EmbodiSafety 基準，全面評估具身基礎模型在多種情境下的風險理解與反應模式。

### 10. DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation
- **作者**：Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias
- **連結**：[arXiv:2611.30907](https://arxiv.org/abs/2611.30907)
- **來源**：arxiv_cs.RO, arxiv_cs.CV, arxiv_cs.LG
- **摘要與亮點**：利用點雲觀測與對比學習，直接從重標定的人類操作示範中學習 3D 跨具體型連續潛在動作世界模型。

### 11. RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments
- **作者**：Zheng Sun, Zhuo Li, Zhihao Li, Hengyi Sim, Ge Wang
- **連結**：[arXiv:2611.31894](https://arxiv.org/abs/2611.31894)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：提出僅需單一真實示範，即可重建接觸豐富的模擬世界並自我改進跨具體型技能的框架。

### 12. One Policy, Many Bodies: Cooperative Human-Object Interaction with Heterogeneous Teams
- **作者**：Zhihao Cao, Tianxu An, Chenhao Li, Chenyangguang Zhang, Stelian Coros
- **連結**：[arXiv:2611.30312](https://arxiv.org/abs/2611.30312)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：提出 MorphHOI 分散式框架，透過統一的表徵使單一物理基政策能夠支援跨多種異質具體型與團隊組成的協同人機物互動。

### 13. Co-DRIS: Physics-Informed Predictive Belief and Variable-Impedance Learning for Reactive Catching under Coupled Uncertainty
- **作者**：Yonglong Zhang
- **連結**：[arXiv:2611.31843](https://arxiv.org/abs/2611.31843)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：結合慣性世界框架物理預測信念與變阻抗學習，解決具身操作在面對感知與致動耦合不確定性時的反應式抓取難題。

### 14. AirLeg: A Robust and Accurate Self-Supervised Visual-Inertial-Leg SLAM System
- **作者**：Kuan Xu, Tianxin Hu, Ruofei Bai, Ruimeng Liu, Yuefan Hao
- **連結**：[arXiv:2611.32523](https://arxiv.org/abs/2611.32523)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：提出結合視覺與腿部本體感覺的自監督 VIL SLAM 系統，透過模擬器預訓練並在真實部署中相互適應，提升足式機器人定位準確度。

### 15. Seeing Together, Acting Apart: Shared Environmental Understanding for Multi-Robot Navigation
- **作者**：Haihong Hao, Lei Chen, Mingfei Han, Chenglong Yan, Dong An
- **連結**：[arXiv:2611.30310](https://arxiv.org/abs/2611.30310)
- **來源**：arxiv_cs.RO
- **摘要與亮點**：提出共享環境理解（Shared Environmental Understanding）表徵，將多機器人的局部自我中心觀測聚合至共享潛在世界模型，將協作從政策空間前移至表徵空間。

## Interesting

本日選出 3 篇關聯較間接但具備創新想法的論文，提供不同視角的啟發：

1. **EnvTrap (`2611.30004`)**：跳脫傳統演算法與模型本身的安全攻防，從「環境物體排列」出發探討具身 AI 的隱含攻擊面，對實體世界的魯棒性測試提供全新視角。
2. **AirLeg (`2611.32523`)**：專注於腿式機器人的自監督視覺-慣性-腿部混合 SLAM，利用本體感覺與視覺的互補迴圈解決 sim-to-real 標註成本高昂的問題。
3. **Seeing Together, Acting Apart (`2611.30310`)**：探討多機器人協作不一定要在動作層面綁定，透過「共享環境表徵」在潛在空間先建立共識，再各自進行分散式決策。

## Idea Sparks

1. **跨具體型運動學圖（Kinematic Graphs）與世界模型的融合**
   - *觀察*：如 `OmniAct` 與 `DexLatentWorld` 等研究顯示，將機器人局部的運動學圖或 3D 點雲潛在動作引入世界模型，能有效解決跨異質具體型（Cross-Embodiment）的策略轉移難題。
   - *後續問題*：當面對具有極端自由度差異的機器人（如從四足到多指靈巧手人形），如何設計一種統一的動態世界動作模型，在不重新訓練核心骨幹的情況下實現零樣本（Zero-shot）形態適應？
2. **從端到端可微分訓練到動態控制的閉環回饋**
   - *觀察*：`DiffGR00T` 嘗試打破傳統 VLA 階層式架構中「生成與執行脫節」的限制，透過可微分訓練將追蹤與平衡誤差直接回饋給 VLA 生成器。
   - *後續問題*：這種可微分架構是否能推廣至更廣泛的長序列操作任務中？當面對未知動態接觸與突發物理干擾時，可微分鏈的計算瓶頸該如何突破以滿足即時控制需求？
3. **從政策協調轉向表徵空間共識的多機協同**
   - *觀察*：`MAWAM` 與 `Seeing Together, Acting Apart` 分別在多機世界動作模型與導航中展示了「在表徵空間或想像空間先對齊，再行使分散式動作」的威力。
   - *後續問題*：如果在多代理協同中引入分散式的安全護欄（Safety Guardrails），如何確保在各自獨立推理時，表徵空間的共享資訊不會被惡意環境物件（如 `EnvTrap` 所揭示的空間威脅）所汙染？
