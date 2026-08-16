# 提取笔记：METHOD-022 — Li & Yan 2024 元分析（纸 vs 数字阅读）

- **Source ID**: `METHOD-022`
- **Local path**: `sources/library/papers/methods/2024_Li_DigitalVsPaper.pdf`（SHA-256 见 catalog，已核验一致）
- **Full citation**: Li, Y. & Yan, L. (2024). Which reading comprehension is better? A meta-analysis of the effect of paper versus digital reading in recent 20 years. *Telematics and Informatics Reports, 14*, 100142. DOI: [10.1016/j.teler.2024.100142](https://doi.org/10.1016/j.teler.2024.100142). CC BY-NC 4.0（© 2024 The Author(s), Elsevier）。
- **书目核对**：PDF 首页（作者、标题、venue、DOI、许可）与 `sources/catalog.yaml` 条目一致，无出入。PDF 共 9 物理页；下文页码均指 PDF 物理页。
- **审计角色**：Class 4 最新元分析；焦点为效应量、与既有元分析的差异、边界条件。

## 结论速览（中文）

投递模式（paper vs digital）作为「阅读媒介」变体，总体不移动阅读理解分数分布（随机效应 g=0.046, p=0.706），但异质性极高（I²=91.79%）且所有 moderator 均显著或方向交替：限时（g=−0.468）、大学及以上（g=−0.432）、中国样本（g=−0.66）下**纸本显著更优**；文学文本（g=0.968）、交互型数字阅读（g=0.959）、使用阅读策略（g=0.781）、外国样本（g=0.279）下**数字显著更优**。结论：模式效应不是常数，而是受时间压力、学段、文本类型、交互 affordance、地区调节的估量（estimand）位移。本论文**无过程指标、无缺失率数据**，对 Class 2/3 无直接贡献；对 Class 4 是当前审计中第一份全文级「阅读媒介 × 阅读效果」元分析证据。

## 研究概览

- **研究问题**：纸本与数字阅读的阅读理解效果差异；受众特征（学段、国家）、文本特征（类型、长度）、阅读条件（策略、时间限制、交互性）的调节作用。
- **样本**：37 篇实验研究、46 个独立实验/效应量（"integrated 46 effects from 46 experiments in 37 literature"，PDF p.3）；检索 2000–2022 年、检索日期 2023-01-09；中英文库（CNKI/VIP/WANFANG/台湾 TWS + WoS/ScienceDirect/EBSCO/JSTOR/SAGE/Scopus/Wiley）初筛 4016 篇（含 14 篇雪球）（PDF p.2）。
- **设计**：元分析（"a meta-analysis"，PDF p.1 摘要）；纳入标准为纸/数字对照、文本内容一致且长于一句、学生群体、排除视障/自闭等特殊人群（PDF p.2）；分析单元为单个实验；异质性检验 I²=91.790% 极高 → 随机效应模型；效应量用 Hedges' g（小样本校正，CMA 3.0 计算）（PDF pp.3, 5）。
- **任务与材料**：各一手研究自带的阅读理解任务；DV 依 NEPS 阅读能力框架归为定位/回忆、综合/解释、批判/评价三类（PDF p.3）——但实际纳入研究含词汇、记忆、emergent literacy 等任务（见 Table 1，PDF pp.4–5），"reading comprehension effect" 的 operationalization 跨研究不一（审计注意点）。
- **变量**：
  - 产品分数：阅读理解效果（g，正=数字优、负=纸本优）。
  - Moderators（Table 3，PDF p.7）：学习阶段（幼儿园 8 / 小学 6 / 中学 8 / 大学及以上 22 效应）、国家（中国 12 / 外国 34）、文本类型（文学 12 / 信息 26）、文本长度（≤1000 词 8 / 1000–2000 词 6 / >2000 词 9）、阅读策略（用 12 / 不用 8）、时间限制（限时 10 / 自由 26）、交互性（交互 11 / 非交互 33）。
  - 过程指标：**无**。缺失指标：**无**。

## 核心发现（按四类主张分组）

### Class 4 — 学习/构念与 estimand（核心贡献）

1. **总体模式效应小且不显著，但异质性极高**（PDF pp.5–6）：随机效应 g=0.046（95% CI −0.192, 0.283），p=0.706；固定效应 g=0.004；I²=91.790%。Egger 检验 p=0.5476，无显著发表偏倚（PDF p.5）。原文："the average effect size g = 0.046 … is a small effect; that is, the impact of digital reading on students' reading comprehension is slightly better than that of paper reading. However, due to p = 0.706, there is no significant difference"（PDF p.6）。→ 投递模式总体不移动分数分布，但效应高度不稳定，moderator 才是信息所在。

2. **学段调节模式效应：大学及以上纸本显著更优，低年级数字略优但不显著**（PDF pp.6–7）：大学及以上 g=−0.432（95% CI −0.654, −0.21, p=0.000）；幼儿园 g=0.866（p=0.067）、小学 g=0.688（p=0.081）、中学 g=0.204（p=0.487）均 ns；组间 Q=16.147, p=0.001。原文："the group effect size of university and above is negative, and there is a significant difference, indicating that the reading comprehension effect of paper reading is significantly better than that of digital reading in this group"（PDF p.6）。

3. **国家调节模式效应，方向相反**（PDF p.6）：中国 g=−0.66（95% CI −1.108, −0.212, p=0.004）纸本优；外国 g=0.279（95% CI 0.025, 0.534, p=0.032）数字优；组间 Q=12.768, p=0.000。原文："in China (g = − 0.66), the understanding effect of paper reading is better than that of digital reading, while in other countries (g = 0.279), it is the opposite"（PDF p.6）。作者归因于数字阅读环境、设备、阅读观念与体验差异（PDF p.6）。

4. **文本特征调节模式效应**（PDF p.6）：文学文本 g=0.968（95% CI 0.321, 1.616, p=0.003）数字显著优 vs 信息文本 g=−0.218（p=0.053）纸本略优，组间 Q=11.570, p=0.001。文本长度组间不显著（Q=3.189, p=0.203），但 1000–2000 词文本纸本显著优（g=−0.391, 95% CI −0.633, −0.150, p=0.001）；>2000 词 g=−0.524（p=0.081）；≤1000 词 g=0.125（p=0.662）。作者解释为长文本下数字阅读疲劳、滚动致视线跳跃、弹窗干扰（PDF p.6）。

5. **时间限制调节模式效应**（PDF pp.6–7）：限时 g=−0.468（95% CI −0.75, −0.186, p=0.001）纸本显著优 vs 自由 g=0.192（p=0.209）数字略优；组间 Q=9.871, p=0.002。原文："When students freely engage in reading (g = 0.192) … the understanding effect of digital reading is better than that of paper reading, and there is a significant difference (p < 0.05) under the two variables of using reading strategies and using digital reading devices to provide interactive functions"；"reading under time constraints (g = − 0.468)" 纸本优且显著（PDF p.7）。→ 时间压力是模式效应显现的关键边界条件，直接相关 RQ0「限时 vs 自由」。

6. **交互性调节模式效应**（PDF pp.6–7）：交互型数字阅读 g=0.959（95% CI 0.297, 1.622, p=0.005）数字显著优 vs 非交互 g=−0.172（p=0.149）；组间 Q=9.96, p=0.002。原文："use digital reading devices to provide interactive functions (g = 0.959), the understanding effect of digital reading is better than that of paper reading"（PDF p.7）。→ 数字端交互 affordance 不是中性装饰，而是可移动产品分数的构成。

7. **策略使用调节模式效应**（PDF pp.6–7）：使用策略 g=0.781（95% CI 0.199, 1.362, p=0.008）数字显著优 vs 不使用 g=−0.172（p=0.368）；组间 Q=7.291, p=0.007。

8. **机制解释（讨论层，非测量）**（PDF p.7）：作者以 shallowing hypothesis（浅层加工假设）解释数字劣势；并指出数字环境不便使用划线/批注等传统阅读技能（引用一手研究 [3]，非本文测量）。

### Class 2 — 行为改变（无直接证据，仅机制假设）

- 本元分析**不含任何过程/行为指标**；四类主张中 Class 2 只能获得讨论层的机制假设：数字环境下"marking and scribing"等传统技能使用受阻（PDF p.7，引用 [3]）、翻页/回看时滚动导致"gaze to jump"干扰理解（PDF p.6，引用 [3]）、弹窗等干扰因素（PDF p.6）。这些是作者引述的定性解释，**不是本文测量的行为数据**，不可当作行为改变证据。

### Class 3 — 仪器信度与缺失（无直接证据）

- 论文**不报告缺失率、遗漏、作答时间或数据质量筛查**。唯一间接含义：I²=91.79% 的极高异质性（PDF p.5）+ 国家 moderator 方向相反（PDF p.6）说明「模式效应」的稳定性与可推广性本身受情境限制，跨模式/跨情境的分数可比性不能默认成立——但这属于 Class 4 推论，非 Class 3 测量证据。

### Class 1 — 可用性/偏好（无证据）

- 不测量满意度、偏好或可用性。Limitations 中仅建议未来研究纳入 "media preferences"（PDF p.8）；Discussion 提及数字阅读的 "subjective shortcomings"（PDF p.7）。→ Class 1 无贡献。

## 与既有元分析的差异（审计焦点）

- **Jiang Hong 2017**（36 篇、106 效应）：结论为数字显著优于纸本（PDF p.2，转述）。**Zhang Xiyan 2021**（48 篇、127 效应，2010–2020）：结论为无显著差异（PDF p.2，转述）。**Li & Yan 2024**（37 篇、46 效应，2000–2022）：总体无显著差异，但 moderator 层差异显著且方向交替。作者把差异归因于"纳入的一手文献不同 + 数据处理方法不同"（PDF p.2）。
- 与西方成人谱系元分析（Clinton 2019 等，本文引为 [13]）的关系本文未做直接效应量对比；但本样本结构不同——46 效应中 12 个来自中国研究、低龄学段占比高（幼儿园+小学+中学=22，大学=22），这可能解释国家/学段 moderator 的结果方向。
- 与 `METHOD-012`（ACT，online>paper, d=.16–.22）对照：Li & Yan 总体数字略优（g=0.046 ns），而大学及以上（g=−0.432）、限时（g=−0.468）、中国（g=−0.66）纸本更优。二者机制不同（ACT 是**作答测试模式** paper vs online；Li & Yan 是**阅读媒介/载体**），方向不可直接互推；但共同确认「投递层变体可移动阅读相关估量」这一前提。

## 边界与局限

作者自述（PDF p.8）：① 收录难免遗漏；② 各 moderator 类别样本量不均（大学生占比高），结果须谨慎；③ **不区分数字设备**（平板/台式/手机/Kindle 混编），无法得出设备级结论；④ 只覆盖学生群体；⑤ 未纳入阅读速度等效应指标、媒体偏好、细分媒体类型。
审计补充的方法局限（笔记作者）：⑥ "reading comprehension effect" operationalization 跨研究不一（含词汇/记忆/emergent literacy 任务，Table 1, PDF pp.4–5），被测量本身非统一构念；⑦ 未报告双编码者一致性（inter-rater reliability）；⑧ moderator 间可能混杂（交互型研究多为幼儿文学书、大学研究多为信息长文本）；⑨ 发表偏倚仅 Egger 检验（p=0.5476），无 trim-and-fill；⑩ 数据仅 "available on request"（PDF p.8）；⑪ 无过程指标、无缺失率，Class 2/3 不可由本文回答；⑫ 阅读场景（学习/阅读效果），**非作答/测试场景**，外推到答题 UI 变体须留余量。

## 对审计的用途

- **解除既有限制**：审计主文件 `reports/research/ui-instrument-effects-evidence-audit.md` 第 175、186 行将 Li & Yan 2024 列为"仅 metadata 层筛选、结论不得断言"；本笔记为全文级提取，该限制对本文解除（正文 p.175 所列 meta 序列中 Li & Yan 一项可转正）。
- **支持 `UIE-27`（METHOD-012）**：独立元分析证据确认投递层变体可移动阅读分数分布，且补充边界条件（限时、学段、地区）。**限定**：ACT 是作答测试模式效应，Li & Yan 是阅读媒介效应，综合时必须区分「作答模式」与「阅读媒介」两个变体族，方向不可互推（ACT online 优 vs Li & Yan 大学/限时/中国纸本优）。
- **对照 `UIE-26`（METHOD-011）**：为 TME 威胁提供具体效应量与 moderator 结构；总体小效应（g=0.046）与 K-12 谱系"小/null"线索（审计正文 p.177 引 Wang 2008 等）一致，成人/大学情境效应更大且为负。
- **回应审计正文 p.177 的"K-12 小/null vs 成人媒介元分析"张力**：Li & Yan 的学段 moderator（低年级正 ns、大学显著负）为两个谱系的方向差异提供学段调节解释。
- **对 RQ0**：时间限制 moderator 是直接相关结论——自由阅读下模式效应不显著（g=0.192 ns），限时下纸本显著占优（g=−0.468）；baseline 是否限时、以及"限时属于构念（speededness）还是仪器条件"，决定了纸/屏变体是否会移动估量。

## 建议新增 UIE 条目（草稿）

- **UIE-31（新增，Class 4）**：投递模式 × 时间压力——限时条件下纸本阅读显著优于数字（g=−0.468, p=0.001），自由阅读无显著差异（g=0.192, p=0.209）；组间 Q=9.871, p=0.002。verdict `SUPPORTED`（元分析范围）。Scope：学生群体、阅读理解任务；限时为调节变量；无作答 UI 细节；阅读场景非作答场景。
- **UIE-32（新增，Class 4）**：投递模式总体效应小且不显著（随机 g=0.046, p=0.706；固定 g=0.004），但 I²=91.79% 且各 moderator 方向交替 → 任何"数字阅读总体更差/更好"的断言不受支持，模式效应高度情境依赖。verdict `SUPPORTED`（对总体小效应；反向约束方向性断言）。Scope：元分析总体（37 研究/46 效应）。
- **UIE-33（新增，Class 4）**：数字交互 affordance 移动产品分数——交互型数字阅读显著优于纸本（g=0.959, p=0.005），非交互数字与纸本无显著差异（g=−0.172, p=0.149）。verdict `PARTIAL`（交互性二值编码；与学段/文本类型混杂；阅读场景非作答场景）。含义：交互功能不只是 UX 偏好，可改变被测量。
- **UIE-34（新增，Class 4）**：学段 × 投递模式——大学及以上纸本显著优（g=−0.432, p=0.000），低年级数字略优但 ns（幼儿园 0.866 / 小学 0.688 / 中学 0.204）。verdict `SUPPORTED` within meta-analytic scope。含义：模式效应随年龄/任务复杂度变化，跨学段外推受限。
- **UIE-35（可选，新增，Class 4）**：地区 × 投递模式——中国样本纸本优（g=−0.66, p=0.004）、外国样本数字优（g=0.279, p=0.032），组间 p=0.000。verdict `SUPPORTED` within data；外推受限（语言/设备/环境差异）。若空间有限可并入 UIE-32 作为"方向交替"的实例。
