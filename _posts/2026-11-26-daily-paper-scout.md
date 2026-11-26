---
layout: post
title: "每日論文雷達｜2026-11-26"
date: 2026-11-26 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-11-26
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次資料庫共爬取 1,533 篇論文，去重後有 1,175 篇候選，經初篩與決策評估後，收錄 18 篇高品質且高度相關的研究成果。
- **資料統計分佈**：涵蓋 Hugging Face、`arxiv_cs.RO`、`arxiv_cs.AI`、`arxiv_cs.CV` 及 `arxiv_cs.LG` 等主要來源。今日研究重點明顯聚焦於跨本體 (Cross-Embodiment) 知識轉移、具身大語言與視覺語言動作模型 (VLA)、複雜地形下的機器人與人形機器人運動控制，以及長序列靈巧操作規劃。

## Must-Read

1. **CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with Large Language Models**
   - **作者**：Woojin Kim, Jemin Hwangbo
   - **來源/連結**：[arXiv:2611.33911](https://arxiv.org/abs/2611.33911)
   - **突破點與啟發**：針對單一四足機器人難以克服的複雜環境（例如需同伴背部攀爬的高台或需利用箱子填補的裂縫），傳統任務與動作規劃（TAMP）受限於預定義技能集。本篇提出由大型語言模型（LLM）驅動的雙模組框架，能夠自主「發明」未預先定義的動作，並透過程式碼導向的模組實現具體運動生成。這項研究展示了多機器人協同中，LLM 如何超越預設指令，直接參與動態環境中的策略創新。

2. **Riding the Wave: Sim-to-Real Humanoid Control on Elastic Terrain**
   - **作者**：Yinglei Zhu, Qin Li, Honghao Pan, Bozhao Wang, Binghui Xu
   - **來源/連結**：[arXiv:2611.34569](https://arxiv.org/abs/2611.34569)
   - **突破點與啟發**：人形機器人在可變形彈性地形上行走時，支撐面會隨空間與時間強烈耦合（形變、回彈與足點負載連動）。作者提出 RIPPLE 模擬到真實（Sim-to-Real）學習框架，整合了能模擬空間耦合形變與能量儲存的預張力質量－彈簧網格模型 `ElasticMembrane`。這對人形機器人在不確定、非剛性自然地表上的本體感測控制提供了突破性的建模典範。

3. **Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models**
   - **作者**：Guangyu Liu, Hanzhang Wang, Huijia Zhang, Hanbei Zhan, Linjie Hu
   - **來源/連結**：[arXiv:2611.34288](https://arxiv.org/abs/2611.34288)
   - **突破點與啟發**：現有具身世界模型多專注於 2D 視覺預測，往往忽略 3D 物體結構與接觸關係的物理一致性。本文提出 `RehearsalWorld`，結合 3D 互動排演（3DIR）與互動一致性排演（ICR），利用預訓練模型在明確的 3D 狀態空間中強制施加結構與物理約束。這項技術為具身代理提供了解析度更高、可編輯且具備物理真實感的未來互動預測能力。

4. **Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics**
   - **作者**：Xuetao Li, Xuan Jiang, Chen Liu, Zhongrui Rao, Yu Ling
   - **來源/連結**：[arXiv:2611.34302](https://arxiv.org/abs/2611.34302)
   - **突破點與啟發**：為了解決機器人軌跡稀缺但人類影片豐富的痛點，本篇提出共同世界模型（CoWM），透過對齊未同步的人類與機器人資料流，建構共享的潛在動態空間。這克服了跨本體動態差異（cross-embodiment dynamics mismatch）與動作未對齊的難題，為實現零樣本（zero-shot）人類技能轉移鋪平了道路。

## Highly Relevant

1. **End-to-End Image-Goal Navigation for Agile Quadrotors via Recurrent State Distillation**
   - **作者**：Simone Nascivera, Ismail Geles, Davide Scaramuzza
   - **來源/連結**：[arXiv:2611.34046](https://arxiv.org/abs/2611.34046)
   - **摘要重點**：結合循環狀態蒸餾，實現敏捷四旋翼無人機在沒有地圖或目標位姿下，透過單目影像進行端到端基於目標影像的 3D 導航與連續控制。

2. **Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution**
   - **作者**：Yusen Feng, Zixi Kang, Zhijun Yin, Changxiao Liu, Tianhong Gao
   - **來源/連結**：[arXiv:2611.34655](https://arxiv.org/abs/2611.34655)
   - **摘要重點**：探討導航與靈巧操作的共同演化（Co-Evolution），透過建立回饋迴路解決傳統導航過於粗糙、無法滿足精確操作基座定位的問題。

3. **Ask to Land: Learning a Mask-Conditioned Open-Vocabulary Landing Policy via Differentiable Physics**
   - **作者**：Fangyu Sun, Guanyan Wu, Yang Deng, Jiahao Cui, Fanxing Li
   - **來源/連結**：[arXiv:2611.34020](https://arxiv.org/abs/2611.34020)
   - **摘要重點**：運用可微分物理與遮罩條件化框架，讓四旋翼無人機根據自然語言提示，在各種動態及隨機移動的平台上進行開放詞彙降落。

4. **CHASE: Curiosity-Guided Skill Acquisition for Embodied Task Execution**
   - **作者**：Zixuan Wang, Wei Zhang, Chenlei Zhu, Naiyu Chen, Xihua Wang
   - **來源/連結**：[arXiv:2611.34416](https://arxiv.org/abs/2611.34416)
   - **摘要重點**：借鏡人類好奇心，提出基於好奇心的任務不確定性解析與隨需技能獲取框架，增強代理在部分觀測環境下的執行韌性。

5. **SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator**
   - **作者**：Xiang Li, Hongyu Zhou, Ya-Li Li, Tao Li, Rui Zhang
   - **來源/連結**：[arXiv:2611.34750](https://arxiv.org/abs/2611.34750)
   - **摘要重點**：提出免訓練的多模態 LLM 代理策略，透過輸出稀疏且有序的 6-DoF 末端執行器關鍵位姿（keyposes），大幅降低密集控制的推理成本並提升長距離操作效率。

6. **Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport witha Humanoid**
   - **作者**：Rikuto Hidaka, Tsung-Yuan Chen, Kento Kawaharazuka
   - **來源/連結**：[arXiv:2611.33828](https://arxiv.org/abs/2611.33828)
   - **摘要重點**：透過單一強化學習策略，協調人形機器人的全身步態、平衡控制與重物搬運時的旋轉樞軸行走（pivot walking）。

7. **A general-purpose safe manipulator planning framework for diverse environments without retraining**
   - **作者**：Mingkang Long, Rong Su, Luhang Hong, Qingqing Wang, Ruochen Tai
   - **來源/連結**：[arXiv:2611.33721](https://arxiv.org/abs/2611.33721)
   - **摘要重點**：設計通用型機械臂任務規劃框架，使機器人在環境變更時無需重新訓練即可安全執行抓取等操作。

8. **Towards 360$^^\circ$ Embodied UAV Tracking Without Turning**
   - **作者**：Bingyu Li, Wu Du, Zhiyuan Zhao, Junyu Gao, Xuelong Li
   - **來源/連結**：[arXiv:2611.33934](https://arxiv.org/abs/2611.33934)
   - **摘要重點**：提出全景視覺語言動作框架（360UAV-TVLA），利用全方位感知在無須主動調整航向的情況下進行無人機目標追蹤。

9. **Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data**
   - **作者**：Koshi Oishi, Seigo Ito
   - **來源/連結**：[arXiv:2611.33880](https://arxiv.org/abs/2611.33880)
   - **摘要重點**：將 VLA 控制模型成功應用於工業堆高機的自動卸貨任務，並探討在有限真實資料下的整合可行性。

10. **DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data**
    - **作者**：Wongyun Yu, Honggeun Kim, Donguk Lee, Minchan Kim, Kyoung Whan Choe
    - **來源/連結**：[arXiv:2611.33579](https://arxiv.org/abs/2611.33579)
    - **摘要重點**：建構自動化模擬管線，將人類手部與物件示範轉化為機械臂全機具備運動學可行性與物理執行力的訓練數據。

11. **X-World: Transferring Video Priors to Cross-Embodiment Robot Control**
    - **作者**：Chun Gu, Xiaofei Wei, Yiming Chen, Juntong Zhang, Li Zhang
    - **來源/連結**：[arXiv:2611.33914](https://arxiv.org/abs/2611.33914)
    - **摘要重點**：藉由預訓練影片擴散模型（video diffusion）提取時空先驗，透過共享流匹配專家模型轉化至跨本體的機器人控制。

12. **SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation**
    - **作者**：Zeyang Guan, Qihao Zhao, Rui Gong, Zhang Haitian, Yalun Dai
    - **來源/連結**：[arXiv:2611.33915](https://arxiv.org/abs/2611.33915)
    - **摘要重點**：使代理機器人在任務執行後能夠保留執行知識（execution knowledge），避免在重複嘗試時犯下相同錯誤，實現自我演化。

13. **RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints**
    - **作者**：Qineng Wang, Jianwen Lyu, Pingyue Zhang, Reuben Tan, Xiaoyu Huang
    - **來源/連結**：[arXiv:2611.33390](https://arxiv.org/abs/2611.33390)
    - **摘要重點**：推出包含 90 項物理約束任務的基準測試集 `RoboARC`，用以評估機械臂在狹窄間隙或互鎖零件等幾何約束下的推理與解題能力。

14. **WISER-RL: A Wake-Sleep Learning Mechanism for Robot Reinforcement Learning from One Demonstration**
    - **作者**：Kwunhang Wong, Yang Bai, Qingyang Bao, Liudi Yang, Chenzhi Liu
    - **來源/連結**：[arXiv:2611.34043](https://arxiv.org/abs/2611.34043)
    - **摘要重點**：提出結合清醒與睡眠學習循環的強化學習框架 `WISER-RL`，僅需單一示範即可透過自主實踐將人類指導轉化為穩定控制策略。

## Interesting

1. **CoTAMP (arXiv:2611.33911)**
   - 透過 LLM 自主生成非預定義動作的嘗試十分新穎，但程式碼動態生成的安全性與即時運算開銷在真實工業場景中仍具挑戰。
2. **RoboARC (arXiv:2611.33390)**
   - 借鏡類似 ARC 智力測驗的概念來測試機械臂的物理空間推理，為具身智慧的評測基準提供了一個跳脫傳統抓取任務的有趣切入點。

## Idea Sparks

1. **跨本體影片先驗與物理世界模型的融合**
   - 觀察多篇論文（如 `X-World` 與 `CoWM`）皆嘗試利用網路上豐富的人類影片或跨本體示範來解決機器人資料稀缺的問題，同時配合 3D 結構世界模型（如 `RehearsalWorld`）確保物理一致性。
   - **後續問題**：當我們將大規模人類影片先驗注入跨本體控制時，如何有效濾除人類與機器人在動力學限制（如關節極限、負載扭矩）上的根本差異，避免幻覺動作導致硬體受損？

2. **稀疏關鍵位姿與多模態代理的高效推理**
   - 從 `SOLVE` 等研究可以看出，捨棄傳統高頻密集控制、改由 VLA 代理輸出稀疏且有序的關鍵位姿（Keyposes），是兼顧靈活性與推理效率的重要趨勢。
   - **後續問題**：在面對動態、非結構化且具干擾的環境時（例如移動中的物件），基於稀疏關鍵位姿的策略該如何設計閉環修正機制，才能在動態干擾下維持足夠的反應頻寬？
