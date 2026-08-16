# METHOD-034 — Ulitzsch et al. (2024) 量表格式 × careless/insufficient effort responding 全文提取笔记

## 结论速览（中文）

- 这是一篇以「数据质量筛查」为核心的方法学论文：作者开发了多源 C/IER 指标（response-pattern multiple-hurdle × screen-time mixture decomposition 的乘积），应用于 PISA 2022 field trial 背景问卷（N=206,153，75 国）。
- 对审计最重要的两类结果：(1) **单源行为通道的 C/IER 筛查可严重过度标记**——long-string 单指标标 64% 受访者而多源指标仅 6%（PDF p.19–20），纯时间混合分解标 85% 而多源仅 4%（PDF p.20）；阈值从 .01 放宽到 .05 使单指标中位污染率 .05→.08，而多源指标几乎不变（PDF p.18）。这直接支撑 Class 3「过程数据可用于数据质量筛查，但单通道指标不可当作真值」。(2) **两种量表格式操纵对 C/IER 发生为零效应**（agreement↔frequency 双方 .08 [.04; .11]；abstract↔approximate 标签 .05 vs .06），且作者明确声明「零效应 ≠ 数据质量等价」——construct validity 与 response styles 等其他质量威胁仍可能被格式移动（PDF p.27）。
- 未决/反向证据：多源指标仍有假阳性残留（当时间与模式两个成分给出相同错误标签时，PDF p.24）；「要求同意」可能过度保守（PDF p.26）；少数国家/语种组存在显著方向差异，作者无法排除 culture-/language-specific 效应（PDF p.23, p.27）。

---

## 头部

- **Source ID**：`METHOD-034`
- **本地路径**：`sources/library/papers/methods/2024_Ulitzsch_ScaleFormatCIER.pdf`（PDF 30 页；物理页 = 打印页，无封面偏移）
- **完整书目**：Ulitzsch, E., Buchholz, J., Shin, H. J., Bertling, J., & Lüdtke, O. (2024). Using a novel multiple-source indicator to investigate the effect of scale format on careless and insufficient effort responding in a large-scale survey experiment. *Large-scale Assessments in Education*, 12, Article 18. https://doi.org/10.1186/s40536-024-00205-y. CC BY 4.0（© The Author(s) 2024; SpringerOpen）。
- **与 catalog 核对**：`sources/catalog.yaml` 的 `METHOD-034` 条目（title/authors/year/venue/doi/license/sha256）与 PDF 首页（p.1）一致，无出入。catalog 中 `Hyo J. Shin` 为 PDF 首页 `Hyo Jeong Shin` 的缩写，属同一人。
- **提取日期**：2026-08-15；全文 `pdftotext -layout` 逐页通读（p.1–30），无 `ABSTRACT-ONLY` 条目。

---

## 研究概览

- **研究问题**（p.4, p.8–9）：
  1. 开发一个要求多行为源「一致」才判定 C/IER 的多源指标 q（Curran 2016 multiple-hurdle × Ulitzsch et al. 2024 screen-time mixture decomposition 的乘积，p.12）；
  2. 用 q 复现两个公认外部效标关联：与 self-reported effort 的负相关、位置效应（p.8）；
  3. 利用 PISA 2022 field trial 内嵌的两组大规模量表格式实验，检验对 C/IER 的影响：**E1** agreement ↔ frequency 格式；**E2** frequency 量表的 abstract ↔ approximate 标签（p.9）。
- **样本**：PISA 2022 field trial 学生背景问卷（计算机管理），206,153 名学生、75 个国家和经济体，组内样本量 309–7,140（p.9）。双 booklet 设计；较长的量表用 incomplete block design（每个学生只拿到部分题项）（p.9）。
- **设计**：内嵌在 PISA 2022 field trial 的**大规模调查实验**（booklet 级操纵；非个体随机、无对照组个体级随机化——两组实验分别由 booklet 1 的 10 个量表与 booklet 2 的 6 个量表承载，p.9–10）。非随机对照试验意义上的随机实验，也不是相关设计。
- **任务与材料**：背景问卷中 closed response format、≥2 选项、≥3 题、全部组共有的量表（booklet 1: 31 个；booklet 2: 33 个）；**每个量表单独一屏**（p.9）。Booklet 1：10 个社会情感量表（如 trust/assertiveness），同一陈述配 5 点 agreement 标签（"strongly disagree"…"strongly agree"）或 frequency 标签（"never or almost never"…"all or almost all of the time"）（p.9–10）。Booklet 2：6 个数学内容接触/教师行为量表，配 abstract 锚点（"never", "rarely", "sometimes", "frequently"）或 approximate/concrete 锚点（"never or almost never", "about once or twice a year", "about once or twice a month", "about once or twice a week", "every day or almost every day"）（p.10）。
- **变量**：
  - 产品分数：无能力/构念分数；唯一效标为 self-reported effort（PISA 问卷第 3 题，10 点量表，p.9）。
  - 过程指标：每题几何平均屏时 `t_is`（p.11–12）；response-pattern 指标 I1（全漏答）、I2（long-string，全选同一选项）、I3（Mahalanobis 距离 > χ² 99 分位）（p.11）；混合分解后验 C/IER 类概率 `π^C/IER`（p.12）；多源指标 `q = dis_MH · π^C/IER`（p.12）。
  - 缺失指标：I1（全量缺答比例）为唯一直接缺失类指标；屏时分解按组单独进行以规避语种时间差（p.12）。
- **分析**：scale-by-group 层面 C/IER 比例；组间格式差异 z 检验（.05 水平，p.14）；位置效应用贝叶斯层级 Beta 回归（random intercept per group；Stan/rstan；p.13–14）。

---

## 核心发现（按四类主张分组）

> 页码均为 PDF 物理页。

### Class 3 — 仪器信度与缺失（数据质量筛查；本文主战场）

- **C3-1 | 单源 C/IER 指标之间的识别率差异巨大，且相互相关低——同一数据用不同指标得到不同的污染率**：成分指标（I1/I2/I3/π^C/IER）的 scale-by-group 中位 C/IER 比例：booklet 1 为 .04–.11，booklet 2 为 .04–.20；多源 q 中位 .05 [.03; .09]（两 booklet 相同）（p.15–16, Table 1）。指标间相关多为近零或负（如 I1×I2 r = −.07/−.11），说明**不同指标标记了不同的人**（p.15–16, Table 1）。
  - 原文（p.15）："Median C/IER proportions implied by q's constituting components ranged from .04 to .11 in booklet 1 and from .04 to .20 in booklet 2. Low correlations between the majority of dMH's constituting components suggest that different response-pattern-based indicators flagged different respondents."
- **C3-2 | 纯响应模式通道可严重过度标记：long-string 单指标标 64% vs 多源 6%**：Fig. 5a 示例中，仅凭 long-string 指标，64% 的受访者被标为 C/IER；但其中大量是屏时正常者（被推断为误标）。多源 q 只把「短屏时 + 异常模式」者计为 C/IER，给出 6% 的污染率（p.19–20）。
  - 原文（p.19–20）："Based on the long-string index only, 64% of the respondents were flagged. The proposed indicator, however, considered information from the long-string index only for respondents with aberrantly short screen times and indicated a much lower C/IER rate of 6%."
- **C3-3 | 纯时间通道可严重过度标记：混合分解标 85% vs 多源 4%**：Fig. 5b 示例中，单峰但重尾的屏时分布被分解为两个正态成分，低均值成分被标为 C/IER（85%）；但对应响应模式几乎没有异常，多源 q 给 4%（p.20）。
  - 原文（p.20）："Fig. 5b depicts an example where a unimodal but heavy-tailed screen time distribution was decomposed into two normal distributions and the component with the slightly lower mean was labeled as C/IER. … The mixture decomposition indicated a C/IER rate of 85%. The proposed indicator was capable to alleviate the presumably artefactual conclusions on C/IER, yielding a much lower C/IER rate of 4%."
- **C3-4 | 单指标对阈值高度敏感，多源同意可对冲阈值设定**：Mahalanobis 阈值从 .01（I3）放宽到 .05（I3L）级别时，单指标中位 C/IER 比例从 .05 [.02; .08] 升到 .08 [.04; .14]；而 q 与 qL 均为 .04 且比例间相关 .99——多源指标对成分阈值不敏感（p.18）。
  - 原文（p.18）："I3 and I3L identified median C/IER proportions across all groups of .05 … and .08 …, respectively. q and qL, in contrast, were not heavily impacted by these different choices of threshold settings … both yielding a median C/IER proportion of .04 [.08; .11] and exhibiting a correlation of C/IER proportions of .99."（注：原文此处 IQR [.08; .11] 与中位 .04 矛盾，疑为排印错误；不影响相关 .99 与稳健性结论。）
- **C3-5 | 反直觉高污染案例表明「快而认真」的受访者会被行为筛查误标**：ST266（5 题 yes/no，校园安全）在位置 49 的 q 污染率 .86；82% 受访者 long-string 全选同一选项，其中 99% 是「没有经历过任何安全事件」的认真作答者；较快模式成分均值 1.64 s，仍高于 booklet 1 其他 C/IER 成分平均（0.98 s，IQR [0.72; 1.33]）——即被标为 careless 的成分耗时相对并不低，作者推断该成分捕获的是 C/IER 之外的行为（p.20–21）。
  - 原文（p.20–21）："Closer inspection of response patterns failing on the long-string index revealed that 99% of these went back to respondents stating that they did not encounter any of the safety-related phenomena. … The mean (corresponding to 1.64 s) of the presumed C/IER component was still relatively high compared to the means … (corresponding, on average, to 0.98 s; interquartile range: [0.72; 1.33]) for all mixture-decomposition-implied C/IER components in booklet 1."
- **C3-6 | 缺失（全漏答）是多源判定中占主导的行为通道**：I1（漏答全部题项）与 q 的相关最强（booklet 1/2 分别为 .83/.80），π^C/IER 与 q 相关 .99/.98；而 I2、I3 与 q 相关近零且 IQR 很宽（p.16, Table 1）。结论：被识别为 C/IER 的受访者往往全漏答，且全漏答者屏时后验概率也高；I2/I3 标出的模式异常往往没有伴随异常短屏时，故对 q 贡献有限（p.16–17）。
  - 原文（p.16–17）："respondents identified as displaying C/IER oftentimes tended to omit all items administered"；"the informativeness of single behavioral indicators regarding C/IER may be scale-dependent. For instance, the long-string index's informativeness on C/IER can be assumed to vary as a function of, among others, scale length, item homogeneity, and whether or not all items are worded in the same direction."
- **C3-7 | 位置效应：污染率随仪器内部位置单调上升**：贝叶斯层级 Beta 回归，screen position 系数 booklet 1 β = 0.02 [0.02; 0.02]、booklet 2 β = 0.01 [0.01; 0.02]（p.22, Table 2）；booklet 1 首位置（44）预期污染率 .05 → 末位置（89）.10；booklet 2 首（37）.05 → 末（82）.08（p.21）。组间基线差异大（随机截距 SD .59/.52，p.22, Table 2）。
  - 原文（p.21）："screen position was positively related to scale-by-group-level C/IER proportions. … expected average C/IER proportions of .05 and .10 for the first (44) and last (89) scale position considered."
- **C3-8 | 多源指标并不免疫假阳性，且「要求一致」可能过度保守**：(a) 当时间混合分解与至少一个 multiple-hurdle 成分给出**相同**的错误标签时，q 仍有假阳性（p.24）；(b) 若短屏时确实来自 C/IER 但模式指标未检出，要求一致会漏检（p.26）。作者建议多指标 + 较宽松阈值，并要求做 specification curve analysis 敏感性检验（p.26）。
  - 原文（p.26）："if the short screen time indeed goes back to C/IER, but the employed indicator-threshold combinations used for dMH simply do not detect the resultant aberrant response pattern, requiring agreement between response patterns and timing data may be overly cautious."
- **C3-9 | 在线调查平台数据质量背景（作者引证）**：作者引 Douglas et al. (2023) 报告常用在线平台高质量数据比例仅 68%–26%，据此论证多源筛查工具的用途（p.25）。此为引证层级，非本研究直接测量。

### Class 2 — 行为改变（量表格式/标签对作答行为的效应）

- **C2-1 | agreement ↔ frequency 格式对 C/IER 行为零效应（无系统方向）**：q-implied C/IER 比例双方格式均为 .08 [.04; .11]（p.22）；25% 的 scale-by-group 对差异显著，其中 45%（即全部对的 11%）方向为 agreement 更高——没有一致优势方（p.22）。组级中位差异围绕 0 分布，IQR [−0.02; 0.01]，跨组总体稳定（p.22–23）；仅少数组差异明显（范围 [−0.11; 0.05]，p.23）。
  - 原文（p.22）："Overall, the multiple-source indicator q indicated no effect of scale format on the occurrence of C/IER; q implied C/IER proportions of .08 [.04; .11] for both agreement and frequency scales."
- **C2-2 | abstract ↔ approximate frequency 标签对 C/IER 行为零效应**：q-implied C/IER 比例 abstract .05 [.03; .08] vs approximate .06 [.03; .10]（p.23）；38% 的 450 对差异显著，其中 65%（112 对）approximate 更高——但差异围绕 −0.01，IQR [−0.03; 0.01]（p.23）；少数组双向均有显著差异（范围 [−0.17; 0.08]），作者无法排除 culture-/language-specific 效应（p.23, p.27）。
  - 原文（p.23）："Differences were distributed around −0.01, and variation was somewhat larger than for our comparisons of agreement and frequency formats (interquartile range: [−0.03; 0.01])."
- **C2-3 | 仪器长度/位置驱动的行为漂移是稳健可复现的**：位置效应是作者成功复现的已知效应，且 q 与 self-reported effort 的负相关（booklet 1 中位 r = −.14 [−.17; −.09]；booklet 2 r = −.13 [−.17; −.09]）（p.21）与既有行为指标研究一致（p.21, p.24）。
  - 原文（p.21）："We observed small negative correlations between self-reported effort and average values on q. … the median within-group correlation was −.14 (interquartile range: [−.17; −.09])."
- **操作化边界（重要）**：两组操纵都是**标签措辞层面**的：作者明示"the investigated changes in scale format were relatively subtle and only concerned wording, while the overall mode of responding set by the Likert-type scales was left unchanged"（p.27）。因此零效应不能外推到改变反应模式（如 forced choice、drag-and-drop、选项数变化）的格式变化（p.27）。

### Class 4 — 学习/构念与 estimand

- **C4-1 | 零效应 ≠ 数据质量等价（作者明示，反过度解读）**：C/IER 只是数据质量威胁之一；格式变化完全可能经其他机制（construct validity、response styles 等偏差）移动分数分布。作者据此建议格式决策以**构念/实质考虑**为主导，而非 C/IER 考量（p.24–25, p.27）。
  - 原文（p.27）："the minor effects of the investigated scale characteristics on C/IER do not imply that the investigated scale formats provide data of comparable quality. C/IER is by far not the only threat to data quality, and it may well be that other aspects (e.g., construct validity or the occurrence of other biases such as response styles) are impacted by the investigated changes in scale characteristics."
  - 原文（p.24–25）："we recommend that researchers' decision on scale format should predominantly be guided by substantive consideration … because overall, the effects of this decision on C/IER occurrence are negligible."
- **C4-2 | 格式→response styles 的机制（引证层级）**：作者综述指出 response styles（mid-point、extreme、acquiescent）受评分量表格式影响（Weijters et al. 2010; Deng & Bolt 2016; Moors et al. 2014; Kieruj & Moors 2013; Hui & Triandis 1989; Henninger & Meiser 2020）（p.8）。即格式移动分数分布是有文献支持的机制，只是本研究未在 C/IER 通道检出。此为文献引证，非本地全文核验（`PARTIAL` 层级）。
  - 原文（p.8）："from the response bias literature on mid-point, extreme, and acquiescent response styles, it is known that the extent to which scales and items are affected by response styles is related to rating scale format."
- **C4-3 | 未调整的 C/IER 污染会移动群体参数**：作者引证指出任其污染会使相关与组均值偏倚（DeSimone et al. 2018; Woods 2006 等），而**排除有效数据也会系统性地排除特定亚组**（如均匀高分者），造成新的偏倚（p.2–3, 脚注 1）。这为「数据质量筛查决策本身会影响 estimand」提供了框架性论述（引证层级）。
  - 原文（p.2–3）："one can easily imagine scenarios where the exclusion of presumed C/IE responses leads to the systematic exclusion of specific sub-groups from the data … This, in turn, can result in bias of parameters of interest, e.g., correlation coefficients or group means."

### Class 1 — 可用性/偏好

- **C1-1 | 本研究未测可用性/偏好**：无满意、偏好、易用性数据。唯一相关的是引 Robie et al. (2022)（response option order 对 psychometric properties 与 **reactions** 的影响）作为量表格式×C/IER 研究的近期例外（p.8）——reactions 属 Class 1 但为引证层级。Class 1 在本研究中 `UNRESOLVED`。

---

## 边界与局限

- **人群/语种边界**：PISA 2022 field trial 学生背景问卷，75 国/经济体，15 岁学生。作者明确提示少数组存在双向显著差异，culture-/language-specific 效应未决（p.23, p.27）。屏时分解按组进行以规避语种时间差异（p.12），但语种×格式交互仍是开放问题。
- **任务边界**：背景问卷 Likert 型量表（每题一屏、每屏一量表），**非阅读作答 UI、非能力测试**；无产品分数。操纵仅限标签措辞，作答模式（Likert 反应格式）未变（p.27）。零效应不能外推到反应模式级变化（forced choice、drag-and-drop、选项数变化等，作者自己点名，p.27）。
- **指标边界**：多源 q 的「有效性」证据是效标复现（effort 相关、位置效应）+ 示例性演示，作者明示**这不能证明 q 比成分指标更有效**（p.26）："from these illustrations it cannot be concluded that the proposed indicator generally provides a more valid measure of C/IER than its constituting components." 作者呼吁实验性 C/IER 操纵提供 ground truth（p.26–27）。
- **作者自陈局限**：(a) q 非零错误率，同源假阳性残留（p.24, p.26）；(b) 成分选择与阈值仍是主观决定，建议 specification curve analysis（p.26）；(c) 混合分解的分布假设（log 屏时正态成分、恰一个 C/IER 成分）被违反时结论严重失真（p.6–7, p.20 示例）；(d) 屏时层面无法区分「快而确定」与 careless（distance-difficulty hypothesis，p.7）；(e) 位置代理变量因 routing 而不精确（脚注 6，p.13）。
- **不可外推处**：C3-2/C3-3/C3-5 的百分比（64%/6%、85%/4%、.86）是**示例性 scale-by-group 个案**，不是系统性模拟或全数据率；不可当作筛查误判率的通用估计。C/IER 污染率（.04–.20 中位）是 PISA field trial 背景问卷的，不是阅读能力测验的。

---

## 对审计的用途

### 支持/限定既有条目

- **强化 UIE-22（`METHOD-010` cursor paradata 筛查）**：本文把「过程数据可做 C/IER/数据质量筛查」从 cursor 通道扩展到 **screen-time + response-pattern 双源**，并给出该用途的失败模式：单通道（无论时间还是模式）都会过度标记（C3-2/C3-3），阈值敏感（C3-4），「快而认真」会被误标（C3-5）。对审计的含义：指针/时间流适合做**数据质量/投入度筛查层**（`E6` rapid-guessing 过滤器类似角色），但任何单通道筛查的绝对数值都不构成行为真值。
- **限定 UIE-11/UIE-13（缺失与信号缺省是设计/行为依赖）**：C3-7 证明即使在同一仪器内，污染/缺失率也是**仪器位置设计**的函数（.05→.10）；C3-5/C3-6 证明缺失（全漏答）与快速作答的语义因题目内容/格式而异——为「缺失率不可跨仪器位置/跨格式直接比较」补充了大规模数据点。
- **限定 UIE-01/UIE-02（`B7` 反应格式效应）**：本文显示「格式」效应具有**变化粒度边界**——标签措辞级格式变化在 N=206,153 中零效应，而 `B7` 的反应模式级变化（D&D vs dropdown vs click-on-grid）显著移动行为与产品。两者不矛盾：支持「效应随格式变化类型与任务类型而变」的判断，反对把任何格式差异一律视为 C/IER/行为差异源。注意 `B7` 是作答 UI（阅读任务），本文是问卷量表，任务边界仍分离。
- **补充 Class 3 空白区**：审计 Class 3 的现有证据集中在缺失率与过程通道完整性（UIE-11..15）；本文新增了「响应有效性筛查」的第二个本地全文证据（继 `METHOD-010`/UIE-22），并把「筛查指标本身的误判率/阈值敏感性」作为可钉页证据纳入。

### 建议的新 UIE 条目草稿（均待主审计整合定稿）

| 草案 ID | Claim（中文） | 主要证据（PDF 页） | 暂定 verdict | Scope boundary |
| --- | --- | --- | --- | --- |
| UIE-31（Class 2） | 标签措辞级量表格式操纵（agreement↔frequency；abstract↔approximate frequency labels）在 PISA 2022 field trial 大规模调查实验中对 C/IER 行为零效应：q-implied C/IER 双方 .08 [.04; .11]；组级差异围绕 0（IQR [−0.02; 0.01] / [−0.03; 0.01]）。 | p.22–23 | `SUPPORTED`（零效应；null result 不升级为「格式无效应」普遍结论） | 15 岁学生背景问卷、Likert 型标签措辞变化、作答模式不变；不覆盖反应模式级格式变化。 |
| UIE-32（Class 3） | 单源行为通道的 C/IER 筛查可严重过度标记且阈值敏感：long-string 单指标 64% vs 多源 6%；纯屏时混合分解 85% vs 多源 4%；Mahalanobis 阈值 .01→.05 使单指标中位污染率 .05→.08，而多源指标不变（相关 .99）；「快而认真」的 yes/no 作答者可被误标（案例污染率 .86）。 | p.18, p.19–21 | `SUPPORTED`（本研究的示例性演示；百分比是 scale-by-group 个案，非通用误判率） | PISA 2022 field trial 背景问卷，scale-by-group 层面；不量化阅读作答 UI 的筛查误判率。 |
| UIE-33（Class 3） | 仪器内位置效应：C/IER 污染率随问卷位置单调上升（Beta 回归位置系数 0.02/0.01；预期污染率首 .05 → 末 .10/.08），组间基线差异大（随机截距 SD .59/.52）——污染率/缺失率是仪器长度与位置设计的函数。 | p.21–22（Table 2） | `SUPPORTED` | 长问卷背景量表；位置代理因 routing 不精确（脚注 6）。 |
| UIE-34（Class 4） | 格式零效应 ≠ 数据质量等价：作者明示 C/IER 非唯一质量威胁，construct validity 与 response styles 等可能被格式移动；格式→response styles 机制有文献支持（Weijters 2010 等引证）；建议格式决策以构念考虑为主导。 | p.8, p.24–25, p.27 | `PARTIAL`（本研究零效应为直接证据；response-styles 迁移为引证层级） | 问卷量表背景；对阅读作答 UI 为 `PROJECT-INFERENCE`。 |

---

## 提取验证记录

- `scripts/bootstrap`：`OK`（sources=ready, skills=ready, hooks=.githooks；sources doctor 110 项通过）。
- 全文通读：`pdftotext -layout` 30 页全部读取（p.1–30），所有页码钉为 PDF 物理页；无 `ABSTRACT-ONLY` 条目。
- 页码核对：Table 1（p.16）、Table 2（p.22）、Fig. 3–8（p.15/18/19/21/22/23）与正文引用一致。
- 已知文本异常：p.18 中 q/qL 的 IQR "[.08; .11]" 与中位 ".04" 矛盾，疑为原文排印错误，笔记按原文引用并标注，未影响结论（相关 .99 与稳健性论点不依赖该区间）。
