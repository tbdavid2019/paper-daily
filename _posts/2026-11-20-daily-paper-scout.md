---
layout: post
title: "每日論文雷達｜2026-11-20"
date: 2026-11-20 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-11-20
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 1,513 篇論文，經去重與候選篩選後，評估 250 篇，最終收錄 19 篇重點研究（包含 Must-Read 2 篇、Highly Relevant 16 篇、Interesting 1 篇）。

---

## Must-Read

1. **JARVIS: An Agent That Designs, Builds, and Tests Circuit Boards on Its Own**
   - **作者**：Shibo Zhou, Tianqi Hong, Zheng Yan, He Yang
   - **來源**：[arXiv:2611.26503](https://arxiv.org/abs/2611.26503)
   - **技術突破點與啟發**：本篇提出 JARVIS，這是一個能自主完成電路板設計、製造與測試閉環的具身 AI 代理。JARVIS 透過機器人搭載的 3D 掃描器掃描工作區，並建構一個可執行的數位雙生（Digital Twin），在實際消耗材料前於虛擬環境中預演機器人動作、製造步驟與電路行為。這項研究展示了具身智慧從單純的桌面或雙足移動操作，跨足至高精度硬體工程製造的巨大潛力，對未來自動化硬體研發極具啟發。

2. **Bridging vision-language reasoning and learned control for legged navigation in the wild**
   - **作者**：Takahiro Miki, Robin Schmid, Manthan Patel, Turcan Tuna, Julia Richter
   - **來源**：[arXiv:2611.25215](https://arxiv.org/abs/2611.25215)
   - **技術突破點與啟發**：提出 ROAM（Robust Open-world Autonomous Mobility）系統，成功將網際網路規模預訓練的視覺語言模型（VLM）高階環境推理能力，與在模擬環境中透過強化學習訓練的低階運動控制與區域規劃策略相結合。此研究證明了結合高階語義理解與低階強健移動控制，能賦予四足或雙足機器人在複雜高山與都市環境中進行公里級野外導航的能力。

---

## Highly Relevant

1. **Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience**
   - **作者**：EngineAI
   - **來源**：[arXiv:2611.26420](https://arxiv.org/abs/2611.26420)
   - **摘要重點**：建構了 Awaken-Human 資料集，包含約 50,000 小時的第一人稱立體影片與同步全身人類動作資料，並推出 Awaken-HI 視覺語言動作模型，用於人形機器人的全身loco-manipulation。

2. **Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning**
   - **作者**：Ganeshvar Soenessardien, Michael Przystupa, Kevin Sebastian Luck
   - **來源**：[arXiv:2611.26054](https://arxiv.org/abs/2611.26054)
   - **摘要重點**：探討人形機器人物件介導移動（object-mediated locomotion），透過終止形塑強化學習（termination-shaped RL），在無需人類示範或系統辨識解析轉向模型的情況下實現滑板運動。

3. **PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation**
   - **作者**：Kai Lu, Chenyang Ma, Ioannis Havoutis
   - **來源**：[arXiv:2611.26596](https://arxiv.org/abs/2611.26596)
   - **摘要重點**：提出將長跨度全身loco-manipulation分解為三層架構，將時間與精度控制交給無需訓練的傳統組件，讓 VLA 模型專注於階段性技能動態。

4. **Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation**
   - **作者**：Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang
   - **來源**：[arXiv:2611.26444](https://arxiv.org/abs/2611.26444)
   - **摘要重點**：推出診斷型基準測試 Mind2Act World，用於分離評估具身智能中的認知推理、物理執行及其環境回饋下的組合能力。

5. **WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation**
   - **作者**：Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo
   - **來源**：[arXiv:2611.25251](https://arxiv.org/abs/2611.25251)
   - **摘要重點**：提出無遠端遙控的後訓練框架 WEVO，利用動作條件式影片世界模型（WM）來改善全身人形 VLA 策略，減少實體探索風險。

6. **Collision-Free Is Not Enough: Passage-Conditioned Navigation for Wheeled-Legged Robots**
   - **作者**：Wai Ka Sun, Waiyiu Pong, Bowen Wang
   - **來源**：[arXiv:2611.25788](https://arxiv.org/abs/2611.25788)
   - **摘要重點**：針對輪足機器人提出通道條件導航（passage-conditioned navigation），利用短暫教學示範記住每個階梯與邊緣的實際跨越方式，解決無碰撞但無法精準對位或卡住的問題。

7. **ECHO: In-Context Behavior foundation model for Humanoid Whole-Body Control**
   - **作者**：Xingyi Wang, Li Bin, Jiyuan Shi, Chenyun Zhang, Weiji Xie
   - **來源**：[arXiv:2611.25778](https://arxiv.org/abs/2611.25778)
   - **摘要重點**：提出 ECHO 上下文行為基礎模型，將互動經驗轉化為環境特定的控制，將一般行為能力與動態特定執行分離。

8. **Mapping the Wind to Find the Source: Online Physics-Informed Gas Source Localization with Mobile Robots**
   - **作者**：Wanting Jin, Thomas Wiedemann, Fan Han, Achim Lilienthal, Alcherio Martinoli
   - **來源**：[arXiv:2611.25067](https://arxiv.org/abs/2611.25067)
   - **摘要重點**：提出輕量級物理啟發的機率框架，用於行動機器人在室內動態風場下的高效氣體源定位。

9. **Learning optimal gaits and styles for terrain-adaptive quadruped locomotion**
   - **作者**：Guillaume Bellegarda, Auke Ijspeert
   - **來源**：[arXiv:2611.25958](https://arxiv.org/abs/2611.25958)
   - **摘要重點**：結合深度強化學習與脊髓中央模式產生器（CPG）網路，探討地形、性能指標與速度如何共同決定四足機器人的最佳步態。

10. **Cognitive-Horizon Action Chunking: Memory-Guided Adaptive Reasoning for Embodied Navigation**
    - **作者**：Weile Gong, Zijian Lu, Jiahao Zheng, Bo Xu, Yiping Zuo
    - **來源**：[arXiv:2611.25587](https://arxiv.org/abs/2611.25587)
    - **摘要重點**：提出 CHAC 框架，透過保留視覺環境與控制器回饋來動態決定認知地平線（cognitive horizon），在不增加額外模型呼叫下進行記憶引導的適應性推理。

11. **MoRE: Mixture-of-Experts for Multi-Physics Robotic World Models**
    - **作者**：Ziyu Zhu, Shaowei Liu, Albert J. Zhai, Henry Che, Wei-Chiu Ma
    - **來源**：[arXiv:2611.25336](https://arxiv.org/abs/2611.25336)
    - **摘要重點**：提出 MoRE，這是一個基於混合專家架構（MoE）的 3D 世界模型，專門將機器人互動解構並分配給剛體、形變體與抓取動態等不同物理專家。

12. **Trajectory-Calibrated Merging of Embodied Policies**
    - **作者**：Wenshuo Chen, Honglei Jin, Le Yang, Jianfei Song, Shaofeng Liang
    - **來源**：[arXiv:2611.25575](https://arxiv.org/abs/2611.25575)
    - **摘要重點**：提出軌跡校準迴歸（TCR）框架，解決現有模型合併方法在閉環執行中無法可靠保留多個任務專家能力的問題。

13. **PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity**
    - **作者**：Hao Vo, Taisei Hanyu, Yuki Ikebe, Pham Tri Quang, Sreevenkata Anjani Tishita Godavarthi
    - **來源**：[arXiv:2611.26565](https://arxiv.org/abs/2611.26565)
    - **摘要重點**：推出 PhyDEX 投擲基準測試，透過動態外在靈巧性（dynamic extrinsic dexterity）來評估 VLA 模型對質量、質心與摩擦力的物理推理能力。

14. **HumanCOIN: A 12,500-Hour Dataset for Human Intent in Egocentric Manipulation**
    - **作者**：Shihan Wu, You Liu, Chunyu He, Minghui Qin, Longhan Jiao
    - **來源**：[arXiv:2611.26434](https://arxiv.org/abs/2611.26434)
    - **摘要重點**：提出 12,500 小時的第一人稱操作資料集 HumanCOIN，記錄人類在操作過程中的意圖路徑（如視線、肌肉負載、皮層活動等）。

15. **Reasoning on Call: Efficient Agentic Robot Control for Long-Horizon Robot Manipulation**
    - **作者**：Zilang Cen, Chao Tang, Fangcheng Liu, Weishi Mi, Wei Hao
    - **來源**：[arXiv:2611.26341](https://arxiv.org/abs/2611.26341)
    - **摘要重點**：提出 RoC 框架，透過在線任務狀態監視器協調低階策略與高階推理代理，減少長跨度操作中的模型呼叫延遲與成本。

16. **MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation**
    - **作者**：Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang, Yecheng Wu
    - **來源**：[arXiv:2611.25105](https://arxiv.org/abs/2611.25105)
    - **摘要重點**：提出 MAWAM 多代理世界動作模型，透過跨代理注意力機制同時預測機器人團隊的未來視角與動作區塊，實現協同操作。

---

## Interesting

1. **Mapping the Wind to Find the Source: Online Physics-Informed Gas Source Localization with Mobile Robots**
   - **作者**：Wanting Jin, Thomas Wiedemann, Fan Han, Achim Lilienthal, Alcherio Martinoli
   - **來源**：[arXiv:2611.25067](https://arxiv.org/abs/2611.25067)
   - **想法亮點**：將物理資訊機率模型應用於氣體源定位（Gas Source Localization），在沒有預先計算氣流場或詳細環境佈局的情況下，讓行動機器人在室內動態風場中導航。雖然應用領域較為垂直和小眾，但其「線上物理資訊與稀疏測量結合」的思路，對其他具體環境感測任務（如熱源或輻射源追蹤）具有不錯的啟發性。

---

## Idea Sparks

1. **高階語義推理與低階動態控制的架構分工（Hybrid & Hierarchical Decomposition）**
   - *觀察*：今日多篇重量級研究（如 ROAM、PGX、RoC）均指出，將端到端的視覺語言動作（VLA）模型全權負責從高階任務規劃到低階精確控制並不穩定，傾向採用「混合架構」——讓 VLA 負責階段性技能動態或高階推理，而將時間進展、精度控制或動態調整交給狀態機、世界模型或傳統控制組件。
   - *後續問題*：在這種分層架構下，當高階 VLA 的語義指令與低階物理狀態發生衝突時（例如導航 VLA 指令穿過障礙但底層碰撞檢測偵測到無法通行），最優的即時干預與回饋反傳機制應該如何設計才能避免震盪？

2. **從單一機器人到多代理與具身世界模型的模擬與後訓練（World Models and Multi-Agent Scaling）**
   - *觀察*：諸如 WEVO 與 MAWAM 的研究顯示，利用動作條件式影片世界模型（World Models）進行模擬與後訓練，以及將多個代理的狀態與動作透過交叉注意力（Cross-Agent Attention）在世界模型中聯合預測，正成為解決資料稀缺與協同操作的重要手段。
   - *後續問題*：多代理世界模型在面臨未見過的動態互動（例如協同搬運變形體或未知剛體碰撞）時，其合成資料的真實感（Sim-to-Real gap）該如何量化並建立自動校正機制？
