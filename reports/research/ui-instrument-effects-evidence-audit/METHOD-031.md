# Evidence Extraction Notes — METHOD-031

Source ID: `METHOD-031`
Local path: `sources/library/papers/methods/2024_Witmer_ExtendedTimeScoreComparability.pdf`

## 书目核对（catalog vs PDF 首页）

- catalog 条目：Witmer, S. E., & Marinho, N. (2024). Extended time test accommodations: Does use correspond to score comparability for students with disabilities deemed in need? *Psychology in the Schools*, 61(11), 4175–4188. DOI: 10.1002/pits.23275. License: CC BY (© 2024 The Authors; Wiley Periodicals LLC). `REDISTRIBUTION_ALLOWED`。
- PDF 首页核对：标题、venue（页脚 4175–4188）、年份、DOI、CC BY 声明一致。
- **不一致处（不改 catalog，仅标注）**：catalog 第二作者名为 "Nicole Marinho"，PDF 首页（PDF p.1）署名为 **"Nathalie Marinho"**。以 PDF 首页为准，建议综合时修正 catalog 作者拼写。

Page locators 一律为 PDF 物理页（本文件 14 页，PDF p.N = 印刷页 N+4174；页眉映射已逐页验证：p.1=4175 标题页，p.2=4176 引言，p.5=4179，p.6=4180，p.7=4181，p.8=4182，p.9=4183，p.10=4184，p.11=4185，p.12=4186，p.13=4187，p.14=4188 参考文献）。

---

## 研究概览

- **研究问题**（PDF p.5）：对 IEP 团队认定为需要延长时间的 SWD，(RQ1) 需要延长但未实际使用 vs 无残疾参考组，是否存在 score comparability 缺失（以 substantial DIF 表示）？(RQ2) 使用了延长 vs 参考组，是否存在 score comparability（limited DIF）？H1：未使用组应有 substantial DIF（需要未满足）；H2：使用组应 limited DIF（需要被满足）。作者自标为"首项在 score comparability 检验中纳入 accommodation implementation fidelity（实际使用）的研究"（PDF p.9）。
- **设计**：extant data 非实验研究（no experimental manipulation，作者在 Limitations 明示，PDF p.11）。两组独立 DIF 比较（focal vs reference），分析工具为 Poly-SIBTEST（Chang et al. 1996；R 实现 Weese et al. 2023，PDF p.6）。两轮分析：第一轮以全部其余 14 项为匹配子测试探测 DIF，显著 DIF 项自匹配子测试移除后第二轮再测全部 15 项（PDF p.6）。
- **数据**：2017 NAEP 八年级数学一个数字化管理的 15 题块（block；NAEP 全程为两个 block，本 block 非全卷；restricted use license，NCES，PDF p.5）。题型含 MC 单选/多选、matching、zone-multiple select、grid items；25 分原始分（7 题二分 + 7 题 0–2 + 1 题 0–4，PDF p.6）。block 目标时长 30 min，延长时间资格者上限 90 min（PDF p.6）。
- **样本与分组**（PDF p.6, 表 1 PDF p.7；IES 要求样本量四舍五入到 10）：焦点组 1 = 有资格未使用（duration ≤30 min）N=1010；焦点组 2 = 有资格且使用（duration >30 min）N=5001；参考组 = 无残疾、正常时限内完成（≤30 min）N=1010（单一随机抽样）。排除英语学习者。分析样本内未使用比例 ≈16.8%（1010/6011）。
- **"使用"的操作化**（PDF p.6）：*"we coded students who were deemed eligible for extended time as either using (i.e., test duration >30 min) or not using (i.e., test duration ≤ 30 min) extended time"* —— 以 block 时长截断 30 min 二分。
- **DIF 判定阈值**（PDF p.6）：第一轮自匹配子测试移除用 standardized effect size 阈值 "10" + p<.003（15 项 Bonferroni 近似）；第二轮解释用 Weese et al. (2023) 阈值 "164 for moderate DIF and 241 for large DIF" + p<.003。**阈值文字疑似排版丢失小数位**（详见边界与局限）。
- **变量**：产品分数 = 15 题 item 参数（DIF 分析）+ block 原始分（表 1）；过程指标 = test duration（仅用于二分"使用/未使用"）；缺失指标 = 无独立缺失分析，但"未使用住宿"构成一种使用缺失（见 Class 3）。

---

## 核心发现（按四类主张分组）

### Class 4 — 学习/构念与 estimand（本论文核心贡献）

- **C4-1 时间条件住宿（延长时间可用性）未移动 item-level 测量参数——使用与未使用两组相对参考组的 DIF 均极少**：RQ1 比较（no-use vs reference）第一轮 15 项**无一项**显著 DIF，无需第二轮 → *"There correspondingly did not appear to be score comparability concerns between these groups"*（PDF p.8）。RQ2 比较（use vs reference）第一轮识别 1 项（item 12，favors focal group），第二轮（14 项 DIF-free 匹配子测试）确认同一项，标准化效应量 δ=−0.226，作者按 Weese 阈值定性 *"only small DIF"*（PDF p.8, 表 3 PDF p.9, 表 4 PDF p.10）；作者并称 use 组相对 no-use 组 *"did indicate slightly less comparability"*（PDF p.8）。**SUPPORTED within study**。摘要（PDF p.1）：*"Score comparability was evident regardless of whether or not the students actually used extended time, begging the question of whether, for many SWD, extended time is truly necessary for score comparability to be achieved."*
- **C4-2 H1 被否定、H2 被支持，但两组的实质结论相同（DIF 都极少）**：*"Our hypothesis that substantial DIF would be present for the non‐use group was not supported, but our hypothesis that limited DIF would be evident for the used extended time group was supported"*（PDF p.9）。作者由此推断很多被认定需要延长的学生"不需要"它即可获得分数可比性 → over-recommendation 议题（PDF p.9 "begs the question"，PDF p.12 "school teams may be over‐recommending extended time"）。**注意**：这是讨论级推断（作者用 "begs the question"，非直接测量），不采用为事实前提。
- **C4-3 边际分数分布确实大幅移动，但这是组间能力差异而非住宿效应**：三组 block 均分 5.3 (3.5) / 6.7 (3.8) / 9.6 (4.7)（/25），ANOVA 显著且 Bonferroni 事后两两均 p<.001（PDF p.7 表 1 脚注）；used 组显著高于 no-use 组（6.7 vs 5.3）。作者不作因果解读（非实验）；DIF 检验的是"以匹配子测试条件化后的 item 表现"——marginal distribution shift 与 item-level 测量不等价是正交的两个事实（方法论区分，见 UIE-34 草稿）。
- **C4-4 对"速度是否构念"提供经验锚点（间接）**：在 NAEP 八年级数学语境，时间条件变化（30→90 min 可用、使用与否）未引入 item 层面 construct-irrelevant variance（DIF 层面），与该测试"速度非核心构念"相容；但作者未直接测量速度在构念中的作用，且外推受限（数学、低 stakes、单 block、非实验）。

### Class 3 — 仪器信度与缺失

- **C3-1 住宿"使用"的过程数据操作化粗糙：duration 二分只能区分超时与否，不能区分额外时间如何使用**：作者自认编码仅基于 block duration（PDF p.6），并在 4.2 明确未来方向：用 process data 考察 *"item review and checking, consistent use across the test or targeted use on particularly difficult or unique items"*、其他住宿（text-to-speech）激活（PDF p.11）——即"使用时长"与"如何使用额外时间"是不同构念。**SUPPORTED as authors' operationalization & self-declared limit**。
- **C3-2 住宿"使用缺失"是自愿的、随个体与情境变化的：分析样本内约 17%（1010/6011）有资格者未实际使用**；作者强调住宿使用依赖 *"student initiation and agency"*、学生可自由选择用或不用（PDF p.3）；并引 prior work 称大规模 CBT 中多种住宿实际使用率低（Lee et al. 2021; Witmer & Bouck 2023; Witmer et al. 2023——**secondhand**，PDF p.5）。**PARTIAL**：17% 为本文样本内选择数据（SUPPORTED），"低使用率普遍"为引证层级（PARTIAL）。
- **C3-3 未使用 ≠ 住宿无效（反向保留，防误读使用率）**：*"just because a student didn't use extended time doesn't necessarily mean that it wouldn't have been helpful for them to use it; it could be the case that students who didn't use it were simply not knowledgeable or motivated enough"*（PDF p.10）——使用缺失可能反映知情/动机，不直接反映需要或工具无效。
- **C3-4 使用率/缺失率是 stakes 依赖的（作者声明，不可外推）**：NAEP 是低 stakes（*"performance and associated scores are not used to make decisions that directly affect them"*），*"Results may be different on tests in which students may be more motivated to perform well"*（引 DeMars 2000；PDF p.10）。另引 Lee et al. (2021)：住宿使用随测试进程下降（*"reduced use of accommodations over the course of a test"*，PDF p.10）——使用缺失在仪器内随位置/进程变化。
- **C3-5 技术性可比性约束（作者 Limitations）**：无独立匹配子测试（用被测项互配）；三组能力分布差异大，可能影响 DIF 识别（引 Buzick & Stone 2011）；参考组为单一随机样本；未按残疾类别分拆（样本量不允许）（PDF p.11）。

### Class 2 — 行为改变

- **C2-1 无 UI/格式操纵，无直接行为改变证据**：本研究不操纵任何 UI 或格式维度；"使用/未使用延长"是学生自愿行为分类，不是仪器操纵。**不产生直接 Class 2 条目**。
- **C2-2 相关方向观察（非因果）**：used 组均分高于 no-use 组（6.7 vs 5.3，p<.001）——"实际用完/超出目标时长"的行为与更高分数共存，但作者明示非实验（PDF p.11），更可能反映能力/动机选择效应，**不得用作"延长时间提高分数"证据**。
- **C2-3 机制性讨论（引用层级，非本文数据）**：低动机学生可能 rapid guessing（Los et al. 2022）、焦虑学生可能用额外时间做 perseverative checking、有效使用额外时间需要 self-regulation（Baird et al. 2009）（PDF pp.3–4）——"时间条件如何被学生使用"是学生特征与仪器条件共同决定的，本文数据不检验这些机制。**secondhand/作者讨论**。

### Class 1 — 可用性/偏好

- **无贡献**：论文无任何可用性、满意度、偏好或感知易用性测量。唯一相关点是"提供但未使用 ≠ 不可用"的反向保留（PDF p.10，见 C3-3）与"住宿使用需要学生主动发起"（PDF p.3）——均为使用行为视角，不是偏好证据。**不产生 Class 1 条目**。

---

## 边界与局限

- **人群/测试边界**：美国 2017 NAEP 八年级数学（SWD 中 IEP 认定为需要延长时间者），低 stakes；不是阅读、不是高 stakes、不是高中/成人。
- **任务边界**：单个 15 题数学 block（非全卷），题块对全员偏难（三组均分 5.3–9.6/25），作者自认 *"it could be that there may be different results on an easier test"*（PDF p.10）；题型为 MC/匹配/网格等数学题型，与阅读 passage+item 作答 UI 无直接对应。
- **"使用"操作化边界**：duration>30 min 二分是粗代理（C3-1）；无法区分"真正用额外时间检查/重读"与"单纯慢"；无法识别额外时间里发生了什么（无细粒度日志分析）。
- **因果边界**：非实验（作者 Limitations 原文：*"experimental manipulation of extended time use was not applied ... we were not able to isolate the specific effects of the accommodation on score comparability"*，PDF p.11）；"住宿非必要"推断是 discussion 级，counterfactual（未获住宿时的表现）不可得（PDF p.4 明确此既往局限）。
- **DIF 阈值排版歧义（提取层注明）**：PDF p.6 原文 "a standardized effect size magnitude threshold of 10" 与 "thresholds of 164 for moderate DIF and 241 for large DIF" 均缺小数位。若为 0.10/0.164/0.241：第一轮筛选与 item 12 的定性存在内部张力（表 4 中 item 3 第二轮仍 p=.001, δ=0.197，按 0.10 阈值亦过，但作者只报 item 12 为 DIF）；若阈值应用于 β 或另有标度则自洽。**提取以作者自报结果为准**：no-use 0/15 项、use 1/15 项（item 12）DIF，δ=0.226 处于 small–moderate 边界带；"仅 small"按原文引用，不进一步断言。
- **组间可比性**：参考组单一随机样本、能力分布差异大（Buzick & Stone 2011 引证）可能影响 DIF 检出（C3-5，PDF p.11）；未按残疾类别分拆。
- **阴性/反向证据保留**：H1 的 null（未使用组无 DIF）、C4-1 的整体 null、C3-2 的反向保留（未使用≠无效）、C3-4 的 stakes 外推限制，均保留如上。

---

## 对审计的用途

**支持**：
- 部分闭合审计 Class 4 缺口（主审计 p.179 行："no locally held source demonstrates that a specific variant change ... quantifies such an effect for accessibility adaptations"）：本文是第一手实证——一个住宿变体（时间条件 30→90 min）在操作化大样本数字测试中未移动 item 参数（DIF 层面）。不闭合阅读部分（数学、非阅读）。
- 为主审计 Class 4 分析（p.175 行 "An accommodation therefore does not merely assist a subgroup; it moves the process distribution for that subgroup ... must be measured"）提供测量后的边界样本：accommodation 可能**不**移动 item 参数——支持"必须测量"而非"必然移动"。
- 为 Decision implication #6（主审计 p.205，SC 2.2.1 "essential" exception 是构念声明）提供经验锚点：在一个大样本操作化测试中，延长时限未引入 DIF 层面偏差，与"该测试速度非核心构念"相容；同时说明构念声明必须在具体测试上验证。
- 扩展 Class 3 "缺失是设计/行为/情境依赖"（UIE-11/13）到住宿使用维度：约 17% 有资格者未使用（自愿、self-regulation 依赖、stakes 依赖、随测试进程下降）。

**限定/反驳**：
- 与 `UIE-02`（`B7` 格式移动分数 OR=1.40）和 `UIE-27`（`METHOD-012` 模式移动 scale score d=.16–.22）的方向张力：本文显示时间条件未移动 item 参数。调和框架：层级（item 参数 vs scale 分布）、变体类型（时间 vs 格式/模式）、学科（数学 vs 阅读/ELA）、stakes（低 vs 高）均不同——"仪器变体移动 estimand"不能作为普适前提，也不能被本文 null 反证；必须逐变体、逐层级、逐语境测量（C4-3/UIE-34 草稿提供分层表述）。
- 警告反方向误用：本文的 DIF 层面 null **不得**被引用为"时间条件/住宿测量中性"的普遍证据（低 stakes、非实验、单 block、数学、marginal 分数差异巨大）。
- 与审计 W4 行（"cites a low-actual-use-of-accommodations line (Lee et al. 2021; Witmer & Bouck 2023)"）核对：PDF p.5 确证该引用；但本文自身样本未使用率 ≈17%（多数人用了），引用与本文数据分属不同测试语境，引用时不可混用。

**建议新增 UIE 条目（4 条草稿；编号沿用"接 UIE-30"惯例，与并行提取笔记的草案编号可能碰撞，最终编号以综合去重为准）**：

1. **UIE-31（Class 4，暂定 `SUPPORTED`）**：时间条件住宿（延长时间可用性 30→90 min，使用与否分开）在操作化大样本数字测试中未移动 item-level 测量参数：no-use 组 0/15 项 DIF，use 组 1/15 项（item 12，δ=−0.226，small，favors focal），两组相对无残疾参考组均显示 score comparability（DIF 层面）。Pages: PDF pp.1（摘要）, 8–9（结果与讨论）, 8–10（表 2/3/4）。Scope: NAEP 2017 八年级数学、低 stakes、单 block、Poly-SIBTEST DIF 层面、非实验；非阅读、非 scale-score 分布、非高 stakes；"住宿对可比性非必要"是讨论级推断（begs the question），不作事实采用；与 `UIE-02`/`UIE-27` 的移动证据形成"变体效应是否出现取决于变体类型/层级/学科/stakes"的对照。
2. **UIE-32（Class 3，暂定 `SUPPORTED`）**：住宿/功能"使用"的过程数据操作化是粗代理，需独立效度验证：duration 二分（>30 min = used）只能区分超时与否，无法区分额外时间如何使用（检查/重读/发呆/其他住宿激活）；作者自认未来需 process data 细粒度分析（item review and checking、consistent use、targeted use、text-to-speech 激活）。Pages: PDF p.6（编码规则）, p.11（4.2 未来方向）。Scope: NAEP 数学；对 instrument contract 的教训：任何"使用/参与度"代理（如 dwell、active time）必须先验证其与目标行为的对应。
3. **UIE-33（Class 3，暂定 `PARTIAL`）**：住宿/功能"使用缺失"是自愿的、stakes 与自我调节依赖的：分析样本内约 17%（1010/6011）有资格者未使用；住宿使用依赖学生主动发起（student initiation and agency），且随测试进程下降（Lee et al. 2021 引证）；NAEP 低 stakes 下结果不可外推高 stakes（DeMars 2000 引证）；未使用 ≠ 住宿无效（可能不知情/动机不足）。Pages: PDF p.6（组构成）, p.10（讨论：stakes、not knowledgeable/motivated、使用率随进程下降）, p.5（低使用率引证）。Scope: NAEP 数学低 stakes；17% 为本样本选择数据（SUPPORTED），低使用率普遍性与 stakes 影响为 secondhand/作者讨论（PARTIAL）；扩展 UIE-11/13"缺失是设计/行为/情境依赖"到住宿使用维度。
4. **UIE-34（Class 4 方法论，暂定 `SUPPORTED`）**：分数分布移动与 item 测量等价是正交的两个事实：焦点组边际分数显著低于参考组（5.3/6.7 vs 9.6/25，ANOVA 两两 p<.001）但 DIF 极少——marginal distribution shift（组间能力差异）不构成 construct-irrelevant item-level 不等价；"仪器变体是否移动 estimand"必须指定层级（item 参数 vs scale 分布）再表述。Pages: PDF p.7（表 1 分数）, pp.8–9（DIF 结果）。Scope: 数学测试组间比较；为 `UIE-27`（scale 分布移动，d=.16–.22）与本文（item 参数无效应）提供不可互斥解读的分层框架。
