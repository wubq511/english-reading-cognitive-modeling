# Evidence Extraction Note — METHOD-028

Source ID: `METHOD-028`
Local path: `sources/library/papers/methods/2008_Wang_TestModeEffects.pdf`（PDF 20 页，物理页码制）
Full citation: Wang, S., Jiao, H., Young, M. J., Brooks, T., & Olson, J. (2008). Comparability of Computer-Based and Paper-and-Pencil Testing in K–12 Reading Assessments: A Meta-Analysis of Testing Mode Effects. *Educational and Psychological Measurement*, 68(1), 5–24. DOI: 10.1177/0013164407305592

**书目核对**：标题、期刊卷期（EPM 68(1), Feb 2008, pp. 5–24）、年份、DOI 与 PDF 首页一致。一处差异：catalog 第五作者记 "Jane Olson"，PDF 首页与正文作者自引（"Wang, S., Jiao, H., Young, M. J., Brooks, T. E., & Olson, J. (2007)"，PDF p.20）均为 "John Olson"。按纪律不改 catalog，在此标注待更正。

---

## 结论速览（中文）

- **核心结论**：K-12 阅读测验 CBT vs PPT 投递模式的元分析。排除 6 个速度化/缺失驱动的离群研究后，36 个同质研究加权均值效应 `d_w = −.004`（95% CI [−.031, .023]，p = .782），**平均无统计显著模式效应**；即使全样本固定效应估计显著（`d_w = −.077`，p = .000），按 Cohen 标准也属「实际可忽略」（<.2）。审计元数据级记录「small/null mean differences」得到全文确认，但需带两条限定：① 全样本存在强异质性（Q(41)=356.54，p<.01），42 个 ES 中 12 个（28.6%）单研究显著；② 被排除的 6 个研究（Ito et al. 2004）呈**最大且全部为 CBT 更低**的效应（d = −.31 至 −.56），作者归因于 CBT 速度化导致的**逐项未作答率递增**（9%–17% 学生自报时间不足）。
- **怎么得出的**：全文 `pdftotext -layout` 通读，所有页码为 PDF 物理页；效应量与 moderator 统计量逐表核对（Table 3 / Table 4）。
- **未决项**：moderator 回归仅 11 项原始研究、10 个预测变量，统计功效与过拟合风险未在文中讨论；"type of test" 的 p = .06 处于边缘，且该变量指测验类别（national/state 等），**不是题目格式或 UI 变体**，不可外推为「题目类型不调节模式效应」。

## 研究概览

- **研究问题**：CBT（计算机投递）与 PPT（纸笔）两种管理模式对 K-12 学生阅读测验分数是否有系统性差异；哪些研究属性（design、grade、sample size、test type、delivery method、delivery algorithm、computer practice）调节该差异（PDF p.1, pp.6, 10）。
- **样本**：1980–2005 文献检索（期刊、ERIC 等 8 个数据库、出版商站点、Google/Yahoo 关键词、手工检索、个人联系）→ 初始 312 篇 → 纳入标准（1980–2005；K-12 学生；组内样本量 >25；报告 CBT/PPT 双模式阅读分数均值与 SD；英语测验）→ **11 项原始研究、42 个独立实验/数据集**（PDF pp.6–7）。样本分布：>80% 来自初/高中（Elementary 24.3%），52.4% 样本量 ≥400，90.5% 未报告 PC 经验（Table 2，PDF p.13）。
- **设计**：元分析。ES 用 Hedges `g` 校正为无偏 `d`（CBT − PPT 均值差 / 合并 SD，正 d = CBT 更高）；固定与随机效应模型；Q 同质性检验（显著则剔除离群研究后重跑）；moderator 用加权多重回归（随机效应）（PDF pp.11–12, 16）。71.4% 原始研究为随机化实验；22/42（>半数）为重复测量设计（同一学生两模式，counterbalancing 或随机分配模式顺序）（PDF p.10）。
- **任务与材料**：阅读成就/能力/诊断测验——national achievement tests、national aptitude/ability/diagnostic tests、state-specific tests；结果变量为阅读总分（88.1% 原始分，11.9% 量表分）；83.3% 为固定线性投递、16.7% CAT；47.6% 单机 PC、35.7% Internet（Table 2，PDF p.13）。
- **变量**：产品分数 = 跨模式阅读总分 ES（d）；moderators = study design、grade level、sample size、type of test、computer delivery method、computer delivery algorithm、computer practice provided、publication type、ethnicity 等。**无过程/行为指标**；缺失信息仅以被排除研究的速度化未作答率形式出现（PDF p.15）。类别编码双人独立完成，编码者间一致率 89%–99%（PDF p.8）。

## 核心发现（按四类主张）

### Class 1 — 可用性/偏好（usability, satisfaction, preference）

- 本文**没有**测量可用性或偏好；仅有二手引用：`Park (2003)` 称从受测者视角 computerized assessment "was easier"；`Wang, Young & Brooks (2004)` 报告对 CBT 的态度总体比 PPT 更积极（"The attitudes expressed by test takers were generally more positive toward CBT than PPT"）。PDF p.4。
- 判定：`PARTIAL` / 二手转述，`ABSTRACT-ONLY` 性质（本文元分析未把偏好作为结果变量）。对审计 Class 1 的贡献：**不关闭**「阅读测评 UI 可用性实证缺位」的 `UNRESOLVED` 状态，仅提示偏好信号方向可能偏 CBT，但无测量含义。

### Class 2 — 行为改变（UI/格式/布局改变可观察行为与过程指标）

- 本文未采集任何行为/过程指标，但明确提出**阅读特异的 CBT 功能假设清单**作为模式差异来源：scrolling text、testlet 形式下 passage 内前后跳题、highlighting a passage、pop-up notes、zooming 等，"might cause difference between test modes"（PDF p.5）。这是作者动机句，**不是测量结果**。
- 论文引述的界面层面模式效应来源：`Mazzeo & Harvey (1988)` multiscreen/graphical/complex displays 导致模式效应；`McKee & Levinson (1990)` screen size、font size、graphics resolution 可能剧烈改变任务性质，使 CBT 与 PPT "no longer measure the same construct"；`Vispoel et al. (1992)` CBT 有无 item review 与 PPT 结果并不必然等价；`Wise & Plake (1989)` 不能 review/revise 对成绩有显著负面影响；`Mueller & Wasser (1977)` item review 是正向应试策略（PDF p.3）。
- 判定：上述均为**引文级假设/转述**，不是本文证据；任何「UI 功能改变阅读行为」主张若以本文为依据属 `OVERSTATED`。对审计用途：为 UIE-06/07 类「UI affordance 会改变行为/可观测性」提供**方向性动机与理论锚**（与本项目双栏滚动 passage + 单题面板的直接对应），但证据强度为零，转述层级标注 `PARTIAL`。

### Class 3 — 仪器信度与缺失（missingness、数据完整性、可比性、数据质量筛查）

- **模式依赖的缺失是本文最强的间接证据**：被排除的 6 个研究（Ito et al. 2004，全部为 Web-based linear tests，CBT:PPT 样本约 3:1）中，CBT "consistently displayed a pattern of steadily increasing percentages of unrecorded responses because of speededness"，且 9%–17% 学生在 CBT 问卷中自报没有足够时间完成全部题目——作者强调这对一般标准化成就测验（power tests，非 speeded tests）"really unusual"（PDF p.15）。即：投递仪器（时间限制/逐题计时/作答捕获方式）可在 K-12 阅读测验中制造**大比例、逐题递增的产品级缺失**，且这种缺失与最大分数效应（d = −.31 至 −.56，CBT 更低）同源。
- **ES 估计方法影响结论**：22/42 重复测量设计未报告组间相关，只能由均值/SD 估计 ES，忽略相关会**高估 ES**；作者自认"the overall result of the calculated ESs that ignore the distinction between these two types of designs can be regarded as the upper bound of the actual ESs"（PDF p.10）。即本元分析的效应量应视为上界。
- **同质性/离群处理改变结论方向**：全样本固定效应显著（`d_w = −.077`，CI [−.094, −.060]，p = .000）→ 剔除 6 个离群后随机效应 `d_w = −.004`（CI [−.031, .023]，p = .782）不再显著；Q(41)=356.54 (p<.01) → Q(35)=54.75 (p=.018)（α=.01 下接受同质）（PDF pp.12, 15）。
- 判定：`SUPPORTED`（缺失-速度化关联为作者明示的排除依据；估计方法上界为作者自述方法局限）。对审计 Class 3：与 UIE-11/12/27 同向，构成 **K-12 阅读语境下「缺失是仪器设计函数」的第一手元分析证据**。

### Class 4 — 学习/构念与 estimand（产品分数、构念等价、模式/格式效应移动分数分布）

- **平均模式效应（核心结果）**：42 个 ES 固定效应加权均值 `d_w = −.077`（95% CI [−.094, −.060]），α=.01 显著（p = .000），方向为 CBT 略低于 PPT；但作者明确按 Cohen (1988) 判定全部 ES "practicably negligible"（<.2 为 negligible）（PDF p.12）。剔除 6 个离群后 36 个同质研究随机效应 `d_w = −.004`（95% CI [−.031, .023]），p = .782，不显著（PDF p.15）。**结论：平均而言投递模式不移动 K-12 阅读分数分布**。
- **单研究层有明显效应**：42 个 ES 中 12 个（28.6%）95% CI 不含零（显著），且被排除的 6 个 Ito 研究全部为 CBT 显著更低（d = −.308, −.562, −.308, −.418, −.388, −.211；Table 3, PDF pp.14–15）。**「均值为零」与「个别仪器（速度化 CBT）可大幅移动分数」并存**。
- **Moderator 分析**（Table 4，PDF p.16，加权回归随机效应，10 预测变量合计解释 ES 方差 33.3%）：
  - 显著：Study design（B = −0.16，Beta = −.49，p < .01）、Sample size（B = −0.13，Beta = −.44，p < .01）、Computer practice provided（B = −0.07，Beta = −.24，p < .01）、Computer delivery algorithm（B = +0.05，Beta = .22，p < .01；linear 固定形式的平均 ES 高于 CAT）。
  - 不显著：Grade level（B = −0.01，Beta = −.10，p = .19）、Type of test（B = −0.04，Beta = −.19，p = .06，**边缘**）、Computer delivery method（B = +0.01，Beta = .05，p = .66）。
  - 摘要/总结同此（PDF p.1, p.17）。注意：文内对负系数含义的表述本身含糊（"studies providing such information tended to have greater ESs"与系数符号方向待编码表确认），审计只取显著/不显著划分与系数符号。
- **框架主张**：引 Kolen & Brennan (1995) —— 影响 CBT 效度的因素很可能 test-specific，因此**任何双模式提供的测验都必须做模式效应分析**；引 Green et al. (1984) —— 只有被证明产出等价测量，CBT 与 PPT 才同等有效；并建议除均值外还应考察 passing rate 与 score distribution 的模式效应（PDF p.17）。作者明言元分析只给总览，"does not mean that comparability studies are not needed in specific circumstances"（PDF p.17）。
- 判定：`SUPPORTED`（在其研究范围内：K-12 阅读、投递模式级、1988–2005 研究）。**限定**："type of test" 是测验类别而非题目格式/反应格式，本元分析对项目/UI 变体层无可提供证据。

## 边界与局限

- **人群**：美国 K-12 学生英语阅读测验；中小学为主（>80% 初高中），90.5% 样本无 PC 经验；结论不可外推到成人、非英语、非阅读科目。
- **时间窗口**：纳入研究 1988–2005；CBT 技术（屏幕、投递方式）与该年代绑定，**对 2020s 现代 web 测评 UI 的外推受限**。
- **设计层局限（作者自述）**：① 重复测量相关缺失导致 ES 上界（PDF p.10）；② 同质性检验采用 α=.01，剔除后 Q(35) p=.018 仅在此 α 下接受同质，若取 α=.05 仍边缘（PDF p.15）；③ 离群剔除标准为 CBT/PPT 样本量差最大，与速度化-缺失理由并置，剔除理由非纯统计（PDF p.15）。
- **分析层局限（审计补充）**：moderator 回归仅 11 项原始研究、10 个预测变量（R²=33.3%），功效与多重预测过拟合风险文中未讨论；type of test p=.06 属边缘，摘要称其「不影响」有弱化之嫌。
- **层级边界**：这是**投递模式级（paper vs computer）**证据，不是 within-mode UI 变体证据；无任何过程/行为指标；无题目格式 moderator。任何「题目格式/UI 布局不影响分数」的引用都是 `OVERSTATED`。
- **方向性张力**：本文平均方向为 CBT 略低（主要由速度化离群研究驱动）；与 METHOD-012（ACT 2019–2020，online reading > paper，d=.16–.22）方向相反；审计不得据此断言任何方向性模式主张。

## 对审计的用途

### 既有 UIE 条目与待决问题的影响

- **直接解决审计 Limitations 的 queue 项**（`ui-instrument-effects-evidence-audit.md` L186：「Wang et al. 2008 … must not be asserted in either direction until acquired」）：现已获取全文，元数据级「small/null mean differences」**确认**，但需以「平均为零 + 异质 + 缺失驱动离群」三件套替换简单表述（本笔记核心发现）。
- **限定 UIE-27**（METHOD-012，ACT online > paper）：K-12 元分析平均为 null 且个别方向相反，**投递模式的分数方向不可一般化**；两者共同支撑的只有「投递仪器可以移动分数分布/缺失」这一存在性主张。
- **支持 UIE-26**（METHOD-011 综述）：投递机制变量（linear vs CAT、practice availability）确实调节模式效应，与 TME 来源分类一致。
- **扩充 Class 3 缺失证据链**（UIE-11/12/27）：新增 K-12 阅读语境「速度化 → 逐题未作答递增 → 最大分数效应」的直接元分析证据。
- **Class 1 缺口不变**：偏好信号仅二手，`UNRESOLVED` 维持。
- **Class 2 缺口不变**：本文无过程数据；UI affordance 清单仅假设，`PROJECT-INFERENCE` 只能作为动机引用。

### 建议的新 UIE 条目草稿

- **UIE-31（draft）** Claim: K-12 阅读测验投递模式元分析：平均效应为 null（排除速度化离群后 `d_w = −.004`，p = .782；全样本固定效应 −.077 亦属 Cohen「实际可忽略」）；单研究层 28.6% 显著，异质性显著（Q(41)=356.54, p<.01）。Pages: PDF 12, 15, 17. Verdict: `SUPPORTED`（在其研究范围内）。Boundary: K-12 英语阅读，1988–2005 研究，paper vs computer 投递模式级；不覆盖 within-mode UI 变体；重复测量相关缺失使 ES 为上界（PDF p.10）。
- **UIE-32（draft）** Claim: 模式诱导缺失与最大分数效应同源：6 个速度化 CBT 研究「逐项未作答率递增」，9%–17% 学生自报时间不足，且这 6 个研究呈全部 CBT 更低的最大效应（d = −.31 至 −.56）；缺失是仪器（计时/投递）设计函数而非随机噪声。Pages: PDF 15. Verdict: `SUPPORTED`。Boundary: 同 UIE-31；缺失率为作者转述的 CBT 调查自报，非逐题日志测量。
- **UIE-33（draft）** Claim: 模式效应 moderator：study design（Beta −.49）、sample size（−.44）、computer practice provided（−.24）、computer delivery algorithm（+.22，linear > CAT）显著预测 ES；grade level（p=.19）、type of test（p=.06，边缘）、computer delivery method（p=.66）不显著。Pages: PDF 16. Verdict: `SUPPORTED` + 功效警示（11 原始研究/10 预测变量）。Boundary: "type of test" 为测验类别，非题目格式/反应格式；不得外推为「题目类型不调节」。
- **UIE-34（draft）** Claim（框架）: 模式效应 test-specific：任何双模式提供的测验都必须单独做可比性/等值分析（引 Kolen & Brennan）；元分析总览不豁免逐测验义务；passing rate 与分数分布的模式效应应单列考察。Pages: PDF 17. Verdict: `SUPPORTED` 作为作者框架主张。Boundary: 规范性建议，非经验效应；与 METHOD-012 的「以等值而非等价声明为缓解」立场一致。
