---
layout: post
title: "每日論文雷達｜2026-10-26"
date: 2026-10-26 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-26
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總數計 1,149 篇，經過重複刪除與過濾後剩餘 911 篇候選文。其中進入決策評估的論文為 250 篇，最終收錄並推薦 18 篇高品質研究。
- **資料統計**：涵蓋領域包含機器人學 (`arxiv_cs.RO`)、人工智慧 (`arxiv_cs.AI`)、電腦視覺 (`arxiv_cs.CV`) 與機器學習 (`arxiv_cs.LG`) 等。

---

## Must-Read

本期最值得關注的突破性研究，在於 VLA 模型的效能診斷、硬體自我複製機制、以及多模態世界模型的具體實踐：

1. **Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems**
   - **作者**：Christian A. Rogers, Qian Lin, Daniel S. Brown
   - **連結**：[arXiv:2610.32208](https://arxiv.org/abs/2610.32208)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.LG`
   - **技術突破與啟發**：該研究透過稀疏自編碼器（Sparse Autoencoders, SAE）解析 OpenVLA 的內部啟動狀態，成功在機器人進入不可挽回的失敗狀態前預測任務失敗。這項研究為黑盒子 VLA 模型提供了可解釋的成功與失敗模式，讓研究者能精準追蹤行為特徵與任務階段的關聯。

2. **RynnUnify: Towards Unified Embodied Brain**
   - **作者**：Minghao Zhu, Bohan Hou, Kun Xiang, Zixuan Wang, Yinzhou Tang
   - **連結**：[arXiv:2610.32965](https://arxiv.org/abs/2610.32965)
   - **來源**：`huggingface`, `arxiv_cs.RO`
   - **技術突破與啟發**：提出 16B 規模的統一具身模型（Unified Embodied Brain），透過交錯視訊與語言推理（Interleaved Video-Language Reasoning），無縫結合具身理解、長視距視覺規劃與物理狀態預測，為具身代理提供更強大的世界狀態預期能力。

3. **Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates**
   - **作者**：Shubham Singh
   - **連結**：[arXiv:2610.31859](https://arxiv.org/abs/2610.31859)
   - **來源**：`arxiv_cs.RO`
   - **技術突破與啟發**：本篇研究點出實務上常被忽略的關鍵訓練陷阱：在 bfloat16 權重下進行 VLA 全參數微調若缺少 fp32 主副本（Master Copy），AdamW 優化器會無聲地將小於 $1/512$ 的更新四捨五入歸零，導致多數開源碼庫（包含 LeRobot 等）的微調更新被靜默抹除。這對所有進行具身微調的研究者具有極高的警示與實用價值。

4. **Robotic Budding: From Homogeneous Cells to Diverse Morphologies in Physical Self-Reproduction**
   - **作者**：Siyuan Zhang, Junyan Liu, Wanglin He, Hod Lipson
   - **連結**：[arXiv:2610.31929](https://arxiv.org/abs/2610.31929)
   - **來源**：`arxiv_cs.RO`
   - **技術突破與啟發**：借鏡生物細胞分化原理，設計出結合磁性對接介面與雙驅動關節的標準化模組，能從平坦的 2D 結構折疊為 3D 形態，並在實體硬體中組裝成三葉蟲（trilobite）與海豹（seal）等多樣化形態，推進了模組化機器人實體自我複製的極限。

---

## Highly Relevant

1. **WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations**
   - **作者**：Tianling Xu, Weijie Wan, Honghao Su, Kailun Su, Junyuan Tang
   - **連結**：[arXiv:2610.31834](https://arxiv.org/abs/2610.31834)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
   - **摘要**：結合通用代理與生成模型，從野外機器人示範中自動重建高保真視覺與具備物理一致性的互動模擬世界，提升 Sim-to-Real 的擴展性。

2. **Emergent Cooperative Thermoregulation in Lunar Swarm Robotics**
   - **作者**：Anais Jeger, Harry Holt, Lennart Puck
   - **連結**：[arXiv:2610.31868](https://arxiv.org/abs/2610.31868)
   - **來源**：`arxiv_cs.RO`
   - **摘要**：探討月球夜間極端低溫下，群體機器人如何透過共享強化學習策略，利用彼此身體作為熱屏障進行集體熱調節。

3. **Multimodal MPC via Bayesian Set Optimization for Dynamic Manipulation of Deformable Linear Objects**
   - **作者**：Youyuan Long, Gokhan Solak, Arash Ajoudani
   - **連結**：[arXiv:2610.31852](https://arxiv.org/abs/2610.31852)
   - **來源**：`arxiv_cs.RO`
   - **摘要**：提出 BM2PC 貝氏多模態模型預測控制框架，解決可變形線狀物（DLO）動態操作中的高維動力學與多重可行動作選擇難題。

4. **Facultative Swarming: A Capability, Not a Category, for Multi-Robot Systems**
   - **作者**：Ning Zhou, Edmund R. Hunt
   - **連結**：[arXiv:2610.32526](https://arxiv.org/abs/2610.32526)
   - **來源**：`arxiv_cs.RO`
   - **摘要**：打破集中式與分散式多機器人的傳統界線，提出「隨需群體化」（facultative swarming）混合架構，在正常條件下集中規劃，壓力下則平滑降級為分散式自組織。

5. **DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation**
   - **作者**：Meng Li, Lijiang Chen, Qi Zhao, Jun Jiang, Longhao Zou
   - **連結**：[arXiv:2610.32330](https://arxiv.org/abs/2610.32330)
   - **來源**：`arxiv_cs.RO`
   - **摘要**：針對機器人操作引入以槽（Slot）為中心的 3D 動態預訓練，避免傳統全景式建模混淆局部互動與無關背景。

6. **OWLS: Open-world Language-conditioned Speed Fields for Zero-Shot Rover Navigation**
   - **作者**：Chahyon Ku, Erica Tevere, Georgios Georgakis, Rudra Mukherjee, Bernadette Bucher
   - **連結**：[arXiv:2610.32596](https://arxiv.org/abs/2610.32596)
   - **來源**：`arxiv_cs.RO`
   - **摘要**：利用開放詞彙視覺語言模型（VLM）對影像像素評分，將語義對應至地表速度場，實現零樣本（Zero-Shot）探測車導航。

7. **From Freehand Demonstrations to Autonomous Robotic Ultrasound: An Anatomy-Anchored Learning Framework**
   - **作者**：Yuan Bi, Fangxu Han, Ye Su, Yiping Zhou, Zhongliang Jiang
   - **連結**：[arXiv:2610.32525](https://arxiv.org/abs/2610.32525)
   - **來源**：`arxiv_cs.RO`
   - **摘要**：提出以解剖學為錨點的模仿學習框架，將徒手示範轉換為一致且精準的自主超音波掃描控制策略。

8. **FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation**
   - **作者**：Xiao Tan, Yixuan Wang, Zhexi Wang, Wenzhen Yuan
   - **連結**：[arXiv:2610.31841](https://arxiv.org/abs/2610.31841)
   - **來源**：`arxiv_cs.RO`
   - **摘要**：運用視覺與腕部力/扭矩（F/T）回饋作為輸入的編程代理，自動編寫並診斷接觸密集型操作的 Python 控制程式。

9. **See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space**
   - **作者**：Jiawei Chen, Yinxi Wang, Zihan Yang, Meijun Gao, Yaowei Liu
   - **連結**：[arXiv:2610.31762](https://arxiv.org/abs/2610.31762)
   - **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
   - **摘要**：提出 RepresentNav 導航基礎模型，透過特徵殘差（Representation Residuals）建構專屬於導航任務的自主視覺表徵空間。

10. **TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation**
    - **作者**：Samuel Triest, Amirreza Shaban, David D. Fan, Wenshan Wang, Sebastian Scherer
    - **連結**：[arXiv:2610.32130](https://arxiv.org/abs/2610.32130)
    - **來源**：`arxiv_cs.RO`
    - **摘要**：專為高速越野導航設計的自監督、具備不確定性感知能力的通行性評估系統。

11. **HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching**
    - **作者**：I-tak Ieong, Hao Tang
    - **連結**：[arXiv:2610.32554](https://arxiv.org/abs/2610.32554)
    - **來源**：`arxiv_cs.RO`
    - **摘要**：結合 LLM 房間錨點先驗與持久性空間語義記憶的階層式圖引導世界模型，用於零樣本物件導航。

12. **Move, don't think: sample-efficient collision avoidance with lossy proximity sensors**
    - **作者**：Carson Kohlbrenner, Niraj Pudasaini, William Xie, Naren Sivagnanadasan, Nikolaus Correll
    - **連結**：[arXiv:2610.31891](https://arxiv.org/abs/2610.31891)
    - **來源**：`arxiv_cs.RO`
    - **摘要**：發現低解析度的有損全身鄰近感測器比高解析度感測器更具備學習樣本效率，能有效引導機器人進行反射式防撞。

13. **UAV-SwarmAgent: Scalable Multi-UAV Reconnaissance and Task Allocation via Code Generation and Vision-Language Reasoning**
    - **作者**：Oleg Sautenkov, Yaasheerah Yaqoot, Muhammad Ahsan Mustafa, Grigorii Kalinin, Chih-Yung Wen
    - **連結**：[arXiv:2610.32559](https://arxiv.org/abs/2610.32559)
    - **來源**：`arxiv_cs.RO`
    - **摘要**：利用自然語言指令透過代碼生成與 VLM 推理，實現多無人機偵察任務的自動化路線規劃與工作分配。

14. **SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning**
    - **作者**：Yuhan Liu, Lianhui Qin, Shenji Wan
    - **連結**：[arXiv:2610.32978](https://arxiv.org/abs/2610.32978)
    - **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
    - **摘要**：結合擴散視覺先驗與合約引導的 3D 編譯，自動生成多樣化且符合物理規律的室內模擬環境。

---

## Interesting

此處收錄概念創新但架構或場景較為小眾的研究：

1. **資料未提供 (Robotic Budding 系列拓展或模組化分支)**：部分探索微型模組化機器人在極端環境下重組的研究，雖具啟發性但實用落地期較長。

---

## Idea Sparks

1. **跨論文趨勢一：從 VLA 的黑盒子輸出轉向內部表徵的可解釋性與數值穩定性監控**
   - 觀察：近期研究（如利用 SAE 預測 VLA 失敗、點出 bfloat16 微調權重被靜默四捨五入）顯示，具身基礎模型的痛點已從「如何架構模型」轉向「如何診斷與穩定訓練」。
   - 後續問題：我們能否設計一套線上即時診斷工具，在 VLA 執行動作時即時攔截並修正因數值精度或潛在特徵異常所導致的錯誤決策？

2. **跨論文趨勢二：解耦物件與場景動態的世界模型建構**
   - 觀察：從 DynaSlots 的槽中心 3D 動態預訓練到 WorldMirror 的代理式 Real-to-Sim 生成，近期世界模型強調「區域化與語義分離」，揚棄了過往粗糙的全景壓縮。
   - 後續問題：將槽中心（Slot-centric）表徵與具身語言動作模型（VLA）結合後，能否在動態干擾頻繁的真實家庭環境中大幅提升長序列操作的泛化能力？
