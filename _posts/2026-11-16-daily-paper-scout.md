---
layout: post
title: "每日論文雷達｜2026-11-16"
date: 2026-11-16 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-11-16
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總數為 936 篇，經去重與候選篩選後，評估 250 篇，最終精選出 42 篇高品質論文，並於本文中重點呈現最具突破性與高度相關的研究。

---

## Must-Read

### 1. X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot
- **作者**：Jiaxin Huang, Chengxing Lin, Xiaoyu Luo, Sirui Chen, Jingyu Guo
- **連結**：[arXiv:2611.17598](https://arxiv.org/abs/2611.17598)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
- **技術突破與啟發**：本篇技術報告填補了人形機器人從室內到室外跨域長距離導航的空白。面對室內室外環境轉換、相機隨著步態強烈晃動等挑戰，作者提出 X-Nav 系統，透過涵蓋開源場景、部署地數位雙生（Digital Twins）等完整資料引擎，成功實現雙足人形機器人執行基於自然語言指令的長距離任務。這對具身智慧在現實世界中的自主工作能力（Worken）具備極高的實務參考價值。

### 2. Envisioning Agentic Robotics: A New Era of Robotic Systems
- **作者**：Grid Robotics, Qingfeng Lan, Duo Li, Siyao Li, Yiheng Lyu
- **連結**：[arXiv:2611.18359](https://arxiv.org/abs/2611.18359)
- **來源**：`huggingface`, `arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
- **技術突破與啟發**：本文探討了隨著前沿模型帶動的機器人新典範——自主代理型機器人（Agentic Robotics）。跳脫過去針對單一任務訓練專屬策略的模式，此系統運用基礎模型在開放世界中執行閉環任務（觀察環境、理解意圖、推理任務、呼叫工具與技能、驗證成果並調適策略）。這為 VLA 與具身代理的架構設計提供宏觀的前瞻視角。

---

## Highly Relevant

### 1. PoliMop: Policy-in-the-Loop Motion Planning in 3D Spaces for Mobile Robots
- **作者**：Yael Fassbind, Valentin N. Hartmann, Huang Su, Yijiang Huang, Stelian Coros
- **連結**：[arXiv:2611.18110](https://arxiv.org/abs/2611.18110)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：結合物理模擬與 kinodynamic RRT 規劃器，利用控制策略中編碼的技能，讓機器人在複雜 3D 地形中找尋可行路徑。

### 2. Training Reasoning Models in Simulation to Natively Use Real Robots
- **作者**：Jiaming Tang, Zhuoyang Zhang, Junxian Guo, Fangzhou Zhao, Yilong Zhao
- **連結**：[arXiv:2611.18562](https://arxiv.org/abs/2611.18562)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`, `arxiv_keyword`
- **摘要與啟發**：展示如何透過強化學習在純模擬環境中訓練開源 27B 推理模型，使其原生具備操作真實機器人的能力，減少對專有模型的依賴。

### 3. PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion
- **作者**：Siyuan Wang, Dongjie Zhu, Jinxuan Lu, Wenjun Xu, Jiankun Wang
- **連結**：[arXiv:2611.18305](https://arxiv.org/abs/2611.18305)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：針對視覺感知退化（遮擋、反光、光照變化）的情況，提出 OOD 備援機制，提升四足與人形機器人感知 locomotion 的魯棒性。

### 4. ERA: Error-Resistant Autonomous Object Navigation with Predicted Depth
- **作者**：Shunyang Huang, Shuo Wang, Wenyuan Xie, Mingyu Lin, Yue Ding
- **連結**：[arXiv:2611.17730](https://arxiv.org/abs/2611.17730)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：提出「Move with Error」範式，利用 RGB 預測深度進行零樣本導航，透過移動過程中的視角變化自動修正地圖累積誤差。

### 5. Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation
- **作者**：Zihao Lu, Trong Gia Hung Nguyen, Fuquan Wang, Yifan Zhu
- **連結**：[arXiv:2611.18298](https://arxiv.org/abs/2611.18298)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：透過統一的任務表達方式，將預訓練 VLM 連接到基於採樣的模型預測控制（MPC），以解決接觸豐富（Contact-Rich）的操作問題。

### 6. A Generalizable Approach to Safety-Aware Robotic Behavior Planning with an Explicit Constraint Space
- **作者**：Xianxu Wu, Shang-Ching Liu, Zhaocong Liang, Hengxiang Chen, Yujian Ma
- **連結**：[arXiv:2611.18026](https://arxiv.org/abs/2611.18026)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`
- **摘要與啟發**：引入具備顯式約束空間（Constraint Space）的安全感知行為規劃框架，透過可重用文字規則確保桌面操作的安全性。

### 7. Natural Swing-Up of an Underpowered Double Pendulum
- **作者**：Arne Sachtler, Manuel Keppler, Florian Loeffl, Alin Albu-Schäffer
- **連結**：[arXiv:2611.17575](https://arxiv.org/abs/2611.17575)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：探討低功率馬達如何利用非線性正常模態與動力學進行雙擺擺起控制，對能源受限的機器人設計深具啟發。

### 8. Grounding Object-to-Object Hazard Reasoning into 3D Risk Fields for Task-Conditioned Safety
- **作者**：Mariana Sosa Guzmán, Yide Song, Amin Abyaneh, Gregory Dudek, Hsiu-Chin Lin
- **連結**：[arXiv:2611.17566](https://arxiv.org/abs/2611.17566)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：運用 VLM 推斷任務與場景相依的安全約束，並將物件間的危害推理接地（Grounding）至 3D 風險場。

### 9. When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners
- **作者**：Mohammad Khoshnazar, Mike Degany, Deyuan Qu, Qing Yang, Matyas Szanto
- **連結**：[arXiv:2611.18491](https://arxiv.org/abs/2611.18491)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：發現自對弈（Self-Play）交接政策在面對陌生合作夥伴時失效的原因，並透過引入隱藏啟動延遲大幅提升魯棒性。

### 10. Per-Agent-Safe Navigation of Globally Driven Robot Collectives via Affine Field Design
- **作者**：Seunghwan Jang, Steven Ceron, Wei Xiao
- **連結**：[arXiv:2611.17859](https://arxiv.org/abs/2611.17859)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：提出廣播控制公式，利用單一空間仿射場（Affine Field）同時統御機器人群體的運動與變形，確保各個代理的安全性。

### 11. VLAN: Vision-Language Accessible Navigation
- **作者**：Jie Hu, Yu Zheng, Wenzhi Wu, Weixing Feng, Cunlei Cheng
- **連結**：[arXiv:2611.18346](https://arxiv.org/abs/2611.18346)
- **來源**：`arxiv_cs.AI`, `arxiv_cs.CV`
- **摘要與啟發**：提出支援不同具體型態（人形、四輪等）之可及性導航基準 VLAN，包含 1,000 個場景與 20K 軌跡，強調無障礙移動取決於具身特徵。

### 12. ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents
- **作者**：Yundi Cai, Zihan Wang, Chenxi Han, Yi Cheng, Houde Liu
- **連結**：[arXiv:2611.18176](https://arxiv.org/abs/2611.18176)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：建立具身自臻完善飛輪（ESI），透過環境互動對齊 LLM 的高階推理與 VLA 的底層動作，解決模組化代理策略衝突問題。

### 13. AI-guided robotic in situ fabrication of curvature- and tissue-adaptive wireless bioelectronics
- **作者**：Hiroyuki Tetsuka, Jiaju Ma, Naomi Kumano, Minoru Hirano
- **連結**：[arXiv:2611.17638](https://arxiv.org/abs/2611.17638)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：整合 3D 視覺相機、6-DoF 機械臂與直接墨水書寫，實現傷口無線生醫電子裝置的 AI 引導原地製造。

### 14. Reusing Locomotion Training Recipes Across Humanoids via Body-Aligned Virtual Joints
- **作者**：Sol Choi, Mingon Kim, Seokin Seo, Jongeun Choi, Donghyeon Kim
- **連結**：[arXiv:2611.18003](https://arxiv.org/abs/2611.18003)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：引入身體對齊的虛擬關節空間，標準化暴露給策略的座標介面，使不同結構的人形機器人能跨機型複用強化學習訓練配方。

### 15. On the Utility of Pre-Trained Visual Representations for Policy Learning of Contact-Rich Insertion Tasks
- **作者**：Leon Kim, Dinesh Jayaraman, Michael Posa
- **連結**：[arXiv:2611.17631](https://arxiv.org/abs/2611.17631)
- **來源**：`arxiv_cs.RO`
- **摘要與啟發**：深入探討網際網路規模預訓練視覺表徵在接觸豐富插拔任務中的適用性與任務相依性。

### 16. Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment
- **作者**：Suvarna Kadam, Soran Parsa
- **連結**：[arXiv:2611.18372](https://arxiv.org/abs/2611.18372)
- **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.LG`, `arxiv_keyword`
- **摘要與啟發**：全面回顧 2022 年 12 月至 2026 年 10 月間 88 篇 VLA 領域文獻，沿著七大軸線梳理模型設計、訓練與部署的生命週期。

---

## Interesting

*(本期未收錄符合低相關/小眾創新但需要額外標註的邊緣想法論文，所有精選文獻皆已納入上述高相關與突破性清單中。)*

---

## Idea Sparks

1. **跨具身型態（Cross-Embodiment）訓練與座標標準化的界線在哪裡？**
   - 從 `Reusing Locomotion Training Recipes Across Humanoids`（虛擬關節空間）與 `VLAN`（體現式可及性導航）的趨勢來看，社群正逐漸擺脫對單一機器人硬體配置的過度依賴。
   - **後續問題**：當我們引入高自由度虛擬關節空間或統一抽象介面時，是否會在大規模平行訓練中犧牲掉特定硬體（如非線性彈性驅動器）的動力學細節？如何量化這種抽象化帶來的性能折損？

2. **語言推理模型（LLM/VLA）與底層模型預測控制（MPC）的閉環對齊**
   - 從 `Objectives as Policies` 與 `ESI` 的設計思路中，高階語義推理與低階物理穩定控制的摩擦（Friction）仍是當前痛點。
   - **後續問題**：在需要毫秒級反應的接觸豐富（Contact-Rich）操作中，如何設計輕量化的反饋迴路，讓 VLA 的語義修正能夠即時且無損地注入 MPC 的成本函數（Cost Programs）？
