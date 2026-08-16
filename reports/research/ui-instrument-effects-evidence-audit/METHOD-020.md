# METHOD-020 全文证据提取笔记 — Schwabe et al. (2022)

## 头部

- **Source ID**: `METHOD-020`
- **本地路径**: `sources/library/papers/methods/2022_Schwabe_ScreenVsPrintComprehension.pdf`（19 页；CC BY 4.0）
- **完整书目**: Schwabe, A., Lind, F., Kosch, L., & Boomgaarden, H. G. (2022). *No Negative Effects of Reading on Screen on Comprehension of Narrative Texts Compared to Print: A Meta-analysis*. Media Psychology, 25(6), 779–796. DOI: 10.1080/15213269.2022.2070216
- **catalog 核对**: `sources/catalog.yaml` 条目（authors/title/year/venue/DOI）与 PDF 首页完全一致，无出入。
- **审计角色**: 审计文件检索记录 C4/S3（`ui-instrument-effects-evidence-audit.md` L46/L60）将其列为 Delgado/Clinton 的「contrary-direction record」；L175、L186、L245 三处均声明其结论在全文获取前「不得以任一方向断言」。本笔记裁决这一悬置（见「对审计的用途」）。

## 研究概览

- **研究问题**: RQ1 同一叙事文本在屏幕 vs 纸上阅读，理解是否不同？RQ2 多媒体/交互增强叙事书 vs 纸质版？RQ3 附加功能类型（娱乐性 vs 理解支持性）？RQ4 效应是否随时间（1982–2021）变化？RQ5 不同阅读设备（computer/tablet/e-reader/smartphone/television）？
- **样本**: 元分析。k = 32 个独立样本（19 篇期刊文章 + 10 项灰色文献），N = 2239（M = 69.97, SD = 54.74, 范围 19–284），66 个效应量；11 国（北美 17、亚洲 7、欧洲 5）；1982–2021 出版（PDF p.8，printed 785）。
- **设计**: 元分析（meta-regression with RVE, `robumeta`, ρ = .8，小样本校正；TOST 等价检验；Egger Sandwich 出版偏倚检验）。纳入标准：屏幕 vs 纸同一文本的比较（within/between 均可）、刺激必须含至少一篇叙事文本且有独立效应量、被试至少小学一年级且自行阅读、第一语言文本、排除视觉小说/文字游戏、干预研究与非实验（PRISMA 图 PDF p.7，printed 784；编码流程 PDF p.8，printed 785）。
- **任务与材料**: 叙事文本（fictional stories），多数为休闲阅读语境；理解测试类型多样（MC / 开放题 / retelling，literal/inferential/spatiotemporal）。
- **变量**: 产品分数（阅读理解 test scores，Cohen's d，正值 = 屏幕优于纸）；调节变量 = 附加功能（有/无；娱乐性 vs 理解支持性）、出版年、设备类型、设计类型、出版类型、年龄组。**无过程指标、无缺失率/数据质量指标**——本元分析只汇总产品分数。
- **效应量说明**: 主效应 d 正值为数字媒体占优；narrative 体裁、休闲阅读、非速度、非作答 UI 语境。

## 核心发现（按四类主张分组）

### Class 4 — 学习/构念与 estimand（产品分数）

- **F4-1｜主效应：屏幕 vs 纸对叙事文本理解无显著差异。** d = 0.10, SE = 0.06, p = .12, 95% CI [−0.03, 0.22]，不显著；但异质性高（I² = 74.25%, τ² = 0.10）。PDF p.12（printed 789）。引文：*"The results of the meta-analysis using the whole sample (k = 32) do not suggest a significant difference in reading comprehension of a narrative text between reading an e-book and reading in print (d = 0.10, SE = 0.06, p = .12, 95% CI [−0.03, 0.22])."*
- **F4-2｜主效应统计上与零等价。** TOST 等价检验（边界 d = ±0.25）：lower bound Z = 5.80, p < .001；upper bound Z = −2.55, p < .01；null test Z = 1.62, p = .10。作者结论：即使效应存在，也太小以致不相关。PDF p.14（printed 791）。引文：*"the equivalence test and the null hypothesis test suggested the observed main effect was statistically equivalent to zero … We can therefore conclude that … the effect of a reading medium on comprehension of narrative texts does exist, it is too small to be relevant."*
- **F4-3｜无附加功能的纯文本子样本：效应 ≈ 0。** k = 21，d = −0.02, SE = 0.06, p = .67, 95% CI [−0.14, 0.09]（τ² = 0.07, I² = 71.40%）。PDF p.12（printed 789）。引文：*"When there are no multimedia functions or additional support (k = 21) … the effect of the reading medium on reading comprehension is almost zero and not significant (d = −0.02 …)."*
- **F4-4｜多媒体/交互功能显著正向移动分数分布。** k = 12，d = 0.37, SE = 0.11, p < .01, 95% CI [0.13, 0.61]（τ² = 0.12, I² = 69.15%）——增强内容使数字阅读显著优于纸。调节变量显著：Table 2 中 additional functions yes b = 0.35 (SE = 0.13), p = .047, CI [0.01, 0.69]。**但所有附加功能研究均为学龄儿童（2–12 年级）**，作者明确警示不可推广到熟练读者。PDF p.13（printed 790）；Table 2 PDF p.15（printed 792）。引文：*"when multimedia or interactive functions are present (k = 12), the positive effect of the digital reading medium on comprehension is small but significant (d = 0.37 …)."* 与警示：*"all primary studies using multimedia/ interactive functions were conducted on school children (2nd–12th grade)."*
- **F4-5｜功能类型（娱乐性 vs 理解支持性）无差异。** b = 0.07, SE = 0.20, p = .74, 95% CI [−0.40, 0.54]。作者无法分离纯娱乐性功能的独立效应（样本中大多与词典/发音支持配对）。PDF p.13（printed 790）。
- **F4-6｜设备类型无显著差异。** computer d = 0.06, SE = 0.08, p = .45, CI [−0.11, 0.23]（τ² = 0.10, I² = 75.27%）；tablet d = 0.04, SE = 0.03, p = .29, CI [−0.07, 0.16]（τ² = 0.00, I² = 0.00%）；e-reader d = 0.14, SE = 0.12, p = .28, CI [−0.14, 0.43]（τ² = 0.15, I² = 81.27%）。Table 2 中 e-reader 调节项 b = 0.27 (SE = 0.14), p = .07（边缘不显著）。PDF p.13–14（printed 790–791）；Table 2 PDF p.15。
- **F4-7｜出版年无调节效应。** b = 0.00 (SE = 0.02), p = .94——屏幕理解效应 40 年内无变化，屏幕技术改善与「浅阅读习惯」假设均未得到支持。PDF p.13（printed 790）；Table 2 PDF p.15。

### Class 2 — 行为改变

- **F2-1｜元分析层面无过程指标，本文不直接提供行为改变证据。** 唯一与行为/交互相关的发现是 F4-4：数字文本附加的交互/多媒体功能（词典、发音支持、动画、音效）把产品分数从 d ≈ 0 移到 d = 0.37——这发生在**阅读材料/内容层**（stimulus enhancement），不是作答 UI 或导航/布局变体；且对阅读过程本身（skimming/shallow processing 假设）作者只在理论背景中讨论（PDF p.3–4，printed 780–781），没有测量任何过程变量。作者在讨论中把「数字媒体触发浅阅读策略」归为未被自身数据支持的理论预期（PDF p.15–16，printed 791–793）。
- **F2-2｜设计/出版类型不影响效应。** within vs between 设计（b = 0.09, SE = 0.11, p = .41）与期刊 vs 灰色文献（b = −0.13, SE = 0.11, p = .28）均不显著（Table 2，PDF p.15），因此作者未拆分样本分析——对审计的含义是：任务设计差异（within-subject 作答重复测量）在本元分析中不构成调节证据，但这也意味着它无能力检出作答层设计效应（范围边界，见下）。

### Class 3 — 仪器信度与缺失

- **F3-1｜本文未报告任何缺失率/数据完整性指标**，元分析层面无 missingness 证据。
- **F3-2｜测量仪器与构念匹配问题的声明（边缘相关）。** 作者指出纳入研究大多使用「与文本体裁无关、默认按说明文设计」的理解测试：*"most studies with a narrative text as stimuli used reading comprehension tests designed to measure reading comprehension regardless of text genre, which translates to expository texts being the default. These instruments might not be suitable for researching reading comprehension of narrative texts, and new methods need to be developed."*（PDF p.16，printed 792）——工具与构念错配可能解释「找不到显著效应」，这是测量效度层面的声明，可作为 Class 3/4 边界背景，非缺失率证据。

### Class 1 — 可用性/偏好

- **F1-1｜本文未测量可用性、满意度或媒介偏好**；个体差异（含媒介偏好）仅在讨论中被列为未来研究方向（PDF p.16，printed 793）。无可用性主张。

### 出版偏倚与稳健性（元分析自身质量，必提）

- **Egger Sandwich 检验显著**：β = 1.29, SE = 0.60, p = .02（漏斗不对称）。作者辩称：灰色文献与期刊效应无显著差异 + 66 个效应量中仅 21 个显著 → 不可能是掩盖主效应非显著的出版偏倚。PDF p.14（printed 790–791）。
- **ρ 稳健性**：ρ = 0/0.2/0.4/0.6/0.8/1 结果一致（至少到小数点后第三位）。PDF p.14（printed 791）。

## 边界与局限

- **人群边界**: 附加功能效应仅基于学龄儿童样本（2–12 年级），不可外推到熟练读者/成人（PDF p.16，printed 792–793）；排除二语学习者（最可能受益于词典类功能）；无个体差异（性别、工作记忆、人格、媒介偏好）分析。
- **任务/材料边界**: 仅叙事文本、休闲阅读语境、阅读后立即作答（无延迟/长期记忆效应，PDF p.16 printed 793）；多数研究在受控实验室/学校环境进行，排除真实干扰（网络/消息），作者承认外部效度问题；**非速度性、非测评语境、非作答 UI 变体**——与 ACT 式高速度标准化阅读测试（METHOD-012）不可直接类比。
- **效应量边界**: 主效应 d = 0.10 等价于零的结论受 TOST 边界 ±0.25 约束（PDF p.14 printed 791）；异质性高（I² = 74.25%）。
- **设备边界**: smartphone 样本仅 k = 2、television 仅 k = 1，无法对智能手机做元分析（PDF p.16 printed 793）；e-reader 子样本 I² = 81.27%，异质性极高。
- **作者自声明的局限**: 全部见于 PDF p.16（printed 792–793），如上；另承认测试仪器不适配叙事文本构念（F3-2）。
- **不可外推处**: 任何关于「作答 UI / 反应格式 / 导航 / 反馈」变体的结论均不可由此元分析推出——它只比较投递媒介（medium）+ 阅读材料增强，不操作 instrument 层。

## 对审计的用途

**裁决「contrary-direction record」**（审计 L46/L60/L175/L186/L245 的悬置点）:

- Schwabe 2022 **不是** Delgado/Clinton 结论的简单反向，而是**体裁调节的限定**：Schwabe 自己的讨论确认与 Clinton (2019)、Delgado et al. (2018) 的叙事文本子样本一致（后两者各自仅 7 个叙事样本），差异在于 Schwabe 用近 5 倍样本（k = 32）证明叙事体裁下屏幕 vs 纸理解效应统计上等价于零（TOST, ±0.25）。Clinton/Delgado 报告的总体负效应主要来自说明文（expository）研究。审计 L175 的「方向张力」应表述为：**投递模式对阅读理解产品分数的效应是任务/体裁/速度条件性的**——说明文 + 时间限制语境负向（Delgado/Clinton 总体 g ≈ −0.21，本笔记 ABSTRACT-ONLY 层面转述），叙事 + 非速度语境为零（Schwabe，全文已核），高速度标准化阅读测试（ACT, METHOD-012/UIE-27）正向 d = .16–.22。三个方向并存而非互相矛盾；不可把任一方向的单一记录作为普适模式效应。
- **支持/限定既有 UIE 条目**: UIE-27（METHOD-012，投递模式移动阅读分数分布）——METHOD-020 表明该效应**不能普适化到叙事/非速度语境**，UIE-27 的 scope boundary 应补一句「叙事体裁与无时间压力语境下模式效应为零（METHOD-020）」；同时也强化其「模式级而非变体级」的定位（METHOD-020 完全不触及作答层变体）。
- **对审计 L179 的贡献**: 「没有任何本地源证明阅读 MC 作答 UI 的具体变体改变所测构念」——METHOD-020 不改变这一结论（它证明的是 medium 层与 content 增强层，非 instrument 层）。
- **对 Class 4 的净贡献**: 为「投递方式/内容增强可移动分数分布」增加一个全文级锚点：medium 不移动（叙事、非速度），content-layer 增强移动（d = 0.37, 儿童样本）。

**建议新 UIE 条目草稿**:

- **UIE-31（建议）｜投递模式对阅读理解产品分数的影响是体裁/速度条件性的：叙事文本、休闲阅读语境下屏幕 vs 纸无显著差异且统计上等价于零（d = 0.10, p = .12, TOST ±0.25 显著等价），而数字文本的多媒体/交互增强显著提高理解（d = 0.37, p < .01, k = 12）——与说明文语境下的纸优结论（Delgado/Clinton）及高速度标准化测试中的屏优结论（METHOD-012/UIE-27）并存，方向由任务语境决定。**
  - 证据: `METHOD-020`, 主效应 PDF p.12；TOST PDF p.14；附加功能 PDF p.13；Table 2 PDF p.15。
  - 暂定 verdict: `SUPPORTED`（在其范围内：叙事体裁、非速度、非作答 UI、元分析层面）。
  - Scope boundary: 元分析 k = 32, N = 2239, 1982–2021, 11 国；附加功能效应仅限学龄儿童样本；不涉及作答 UI/反应格式/导航/反馈变体；无过程与缺失率证据。

## 笔记元信息

- 提取范围：全文 19 页逐页通读（`pdftotext -layout`），无 `ABSTRACT-ONLY` 条目。
- 页码均为 PDF 物理页；printed 页码（杂志卷期页码）在括号内标注。
- 未修改 catalog、checksums、审计主文件或任何其他文件。
