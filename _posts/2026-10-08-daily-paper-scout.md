---
layout: post
title: "每日論文雷達｜2026-10-08"
date: 2026-10-08 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-10-08
- **主題**：具身智能（Embodied Intelligence）
- **收錄數量**：本次爬取總計 1,524 篇論文，經去重與候選篩選後，評估 250 篇，其中 136 篇通過決策門檻，並精選出最具代表性的研究成果。

## Must-Read
- **On-Demand Robotic Assembly via Differentiable Geometric Part Repair**
  - **作者**：Millicent Schlafly, Fabio Schaub, Diogo Costa Pais, Luca Lelli, Janne Dvorak
  - **連結**：[arXiv:2610.09777](https://arxiv.org/abs/2610.09777)
  - **來源**：`arxiv_cs.RO`
  - **技術突破與啟發**：本文提出端到端的自動化管線，透過生成式 AI 代理將使用者指令轉化為 3D 幾何結構，並結合梯度基底的修復階段（透過圖注意力網路代理進行反向傳播），解決數位設計與機器人組裝限制間的落差。此研究對具身操作（Robot Manipulation）帶來重要啟發，展示了如何將可微分幾何代理與生成模型結合，實現動態、高精度的自訂實體結構組裝。

## Highly Relevant
- **LLA-MPPI: Rapidly Adaptive Whole-body Control of Legged Robots with GPU-Accelerated Parallel Simulations**
  - **作者**：Sebin Jung, Maitham F. AL-Sunni, Juan Alvarez-Padilla, Zachary Manchester, Changliu Liu
  - **連結**：[arXiv:2610.10465](https://arxiv.org/abs/2610.10465)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：引入前瞻與回顧式自適應模型預測路徑積分控制（LLA-MPPI），透過 GPU 批次化模擬器庫實現四足機器人的快速全身適應控制。

- **Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data**
  - **作者**：Songbo Hu, Qiayuan Liao, Yufeng Chi, Kevin Zakka, Yakun Sophia Shao
  - **連結**：[arXiv:2610.09117](https://arxiv.org/abs/2610.09117)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`
  - **摘要重點**：直接從無機器人的真實人類示範中學習全身人形機械人移動操作（Loco-Manipulation），透過視覺規劃器與強化學習追蹤器協同訓練，並在真實 Unitree G1 上驗證。

- **PhysEvo: Astra Can Act, Let It**
  - **作者**：Wenqing Tian, Zeyu Zhang, Zhaocheng Liu, Fengwei Liu, Qiang Liu
  - **連結**：[arXiv:2610.08995](https://arxiv.org/abs/2610.08995)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
  - **摘要重點**：提出圍繞單一凍結模型的物理遞歸自我改進（RSI）框架，讓任務代理與元代理協同診斷故障並改進技能與工具。

- **Borrowed Eyes: Markerless Nano-UAV Flight with an Active Quadruped Observer**
  - **作者**：Alejandro Lorite Mora, Dimitrios Arapis, Andrés Faíña
  - **連結**：[arXiv:2610.09967](https://arxiv.org/abs/2610.09967)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：利用具備手臂相機的四足機器人作為主動觀測者，為無 GPS 環境下的微型無人機（Nano-UAV）提供無標記的視覺定位與即時導航支援。

- **Robotic Boomerang Throwing via Model-Based Release Design**
  - **作者**：Yang Liu, Colin Jones, Aude Billard
  - **連結**：[arXiv:2610.10472](https://arxiv.org/abs/2610.10472)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：針對具有空氣動力學升力的迴力標投擲任務，提出基於模型的釋放狀態設計框架，克服機械臂在動態捕捉與高速運動上的限制。

- **Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs**
  - **作者**：Namai Chandra, Jaison Jose, Kavi Arya, Shivaram Kalyanakrishnan
  - **連結**：[arXiv:2610.09828](https://arxiv.org/abs/2610.09828)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：結合摺紙啟發輪胎與主動感測幾何控制，透過車體俯仰角變化掃描 LiDAR 並與 IMU 及 RGB-D 進行感測融合，提升移動機器人在緊湊空間中的適應力。

- **HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids**
  - **作者**：An Dang, Arturo Flores Alvarez, Yu-Ming Chen, Conor Mc Gartoll, Helen Sun
  - **連結**：[arXiv:2610.08970](https://arxiv.org/abs/2610.08970)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`
  - **摘要重點**：針對人形機器人搬運重物時的質心偏移與負載挑戰，結合模型預測控制（MPC）與強化學習訓練雙教師架構，實現強力的全身移動操作。

- **MagCilia: A Compact Magnetociliary Tactile Sensor with 3D Force Sensing for Robotic Contact Perception and Grasping Feedback**
  - **作者**：Yu Feng, Hao Wu, Haotian Guo, Haoming Liu, William Su
  - **連結**：[arXiv:2610.09536](https://arxiv.org/abs/2610.09536)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：結合彈性磁毛結構與霍爾感測器的微型觸覺感應器，並透過因果歷史融合迴歸（CHFR）實現高精度的 3D 觸覺接觸感知。

- **Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control**
  - **作者**：Joohwan Seo, Xiaofeng Guo, Jinkun Cao, Roberto Horowitz, Rocky Duan
  - **連結**：[arXiv:2610.09479](https://arxiv.org/abs/2610.09479)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：提出 ResGAC，結合幾何導納控制（GAC）與殘差強化學習，解決人形機器人在全身運動時末端執行器的精確 SE(3) 追蹤難題。

- **ActiveLang: Active Open-Vocabulary 3D Mapping with Semantic-Uncertainty-Guided Exploration**
  - **作者**：Liyan Chen, Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh
  - **連結**：[arXiv:2610.09518](https://arxiv.org/abs/2610.09518)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
  - **摘要重點**：引入基於語義不確定性引導探索的主動開放詞彙 3D 地圖建構系統，支援動態環境下的線上語言特徵適應。

- **FoldBack: Self-Correcting Masked Generative Policy for Long-Horizon Garment Folding**
  - **作者**：Lipeng Zhuang, Shiyu Fan, Yingdong Ru, Zhuo He, Florent P. Audonnet
  - **連結**：[arXiv:2610.10462](https://arxiv.org/abs/2610.10462)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
  - **摘要重點**：為長視距衣物摺疊任務提出具備自我修正機制的遮罩生成策略，能在抓取失敗時精準執行重試與回滾。

- **RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments**
  - **作者**：Zhiqin Yang, Chenxin Li, Xiaomeng Hu, Yibin Liu, Weidong Huang
  - **連結**：[arXiv:2610.10409](https://arxiv.org/abs/2610.10409)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`
  - **摘要重點**：建立包含 84 項任務的模擬測試平台，用於全面評估多模態代理在跨本體（操作、移動、駕駛、飛行）控制上的表現。

- **Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies**
  - **作者**：Yihan Li, Yating Feng, Shengjiu Sun, Jianing Chen, Hao Ren
  - **連結**：[arXiv:2610.10479](https://arxiv.org/abs/2610.10479)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
  - **摘要重點**：提出將場景重建、策略開發與真實機器人執行透過代理框架緊密連結的 Real-to-Sim-to-Real 方法。

- **OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework**
  - **作者**：Yifan Wu, Qin Li, Nan Min, Guojin Zhong, Haoyu Zhao
  - **連結**：[arXiv:2610.10384](https://arxiv.org/abs/2610.10384)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：打造跨模擬與真實環境的統一視覺-觸覺操作基準（OpenViTac），填補觸覺導向機器人策略評估的缺口。

- **Contact-Aware Imitation Learning Through Contact Factorization**
  - **作者**：Jiho Hong, Daeun Song, Sanghyun Kim, Mingyo Seo
  - **連結**：[arXiv:2610.09533](https://arxiv.org/abs/2610.09533)
  - **來源**：`arxiv_cs.RO`
  - **摘要重點**：提出 FACE 框架，將任務意圖與環境相依的接觸因素進行因果分解，提升接觸豐富操作（Contact-rich Manipulation）的泛化能力。

- **SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models**
  - **作者**：Yatai Ji, Zhengqiu Zhu, Yong Zhao, Yue Hu, Fanglong Yao
  - **連結**：[arXiv:2610.09335](https://arxiv.org/abs/2610.09335)
  - **來源**：`arxiv_cs.AI`, `arxiv_cs.LG`
  - **摘要重點**：利用世界模型進行空間價值為基礎的想像，解決無人機在未知都市環境中進行物件搜尋時的部分可觀測性問題。

- **Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment**
  - **作者**：Xiao Zhang, Yuxin Chen, Zhixuan Liang, Guojian Zhan, Chenran Li
  - **連結**：[arXiv:2610.09369](https://arxiv.org/abs/2610.09369)
  - **來源**：`arxiv_cs.RO`, `arxiv_cs.LG`
  - **摘要重點**：分析並解決擴散策略在機器人規劃中常發生的模態崩潰問題，透過無標籤雜訊分配保留多模態動作分佈。

## Interesting
- **Borrowed Eyes (arXiv:2610.09967)**：使用移動四足機器人作為主動觀測載體來協助微型無人機定位，這類「異質機器人協作（Heterogeneous Robot Collaboration）」巧妙地利用大負載機器人的感測優勢來補足微型機器人的硬體極限，是一個極具巧思的系統整合方向。
- **Robotic Boomerang Throwing (arXiv:2610.10472)**：挑戰空氣動力學動態複雜的迴力標投擲任務，將機械臂控制與非直覺物理飛行軌跡結合，展現了模型基底設計在極端動態操作中的獨特價值。

## Idea Sparks
- **跨論文趨勢一：從「單一動態補償」走向「多模態感測與模擬融合（Sim-and-Real Tactile & Whole-Body Integration）」**
  - 觀察到近期如 *OpenViTac*（arXiv:2610.10384）與 *MagCilia*（arXiv:2610.09536）等研究，正積極將觸覺與視覺、模擬與真實環境做更深度的統一整合。
  - **具體後續問題**：當觸覺反饋引入高動態的全身人形機器人控制（如 *HULK* 或 *ResGAC*）時，如何避免過高的感測延遲並實現高頻率的閉環控制？
- **跨論文趨勢二：基於生成式模型與世界模型的「主動自我修復與探索（Active Self-Correction & Exploration）」**
  - 如 *PhysEvo*（arXiv:2610.08995）、*FoldBack*（arXiv:2610.10462）與 *SearchWorld*（arXiv:2610.09335）均強調代理在面對長視距任務或未知干擾時，具備自主診斷、重試或基於世界模型的想像規劃能力。
  - **具體後續問題**：這些基於代理（Agentic）的自我修復機制，能否在即時性要求極高的具身控制迴圈中（如 50Hz 以上）實現端到端的輕量化部署？
