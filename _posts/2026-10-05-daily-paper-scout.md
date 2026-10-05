---
layout: post
title: "每日論文雷達｜2026-10-05"
date: 2026-10-05 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-05
- **主題**：具身智慧（Embodied Intelligence）
- **收錄數量**：本次爬取總計 762 篇論文（去重後 656 篇，符合關鍵字條件 58 篇），挑選出 30 篇候選，精選前 10 篇進行重點分析。
- **資料統計**：涵蓋 `arxiv_cs.RO`（150篇）、`arxiv_cs.AI`（250篇）、`arxiv_cs.CV`（250篇）與 `huggingface`（100篇）等來源。

---

## Must-Read

1. **MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation**
   - **作者**：Chenzhi Liu, Yue Zhang, Jiehong Lin, Jianan Wang, Bo Wang
   - **連結**：[arXiv:2610.03476](https://arxiv.org/abs/2610.03476)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_keyword`
   - **摘要證據與關聯**：針對長時序移動操作（long-horizon mobile manipulation）中常見的累積執行誤差與移動/手臂控制間的容量干擾，該論文提出 MobiAgent，一個結合強健部署執行與遞迴策略自我改善的雙迴圈代理架構（dual-loop agentic framework）。對於研究多階段目標與分層推理的具身智慧研究者而言，此架構嘗試解決現有分層代理在子任務對齊僵化與缺乏持續學習上的限制。

2. **RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer**
   - **作者**：Chenxi Li, Zhangrui Zhao, Rui Li, Yuan Gao, Kehui Liu
   - **連結**：[arXiv:2610.02717](https://arxiv.org/abs/2610.02717)
   - **來源**：`arxiv_cs.RO`
   - **摘要證據與關聯**：探討模擬到真實世界（sim-to-real）轉移與部署後持續調適的挑戰。端對端視覺-語言-動作（VLA）策略雖具備強大操作能力，但通常需依賴視覺與動態條件校準及額外示範。該文提出的 RoboBridge 框架切中具身智慧在現實環境落地時的關鍵痛點。

3. **Equivariant Visual-Tactile Diffusion Policy for Contact-Rich Manipulation**
   - **作者**：Lik Hang Kenny Wong, Yiyao Ma, Xiu-Shen Wei, Zelong Tan, Zhuheng Song
   - **連結**：[arXiv:2610.03333](https://arxiv.org/abs/2610.03333)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
   - **摘要證據與關聯**：針對接觸豐富（contact-rich）操作中模仿學習樣本昂貴的問題，提出 VISTA（workspace-level equivariant visuotactile diffusion policy）。該方法將視覺與觸覺觀測投射為球形 token，透過置換等變球形融合（permutation-equivariant spherical fusion）注入觸感，並利用末端執行器定向旋轉諧波表示。這為多模態感知與觸覺整合提供了高度樣本效率的解決方案。

4. **SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining?**
   - **作者**：Chen Yang, Linzhe Shi, Changjie Wu, Hang Zhang, Ronghan Chen
   - **連結**：[arXiv:2610.02784](https://arxiv.org/abs/2610.02784)
   - **來源**：`arxiv_cs.RO`, `arxiv_keyword`
   - **摘要證據與關聯**：探討是否能在無需大規模觸覺策略預訓練或獨立視觸覺對齊的情況下，將觸覺引入預訓練的 VLA 模型中。作者提出 SimpleTouch，透過在 $\pi_{0.5}$ 擴展觸覺模組來檢驗跨模態鴻溝的橋接可能性，對簡化具身模型觸覺整合流程有直接參考價值。

5. **Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation**
   - **作者**：Xincheng He, Siyu Ma, Chang Yu, Yunuo Chen, Yanjia Huang
   - **連結**：[arXiv:2610.02788](https://arxiv.org/abs/2610.02788)
   - **來源**：`huggingface`, `arxiv_cs.RO`
   - **摘要證據與關聯**：聚焦於零樣本 sim-to-real 機器人操作中的技能轉移，提出 Skill2Real 代理政策框架。透過結合 API、Proposer-Verifier-Governor（PVG）循環來診斷結果與驗證更新，並劃分 Cerebellum（學習局部操作技能）與 Brain（學習任務級組合），提供了一種結合特權模擬證據與公開觀測的代理學習路徑。

---

## Highly Relevant

1. **Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis**
   - **作者**：Keerthi Kaashyap, Dennis Anthony, Akshay Krishnan, Nhi Ngoc Nguyen, Jeremy Collins
   - **連結**：[arXiv:2610.03717](https://arxiv.org/abs/2610.03717)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
   - **摘要證據與關聯**：探討新視圖合成（NVS）在幾何表徵學習中的作用，指出空間表現力過強的解碼器會稀釋場景編碼器能力。對研究世界模型與空間智慧（spatial intelligence）的研究者而言，有助於重新審視特徵學習的架構設計。

2. **OmniAct3D: Leveraging Foundation Geometry and Evidence-Grounded Reasoning for Panoramic 3D Detection**
   - **作者**：Runtong Wu, Fei Teng, Di Wen, Guoqiang Zhao, Kunyu Peng
   - **連結**：[arXiv:2610.03015](https://arxiv.org/abs/2610.03015)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
   - **摘要證據與關聯**：針對移動具身代理所需的 3D 檢測，提出利用等距矩形投影（ERP）編碼連續 360 度場景的 OmniAct3D 框架，克服現有視覺基礎模型（VFMs）在窄視角單目影像上的侷限。

3. **FastOPD: On-Policy Distillation for Lightweight VLA Deployment**
   - **作者**：Yoojin Oh, Jeongsol Kim, Yeonwoo Seo, Jangho Park, Seonghyun Jin
   - **連結**：[arXiv:2610.02832](https://arxiv.org/abs/2610.02832)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
   - **摘要證據與關聯**：針對大型 VLA 模型在真實世界部署面臨的高計算成本，提出基於流對應（flow map）的高效政策內蒸餾（on-policy distillation）框架 FastOPD，兼顧輕量化與執行可行性。

4. **World-Calibrated Proposal-to-Action Flow for Vision-Language-Action Models**
   - **作者**：Jie He, Wei Li, Junwen Tong, Rui Shao, Wei-Shi Zheng
   - **連結**：[arXiv:2610.02323](https://arxiv.org/abs/2610.02323)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`, `arxiv_keyword`
   - **摘要證據與關聯**：提出 ProAct，透過世界校準的提案到動作流（proposal-to-action flow），解決基於流的 VLA 政策在任務無關等向高斯源上捨棄局部連續性的問題，將預測性世界表示納入生成起點與動態條件中。

---

## Interesting

1. **Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models**
   - **作者**：Yukiya Horiba, Koshiro Aoki, Shunsuke Yasuki, Bum Jun Kim, Taiki Miyanishi
   - **連結**：[arXiv:2610.03498](https://arxiv.org/abs/2610.03498)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
   - **摘要證據與關聯**：使用稀疏自動編碼器（SAE）對 VLA 模型的內部機制進行機械式分析，識別出與對抗性貼布（adversarial patch）強相關的特徵並進行推論時抑制。此研究提供了 VLA 模型安全與內部表徵解析的新視角，雖與核心導航/操作動作生成較間接，但對具身系統安全性具參考價值。

---

## Idea Sparks

1. **觸覺整合與等變表示的結合（VISTA vs. SimpleTouch）**：
   - 觀察：今日收錄的論文中，部分研究（如 VISTA）強調透過工作空間層級的等變球面融合來專門處理觸覺與視覺；另一部分研究（如 SimpleTouch）則探討直接在現有大模型（$\pi_{0.5}$）中擴展觸覺模組，免去繁瑣的預訓練。
   - 後續問題：在不需大規模觸覺策略預訓練的情況下，結合等變幾何特徵是否能進一步降低跨模態對齊的樣本需求？

2. **長時序規劃與策略自我改善的閉環架構（MobiAgent vs. Skill2Real）**：
   - 觀察：MobiAgent 與 Skill2Real 分別透過雙迴圈遞迴策略與 Proposer-Verifier-Governor 迴圈，在模擬或真實環境中進行錯誤診斷與任務級組合。
   - 後續問題：如何將這類基於代理（Agentic）的驗證與自我改善機制，輕量化地嵌入到端對端流匹配（Flow-matching）或擴散策略（Diffusion Policy）的推論過程中？
