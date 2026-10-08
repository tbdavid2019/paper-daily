---
layout: post
title: "每日論文雷達｜2026-10-08"
date: 2026-10-08 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況
- **日期**：2026-10-08
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 1,524 篇論文，經去重與候選篩選後，涵蓋 60 篇重點評估文獻，本文精選並推薦其中最具代表性的 18 篇突破與核心研究。

## Must-Read
### 1. Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data
- **作者**：Songbo Hu, Qiayuan Liao, Yufeng Chi, Kevin Zakka, Yakun Sophia Shao
- **連結**：[arXiv:2610.09117](https://arxiv.org/abs/2610.09117)
- **來源**：arxiv_cs.RO, arxiv_cs.LG
- **技術突破與啟發**：本篇研究突破人形機器人在具備視覺與本體感覺下，難以規劃接觸密集之全身操作的瓶頸。Workhorse 直接從完全不需機器人的真人示範中學習全身協同操作。透過視覺規劃器預測軀幹、雙腕與雙足等五連桿目標，並利用強化學習全身追蹤器在機器人上執行。兩者皆在相同的真實人類姿勢上獨立訓練，不須繁瑣的重標定（retargeting），並透過互相模仿彼此部署時產生的誤差來增強訓練數據。這為具身智慧領域提供了無需大量機器人本體資料即可實現具備強健性之全身移動操作的新思路。

### 2. RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments
- **作者**：Zhiqin Yang, Chenxin Li, Xiaomeng Hu, Yibin Liu, Weidong Huang
- **連結**：[arXiv:2610.10409](https://arxiv.org/abs/2610.10409)
- **來源**：arxiv_cs.RO, arxiv_cs.LG
- **技術突破與啟發**：通用代理人目前已能自主編寫程式、使用工具並完成複雜的數位任務，但其能力究竟能延伸至實體世界到什麼程度？本研究推出了 RobotWorld，這是一個充滿挑戰的模擬測試平台，旨在評估代理人透過機器人介面將指令與觀察轉化為實體任務執行的能力。其涵蓋 84 項橫跨操作、移動操作、移動、駕駛與空中控制的任務，並帶有明確的互動預算與可執行成功檢查。對研究者的啟發在於，透過系統性分析執行軌跡與任務結果，能有效診斷多模態代理人跨本體與實體互動的盲點。

### 3. Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment
- **作者**：Xiao Zhang, Yuxin Chen, Zhixuan Liang, Guojian Zhan, Chenran Li
- **連結**：[arXiv:2610.09369](https://arxiv.org/abs/2610.09369)
- **來源**：arxiv_cs.RO, arxiv_cs.LG
- **技術突破與啟發**：擴散策略（Diffusion Policies）原先被期望能完美恢復多模態動作分佈，但作者發現在資料集模態平衡及批次內對稱性皆受保障時，擴散策略仍經常坍縮（collapse）至單一模態。分析顯示，獨立的動作-雜訊配對會增加擴散路徑之間的混合與交叉，進而產生平均化的去噪反應並抑制模態特定行為。本篇提出的「混相擴散策略」（Immiscible Diffusion Policy）透過無標籤的雜訊指派，成功解決了機器人規劃中的模態坍縮問題，對提升具身策略在多峰決策上的表現具備高度啟發性。

### 4. OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework
- **作者**：Yifan Wu, Qin Li, Nan Min, Guojin Zhong, Haoyu Zhao
- **連結**：[arXiv:2610.10384](https://arxiv.org/abs/2610.10384)
- **來源**：arxiv_cs.RO
- **技術突破與啟發**：觸覺回饋為具身代理人提供了視覺以外不可或缺的物理資訊，但現今的視覺-觸覺-語言-動作（VTLA）政策仍缺乏跨模擬與真實環境的統一評估基準。OpenViTac 填補了此空白，建立了一個用於評估機器人策略的視觸覺操作基準，將接觸密集型操作系統化地歸納為四大觸覺相關能力。這有助於加速觸覺多模態模型在模擬與真實世界的對齊與遷移研究。

## Highly Relevant
- **Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs**：結合摺紙啟發輪胎與主動感測幾何控制的緊湊型移動機器人，利用 IMU 與融合節點將 LiDAR 投影至 RGB-D 深度流。[arXiv:2610.09828](https://arxiv.org/abs/2610.09828)
- **Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control**：提出 ResGAC，結合幾何導納控制（GAC）與殘餘強化學習，解決人形機器人全身運動中的浮動基座震盪與動態耦合問題。[arXiv:2610.09479](https://arxiv.org/abs/2610.09479)
- **Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies**：透過代理人框架將場景重建、政策開發與真實機器人執行緊密連結，自動化修復與對齊機器人工作空間的模擬環境。[arXiv:2610.10479](https://arxiv.org/abs/2610.10479)
- **Factorized Tactile Representation and Control for Sim-to-Real Manipulation**：提出因式分解的觸覺表示與控制框架，將接觸反應拆分為幾何、力分佈與時間變化，以橋接觸覺模擬與真實裝置。[arXiv:2610.10510](https://arxiv.org/abs/2610.10510)
- **SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models**：利用世界模型在城市環境下進行無人機（UAV）物件搜尋的空間價值接地想像，突破部分可觀測性限制。[arXiv:2610.09335](https://arxiv.org/abs/2610.09335)
- **Black-Box Adversarial Patch Attacks on VLAs via Ancestor VLM Exploitation**：探討視覺-語言-動作模型（VLA）透過繼承祖先 VLM 能力所產生的黑箱對抗修補攻擊與安全性漏洞。[arXiv:2610.09708](https://arxiv.org/abs/2610.09708)
- **RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation**：針對機器人操作影片生成引入對抗物理偏好最佳化，解決視覺真實但違反物理交互的盲點。[arXiv:2610.09454](https://arxiv.org/abs/2610.09454)
- **EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution**：提出自主演化的代理人框架，解決基底模型在面對環境與指令改變時的效能退化，提升主動探索效率。[arXiv:2610.10498](https://arxiv.org/abs/2610.10498)
- **RFPO: Rectified Flow Policy Optimization for Embodied Control**：提出基於流模型的控制政策最佳化框架，解決少步驟離散化間距問題，確保在粗糙數值積分下的控制可靠性。[arXiv:2610.10453](https://arxiv.org/abs/2610.10453)
- **TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning**：推出大規模包含 500 小時人類視覺與觸覺同步互動資料集，為視覺-觸覺學習提供充沛的物理監督訊號。[arXiv:2610.10288](https://arxiv.org/abs/2610.10288)
- **HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion**：平衡指令追蹤強健性與仿生學特徵，從人類運動資料中即時合成具備轉向能力的移動政策。[arXiv:2610.10489](https://arxiv.org/abs/2610.10489)
- **Point It, Strike It: Direction-Conditioned Dynamic Manipulation of Deformable Linear Objects**：探討可變形線狀物體（DLO）的單揮擊動態操作，納入 3D 位置與抵達方向的目標條件化控制。[arXiv:2610.09573](https://arxiv.org/abs/2610.09573)
- **Co-Evolving Robot Orchestrators and Policies through Deployment**：探討在真實世界部署中，如何透過協同演化來優化 VLA 政策與 VLM 協調器（Orchestrator）之間的互動。[arXiv:2610.09228](https://arxiv.org/abs/2610.09228)
- **Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models**：深入分析並量化 VLA 模型對指令措辭的高度敏感性，指出單一字詞替換即可造成大幅度的成功率波動。[arXiv:2610.10526](https://arxiv.org/abs/2610.10526)

## Interesting
- **Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs**：利用結構輕量、成本低廉且具備摺紙機械變形的輪胎設計來改變 chassis 俯仰角，藉此被動帶動 LiDAR 掃描 elevations，提供了一種非傳統且巧妙的硬體感測融合思路。[arXiv:2610.09828](https://arxiv.org/abs/2610.09828)

## Idea Sparks
1. **跨模態擴散策略中的「路徑交叉」與多峰坍縮防範**
   - 觀察：近期研究指出獨立雜訊配對會導致擴散策略在多模態動作分佈上產生坍縮，這顯示傳統擴散模型的噪聲排布可能不適用於動作空間高度耦合的機器人控制。
   - 後續問題：若將流匹配（Flow Matching）或整流流（Rectified Flow）引入多峰動作生成中，是否能比傳統擴散模型更有效地防止模態平均化？
2. **VLA 模型的語言敏感性與「先重述再行動」的魯棒性設計**
   - 觀察：VLA 模型對指令替換表現出驚人的敏感度，相同的語意僅因換句話說就可能使成功率從 100% 跌至 2%。
   - 後續問題：在 VLA 部署前端加入輕量級的指令正規化或同義句擴增引導模組，是否能實質提升模型在開放世界部署時的語意泛化能力？
3. **視觸覺（Visuo-Tactile）大規模資料集與模擬遷移**
   - 觀察：隨著 TouchScale 等大型視觸覺資料集的出現，觸覺回饋正逐漸從獨立感測走向與視覺、語言深度融合的通用代理人架構。
   - 後續問題：如何有效對齊跨不同觸覺硬體裝置（如 GelSight 等）的物理反應與高維特徵表示，才能使觸覺基礎模型達到類似視覺模型的跨平台零樣本泛化？
