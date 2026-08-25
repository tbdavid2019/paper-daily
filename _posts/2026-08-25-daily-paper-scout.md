---
layout: post
title: "每日論文雷達｜2026-08-25"
date: 2026-08-25 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

* **日期**：2026 年 8 月 25 日
* **主題**：具身智能（Embodied Intelligence）
* **收錄數量與資料統計**：本次檢索共爬取 711 篇文獻（去重後 638 篇，時間窗口內候選 550 篇，扣除已處理 77 篇後為 473 篇新候選論文）。來源涵蓋 arXiv cs.AI (250)、cs.CV (250)、cs.RO (103)、Hugging Face (100) 及關鍵字檢索 (8)。經篩選後本日收錄 10 篇代表性論文進行分析。

---

## Must-Read

本日無符合 Must-Read 門檻（評分 $\ge 80$）之論文。

---

## Highly Relevant

### [Act with Intent: Distilling Behavior Intent for Vision-Language-Action Models](https://arxiv.org/abs/2608.23478)
* **作者**：Sangoh Lee, Sangwoo Mo, Wook-Shin Han
* **來源**：arXiv (cs.RO, cs.AI, cs.CV, keyword)
* **重點與關聯**：傳統 Vision-Language-Action (VLA) 模型的動作解碼器多依賴行為複製（Behavior Cloning, BC）進行訓練，這類方法僅監督給定情境下展示的運動指令，卻未顯式表達該行為所服務的局部語意目標；現有的未來監督信號（如未來畫面、軌跡）亦多側重於特定物理實現而非共享語意目標。本研究提出「意圖蒸餾」（Intention Distillation, I...，詳細名稱文摘未完整提供），旨在捕捉即將執行之行為的共享語意目標，為 VLA 政策提供更具目標導向的動作監督。

---

## Interesting

### [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](https://arxiv.org/abs/2608.21740)
* **作者**：Haru Kondoh, Kei Ota, Asako Kanezaki, Yueh-Hua Wu
* **來源**：arXiv (cs.RO, keyword)
* **重點**：針對行為複製僅提供正向示範、缺乏「哪些動作與指令不符」之負向監督的問題，本文提出 CounterAlign。該方法指出 VLA 的離線強化學習無需依賴人工策劃的非專家軌跡，可直接透過成功的專家示範建構反事實監督信號。

### [Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23224)
* **作者**：Zhiruo Zhou, Zelin Li, Xiwen Chen, Jiazhuo Li, Chenwei Wang
* **來源**：arXiv (cs.RO, cs.AI, cs.CV)
* **重點**：研究發現在凍結的 VLA 策略中直接附加檢索文本會導致「提示形式崩潰」（prompt-form collapse），在 500 個狀態測試中使平均成功率從 92.47% 驟降至 3.00%。為此提出 TOWN-VLA，透過提示權限介面隔離文本干預，僅在必要時進行慢路徑介入。

### [Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23138)
* **作者**：Xiwen Chen, Zelin Li, Zhiruo Zhou, Huiming Chen, Chenwei Wang
* **來源**：arXiv (cs.RO, cs.AI, cs.CV)
* **重點**：針對 VLA 將空間座標序列化為文字或隱式 token 所造成的介面脆弱問題，基於 Embodied-R1 提出 Pointing-VLA。模型利用幾何專用輸出頭預測正規化點、物件功能定位（OFG）熱圖與視覺軌跡，並在 Bridge/WidowX 與實體取放任務中驗證了明確的執行合約設計。

### [UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models](https://arxiv.org/abs/2608.22869)
* **作者**：Lars Osterberg, Maggie Wang, Mac Schwager
* **來源**：arXiv (cs.RO, cs.CV, keyword)
* **重點**：傳統 VLA 在處理非馬可夫（non-Markovian）任務時，常因外掛獨立 VLM 管理長期記憶而導致記憶瓶頸與訓練流程分裂。UniMem 提出統一架構，整合多模態記憶與控制機制，改善多歷史幀輸入可能引發的效能衰退問題。

### [Robust Bimanual Vision-Language-Action Models via Embarrassingly Simple Modality Masking](https://arxiv.org/abs/2608.22419)
* **作者**：Dongzhou Cheng, Ziang Li, Yixiao Zhou, Haojuan Li, Jinghao Zhang
* **來源**：arXiv (cs.RO, cs.CV, keyword)
* **重點**：針對基於 Query 的雙臂 VLA 在多視角與語言融合時因注意力分散而出現動作不連續與執行失敗的問題，提出僅需在訓練階段實施的模態遮罩機制（M3），在不更改模型架構與大規模預訓練的前提下提升雙臂操作的魯棒性。

### [Inferring Action from Future Latent State for Robotic Manipulation](https://arxiv.org/abs/2608.22067)
* **作者**：Fenghao Lei, Zhixiong Huang, Long Yang, Jiabao Chen, Jie Cheng
* **來源**：arXiv (cs.RO, cs.AI, cs.CV)
* **重點**：質疑世界動作模型（WAMs）逐幀生成稠密未來影片的必要性，指出視覺過渡幀消耗過多計算與模型容量。該研究主張世界模型應專注於預測動作執行後的未來潛在狀態（latent state），並從中直接推斷機器人控制動作。

### [Triplet2Track: A Hierarchical System with Object-Centric Representations for Reliable Long-Horizon Manipulation](https://arxiv.org/abs/2608.22800)
* **作者**：Jianxiang Liu, Gaojing Zhang, Chuan Wen, Qipeng Liu, Yuxuan Zhao
* **來源**：arXiv (cs.RO, cs.AI)
* **重點**：針對端到端 VLA 資料黑箱與分層規劃缺乏在線反饋的缺陷，提出閉環長程模仿學習

---

## Idea Sparks

資料未提供
