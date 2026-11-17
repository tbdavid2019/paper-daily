---
layout: post
title: "每日論文雷達｜2026-11-17"
date: 2026-11-17 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-11-17
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次掃描共爬取 1326 篇論文，經過去重與篩選後取得 60 篇候選文獻，其中評估接受 144 篇，本篇報告精選出最具代表性與突破性的研究進行深度解析。

---

## Must-Read

### ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters
- **作者**：Ruixi Yu, Dairu Liu, Xuchuan Chen, Zekun Qi, Zekai Li
- **來源**：[Hugging Face / arXiv](https://arxiv.org/abs/2611.21607)
- **突破點與啟發**：
  前沿視覺語言模型（VLM）在各領域展現強大能力，但大多數視覺語言動作（VLA）政策仍受限於小規模骨幹。本研究打破此現狀，推出了 **ScaleVLA**，將高達 552B 參數的 DeepSeek-V4.1-Flash 骨幹網路與可訓練的動作擴散變壓器（Action DiT）相連接。這項研究系統性地比較了從 2B 到 552B 規模的 VLM 在機器人控制上的表現，證實了超大規模預訓練所帶來的廣泛知識能顯著增強物理動作的泛化能力，為具身基礎模型（Robot Foundation Models）的規模化（Scaling Law）奠定了重要里程碑。

### EgoSwarm: Learning Decentralized Robot Swarm Intelligence from Human Swarm Demonstrations
- **作者**：Ziqiang Liu, Xitong Chen, Min Li, Yiqun Li, Zhuoping Yin
- **來源**：[arXiv](https://arxiv.org/abs/2611.20100)
- **突破點與啟發**：
  從單一具身智慧邁向群體（Swarm）協同是實現通用具身智慧的關鍵步驟，然而多機器人示範資料的收集成本極高。**EgoSwarm** 提出了一種創新解法：利用人類群體的第一人稱視角（Egocentric）示範來學習分散式機器人群體智慧。該方法透過建模代理之間的動作依賴性，有效解決了複雜任務中多機分工、交接與協同操作的監督難題，為可擴展的群體操作策略提供了可行的路徑。

### MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams
- **作者**：Yimin Han, Jiahui Zhang, Wanyue Li, Zeren Luo, Yeke Chen
- **來源**：[arXiv](https://arxiv.org/abs/2611.19998)
- **突破點與啟發**：
  即時人形機器人全身模仿（Whole-Body Imitation）過去往往高度依賴穿戴式追蹤裝置。**MoViC** 框架實現了僅透過單眼 RGB 影片串流即時驅動人形機器人。該系統巧妙結合了單眼人類動作重建、機器人重定向（Retargeting）以及基於變壓器的行為基礎模型，並引入緊湊的頻域動作表示法，在不顯式堆疊未來訊號的情況下提供豐富的時序上下文，大幅降低了人形機器人的部署門檻。

### TaF-Foundation: Wrench-Grounded Cross-Sensor Tactile Representations
- **作者**：Jiaming Jiang, Yuzhe Huang, Baokun Yang, Hao Liang, Li Gao
- **來源**：[arXiv](https://arxiv.org/abs/2611.20718)
- **突破點與啟發**：
  觸覺感測對於接觸豐富的操作（Contact-rich Manipulation）至關重要，但異質的感測機制與資料格式嚴重阻礙了跨硬體轉移。**TaF-Foundation** 回歸牛頓力學的物理本質，將觸覺表徵直接對齊於六維力/力矩（Wrench），在不同感測器之間建立了共同的物理參考基準。透過將各類感測器的觸覺觀測與力矩量測相配對，該方法在無需直接觸覺對觸覺配對的情況下實現了大規模的跨感測器監督學習，對多模態觸覺感知帶來重大突破。

---

## Highly Relevant

1. **Towards Probabilistically Safe Reinforcement Learning: Theory and Deployment on Humanoid and Aerial Robots**
   - **作者**：Pol Mestres, Varun Gabbita, Jason H. K. Siu, Sergio A. Esteban, Hampus Serneke
   - **來源**：[arXiv](https://arxiv.org/abs/2611.19616)
   - **亮點**：擴展強固安全梯度流方法，將其與 PPO 等最新演算法結合，成功在人形與飛行機器人上實現具備機率安全保證的強化學習。

2. **Ego2Sim2Humanoid: Agentic Real-to-Sim for Learning Loco-Manipulation VLAs without Robot Demonstrations**
   - **作者**：Chen Liu, Nikolaus Correll
   - **來源**：[arXiv](https://arxiv.org/abs/2611.19196)
   - **亮點**：透過代理式 Real-to-Sim 轉換，將人類第一人稱眼鏡錄像轉化為具身移動操作 VLA 的訓練資料，擺脫對機器人示範的依賴。

3. **DexFormer 2.0: Towards a Cross-Embodiment Foundation Policy for Dexterous Grasping**
   - **作者**：Lixin Xu, Ke Zhang, Xinyu Liu, Jie Tan, Senming Tan
   - **來源**：[arXiv](https://arxiv.org/abs/2611.20273)
   - **亮點**：提出單一強化學習政策，將各種不同關節佈局與動態特性的多種機械臂-手組合對齊至標準化介面，實現跨具身靈巧抓取。

4. **Cooperative Transport of Unknown Objects by Distributed Effort Regulation in Multi-agent Systems**
   - **作者**：Tamzidul Mina, Shyam S. Kannan, Wonse Jo, Shaocheng Luo, Galen B. King
   - **來源**：[arXiv](https://arxiv.org/abs/2611.19731)
   - **亮點**：針對形狀、質量分佈皆未知的物體，提出基於航向誤差的分散式施力調節協同搬運策略。

5. **ROSE: A Shared Cross-Embodiment Facial-Motion Latent Space for Humanoid Robot Expression**
   - **作者**：Yongji Fu, Man Cao, Yi Zhou, Fei Lin, Mark F. Hansen
   - **來源**：[arXiv](https://arxiv.org/abs/2611.20950)
   - **亮點**：建立跨具身的共享臉部動作潛在空間，繞過傳統的渲染與反演路徑，直接實現具備低延遲的人形機器人生動表情控制。

6. **ARMFUL: Learning Whole-Arm Grasp Configurations for Single-Arm Pickup of Large Objects**
   - **作者**：Xinyi Yu, Yunshuang Li, Daniel Seita, Gaurav S. Sukhatme
   - **來源**：[arXiv](https://arxiv.org/abs/2611.20692)
   - **亮點**：推出包含 170 萬個關節配置的大規模全身抓取資料集（WAG），解決單臂包裹與支撐大型重物的夾持難題。

7. **Recovery-Guided Model-Based Diffusion for Safety-Critical Legged Locomotion**
   - **作者**：Lei Zheng, Shivam Sood, Mithun Vanniasinghe, Guillaume Sartoretti, Armin Lederer
   - **來源**：[arXiv](https://arxiv.org/abs/2611.19775)
   - **亮點**：結合學習型終端恢復評論家與短視界軌跡最佳化，實現安全關鍵的高速四足機器人 locomotion。

8. **Self-Calibrating Vision-Agent-Action: Deploying Pick-and-Place to New Robot Cells without Demonstrations or Fine-Tuning**
   - **作者**：Jae Hun Hwang, Yechan Seo, Hong-In Won
   - **來源**：[arXiv](https://arxiv.org/abs/2611.19251)
   - **亮點**：利用預訓練 VLM 與自身動作自主校準相機幾何與指令圖譜，達成無須微調的跨單元抓取部署。

9. **DAPPT: Domain-Aware Policies from Procedural Trajectories for Sim-to-Real Dexterous Tool Use**
   - **作者**：Beining Han, Jia Deng
   - **來源**：[arXiv](https://arxiv.org/abs/2611.20202)
   - **亮點**：透過追蹤由領域參數化之程序性軌跡，繞過複雜非剛體模擬，實現沙土與黏土等靈巧工具操作的 Sim-to-Real。

10. **TMA: Sim-to-Real Forceful Humanoid Manipulation via Tactile-Driven Motor Adaptation**
     - **作者**：Yiting Chen, Kelin Yu, Sarthak Kaingade, Bryan Trinh, Kaiyu Hang
     - **來源**：[arXiv](https://arxiv.org/abs/2611.18976)
     - **亮點**：結合觸覺驅動馬達適應（TMA），解決人形機器人在開圓形門把等力道導向、高摩擦力需求任務中的零樣本模擬真實轉移。

---

## Interesting

1. **PSK: A Matrix-Free Single-Loop Method for K-Level Physics-Based Control**
   - **作者**：Zherong Pan
   - **來源**：[arXiv](https://arxiv.org/abs/2611.19660)
   - **亮點**：將 $K$ 級物理控制最佳化重構為單一極小極大問題，利用無矩陣（Matrix-free）單迴圈方法避開沉重的 KKT 線性求解，提供另一種物理控制微分的創新視角。

2. **Vision-Language Grounded Semantic Navigation for Autonomous Mobile Robots**
   - **作者**：Ravindran Vasoor Saravanan, Chittin Varunav Ravi, Madhumita Singh, Thirulok Sundar Mohan Rasu
   - **來源**：[arXiv](https://arxiv.org/abs/2611.20558)
   - **亮點**：整合 ROS2、Grounding DINO 與 3D 深度定位，展示了將開語彙視覺感知與古典機器人導航管線結合的完整工程系統實作。

3. **Cooperative Mobile Manipulation using Learned Dynamical Systems**
   - **作者**：Saray Bakker, Wendelin Böhmer, Javier Alonso-Mora
   - **來源**：[arXiv](https://arxiv.org/abs/2611.21198)
   - **亮點**：提出 CALDS 框架，透過合作政策選擇與時間適應，將單一代理學習到的動態系統（DS）成功遷移至協同移動操作。

4. **Physics-Informed Causal Reasoning for Nonstationary Robot Dynamics**
   - **作者**：Jungjin Lee, Se Jin Kim, Sung Kwon On, Insoon Yang
   - **來源**：[arXiv](https://arxiv.org/abs/2611.19251)
   - **亮點**：結合物理資訊神經網路與因果推理，探討在非平穩動態環境中如何透過少量互動快速適應隱藏物理條件的變化。

---

## Idea Sparks

1. **超大規模基礎模型與輕量化動作解碼器的協同擴展**
   - **觀察**：從 `ScaleVLA` 的 552B 參數模型可以看出，利用頂級 VLM 作為骨幹能為具身智慧帶來極其強大的世界知識。然而，如何將巨型模型與機器人即時控制所需的低延遲（Low-latency）動作分發器（如 DiT 或擴散模型）進行更高效的邊緣部署與模型壓縮，將是未來實體落地的一大關鍵。
   - **後續問題**：當 VLA 骨幹規模擴展至 500B 以上時，知識蒸餾（Knowledge Distillation）或量化技術是否會導致空間推理與長程規劃能力的災難性遺忘？

2. **第一人稱人類示範（Egocentric Human Data）的跨具身對齊**
   - **觀察**：本期多篇論文（如 `EgoSwarm`、`Ego2Sim2Humanoid`）皆強調利用人類第一人稱視角或群體示範來繞過昂貴且繁瑣的機器人遙操作（Teleoperation）。這顯示出「人類資料泛化（Human Data Scaling）」正在成為克服機器人資料匱乏的核心解方。
   - **後續問題**：在處理具有高度形態差異（如人類五指與多指機器人靈巧手、不同手臂長度）的動作重定向時，如何從理論上保證動態接觸力（Contact Dynamics）的一致性而非僅僅是視覺軌跡的相似？

3. **觸覺與力學基礎表徵的標準化**
   - **觀察**：`TaF-Foundation` 將異質觸覺感測器統一對齊至六維力（Wrench），呼應了先前視覺領域走向通用表徵的歷程。這意味著觸覺感測正逐漸擺脫特定硬體綁定，走向跨感測器的通用預訓練時代。
   - **後續問題**：基於力矩/六維力的統一觸覺表徵，是否能夠與現有的視覺-語言-動作模型（VLA）進行深度早期融合（Early Fusion），進而完全解鎖盲操與高精度接觸任務？
