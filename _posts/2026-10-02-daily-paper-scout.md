---
layout: post
title: "每日論文雷達｜2026-10-02"
date: 2026-10-02 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-02
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 883 篇論文，經過去重後剩餘 769 篇候選，其中符合關鍵字條件共 74 篇，挑選出 30 篇進行深入追蹤。

---

## Must-Read

- [TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.s/abs/2610.00899)
  - **作者**：Keisuke Shirai, Tomohiro Motoda, Hanbit Oh, Ryoichi Nakajo, Roman Mykhailyshyn
  - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_keyword
  - **重點與關聯**：自迴歸視覺-語言-動作（VLA）模型常將連續機器人動作離散化以符合預測目標。作者探討現有確定性動作標記化方法（如 FAST）在利用有限示範學習時效率不足的問題，並提出隨機機器人動作標記化方法（TOAST）。這對研究 VLA 模型表示學習與資料效率的研究者具有高度啟發性。

- [NarrativeFlow: Flow-Based Vision-Language-Action Model Using Robot Velocity Fields](https://arxiv.s/abs/2610.00981)
  - **作者**：Shota Kobayashi, Koki Seno, Daichi Yashima, Komei Sugiura
  - **來源**：arxiv_cs.RO, arxiv_cs.CV, arxiv_keyword
  - **重點與關聯**：針對語言條件式操控中跨平台資料收集困難的問題，本篇研究提出 NarrativeFlow，利用機器人速度場（Robot Velocity Fields）作為跨本體（embodiment-agnostic）、以動作為中心的表示法。此方向有助於解決多機器人平台資料規模化的瓶頸。

- [DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication](https://arxiv.s/abs/2610.02161)
  - **作者**：Hanchu Zhou, Dechen Gao, Hang Wang, Brendan Lynch, Boqi Zhao
  - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_keyword
  - **重點與關聯**：將 VLM 與 VLA 模型擴展至多機器人協同系統。DuoMind 透過語義通訊（semantic communication）建立分散式階層框架，結合低階動作執行的 VLA 與高階長時序推理的 VLM，提供多機器人協同的新解法。

---

## Highly Relevant

- [PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models](https://arxiv.s/abs/2610.01162)
  - **作者**：Isaiah Milkey, Som Sagar, Aditya Taparia, Xinyuan Liu, Jiqing Wen
  - **來源**：arxiv_cs.RO, arxiv_cs.CV
  - **重點與關聯**：探討視訊世界模型（video world models）在物理屬性（如重量、黏性、摩擦力）上的盲點，並引入 PhysicsLENS 資料集與基準，對評估具身智慧中的預測性物理模擬品質有直接關聯。

- [Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies](https://arxiv.s/abs/2610.00982)
  - **作者**：Xuehui Yu, Eason Yu, Meiyi Wang, Haozhe Du, Stefano V. Albrecht
  - **來源**：arxiv_cs.RO, arxiv_cs.AI
  - **重點與關聯**：以 POMDP 的模仿學習公式出發，將歷史記憶最佳化問題定義為最大化動作與記憶之間的條件互資訊，藉此改善 VLA 策略在歷史相依長時序任務（history-dependent manipulation tasks）中的表現。

- [MIKASA-Robo-VLA: Benchmarking Memory in VLA Models for Long-Horizon Manipulation](https://arxiv.s/abs/2610.00604)
  - **作者**：Egor Cherepanov, Nikita Kachaev, Aleksandr I. Panov, Alexey K. Kovalev
  - **來源**：arxiv_cs.RO
  - **重點與關聯**：提出 MIKASA-Robo-VLA 基準，包含 90 個語言條件式操控任務，專門用來評估 VLA 模型在任務進行中隱藏關鍵線索時的記憶與長時序處理能力。

---

## Interesting

- [Measuring the Stability Assumption Behind Action Chunking](https://arxiv.s/abs/2610.01626)
  - **作者**：Aryan Goyal
  - **來源**：arxiv_cs.AI
  - **重點與關聯**：分析行為複製（behavioral cloning）中常用的動作分塊（action chunking）機制，透過在開迴圈與閉迴圈執行下注入小動作錯誤，量化錯誤增長或縮小的速率。

- [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.s/abs/2610.01351)
  - **作者**：Sophie Higham, Riccardo Andrea Izzo, Matteo Matteucci, Alessandro Suglia
  - **來源**：arxiv_cs.RO
  - **重點與關聯**：擴展 LIBERO 與 LIBERO-Plus 基準，提出基準無關的評估框架，不只看任務成功率，更著重於受擾動下成功軌跡的行為強健性。

- [DITTO-X: Forward and Reverse Teleoperation for Dexterous Manipulation and Human Intervention](https://arxiv.s/abs/2610.00781)
  - **作者**：Zhanpeng He, Joaquin Palacios, Zhangyu Wang, Chenhao Li, Katelyn Lee
  - **來源**：arxiv_cs.RO
  - **重點與關聯**：針對靈巧手與人類介入提出 DITTO-X 遠端操作系統，支援正向與反向操作，特別適用於半自主中由操作者中途接管靈巧抓取任務的情境。

- [Toward Humanoid Robots in Construction: A Teleoperation Feasibility Study](https://arxiv.s/abs/2610.00718)
  - **作者**：Parastoo Ali Pour, David R. Martin, Chang Min Hur, Bo Zhang, Tommy Zhou
  - **來源**：arxiv_cs.RO
  - **重點與關聯**：結合擴增實境（XR）上半身控制與踏板式移動，在 Unitree G1 人型機器人上實現建築任務的同步操控與移動可行性研究。

---

## Idea Sparks

- **觀察一：VLA 模型中的長期記憶與歷史依賴建模**
  多篇論文（如 `2610.00982`、`2610.00604`）指出，現有 VLA 模型在面對僅依賴早期觀察或隱藏線索的長時序（long-horizon）任務時往往表現不佳。這顯示當前多數基於短時序或單一畫面的 VLA 架構仍有結構性限制。
  - **後續問題**：如何將基於互資訊的最佳化記憶模組與大規模預訓練的 VLA 基礎模型無縫整合，而不破壞其原本的零樣本泛化能力？

- **觀察二：跨本體表示與連續動作流的泛化**
  從 `2610.00981` 提出的機器人速度場跨平台表示法來看，社群正積極尋找能擺脫特定機器人本體限制的運動特徵。
  - **後續問題**：以速度場為基礎的跨平台動作表示，是否能有效擴展至具備複雜動態與高自由度的靈巧雙手操控任務中？
