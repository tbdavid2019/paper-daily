---
layout: post
title: "每日論文雷達｜2026-10-08"
date: 2026-10-08 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-08
- **主題**：具身智慧（Embodied Intelligence）
- **收錄數量**：本次總共抓取 1,524 篇論文，經去重與候選篩選後，評估了 250 篇論文，最終收錄 18 篇高品質研究。
- **資料統計**：涵蓋 Hugging Face、arXiv (cs.RO, cs.AI, cs.CV, cs.LG) 等多個來源，其中符合關鍵字與高度相關指標的論文達 75 篇。

---

## Must-Read

### 1. On-Demand Robotic Assembly via Differentiable Geometric Part Repair
- **作者**：Millicent Schlafly, Fabio Schaub, Diogo Costa Pais, Luca Lelli, Janne Dvorak
- **來源**：[arXiv:2610.09777](https://arxiv.org/abs/2610.09777)
- **技術突破點與啟發**：
  本篇論文提出了一個端到端的自主管道，能夠將使用者的文字提示轉化為客製化的木造組裝結構。傳統數位設計轉化為機器人組裝通常需要數月的專家手動調校，以協調零件幾何形狀與機器人約束。作者透過一個圖注意力網路（Graph Attention Network）代理模型，結合梯度式修復階段（Differentiable Geometric Part Repair），在生成過程中同時平衡視覺保真度與物理組裝約束，大幅降低了實體製造的對齊門檻。這對具身操作（Robot Manipulation）與生成式設計的結合帶來重大啟發。

---

## Highly Relevant

### 1. Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data
- **作者**：Songbo Hu, Qiayuan Liao, Yufeng Chi, Kevin Zakka, Yakun Sophia Shao
- **來源**：[arXiv:2610.09117](https://arxiv.org/abs/2610.09117)
- **摘要摘要**：針對人形機器人難以從自我中心視角（Egocentric RGB）與本體感覺規劃接觸豐富的全身操作，Workhorse 提出直接從無機器人的真人示範中學習。透過視覺規劃器預測五連桿目標，並以強化學習進行全身追蹤，兩者在無需重新標定（Retargeting）的相同人類動作資料上訓練，並透過互相模擬部署時的錯誤來增強強健性。

### 2. LLA-MPPI: Rapidly Adaptive Whole-body Control of Legged Robots with GPU-Accelerated Parallel Simulations
- **作者**：Sebin Jung, Maitham F. AL-Sunni, Juan Alvarez-Padilla, Zachary Manchester, Changliu Liu
- **來源**：[arXiv:2610.10465](https://arxiv.org/abs/2610.10465)
- **摘要摘要**：針對足式機器人在動態改變時表現退化的问题，本篇提出 Look-back and Look-ahead Adaptive Model Predictive Path Integral control (LLA-MPPI)。透過 GPU 批次接觸模擬器群（Bank of GPU-batched contact simulators）進行即時動態適應與選擇，有效解決傳統模型結構在接觸動力學上的限制。

### 3. HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids
- **作者**：An Dang, Arturo Flores Alvarez, Yu-Ming Chen, Conor Mc Gartoll, Helen Sun
- **來源**：[arXiv:2610.08970](https://arxiv.org/abs/2610.08970)
- **摘要摘要**：針對人形機器人搬運大型重物時中心偏移與上肢負載的平衡挑戰，提出 HULK 框架。結合模型預測控制（MPC）與強化學習訓練雙教師模型，分別處理腕部受力下的手臂動作與負重定位，提升全身強力移動操作的穩定性。

### 4. PhysEvo: Astra Can Act, Let It
- **作者**：Wenqing Tian, Zeyu Zhang, Zhaocheng Liu, Fengwei Liu, Qiang Liu
- **來源**：[arXiv:2610.09895](https://arxiv.org/abs/2610.09895) (註：對應論文編號 2610.08995)
- **摘要摘要**：引入物理遞迴自我改善（Recursive Self-Improvement, RSI）框架，圍繞單一凍結模型運作。任務代理執行機器人任務，元代理（Meta-agent）利用執行軌跡診斷失敗、修訂工具與技能，實現關節層級控制與可重複使用操作的自我迭代。

### 5. Borrowed Eyes: Markerless Nano-UAV Flight with an Active Quadruped Observer
- **作者**：Alejandro Lorite Mora, Dimitrios Arapis, Andrés Faíña
- **來源**：[arXiv:2610.09967](https://arxiv.org/abs/2610.09967)
- **摘要摘要**：針對室內無全球導航衛星系統（GNSS）環境下，奈米無人機受限於酬載與算力無法自我定位的問題，提出由配備手臂相機的主動四足機器人擔任追蹤與定位觀察者，透過即時無線鏈路回傳位置資訊以實現無標記飛行。

### 6. Robotic Boomerang Throwing via Model-Based Release Design
- **作者**：Yang Liu, Colin Jones, Aude Billard
- **來源**：[arXiv:2610.10472](https://arxiv.org/abs/2610.10472)
- **摘要摘要**：探討迴力標這種高度依賴釋放速度、姿態與自旋的空氣動力學升力物體，提出以模型為基礎的釋放設計框架，克服機械臂無法輕易重現人類高速投擲動作的限制。

### 7. Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs
- **作者**：Namai Chandra, Jaison Jose, Kavi Arya, Shivaram Kalyanakrishnan
- **來源**：[arXiv:2610.09828](https://arxiv.org/abs/2610.09828)
- **摘要摘要**：利用摺紙啟發的輪子進行移動，並透過主動控制感測幾何形狀來恢復場景幾何。結合 IMU 與 LiDAR 投影至 RGB-D 深度流，在嚴格的酬載與成本限制下提升緊湊型移動機器人的感知與適應力。

### 8. Decoding Neural Population Dynamics through Robotic Analog
- **作者**：Wenhui Chen, Jiyue Tao, Yitao Cheng, Yutong Shi, Feitian Zhang
- **來源**：[arXiv:2610.09977](https://arxiv.org/abs/2610.09977)
- **摘要摘要**：開發具備人工肌肉、多模態感測器與強化學習神經網路控制器的生物運動系統機器人模擬，探討大腦運動皮層旋轉神經群體動態與物理動作產出之間的因果關係。

### 9. RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments
- **作者**：Zhiqin Yang, Chenxin Li, Xiaomeng Hu, Yibin Liu, Weidong Huang
- **來源**：[arXiv:2610.10409](https://arxiv.org/abs/2610.10409)
- **摘要摘要**：推出 RobotWorld 模擬測試平台，包含 84 個橫跨操作、移動操作、移動、駕駛與空中控制的任務，用以評估通用多模態智能代理將指令與觀察轉化為物理任務執行的能力。

### 10. FoldBack: Self-Correcting Masked Generative Policy for Long-Horizon Garment Folding
- **作者**：Lipeng Zhuang, Shiyu Fan, Yingdong Ru, Zhuo He, Florent P. Audonnet
- **來源**：[arXiv:2610.10462](https://arxiv.org/abs/2610.10462)
- **摘要摘要**：針對長視界衣物摺疊提出自修正遮罩生成策略（FoldBack），在推論時透過精煉、驗證、回滾與重試等機制，解決抓取失敗後策略仍繼續盲目執行的問題。

---

## Interesting

### 1. ECHO: Embodied Camera Observations of Human Object Carrying
- **作者**：Xuefei Sun, Lorin Achey, Kali Hamilton, Alberto Speranzon, Gregory Grebe
- **來源**：[arXiv:2610.10438](https://arxiv.org/abs/2610.10438)
- **點評**：提出情境式物件放置基準（Contextual Object Placement），研究協助型代理如何根據環境佈局與人類習慣推理物件的自然歸宿，跨越傳統靜態室內掃描或無場景人類動作資料的限制。

### 2. Design of a Fully Actuated 4-DOF Robotic Finger With Joint-Specific Hybrid Remote Actuation
- **作者**：Hyojae Kang, Hyun-mok Jung, Joonho Lee, Dongil Park, Hyunmin Do
- **來源**：[arXiv:2610.10180](https://arxiv.org/abs/2610.10180)
- **點評**：提出具備關節特定混合遠距驅動架構的完全驅動 4-DOF 機器手指，利用滾動接觸接頭（RCJ）線傳動維持線圈長度，為靈巧手（Dexterous Manipulation）提供扎實的硬體創新。

### 3. Contact-Aware Imitation Learning Through Contact Factorization
- **作者**：Jiho Hong, Daeun Song, Sanghyun Kim, Mingyo Seo
- **來源**：[arXiv:2610.09533](https://arxiv.org/abs/2610.09533)
- **點評**：提出 FACE 接觸因式分解模仿學習框架，將預期任務行為與環境相依的接觸因素分離，解決因表面幾何、方向與摩擦力微小改變而難以轉移的力控操作難題。

---

## Idea Sparks

1. **從「真人示範/模擬」到「自我修復 (Self-Correction/RSI)」的政策演進**
   - 觀察到今日多篇論文（如 *Workhorse* 的錯誤互相模擬、*PhysEvo* 的物理遞迴自我改善、以及 *FoldBack* 的推論回滾與重試）皆聚焦於如何在大規模動作生成中引入「動態修正與驗證機制」，而非依賴單向的模仿學習。
   - **後續問題**：當代理在真實物理環境中遭遇未曾見過的破壞性互動失敗時，如何設計低延遲且具備通用性的「零樣本（Zero-shot）安全回滾與路徑重規劃」架構？

2. **跨本體（Cross-Embodiment）協同感測與非對稱觀察者的擴展性**
   - *Borrowed Eyes* 展現了以四足機器人作為移動視角來引導無人機的「主動觀察」模式，而 *RobotWorld* 則強調跨不同本體的基準測試。這顯示具身智慧正從單一機器人本體（如單臂或單足）走向多本體、異質感測器動態互補的分散式系統。
   - **後續問題**：在多本體協同任務中，如何透過端對端視覺語言動作（VLA）模型有效處理通訊延遲與動態遮擋帶來的感知不確定性？
