---
layout: post
title: "每日論文雷達｜2026-11-19"
date: 2026-11-19 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-11-19
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 1,455 篇論文，經去重與候選篩選後，評估 250 篇，最終精選出 18 篇高價值研究進行深度解析與推薦。

---

## Must-Read
最值得閱讀的突破亮點論文，展現了具身智慧在硬體共設計、模擬器閉環、長序列協調與資料轉換的關鍵創新：

1. **[RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop](https://arxiv.org/abs/2611.23855)**
   - **作者**：Ghadi Nehme, Dahyun Nam, Akshay Govind Srinivasan, Faez Ahmed
   - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_cs.CV
   - **技術突破點與啟發**：提出 RoboBuilder 框架，讓 AI 程式代理（Coding agents）能夠從標準零件、馬達與自訂 3D 列印件中共同設計機器的硬體與控制程式。研究發現純粹靠模擬是不夠的（最初 15 個通過模擬的設計在真實賽道全數失敗），因此設計出能透過代理主動請求測量並分析真實運行影片來反向修正模擬器的閉環機制。這對具身智慧研究者的啟發在於：打通「硬體-軟體-真實世界回饋」的自動化共設計迴圈是實現真實世界自主機器人的重要基石。

---

## Highly Relevant
高度相關且扎實的核心論文，涵蓋人形機器人協作、本體結構策略、世界模型與跨型態適應：

1. **[Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration](https://arxiv.org/abs/2611.22275)**
   - **作者**：Ting-Hsuan Chen, Siheng Zhao, Han Jiang, Qi Pan, Louison Lu
   - **來源**：huggingface, arxiv_cs.RO, arxiv_cs.LG
   - **簡介**：針對多台人形機器人長序列協同搬運與動態互動，開發分散式後訓練框架，將基礎追蹤模型適應於物理耦合互動，實現基於局部觀測的協調控制。

2. **[Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation](https://arxiv.org/abs/2611.22713)**
   - **作者**：Lechen Zhang, Chenyuan Chen, Muxin Zhou, Zewen He, Yoshihiko Nakamura
   - **來源**：arxiv_cs.RO
   - **簡介**：借鑑人類透過身體圖式（Body Schema）組織視覺與動作的機制，提出將關節與連桿 Token 嵌入機器人運動學樹的視覺-動作介面，大幅提升全身移動操作的效率。

3. **[Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment](https://arxiv.org/abs/2611.22445)**
   - **作者**：Koki Inami, Takashi Sato, Hiroyuki Oka, Shota Takizawa, Yuya Takahashi
   - **來源**：arxiv_cs.RO
   - **簡介**：在市售通用人形機器人（Unitree G1）上部署完整的自主賽道跑步系統，整合視覺車道感知、路徑追蹤與強化學習跑步政策，成功參與世界人形機器人大賽的 100m、400m 與 1500m 賽事。

4. **[WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation](https://arxiv.org/abs/2611.24011)**
   - **作者**：Junlin Long, Xu Deng, Yiran Wang, Yue Yang, Yang Zhao
   - **來源**：arxiv_cs.RO, arxiv_cs.CV
   - **簡介**：透過跨型態政策適應與隨機政策蒸餾，將原本為機械臂設計的世界動作模型（WAM）成功轉移至四足機器人，實現語言條件下的四足移動操作（Loco-manipulation）。

5. **[Recoverability, Not Invariance: Certified Safety for Robots at the Limits of Performance](https://arxiv.org/abs/2611.23589)**
   - **作者**：Thomas A. Berrueta, Joshua D. Ibrahim, Gilchrist X. Johnson, John Lathrop, Soon-Jo Chung
   - **來源**：arxiv_cs.RO
   - **簡介**：捨棄在效能邊緣難以維持的前向不變性（Forward invariance），改以「可恢復性」（Recoverability）作為合約式安全概念，透過收縮理論認證機器人重新接管受信任恢復模式的能力。

6. **[ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors](https://arxiv.org/abs/2611.23916)**
   - **作者**：Lequn Fu, Yufeng Hu, Yijun Zhong, Jie Zhang, Xiao Li
   - **來源**：arxiv_cs.RO
   - **簡介**：利用行為條件對抗運動先驗，在單一本體感覺政策中統一實現人形機器人的正常移動、任意跌倒姿勢起身與指令恢復。

7. **[SemPhys: Semantic-Physical Co-Learning for Humanoid Motion Generation via Differentiable World Models](https://arxiv.org/abs/2611.24074)**
   - **作者**：Zejian Kang, Yeqiang Wang, Zekai Chen, Boyang Shen, Mingyu Ma
   - **來源**：arxiv_cs.RO, arxiv_cs.CV
   - **簡介**：強調語意對齊必須直接在機器人物理執行的完整動作上評估，透過可微分世界模型進行人形動作生成的語意-物理共學習。

8. **[Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor](https://arxiv.org/abs/2611.21958)**
   - **作者**：Timo Oksanen
   - **來源**：arxiv_cs.RO
   - **簡介**：探討大型語言模型直接讀寫神經網路權重（Weight-space programming）來調整真實拖拉機導航控制器的創新實作。

9. **[BEV-Diffusion: Camera-Only Traversability Navigation with BEV Memory and Efficient Cross-Robot Adaptation](https://arxiv.org/abs/2611.24155)**
   - **作者**：Iana Zhura, Timofei Kozlov, Dmitrii Plotnikov, Ivan Valuev, Miguel Altamirano Cabrera
   - **來源**：arxiv_cs.RO
   - **簡介**：提出僅使用相機的鳥瞰視角（BEV）可通行為導航模型，結合 BEV 記憶與貝氏融合，實現高效的戶外地面分級與跨機器人適應。

10. **[DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects](https://arxiv.org/abs/2611.22001)**
    - **作者**：Yiming Dou, Botao He, Antonio Loquercio, Andrew Owens, Jitendra Malik
    - **來源**：arxiv_cs.RO
    - **簡介**：針對機器人操作設計的原生世界模型，直接在機器人遙操作資料集從頭訓練，展現優異的接觸理解與長序列模擬能力。

11. **[Agile Monoped Hopping on Complex and Discrete Terrain via Kinodynamic Planning with Distilled MPPI Steering](https://arxiv.org/abs/2611.21905)**
    - **作者**：Yue Qin, Denglin Cheng, Jingyu Liu, Yanran Ding
    - **來源**：arxiv_cs.RO
    - **簡介**：提出 FlowRRT 動態規劃器，將轉向視為集合值並預測可行動作分佈，解決單足機器人在離散複雜地形上的靈敏跳躍問題。

12. **[Beyond Episodic Recall: Experience-to-Knowledge Evolution for Lifelong Embodied Navigation](https://arxiv.org/abs/2611.22321)**
    - **作者**：Weitao An, Chenghao Xu, Xu Yang, Cheng Deng
    - **來源**：arxiv_cs.RO
    - **簡介**：提出經驗演進記憶機制，將終身具身導航中累積的片段經驗轉化為環境特定的知識，降低儲存成本並提升搜尋效率。

13. **[Improve How You Improve: Recursive Policy Self-Improvement for Zero-Shot Open-Vocabulary Multi-Object Navigation](https://arxiv.org/abs/2611.23774)**
    - **作者**：Yang Li, Ziju Han, Aming WU, Zihao Zhang, Sijia Zhang
    - **來源**：arxiv_cs.RO
    - **簡介**：探討零樣本開放詞彙多目標導航中的遞迴政策自我改進機制，自動化診斷搜尋問題並優化導航策略。

14. **[RESCUE Jumper: A Centimeter-Scale Rolling and Jumping Robot for Search and Rescue](https://arxiv.org/abs/2611.23531)**
    - **作者**：Kiran Marques, Shashwat Singh, Ben D'Ambrosia, Zeynep Temel, Melisa Orta Martinez
    - **來源**：arxiv_cs.RO
    - **簡介**：設計一款 125 克的公分級移動機器人，結合地面滾動與跳躍能力，能透過反轉輪子動作來跨越狹窄空間與高於滾動極限的障礙。

15. **[Ego2X: Contact-aware Transfer from Egocentric Human Data to Any Robot](https://arxiv.org/abs/2611.24138)**
    - **作者**：Xinke Lyu, Bowen Yang, Zhicheng Wang
    - **來源**：arxiv_cs.RO, arxiv_cs.CV
    - **簡介**：著眼於物理互動與接觸動態，提出將單目第一人稱人類影片轉換為具備物理執行可行性之機器人資料的以物件為中心框架。

16. **[Emo-H2A: Driving a Facial Robot Directly from LLM Hidden States at Token Rate](https://arxiv.org/abs/2611.23932)**
    - **作者**：Yige Liu, Jingcheng Huang, Hao Sun, Min Li, Zhouping Yin
    - **來源**：arxiv_cs.RO
    - **簡介**：提出直接從大型語言模型自迴歸解碼時的隱藏狀態（Hidden states）來驅動表情機器人的範式，實現 Token 速率且具備上下文敏感的低延遲表情同步。

17. **[Zero-Shot Compositional Generalization for Embodied Manipulation](https://arxiv.org/abs/2611.24074 等/2611.22797)**
    - **作者**：Baicheng Li, Wenkang Qin, Youqi Pan, Dongxiao Mao, Yukun Zhou
    - **來源**：arxiv_cs.RO
    - **簡介**：提出幾何監督訓練框架，利用校準的正向運動學將示範指令對應至異質機器人的原生動作介面，實現零樣本組合泛化。

---

## Interesting
關聯較間接但具備創新想法的論文，探索非典型控制與感知介面：

1. **[Emo-H2A: Driving a Facial Robot Directly from LLM Hidden States at Token Rate](https://arxiv.org/abs/2611.23932)**（亦列於上方）
   - **觀察**：跳過傳統的文字情緒標籤轉換，直接利用 LLM 的隱藏狀態（Hidden States）驅動機器人面部馬達。這啟發我們思考：未來具身代理的肢體與面部反應是否能完全端到端地與語言模型的內部推理狀態對齊，從而省去額外的意圖分類中介層？

2. **[Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor](https://arxiv.org/abs/2611.21958)**（亦列於上方）
   - **觀察**：繞過梯度下降與傳統優化器，直接由 LLM 編輯小型神經網路的權重。雖然目前僅適用於超小參數控制器（253參數），但這種「權重空間編程」概念為具身系統在邊緣硬體上的即時自我修復與動態適應提供了一個極其新穎的極簡主義視角。

---

## Idea Sparks
1. **硬體共設計與真實世界回饋的自動化迴圈 (Hardware-Software Co-Design via Closed-Loop Real-World VLM/Agent Feedback)**
   - 跨論文觀察：從《RoboBuilder》透過真實世界影片與測量回饋來修正模擬器，到《Weight-space programming》直接修改控制器權重，顯示具身智慧正在突破「純軟體政策學習」的邊界，朝向軟硬體即時互動修正的代理化架構發展。
   - **具體後續問題**：當代理程式具備修改自身運動控制網路權重或 3D 列印硬體設計的能力時，如何在全自動迭代過程中引入嚴格的物理安全與能量消耗約束，避免硬體損壞或控制失控？

2. **從視覺外觀模仿到接觸物理對齊的資料轉換 (From Visual Mimicry to Contact-Centric Physics Alignment in Cross-Embodiment Transfer)**
   - 跨論文觀察：《Ego2X》強調人類第一人稱資料轉機器人不能只看視覺相似，更需要專注於接觸力學與物件運動；而《Body Schema Policy》則透過內建身體圖式介面來處理機器人本體與動作的對齊。兩者皆指向同一個核心瓶頸：跨型態與跨代理資料遷移的關鍵在於「底層物理與接觸狀態的對齊」，而非單純的像素級模仿。
   - **具體後續問題**：如何在不依賴昂貴且繁瑣的觸覺感測器陣列前提下，利用單目或常規視覺影片精確重建並遷移精細的接觸動態（Contact Dynamics）至不同自由度的異質機器人本體上？
