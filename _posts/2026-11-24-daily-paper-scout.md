---
layout: post
title: "每日論文雷達｜2026-11-24"
date: 2026-11-24 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-11-24
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 125 篇論文，經過去重與候選篩選後，評估並收錄了 35 篇高品質研究。
- **資料統計**：涵蓋 Hugging Face 與 arXiv 關鍵字檢索（包含視覺語言動作模型 VLA、機器人本體控制、模擬與 Sim-to-Real 轉移等重要領域）。今日的研究重點主要聚焦於強化 VLA 模型的長期記憶、3D 空間關係推理、資源感知運算排程以及具身代理基準測試。

---

## Must-Read

1. **[WorldLeague: Benchmarking Physical Agency](https://arxiv.org/abs/2611.30989)**
   - **作者**：Xinyang Zhou, Qi Li, Xinchao Wang
   - **技術突破點**：本篇論文針對當前 AI 系統在實體環境中的操作與自主性缺乏統一評估標準的問題，推出了 WorldLeague 基準測試。透過 60 個模擬機器人任務，涵蓋探索、場景重組等不同組合的感知、記憶、規劃與動作，能精準衡量機器人從軌跡中實現實體目標的進展。
   - **研究啟發**：為具身代理（Embodied Agents）提供了跨任務、多面向的嚴格物理代理評估框架，有助於未來客觀比較不同基礎模型的物理規劃與互動能力。

2. **[ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation](https://arxiv.org/abs/2611.3053)**
   - **作者**：Yicheng Xu, Wencan Jiang, Zihao Zhu, Keru Zhou, Chang Zhou
   - **技術突破點**：針對長歷程（Long-horizon）具身任務中，粗略進度回饋無法有效指導搜尋且容易過擬合的問題，提出了 ReWeave 框架。該框架能在不更新策略權重的情況下，從互動中聯合優化具身代理連接器（harness）與突發性物理任務拓樸。
   - **研究啟發**：展示了無需透過繁重梯度更新即可實現跨任務元蒸餾與適應的新途徑，對於提升長歷程任務的泛化性具備高度參考價值。

3. **[Resource-Aware VLA-MPC Co-Location for Efficient Embodied AI](https://arxiv.org/abs/2611.30177)**
   - **作者**：Zeyu Guo, Hao Lou, Yuhui Hao, Han Zhao, Zihan Liu
   - **技術突破點**：為解決視覺語言動作（VLA）模型推論與高頻模型預測控制（MPC）在行動 GPU 上序列化執行導致的控制死線錯過（deadline misses）問題，提出了 Dubot 框架。透過空間分割、區塊級共置與區塊內融合三種共置機制，在單一行動 GPU 上自動排程這兩項繁重工作負載。
   - **研究啟發**：突破了邊緣運算硬體上的即時控制瓶頸，對推動 VLA 模型在真實機器人硬體上的高頻閉環部署具有決定性工程價值。

4. **[Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.2897)**
   - **作者**：Yue Huang, Tianshan Zhang, Zeyu Zhang, Jayeon Kang, Akide Liu
   - **技術突破點**：結合了區域注意力機制、可恢復循環狀態與持久內容記憶（PCM），提出了基於 Mamba 的根體擴散架構，有效解決了傳統自迴歸擴散方法在長歷程人形控制中受限於注意力快取與重複去雜訊推論開銷過大的問題。
   - **研究啟發**：為人形機器人與互動式動畫提供了兼顧即時反應與長期歷史記憶的高效運動生成方案。

---

## Highly Relevant

1. **[RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See](https://arxiv.org/abs/2611.30209)**
   - **作者**：Yunbei Zhang, Zijian Jin, Shuaicheng Niu, Baian Chen, Weirui Ye
   - **重點摘要**：提出在測試時調適凍結機器人策略的方法，以應對相機畫面無法捕捉到的隱含物理特性（如重量差異、關節減弱或控制器延遲）。 [https://arxiv.org/abs/2611.30209](https://arxiv.org/abs/2611.30209)

2. **[RUIBench: What Makes a Good Robot-Use Interface?](https://arxiv.org/abs/2611.31115)**
   - **作者**：Yanzhe Chen, Zhijun Cao, Zechen Bai, Wenzheng Zeng, Kevin Yuchen Ma
   - **重點摘要**：介紹 RUIBench 與 RUIKit，系統性研究機器人使用介面（RUI）在將基礎模型智慧轉化為可靠機器人執行時的影響。 [https://arxiv.org/abs/2611.31115](https://arxiv.org/abs/2611.31115)

3. **[SWEEP-Bench: Do Embodied Policies Act on the Speed They See?](https://arxiv.org/abs/2611.30637)**
   - **作者**：Hiroaki Honda, Koya Sakamoto, Shu Morikuni, Yusuke Iwasawa, Taiki Miyanishi
   - **重點摘要**：推出包含 80 個輸送帶操作任務的模擬基準測試，用以評估具身策略在各種動態速度下的反應與適應能力。 [https://arxiv.org/abs/2611.30637](https://arxiv.org/abs/2611.30637)

4. **[JEPA-Tuner: From Predictive Fine-Tuning to Asynchronous Execution of Vision-Language-Action Models](https://arxiv.org/abs/2611.29096)**
   - **作者**：Jingxiang Qu, Tian Xie, Youngjin Hong, Changhyun Choi, Yang Katie Zhao
   - **重點摘要**：提出預測微調框架，透過動作條件的時間依賴性正規化 VLA 的原生策略導引，改善非同步執行效率。 [https://arxiv.org/abs/2611.29096](https://arxiv.org/abs/2611.29096)

5. **[NAT: Scaling Causal Neural Action Tokenizers Across Embodiments](https://arxiv.org/abs/2611.28873)**
   - **作者**：Ahad Jawaid, Alexander Swerdlow, Yu Xiang
   - **重點摘要**：研發因果神經動作 tokenizer（NAT），在涵蓋多種本體與資料來源的 49k 小時真實及模擬動作資料上進行規模化訓練。 [https://arxiv.org/abs/2611.28873](https://arxiv.org/abs/2611.28873)

6. **[A2I-VLA: A Two-Stage Vision-Language-Action model with Semantic-Physical Alignment and Integration](https://arxiv.org/abs/2611.29279)**
   - **作者**：Kun Dai, Tianqi Wang, Haibo Lei, Chaoyang Li, Kai Zhang
   - **重點摘要**：針對觸覺與力回饋，提出兩階段 VLA 框架以克服視覺語意與物理測量之間的代表性鴻溝。 [https://arxiv.org/abs/2611.29279](https://arxiv.org/abs/2611.29279)

7. **[Toward Adversarially Robust World Models](https://arxiv.org/abs/2611.28345)**
   - **作者**：Ethan Rathbun, Jonathan Nöther, Christopher Amato, Alina Oprea, Goran Radanović
   - **重點摘要**：探討潛在動態世界模型在具身智慧系統中的安全與對抗強固性，建立統一的防禦與評估視角。 [https://arxiv.org/abs/2611.28345](https://arxiv.org/abs/2611.28345)

8. **[GeoMerge-OPD: Balanced Skill Integration in Vision-Language-Action Models](https://arxiv.org/abs/2611.30632)**
   - **作者**：Le Yang, Haoyang Lyu, Honglei Jin, Wenshuo Chen, Jiawei Liang
   - **重點摘要**：解決 VLA 模型在整合多種異質技能（如全身操作與移動需求）時容易導致個別技能退化的平衡問題。 [https://arxiv.org/abs/2611.30632](https://arxiv.org/abs/2611.30632)

9. **[DexDuet: Learning Contact-Preserving Bimanual Dexterity from Human Demonstrations](https://arxiv.org/abs/2611.30495)**
   - **作者**：Haoran Zhang, Haokai Ding, Han Zhou, Zuxing Lu, Heng Zhang
   - **重點摘要**：利用互動獎勵機制從單一人類示範中學習保持接觸點的雙手靈巧操作。 [https://arxiv.org/abs/2611.30495](https://arxiv.org/abs/2611.30495)

10. **[RMR-VLA: Recurrent Memory Reasoning for Vision-Language-Action Models](https://arxiv.org/abs/2611.30145)**
    - **作者**：Yiheng Du, Jingqi Tian, Xu Jiang, Jiexuan Zhang, Shuyu Wang
    - **重點摘要**：引入循環記憶推理（RMR），使 VLA 模型能在無外部模型輔助下處理長期、依賴歷史視覺線索的任務。 [https://arxiv.org/abs/2611.30145](https://arxiv.org/abs/2611.30145)

---

## Interesting

1. **[WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models](https://arxiv.org/abs/2611.31126)**
   - **作者**：Zien Wang, Yuhao Pan, Yunfeng Fan, Nan Cheng, Xin Xia
   - **亮點**：透過任務條件式稀疏圖神經網路，明確對齊物件、夾爪與環境之間的相對 3D 關聯，改善 VLA 對 3D 空間關係演變的理解。 [https://arxiv.org/abs/2611.31126](https://arxiv.org/abs/2611.31126)

2. **[Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://arxiv.org/abs/2611.31201)**
   - **作者**：Xiao-Ming Wu, Kang Liao, Yuexiao Ma, Taolin Zhang, Mingqian Zhou
   - **亮點**：系統性探討將前沿多模態模型直接作為閉環機器人策略（Frontier-model-as-policy）時的提示詞、規劃、執行與工具使用四個組件。 [https://arxiv.org/abs/2611.31201](https://arxiv.org/abs/2611.31201)

3. **[Defending Vision-Language-Action Models against Transferable Attacks via Visual-Proprioceptive Consistency](https://arxiv.org/abs/2611.28346)**
   - **作者**：Jiahao Wang, Ming F. Li, Han Xu
   - **亮點**：觀察到跨任務對抗攻擊常透過破壞 VLA 對機器自身的感知來發揮作用，因此提出基於本體感受一致性的防禦框架。 [https://arxiv.org/abs/2611.28346](https://arxiv.org/abs/2611.28346)

4. **[HIVE-Bench: Evaluating Patch-Level Visual Representations for Egocentric Robot Manipulation](https://arxiv.org/abs/2611.30813)**
   - **作者**：Qiwei Liang, Zhengtu Liang, Minghao Lai, Yikeng Chen, Yiming Wang
   - **亮點**：強調在第一人稱視角雙手操作中，保留密集的圖像 patch 標記（Patch tokens）遠比將其池化為單一向量來得重要。 [https://arxiv.org/abs/2611.30813](https://arxiv.org/abs/2611.30813)

---

## Idea Sparks

1. **跨模態記憶與空間關係的顯式表徵融合**
   - **觀察**：近期如 *RMR-VLA* 與 *WeaveVLA* 的研究紛紛指出，僅依賴 VLA 模型隱含的注意力機制難以應對長歷程或動態 3D 關係的變化。研究人員開始在模型內部引入顯式的循環記憶推理與圖神經網路，將 3D 空間拓樸結構明確化。
   - **具體後續問題**：我們是否能設計一個統一的圖記憶體架構，既能儲存短期的動態物理狀態（如遮擋物下的物件位置），又能同時維護長期的任務子目標？

2. **資源感知與高效邊緣運算排程對即時具身控制的必要性**
   - **觀察**：隨著 VLA 模型的參數規模擴大，模型推論與高頻控制器（如 MPC）在邊緣硬體上的運算衝突日益顯著（例如 *Dubot* 探討的共置與排程問題）。過去偏向純演算法設計的研究正逐漸轉向軟硬體共設計（Co-design）。
   - **具體後續問題**：當 VLA 模型推論延遲受到硬體頻寬與運算限制時，如何動態調整模型輸出頻率與控制器頻率之間的控制權交接，才能在不犧牲安全性的前提下達到最優的任務執行效率？

3. **從單一示範到多重物理特性的動態適應**
   - **觀察**：如 *RoboAda* 和 *SWEEP-Bench* 等工作顯示，現今策略往往忽略了相機看不見的物理量（如摩擦力、重量、速度變化）。這促使學界從「純視覺模仿學習」轉向「具備物理感知與測試時調適（Test-time Adaptation）」的新範式。
   - **具體後續問題**：如何利用機器人自身在互動過程中產生的微小力回饋誤差，快速在測試階段即時校準隱含的物理參數（如摩擦係數與負載），而不需要重新微調整個大型 VLA 策略？
