---
layout: post
title: "每日論文雷達｜2026-10-23"
date: 2026-10-23 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-23
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量與資料統計**：本次檢索自 Hugging Face 與 arXiv 跨領域（涵蓋機械人學 `cs.RO`、人工智慧 `cs.AI`、電腦視覺 `cs.CV`、機器學習 `cs.LG` 等）共爬取 1,469 篇論文。經過去重複與候選視窗過濾後，獲得 493 篇新候選論文，並經評估模型篩選出 60 篇具備高參考價值的具身智慧相關研究。

---

## Must-Read

1. **GelSlim 5.0: Unifying Vision and Touch with a Single Fingertip Camera**
   - **作者**：Xiangdong Wang, I-Hsuan Huang, Xiaohao Xu, Xili Yi, Nima Fazeli
   - **來源**：[arXiv:2610.31334](https://arxiv.org/abs/2610.31334)
   - **技術突破點與啟發**：此研究針對機器人指尖觸覺與視覺常因外置相機遮蔽而難以融合的痛點，提出 GelSlim 5.0。其透過單一固定相機與連續 UV 響應接觸層，藉由切換照明順序性地獲取穿透膜的視覺影像與接觸敏感的觸覺影像，從根本消除了跨相機外參標定的誤差。搭配全新的多模態 Transformer 架構（VisTacFusion），為靈巧操作提供同步的幾何與區域接觸線索。

2. **In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations**
   - **作者**：Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen
   - **來源**：[arXiv:2610.30988](https://arxiv.org/abs/2610.30988)
   - **技術突破點與啟發**：軟性物件（如衣物）的操作因高維狀態空間與動態變形而極具挑戰。該論文提出具備內文學習能力的世界模型（In-Context Learning World Models），使雙臂機器人能在僅有部分觀測的情況下，「想像」物件的形狀與材質特性，預測動作對未來狀態的影響。這項技術大幅提升了具身智慧在應對真實世界非剛體時的泛化能力。

3. **Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation**
   - **作者**：Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
   - **來源**：[arXiv:2610.31166](https://arxiv.org/abs/2610.31166)
   - **技術突破點與啟發**：人形機器人在動態場景中的協同移動與操作（Loco-manipulation）本質上是非馬可夫的，因為當機器人轉頭或移動時，關鍵物件往往會暫時離開視線。本文提出的 `WholeBodyMem` 引入以物件為引導的感知記憶機制，利用 SAM3 追蹤任務物件，並結合跨注意力機制讓動作專家同時讀取包含外觀、幾何與時間戳記的歷史標記，解決了傳統 VLA（Vision-Language-Action）策略「只看當下」的盲點。

4. **DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models**
   - **作者**：Adam Lee, Mutian Xu, Yukang Cao, Shulin Tian, Ziwei Liu
   - **來源**：[arXiv:2610.30781](https://arxiv.org/abs/2610.30781)
   - **技術突破點與啟發**：現有的世界模型常將動作條件動態、相機運動與視覺合成直接纏結在影片生成模型中，忽略了明確的 3D 物理結構。`DeXplicit` 透過在渲染視覺後果之前，先在度量 3D 空間中明確預測世界如何演化，成功捕捉靈巧操作中的物理狀態。這對需要精細物理推理的機器人靈巧操作帶來了重要的架構轉變。

---

## Highly Relevant

1. **Integrated Respiratory Sensing and Gated Control for Autonomous Needle Insertion Via CT Bore Robotic Arm**
   - **作者**：Emma Huang, Moira Bohley, Krishna Jamakhandi, Rebecca Fellbaum, Sophia Tang
   - **來源**：[arXiv:2610.30452](https://arxiv.org/abs/2610.30452)
   - **摘要重點**：提出能在 CT 內進行呼吸控制與閘控穿刺的機器人系統，減少患者配合憋氣的負擔並降低輻射暴露。

2. **AstroBench: Free-Floating Capture and Space Robotic Manipulation**
   - **作者**：Zizhe Wang, Jia Deng, Xin Lu, Zehao Jia, Yi Huang
   - **來源**：[arXiv:2610.31064](https://arxiv.org/abs/2610.31064)
   - **摘要重點**：建立針對太空無重力環境下自由漂浮目標捕捉與太空機械人操作的開放基準測試集（AstroBench）。

3. **Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation**
   - **作者**：Jingyu Ru, Xiangyuan Xie, Lixuan Jin, Jian An, Xingming Zhang
   - **來源**：[arXiv:2610.30810](https://arxiv.org/abs/2610.30810)
   - **摘要重點**：結合大型語言模型輔助的主動任務生成，解決空中移動操作（Aerial Loco-manipulation）中因質心轉移與慣性變化帶來的控制難題。

4. **OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing**
   - **作者**：Ariel Slepyan, Geeta Chandra Raju Bethala, Jiafeng Gu, Anagha Rajendra Dangle, Yinzhe Zhou
   - **來源**：[arXiv:2610.31661](https://arxiv.org/abs/2610.31661)
   - **摘要重點**：推出可客製化、可擴展且具備 3D 觸覺感測能力的開源觸覺面板生態系 `OpenTac`。

5. **LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation**
   - **作者**：Dewei Wang, Jinrui Han, Jiyuan Shi, Chenyun Zhang, Xianbo Lu
   - **來源**：[arXiv:2610.30876](https://arxiv.org/abs/2610.30876)
   - **摘要重點**：提供涵蓋資料收集、策略訓練、評估與實機部署的人形機械人全身協同測試平台。

6. **DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control**
   - **作者**：Fanxing Li, Yuxiang Huang, Shengyang Wang, Fangyu Sun, Shuyu Wu
   - **來源**：[arXiv:2610.31617](https://arxiv.org/abs/2610.31617)
   - **摘要重點**：將學習型世界模型與可微分模擬緊密耦合，優化具備高動態需求的四旋翼飛行器控制。

7. **TRACE: Traversability-aware Reactive Navigation via VLM-driven Adaptive Constraints Estimation**
   - **作者**：Mario A. V. Saucedo, Midhun Edatharam Kunnath, Elias Small, Akash Patel, Shruti Kotpalliwar
   - **來源**：[arXiv:2610.30994](https://arxiv.org/abs/2610.30994)
   - **摘要重點**：利用視覺語言模型（VLM）驅動的適應性約束估計，實現非結構化森林環境中的可通行性感知導航。

8. **Continuous-Time Motion Planning and Steering with Global Convergence**
   - **作者**：Mohsen Amiri, Sima Didari, Davoud Ataee Tarzanagh, Hankyu Moon, Yeongdae Kwon
   - **來源**：[arXiv:2610.30607](https://arxiv.org/abs/2610.30607)
   - **摘要重點**：將路徑規劃與轉向整合為單一連續時間規劃程式，並在結合平滑成本與約束下具備全域收斂性證明。

9. **Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation**
   - **作者**：Jona Joy
   - **來源**：[arXiv:2610.30197](https://arxiv.org/abs/2610.30197)
   - **摘要重點**：建立系統性故障注入框架，用以評估大型語言模型驅動之具體操作在感知、致動與規劃層面的強健性。

10. **VecTile: A Low-Cost Flexible Tactile Array for 3-DoF Force Sensing**
    - **作者**：Jian Hou, Xin Zhou, Adam J. Spiers
    - **來源**：[arXiv:2610.31472](https://arxiv.org/abs/2610.31472)
    - **摘要重點**：開發低成本、薄型且具備三軸（3-DoF）力量感測能力的彈性觸覺陣列。

---

## Interesting

1. **Probabilistic Energy Modeling Unifies Versatile Swarm Control**
   - **作者**：Xiang Zhou, Xiangyu Zhu, Xiangyu Zhu, Xintong Wang, Qingyuan Yang, Rui Huang
   - **來源**：[arXiv:2610.31371](https://arxiv.org/abs/2610.31371)
   - **點評**：透過基布茲隨機場（Gibbs random field）能量最小化與結構化獎勵最大化的對應關係，將群體機器人控制表述為統一的機率能量模型。雖然屬於多 agente 領域，但其組合式控制原則對具身智慧的模組化行為組合有啟發性。

2. **Multimodal Progress-Residual Fusion for Anticipating Navigation Retreat in Robotic Flexible Endoscopy**
   - **作者**：Chi Kit Ng, Tianchun Wu, Jiatan Sun, Yuming Sun, Jianru Zhang
   - **來源**：[arXiv:2610.31028](https://arxiv.org/abs/2610.31028)
   - **點評**：探討內視鏡機器人在窄小管腔中操作時，如何透過多模態殘差融合預測何時該「後退」以恢復安全構型，展示了微創手術機器人中對非結構化環境反饋的處理。

3. **RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation**
   - **作者**：Aleksandr Lazarev, Sofia Zimina, Roman Kuznetsov, Tatiana Zemskova, Iaroslav Koshelev
   - **來源**：[arXiv:2610.31121](https://arxiv.org/abs/2610.31121)
   - **點評**：針對機器人影片生成模型常出現「看起來合理但互動錯誤」的問題，提出以任務為基礎的時間場景圖（Scene Graphs）進行客觀評估，有助於未來生成式具身模型的評測標準化。

---

## Idea Sparks

1. **從「只看當下」到「物件引導的時間序列記憶」**
   - **跨論文觀察**：本次多篇重要研究（如針對人形機器人 loco-manipulation 的 `WholeBodyMem`）指出，當機器人進行動態任務時，VLA 模型容易因視角轉變而遺失過去的關鍵狀態。這顯示出具身代理不能僅依賴當前影格，必須引入結構化的時間序列與物件感知記憶。
   - **後續研究問題**：如何在保持 VLA 模型即時推理效率的同時，設計出一套低計算負載、長短時間皆宜的記憶壓縮與檢索機制？

2. **具身世界模型的範式轉移：從像素到明確的 3D 物理狀態**
   - **跨論文觀察**：從 `DeXplicit` 揚棄純影像生成的黑盒子預測、改在度量 3D 空間中明確預測物理演化，可以看出具身世界模型正逐步從「純視覺影片預測」轉向「結合 3D 幾何與物理法則的狀態預測」。
   - **後續研究問題**：當我們將明確的 3D 物理狀態引入世界模型後，如何有效結合觸覺（如 `GelSlim 5.0` 或 `VecTile` 的接觸資料）來修正內部物理狀態的偏差？
