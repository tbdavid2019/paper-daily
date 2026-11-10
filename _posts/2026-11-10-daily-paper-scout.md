---
layout: post
title: "每日論文雷達｜2026-11-10"
date: 2026-11-10 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-11-10
- **主題**：具身智能（Embodied Intelligence）
- **收錄數量**：本次檢索共爬取 1,370 篇論文，經去重與候選篩選後評估 250 篇，其中收錄高度相關與突破性論文共 18 篇。涵蓋領域包含視覺語言動作模型（VLA）、機器人基礎模型、世界模型與空間智能、靈巧與移動操作、模擬到真實（Sim-to-Real）轉換，以及多模態感知。

---

## Must-Read

### Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos
- **作者**：Hai Zhang, Siqi Liang, Yanjun Guo, Shoufeng Zhang, Yunhao Wang
- **來源**：[arXiv:2611.12087](https://arxiv.org/abs/2611.12087)
- **技術突破點**：
  現有的具身導航架構通常僅能依賴最近的少數幾張影格，難以在開放世界中維持持久的空間感知與長序列執行穩定性。本文提出 Compass 1，這是首款將「語言理解」與「影片生成」結合的具身導航基礎模型，並透過約 2 分鐘的視覺歷史記憶實現回溯（memory backtracking）。在不更動底層架構的前提下，創新引入「歷史表示（History Representation）」來整合稀疏的視覺關鍵影格。
- **對研究者的啟發**：
  此研究展示了如何透過有效率的視覺歷史壓縮，讓單目 RGB 影片輸入也能支援長達數分鐘的具身導航記憶，突破了過往模型容易在長序列任務中遺失空間脈絡的瓶頸。

---

## Highly Relevant

### Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years
- **作者**：Roshan S. Kaundinya, Hehui Zheng, Robert K. Katzschmann, George Haller
- **來源**：[arXiv:2611.11718](https://arxiv.org/abs/2611.11718)
- **摘要**：針對非線性軟體機器人難以取得大量互動數據或可靠模擬器的痛點，利用軟體機器人動態學的時間尺度分離特性，將其降維至低維不變流形（aSSMs）。透過預收集合成的簡單多項式常微分方程作為 RL 訓練環境，成功將氣動軟臂的軌跡追蹤訓練時間大幅縮短。

### Embodied First Exam
- **作者**：Kangrui Wang, Qineng Wang, Changhe Chen, Pingyue Zhang, Chi Gui
- **來源**：[arXiv:2611.12177](https://arxiv.org/abs/2611.12177)
- **摘要**：探討利用編碼代理（coding agents）直接控制機器人的範式轉移。提出統一且具代理原生特性的評估框架，允許編碼代理自由選擇直接控制、程式碼控制或訓練策略等不同方法，以檢驗在實體世界限制下的表現。

### Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation
- **作者**：Bingzhang Wang, Nathan Zhao, Jialeng Ni, Jiajin Zheng, Yin Zhang
- **來源**：[arXiv:2611.11854](https://arxiv.org/abs/2611.11854)
- **摘要**：為了解決 VLA 模型在閉環控制中因大型骨幹運算導致動作延遲與狀態過時的問題，提出 DASH 系統。將政策拆分為慢速的視覺語言模型（System 2）與快速的流匹配動作頭（System 1），實現延遲無關的縮放與靈巧操作。

### From Festival Video to the Stage: A Sim-to-Real Ladder for Long-Horizon Expressive Whole-Body Dance on a Commercial Humanoid
- **作者**：Hesham Shehata
- **來源**：[arXiv:2611.11127](https://arxiv.org/abs/2611.11127)
- **摘要**：提出一套將傳統阿波舞（Awa Odori）單目影片轉移至 Unitree G1 EDU 機器人的完整管線。結合人體網格恢復、運動重定向、強化學習模擬訓練與 ONNX 板載部署，並透過 11 個版本的部署階梯來修復狀態估計漂移與工件損壞。

### Flip Anything with Agentic Robotics Self-Learning
- **作者**：Shuangyu Xie, Kaiyuan Chen, Ken Goldberg
- **來源**：[arXiv:2611.11941](https://arxiv.org/abs/2611.11941)
- **摘要**：探討雙臂機器人利用夾爪在平面上將多樣化物件翻轉 180 度的任務。證明編碼代理能透過迭代學習，自主開發並優化物件翻轉策略。

### HINT-VLM: Humanoid Interactive Navigation over Rough Terrain with Embodiment-Grounded Vision-Language Model
- **作者**：Ziwon Yoon, Seok Hwan Kim, Yiyu Chen, Quan Nguyen, Lu Gan
- **來源**：[arXiv:2611.11665](https://arxiv.org/abs/2611.11665)
- **摘要**：聚焦於戶外崎嶇地形中的人形機器人導航與動態障礙物互動，提出具身基礎的視覺語言模型，能預測物件可動性並提前規劃。

### LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data
- **作者**：Xueyang Wang, Zehong Shen, Dingkun Wei, Huaijin Pi, Changpeng Wang
- **來源**：[arXiv:2611.12136](https://arxiv.org/abs/2611.12136)
- **摘要**：針對多目的地長序列語言指令的人形機器人導航，透過大腦（任務推理）、路徑點導航與物理落地動作數據的多速率協調，維持長距離執行的自然全身體態。

### CSG-Nav: Confidence-Aware Semantic-Geometric Fusion for Robust Exploration and Accurate Zero-Shot Object-Goal Navigation
- **作者**：Shoubin Chen, Rui Xu, Zehao Wu, Kai Zhang, Tao Huang
- **來源**：[arXiv:2611.11978](https://arxiv.org/abs/2611.11978)
- **摘要**：提出結合信賴度的語意幾何融合導航框架，解決基於基礎模型導航時常見的遠距離感知不可靠、幻覺方向偏差及幾何誤判問題。

### Motion Belief Action: From a Visual Scene Map to Physical Decisions
- **作者**：Dibyendu Ghosh
- **來源**：[arXiv:2611.12113](https://arxiv.org/abs/2611.12113)
- **摘要**：針對人機協作環境，提出在場景地圖之上的決策層。根據物件被移動頻率、所需施力、負載及阻擋狀態，在力量限制下進行物理決策。

### BATCH: Behavior Alignment for Cross-Embodiment Learning from Humans
- **作者**：Zeyi Liu, Shuran Song
- **來源**：[arXiv:2611.10148](https://arxiv.org/abs/2611.10148)
- **摘要**：提出跨實體學習框架 BATCH，利用具備循環一致性目標的自監督時間表徵，無須人工標註即可建立人機行為對應，實現跨實體示範資料重用。

### HARP-Bench: Benchmarking Robot Manipulation Around Active Humans
- **作者**：Qinhong Zhou, Riley Zong, Chunru Lin, Diyi Hu, Shivraj Singh Bhatti
- **來源**：[arXiv:2611.11123](https://arxiv.org/abs/2611.11123)
- **摘要**：推出評估活躍人類共享工作空間中機器人操作表現的基準測試 HARP-Bench，探討人類主動介入、改變目標或限制安全動線時的任務適應能力。

### RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision for Robot Learning
- **作者**：Mayur Deshmukh, Aaron Tung, Junyi Li, Nikash Bhardwaj, Ademi Adeniji
- **來源**：[arXiv:2611.10994](https://arxiv.org/abs/2611.10994)
- **摘要**：推出大型全身動作捕捉與第一人稱視角（egocentric vision）多模態資料集，補足人形機器人下肢移動與足部擺放訓練數據的不足。

### Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation
- **作者**：Yunheng Wang, Jiaxi Zhang, Wei Lu, Yuetong Fang, Taowen Wang
- **來源**：[arXiv:2611.11554](https://arxiv.org/abs/2611.11554)
- **摘要**：提出運動學動作模型（KAMs），將全身運動視為直接預訓練目標，利用預訓練運動生成器作為動作生成骨幹，以強化人機協調 priors。

### DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies
- **作者**：Kevin Park, Izat Rasyad, Dvij Kalaria, Shankar Sastry
- **來源**：[arXiv:2611.10872](https://arxiv.org/abs/2611.10872)
- **摘要**：利用生成的運動軌跡引導模擬環境中的強化學習，將其轉換為可靠的任務執行軌跡，藉此在模擬中訓練 VLA 模型以減少對真實示範的依賴。

### UniLatent: Cross-Embodiment Transfer via Latent Observation Alignment
- **作者**：Yufei Ding, Yi Du, Weiduo Yuan, Hao Jiang, Dylan Goetting
- **來源**：[arXiv:2611.10061](https://arxiv.org/abs/2611.10061)
- **摘要**：提出在共享潛在空間中對齊來源與目標機器人觀察的跨實體轉移框架，無須像素級圖像翻譯即可直接將策略運行於目標實體。

### Beyond Memory Limits: A Hierarchical Spatio-Temporal Map Representation for Large-Scale 3D Autonomous Exploration
- **作者**：Yizhe Zhang, Jianping Li, Yilun Gao, Liangliang Yin, Pengfei Wan
- **來源**：[arXiv:2611.11489](https://arxiv.org/abs/2611.11489)
- **摘要**：針對無人機在大型災後或未探索環境中的長期探索，提出分層時空地圖表示法，在限制板載記憶體消耗的同時保留全局任務脈絡。

### When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary
- **作者**：Yiming Sun, Mi Zhang
- **來源**：[arXiv:2611.11438](https://arxiv.org/abs/2611.11438)
- **摘要**：探討具備數位資源（如網頁、電子郵件）存取能力的編碼代理在控制真實機器人手臂時帶來的數位-實體邊界安全風險，例如間接提示詞注入對物理世界的威脅。

---

## Interesting

資料未提供（本次選定與評估的論文皆具備高度相關與扎實技術，無落入邊際或低關聯區間）。

---

## Idea Sparks

1. **VLA 模型的非同步解耦與系統分層（System 1 / System 2）**
   - **觀察**：近期如 DASH 等研究指出，將耗時的視覺語言主幹（System 2）與快速的動作頭（System 1）進行非同步解耦，是解決人形機器人閉環控制延遲的關鍵。這呼應了具身智能中將「慢速推理」與「快速反射」結合的趨勢。
   - **後續問題**：當系統 1 與系統 2 的更新頻率存在顯著落差時，如何在動態突發事件（如突如其來的外力干擾）發生瞬間，強制中斷慢速主幹並喚醒緊急反射機制？

2. **程式碼代理（Coding Agents）作為機器人通用控制中介**
   - **觀察**：多篇近期文獻（如 Embodied First Exam 與 When Coding Agents Get Arms）開始探討利用大模型生成的程式碼（Code-as-Policies）直接或間接操控硬體。這模糊了傳統「視覺動作策略學習」與「高階任務規劃」的界線。
   - **後續問題**：在面對開放世界中未知的物理限制與動態干擾時，如何即時驗證由編碼代理動態生成的控制程式碼，以確保其在實體硬體上的安全性與穩定性？

3. **跨實體（Cross-Embodiment）與模擬生成資料的規模化遷移**
   - **觀察**：無論是透過潛在空間對齊（UniLatent）、行為對齊（BATCH）還是利用生成式動作引導 RL（DreamVLA），研究社群正全力擺脫對單一機器人示範資料的過度依賴。
   - **後續問題**：在將人類動作或異質機器人示範透過潛在空間轉移至具體人形硬體時，哪一種對齊方式（像素層、潛在特徵層或動作輸出層）對動力學差異（如不同自由度與重量分佈）最具魯棒性？
