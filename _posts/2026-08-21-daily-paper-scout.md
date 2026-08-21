---
layout: post
title: "每日論文雷達｜2026-08-21"
date: 2026-08-21 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-08-21
- **追蹤主題**：具身智能（Embodied Intelligence）
- **文獻統計**：
  - 總檢索篇數：770 篇（經去重後為 664 篇；時間窗口候選篇數為 627 篇，排除已處理篇數後，新增候選為 212 篇）
  - 關鍵字命中與入選：26 篇（本日精選呈現 10 篇代表性文獻）
  - 各來源分佈：Hugging Face (100)、arXiv cs.RO (159)、arXiv cs.AI (250)、arXiv cs.CV (250)、arXiv 關鍵字檢索 (11)

---

## Must-Read

> *本日無達到 Must-Read 門檻（評分 ≥ 80）之文獻。*

---

## Highly Relevant

### [OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation](https://arxiv.org/abs/2608.19589)
- **作者**：Jiaqi Wang, Zhou Fang, Qiongfeng Shi, Yi Zhou
- **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`, `arxiv_keyword`
- **論文重點與關聯**：
  - **摘要證據**：預訓練視覺-語言-動作（VLA）模型在循序適應不同技能時，容易擾動既有表徵與速度映射，產生災難性遺忘（catastrophic forgetting）。既有基於架構隔離的方法會增加推論開銷，而正交子空間約束方法則常對整個模型施加單一統一約束。本研究分析了 VLA 內部各組件的不同角色（其餘具體架構細節在摘要中未完全提供）。
  - **研究關聯**：對於專注於 VLA 模型持續學習與技能擴展的研究者而言，該方法探討如何在不顯著增加推論負擔的情況下，透過子空間適應減少新舊技能間的干擾。

---

## Interesting

### [SafeBranch: Branch-Pair Safety Alignment for Embodied Agents](https://arxiv.org/abs/2608.19729)
- **作者**：Hyunse Lee, Jiwoo Jeong, Haneul Lee, Kyochul Jang, Youngjae Yu
- **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`, `arxiv_cs.CV`
- **重點概述**：基於 VLM 的具身代理在執行指令時常違反安全約束。論文指出安全與任務成功是不同目標，且安全事件僅出現在軌跡中的少數關鍵步驟；標準的模仿或任意安全/不安全軌跡對比難以提供精確的因果信號。為此，作者提出 Branch-Pair 安全對齊方法（具體實作數據資料未提供）。

### [DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](https://arxiv.org/abs/2608.20114)
- **作者**：Siyuan Ma, Boshi Zhang, Yutian Zhang, Qinglian Wu, Jiaqi Zhai
- **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
- **重點概述**：針對足式移動操作（Legged Mobile Manipulation），既有世界-動作模型多針對固定基座設計，未明確區分相機自我運動（ego-motion）與基座、手臂動作。DECOWAM 凍結 FastWAM 主幹並訓練殘差適配器（residual adapters），透過條件介面顯式解耦基座與手臂潛在動作。

### [What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613)
- **作者**：Xizhou Bu, Qingda Hu, Lei Zhou, Lingfeng Zhang, Yingbo Tang
- **來源**：`arxiv_cs.RO`, `arxiv_cs.CV`
- **重點概述**：潛在動作模型（LAMs）能利用大規模無標註影片作為物理動作的替代表示，但現有研究的評估設定零散且不一致。本文針對機器人操作中的潛在動作學習展開實證研究，系統性探討決定下游操作表現的關鍵設計因素。

### [EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891)
- **作者**：Bhavya Sukhija, Oliver Groth, Mohit Shridhar, Tim Hertweck, Michael Bloesch
- **來源**：`huggingface`, `arxiv_cs.AI`
- **重點概述**：探討如何即時（on the fly）微調大型 VLA 策略以學習新任務。針對遙操作數據收集成本高且強化學習樣本效率低的問題，提出利用視覺語言模型（VLM）引導 VLA 策略探索的方法。

### [Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](https://arxiv.org/abs/2608.20087)
- **作者**：Tao Huang, Ruofei Liu, Xuchen Tang, Xinyin Zhang, Junli Ren
- **來源**：`arxiv_cs.RO`, `arxiv_cs.AI`
- **重點概述**：提出 AdaPT 框架，直接從網球轉播影片中學習發球與對打風格，採用階層式設計將風格化運動學規劃與執行追蹤解耦，以在人形機器人上兼顧動作風格與任務完成度。

### [Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms](https://arxiv.org/abs/2608.20111)
- **作者**：Yanchen Guan, Xingcheng Liu, Bin Rao, Chengyue Wang, Guofa Li
- **來源**：`arxiv_cs.RO`
- **重點概述**：回顧以規劃為導向的端到端自動駕駛系統演進，涵蓋行為克隆、特權蒸餾、BEV 向量化規劃、世界模型規劃器以及視覺-語言-動作（VLA）系統的架構轉變與評估機制。

### [Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control](https://arxiv.org/abs/2608.19443)
- **作者**：Chaoyi Pan, Zeji Yi, John Zhang, Zachary Manchester, Guannan Qu
- **來源**：`arxiv_cs.RO`
- **重點概述**：分析基於取樣的 MPC 在高維與開迴路不穩定動力學系統中取樣數隨時間視界指數增長的問題，提出透過優化回授策略實現

---

## Idea Sparks

資料未提供
