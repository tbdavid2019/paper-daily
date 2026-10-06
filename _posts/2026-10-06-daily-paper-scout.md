---
layout: post
title: "每日論文雷達｜2026-10-06"
date: 2026-10-06 00:00:00 +0000
topic: "embodied_ai"
---
## 今日概況

- **日期**：2026-10-06
- **主題**：具身智慧 (Embodied Intelligence)
- **收錄數量**：本次爬取總計 846 篇論文，經過重複篩選後剩餘 731 篇，其中符合關鍵字條件的新候選論文共 604 篇，本次精選出 30 篇進行深度追蹤。

## Must-Read

- **[SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models](https://arxiv.org/abs/2610.06598)**
  - **作者**：Xiaodong Wang, Tianle Li, Chuanxin Song, Junliang Xie, Zhanmi Zhong
  - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_cs.CV, arxiv_keyword
  - **摘要證據與研究關聯**：本篇提出 SimForcing 框架，利用模擬環境作為可轉移的動作知識來源以及預測的控制參考，解決動作條件機器人世界模型在處理異質機器人影片時，難以兼顧精準軌跡回應與真實視覺動態的挑戰。對於探索世界模型與模擬到真實（Sim-to-Real）轉移的研究者而言，提供了一種結合模擬先驗與真實網域的新穎途徑。

- **[PerturBot: Breaking Shortcut Priors in Vision-Language-Action Models with Perturbative Training](https://arxiv.org/abs/2610.04616)**
  - **作者**：Mingyu Liu, Chonghao Sima, Tianjian Feng, Hanqing Wang, Cong Chen
  - **來源**：huggingface, arxiv_cs.RO, arxiv_cs.CV, arxiv_keyword
  - **摘要證據與研究關聯**：研究指出視覺-語言-動作（VLA）模型容易依賴捷徑先驗（Shortcut Priors），例如手腕相機附近的物件干擾、熟悉的詞彙或未閉合的夾爪等無效特徵來預測動作，而忽略任務所需的核心證據。作者透過擾動式訓練（Perturbative Training）來打破這些模態捷徑，對提升 VLA 模型在複雜任務中的決策穩健性具有重要價值。

- **[VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.06271)**
  - **作者**：Jaemin Kim, Jiahn Kim, Taesik Gong
  - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_keyword
  - **摘要證據與研究關聯**：針對 VLA 模型在部署階段適應分佈偏移（Distribution Shifts）的需求，傳統一階適應方法容易超出推論平台的記憶體預算。該論文提出 VLA-ZO，利用零階（ZO）優化與 VLA 計算結構，實現僅需推論級記憶體的快速適應，對資源受限的機器人基礎模型部署是一項具實用性的架構優化。

## Highly Relevant

- **[InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation](https://arxiv.org/abs/2610.06850)**
  - **作者**：Yucheng Zhang, Sirui Xu, Jinhong Li, Liuyu Bian, Anatulya Nandi
  - **來源**：huggingface, arxiv_cs.RO, arxiv_cs.CV
  - **摘要證據與研究關聯**：提出自演化動作模仿框架，將擷取的人類-物件互動資料重新定位至人形機器人參考資料，藉此規模化人形動態操作（Loco-Manipulation）能力。

- **[GeoBridge-VLA: Geometry-Aware Residual Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2610.05026)**
  - **作者**：Hyun Song, Kangmin Kim, Lorenz Jinsoo Um, Minhui Han, Jaehyeok Park
  - **來源**：arxiv_cs.RO, arxiv_cs.CV, arxiv_keyword
  - **摘要證據與研究關聯**：提出二階段方法，透過凍結的 VLA 視覺編碼器學習幾何特徵，並透過門控殘差介面與動作專家結合，補足 VLA 在精確空間推理上的不足。

- **[ExStereo: Lifting 2D Vision-Language-Action Models to 3D with Explicit Stereo Representations](https://arxiv.org/abs/2610.04805)**
  - **作者**：I-Chun Arthur Liu, Jason Chen, Gaurav S. Sukhatme, Daniel Seita
  - **來源**：arxiv_cs.RO, arxiv_cs.CV, arxiv_keyword
  - **摘要證據與研究關聯**：利用立體匹配基礎模型引入 ExStereo 模組，從立體影像對重建場景幾何，將原本依賴單眼 RGB 的 2D VLA 提升至 3D 空間感知。

## Interesting

- **[SUAVE: Unified Video-Action Models via Masked Diffusion](https://arxiv.org/abs/2610.04009)**
  - **作者**：Rhythm Syed, Jean Mercat, Sedrick Keh, Kushal Arora, Paarth Shah
  - **來源**：arxiv_cs.RO, arxiv_keyword
  - **摘要證據與研究關聯**：透過遮罩擴散（Masked Diffusion）將影片生成與動作預測統一於單一架構中，探討模型在行動前「想像未來」的可能性。

- **[TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)**
  - **作者**：Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng, Yichen Feng, Yaorui Ding
  - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_cs.CV
  - **摘要證據與研究關聯**：研究世界動作模型的對抗性漏洞，提出僅使用公開編碼器即可建構跨任務固定區域擾動的 TAPDreamer 攻擊方法。

- **[AffordCraft: Scalable Construction of Task-Ready Simulation Assets from Single Images](https://arxiv.org/abs/2610.06643)**
  - **作者**：Haoyun Yang, Xueyang Zhou, Ziyi Xie, Yongchao Chen
  - **來源**：arxiv_cs.RO, arxiv_cs.AI, arxiv_cs.CV
  - **摘要證據與研究關聯**：透過檢索而非生成的方式，從單張 RGB 影像與任務指令為模擬器構建具備獨立部件與物理屬性的任務就緒資產。

- **[Arm-wise Compositional Generalization in Dual-Arm Vision-Language-Action Models](https://arxiv.org/abs/2610.06184)**
  - **作者**：Zaibin Zhang, Binghao Ran, Yuhan Wu, Zhongbo Zhang, Yifan Wang
  - **來源**：huggingface, arxiv_cs.RO, arxiv_keyword
  - **摘要證據與研究關聯**：推出 ACG-Bench 基準測試，專門用於評估雙臂 VLA 模型在跨手臂組合熟悉原子技能時的臂級組合泛化能力。

## Idea Sparks

1. **從模擬先驗到真實世界模型的混合知識蒸餾**
   - 觀察 `SimForcing` 與 `AffordCraft` 的思路，兩者皆試圖透過模擬環境提供結構化監督或任務資產。這引發了一個後續問題：當模擬環境的視覺動態與真實世界存在差距時，如何設計一種動態權重調節機制，以自動過濾掉模擬中不準確的預期，避免其對真實網域的影片生成與世界模型造成負面引導？

2. **模態捷徑（Modal Shortcuts）與幾何感知強化的結合**
   - 觀察 `PerturBot` 點出 VLA 模型容易依賴如物體位置或字面關聯等捷徑，而 `GeoBridge-VLA` 則試圖透過幾何特徵殘差適應來加強空間推理。這引發了一個後續問題：在 VLA 的訓練過程中，引入顯式的 3D 幾何監督（例如透過 `ExStereo` 這類模組）是否有助於自動抑制或削弱模型對視覺捷徑（Shortcut Priors）的依賴？
