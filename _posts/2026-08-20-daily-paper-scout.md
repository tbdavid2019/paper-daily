---
layout: post
title: "每日論文雷達｜2026-08-20"
date: 2026-08-20 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

* **日期**：2026 年 8 月 20 日
* **主題**：具身智慧（Embodied Intelligence）
* **資料統計**：今日爬取資料總量共 760 篇（來源涵蓋 arXiv cs.RO 148 篇、cs.AI 250 篇、cs.CV 250 篇、Hugging Face 100 篇、arXiv keyword 12 篇，其餘來源為 0 篇）。經去重後為 665 篇，時間窗口內候選論文 623 篇（其中已見過 384 篇，新候選 239 篇）。最終經關鍵字匹配並篩選出 22 篇，本篇雷達精選其中 10 篇最具代表性的預印本研究進行重點剖析。

---

## Must-Read

### The Embodiment Gap in Robot Foundation Models
* **作者**：Yukiyasu Domae, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Tomohiro Motoda
* **連結**：https://arxiv.org/abs/2608.18433
* **來源**：arXiv (cs.RO, keyword)
* **重點與關聯**：機器人基礎模型（Robot Foundation Models, RFMs）與視覺-語言-動作（VLA）策略常依賴擴展資料與模型規模來提升泛化能力。然而，這篇調查預印本指出，模型在通用層面泛化後，要部署於特定硬體構型的機器人本體上仍存在顯著工程差距，論文將此定義為「具身落差（Embodiment Gap）」。研究系統性地探討了可重用模型、特徵表示與資料在遷移至目標機器人執行時所面臨的結構性障礙，對致力於通用機器人模型實際部署的研究者具有高度指引價值。

### SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation
* **作者**：Bowen Jing, Mingxin Wang, Ruiyang Hao, Chenchen Ge, Hanwen Shen
* **連結**：https://arxiv.org/abs/2608.18701
* **來源**：Hugging Face, arXiv (cs.RO)
* **重點與關聯**：現有變形物體操作基準往往僅評估任務是否成功，忽略了操作過程中的滑移或過度擠壓等物理接觸品質。本研究推出了 SoftVTBench，這是一個具備變形感知能力的視觸覺資料集與基準，收錄了 4,000 筆專家示範與超過 50 種物件資產（包含體積可變形物體），將策略可感知的接觸觀測與完整的物理 Ground Truth 進行配對，補足了觸覺回饋與柔性物體操作領域長期缺乏高品質接觸資料的痛點。

### ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning
* **作者**：Jayjun Lee, Jessica Yin, Asif Rana, Nicholas Blauch, Sam Mady
* **連結**：https://arxiv.org/abs/2608.19182
* **來源**：arXiv (cs.RO, cs.AI)
* **重點與關聯**：在高自由度（High-DoF）多指機器人上學習長序列靈巧操作極具挑戰。ADEPT 提出了一套大規模強化學習（RL）框架，先在通用的物體重姿態（reposing）任務上預訓練靈巧策略，再將其行為作為先驗進行下游任務後訓練。該方法直接基於原始視觸覺感知，展現了 Sim-to-Real 的可遷移性，有效解決了多指機器人從零探索困難與重複學習基礎技能的問題。
