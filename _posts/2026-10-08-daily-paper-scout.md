---
layout: post
title: "每日論文雷達｜2026-10-08"
date: 2026-10-08 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-08
- **主題**：具身智慧 (Embodied AI)
- **收錄數量與資料統計**：本次檢索原始爬取共 871 篇論文（涵蓋 Hugging Face、arXiv cs.RO、cs.AI、cs.CV 與關鍵字），經過去重與視窗篩選後，獲得 342 篇新候選論文。經模型評估與篩選，本次精選出 30 篇具代表性研究，涵蓋人形機器人全身控制、機器人操作、多模態感知與視覺語言動作（VLA）模型等核心領域。

## Must-Read

目前資料未提供評分達到 80 分以上的 Must-Read 門檻論文，所有精選論文皆落在高度相關（Highly Relevant）區間。

## Highly Relevant

1. **Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data**
   - **作者**：Songbo Hu, Qiayuan Liao, Yufeng Chi, Kevin Zakka, Yakun Sophia Shao
   - **來源**：[arXiv:2610.09117](https://arxiv.org/abs/2610.09117)
   - **摘要證據**：針對人形機器人難以從具體 RGB 與本體感覺規劃接觸豐富的全體操作，本研究提出 Workhorse，從無機器人的真實人類示範中學習。透過視覺規劃器預測五連桿目標（軀幹、雙手腕、雙腳），並以強化學習全體追蹤器在機器人上執行，兩者分開訓練且無需重新標定。實機部署於 Unitree G1 上成功執行箱子分類。

2. **Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs**
   - **作者**：Namai Chandra, Jaison Jose, Kavi Arya, Shivaram Kalyanakrishnan
   - **來源**：[arXiv:2610.09828](https://arxiv.org/abs/2610.09828)
   - **摘要證據**：探討緊湊型移動機器人在嚴格負載與成本限制下恢復場景幾何的方法。該研究設計了採用摺紙啟發車輪的移動機器人，利用車輪動態改變感測幾何與底盤俯仰角，藉此帶動 2D LiDAR 掃描中繼高程，並結合 IMU 姿態資訊，將 LiDAR 投影至 RTAB-Map 的 RGB-D 深度串流中。

3. **Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control**
   - **作者**：Joohwan Seo, Xiaofeng Guo, Jinkun Cao, Roberto Horowitz, Rocky Duan
   - **來源**：[arXiv:2610.09479](https://arxiv.org/abs/2610.09479)
   - **摘要證據**：為解決人形機器人在全體運動中因浮動基座震盪、重力與動態耦合導致末端執行器追蹤困難的問題，提出 ResGAC 全身控制器。該方法結合幾何導納控制（GAC）提供結構化 $\text{SE}$ 任務空間回授，並利用殘餘強化學習（Residual RL）補償未建模動態，協調共用關節位置動作空間中的平衡與移動。

4. **Contact-Aware Imitation Learning Through Contact Factorization**
   - **作者**：Jiho Hong, Daeun Song, Sanghyun Kim, Mingyo Seo
   - **來源**：[arXiv:2610.09533](https://arxiv.org/abs/2610.09533)
   - **摘要證據**：指出接觸豐富的操作任務中，互動力量易隨表面幾何、方向與摩擦力微幅變化，使得直接基於原始力量測量的策略難以遷移。研究引入 FACE（Contact-Factorized Imitation Learning Framework），將預期任務行為與環境相依的接觸因素分離，以改善模仿學習的泛化能力。

5. **Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment**
   - **作者**：Xiao Zhang, Yuxin Chen, Zhixuan Liang, Guojian Zhan, Chenran Li
   - **來源**：[arXiv:2610.09369](https://arxiv.org/abs/2610.09369)
   - **摘要證據**：分析擴散策略（Diffusion Policies）在機器人規劃中常退化為單一模態（即使資料集模態平衡且對稱）的現象，發現獨立動作-雜訊配對會增加擴散路徑間的混合與交叉，進而壓抑模態特異性行為。該文針對此現象提出不相容擴散策略以保留多模態動作。

6. **RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies**
   - **作者**：Mimo Shirasaka, Takehiko Ohkawa, Takuya Okubo, Nicola Scianca, Tatsuya Matsushima
   - **來源**：[arXiv:2610.09696](https://arxiv.org/abs/2610.09696)
   - **摘要證據**：探討將人類示範資料應用於視覺語言動作（VLA）政策時，人類時間步調無法直接套用於機器人的問題（人類柔韌手部能耐受快速接觸，但機器人可能因過衝而失控；反之機器人在自由空間可移動更快）。研究提出 RoboPace，協調執行速度與接觸安全性。

7. **Point It, Strike It: Direction-Conditioned Dynamic Manipulation of Deformable Linear Objects**
   - **作者**：Yi Yang, Xiang Fei, Lehong Wang, Zilin Dai, Ruogu Li
   - **來源**：[arXiv:2610.09573](https://arxiv.org/abs/2610.09573)
   - **摘要證據**：探討具備方向條件的可變形線性物件（如繩索）動態操作。任務不僅要求繩尖到達特定 3D 位置，更指定其到達方向。針對繩索動態難以建模且缺乏示範的挑戰，延伸現有方法以處理跨工作空間與不同繩索的單揮擊繩索打擊任務。

8. **RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning**
   - **作者**：Seungjun Moon, Subin Jeon, Sangwoo Kim, Hanbyul Joo, Jinwoo Shin
   - **來源**：[arXiv:2610.09455](https://arxiv.org/abs/2610.09455)
   - **摘要證據**：指出現有從人類影片中學習機器人政策的手部追蹤器多半從裁切畫面迴歸姿態，缺乏手部運動與物件互動先驗，導致估計不準確且缺乏實體物理線索。研究提出 RLHND，利用影片基礎模型從單眼自我視角中同時估計手部姿態與逼真的觸覺資訊。

9. **Targeted Modality Dropout for Real-Robot Manipulation Robust to Intermittent Vision Loss**
   - **作者**：Genki Shikada, Kazuki Osamura, Masaru Ide, Tetsuya Ogata, Kanata Suzuki
   - **來源**：[arXiv:2610.09566](https://arxiv.org/abs/2610.09566)
   - **摘要證據**：針對多模態模仿學習政策在訓練時容易過度依賴視覺等單一優勢模態，導致推理時視覺遺失會癱瘓執行的問題，提出標的模態丟棄（Targeted Modality Dropout, TMD）法。透過注意力機制評估各模態依賴性，並選擇性丟棄最具支配力的模態，結合熵正規化在雙臂機器人上驗證可提升視覺遺失時的成功率。

10. **YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding**
   - **作者**：Masatoshi Tateno, Takehiko Ohkawa, Yueh-HuaWu, Hanlong Li, Tatsuya Matsushima
   - **來源**：[arXiv:2610.09718](https://arxiv.org/abs/2610.09718)
   - **摘要證據**：為解決視覺語言動作（VLA）模型需要精細指令與物理互動對齊，但現有機器人示範僅提供粗略任務描述、忽略接觸細節（如使用哪個夾爪、接觸哪個物件、如何抓取與移動）的問題，提出 YUBI-STAG 框架進行時空標註與基礎化，為示範數據豐富化互動語意。

## Interesting

- **Origami-Inspired Mechanisms for Sensor Geometry Adaptation**: `2610.09828` 透過摺紙結構動態調整車輪幾何來驅動 LiDAR 掃描視角，展現了機械結構與感測器佈局共同設計的簡潔巧思，適合受限於成本與負載的行動載具參考。
- **Immiscible Diffusion Policy**: `2610.09369` 指出擴散政策在無意間退化為單一模態的數學路徑交叉問題，對依賴 Diffusion 進行多模態動作生成的模型設計提供了底層防範思路。

## Idea Sparks

1. **從人類示範到機器人執行的動態與時間適應（Temporal and Dynamic Retiming）**
   - *跨論文觀察*：`2610.09117`（Workhorse）透過視覺規劃器與強化學習追蹤器分開訓練來處理人形機器人全體操作，而 `2610.09696`（RoboPace）則探討動作區塊政策中的接觸感知時間最佳化重排。兩者皆指向人類示範資料在物理限制、時間步調與接觸動態上的不匹配問題。
   - *具體後續問題*：能否將接觸感知的時間重排（RoboPace）與無機器人的人類示範追蹤策略（Workhorse）結合，設計出一個在訓練階段即自動最佳化速度與接觸安全性的端到端學習框架？

2. **多模態對齊與感測器退化防禦（Multimodal Robustness and Grounding）**
   - *跨論文觀察*：`2610.09566`（TMD）關注政策在視覺遺失時對單一模態過度依賴的防禦，而 `2610.09718`（YUBI-STAG）與 `2610.09455`（RLHND）則專注於從人類影片中提取並對齊更豐富的物理與接觸語意。
   - *具體後續問題*：在結合影片基礎模型與觸覺/語意基礎化（YUBI-STAG/RLHND）時，引入模態主動丟棄訓練（TMD）是否能有效防止模型過度依賴視覺，進而提升具身代理在真實世界感測器部分失效時的強韌度？
