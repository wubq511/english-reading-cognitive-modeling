# 提取笔记：METHOD-037 — Embedded Accommodation Usage on Statewide CBT（Lee et al. 2021）

> 本文件是 `ui-instrument-effects-evidence-audit.md`（Wayfinder #5）Acquisition queue 中「已定位未读」论文的全文证据提取，最终综合的唯一输入。只读不改动 catalog、checksums、审计主文件。

## 头部

- **Source ID**: `METHOD-037`
- **本地路径**: `sources/library/papers/methods/2021_Lee_EmbeddedAccommodationUsage.pdf`（22 物理页；SHA-256 `61f3d19f…` 与 `sources/catalog.yaml` 一致，已复核）
- **完整书目**: Lee, D., Buzick, H., Sireci, S. G., Lee, M., & Laitusis, C. (2021). *Embedded Accommodation and Accessibility Support Usage on a Computer-Based Statewide Achievement Test.* Practical Assessment, Research, and Evaluation, 26(25).（PDF 首页与文末 Citation 均一致；PARE 文章无 DOI，PDF 全文亦未出现本文 DOI——与 catalog `doi: null` 一致）
- **书目不符点（不改 catalog）**: catalog `authors` 第 4 位写 **"Minhee Lee"**，但 PDF 首页作者栏、ScholarWorks 引用与文末 Citation 均为 **"Mina Lee"**（catalog aliases 的 `EJ1327403` 与审计 E4 行引文 "Lee, Buzick, Sireci & Lee 2021" 一致）。以 PDF 为准：Mina Lee。
- **审计引用现状**（`ui-instrument-effects-evidence-audit.md`）: W4 行（"cites a low-actual-use-of-accommodations line (Lee et al. 2021; Witmer & Bouck 2023)"，作为 queue 项 17 的语境）与 E4 行（"Lee, Buzick, Sireci & Lee 2021 embedded-accommodation usage on statewide CBT (EJ1327403)"）。均属搜索记录，无实质主张引用。

## 研究概览

- **研究问题**（RQ1–5，物理页 5）：(1) 如何经验性地定义数字无障碍支持的「使用」；(2) 支持在学生/题目/子群间用了多少；(3) 不同子群最常用哪些支持；(4) 资格（eligibility）与使用的关系；(5) 如何用资格+使用信息识别过度/不足使用的学区。
- **样本**: 某大州 2018 春 6 年级 ELA 与数学州统考全部考生（正文未给出总 N，仅"All tested students were included in the administrative dataset"，物理页 6；样本量只在表格图像中）。子群：SWD、EL、SWD-EL、GenEd。
- **设计**: 描述性/方法学分析，非实验——对操作性考试的**数字日志**做事后分析（无操纵、无随机分配、无推断统计、无显著性检验、无效应量）。CAT 平台，无时限（物理页 6）。
- **任务与材料**: Smarter Balanced 衍生 CAT（ELA+数学）；平台内嵌 5 类支持——highlighter、line reader、masking、text-to-speech（TTS-entire / TTS-selection）、print（物理页 6，Table 1）。TTS/masking/print 需预先批准（accommodation/designated support）；line reader、highlighter 是 universal tools，所有考生无批准即用（物理页 8）。
- **变量**:
  - 过程/行为指标：每题目-学生支持点击次数、支持使用所在 item ID 与 page（screen）号、使用过支持的学生比例（三种操作化）、平均使用题目数。
  - 缺失/数据质量指标：删除率（约 4% 的 student-by-item 交互）、未使用者比例、低使用学区比例。
  - 产品分数：**不可用**——"Only usage data were available to the researchers—item and total test score data for students were not available"（物理页 6）。

## 核心发现（按四类主张）

> 无任何推断统计/效应量/置信区间：本研究的全部统计量是描述性比例与均值。下表凡引文均先经阅读顺序提取再核对原文；页码为 PDF 物理页。

### Class 1 — 可用性/偏好（usability, satisfaction, preference）

- **可用 ≠ 被用（供给不等于参与）**：universal supports 对全体考生开放（无批准门槛），但 line reader 至少用过一次的学生仅约 52%（ELA）、约 37%（数学）；即使是使用率最高的获批 accommodation（TTS-entire），也有 16–39% 的获批学生全程未用一次（passages 84%、ELA items 67%、math 61% 至少用过一次）。物理页 8、14。原文："In contrast, line-reader and highlighter are universal supports that are allowable for all students without pre-approval. Therefore, the total number of approved students for universal tools is equal to that of the total students."（物理页 8）；"For the line reader, about 52% used the support on at least one item... about 37% of the students used a line reader during the mathematics test."（物理页 14）。
- **论文未测量满意度/偏好**：只有观察到的使用行为；作者把「熟悉度」列为使用的关键驱动（评审人意见转述，非实证检验）。物理页 21。原文："a student's familiarity with a support provided will be a major factor in the degree to which the student uses it. Thus, districts that have higher rates of embedded accessibility support use may have done a thorough job in familiarizing students with the support in the classroom."
- **判定**：`SUPPORTED`（仅对"供给≠使用"这一观察性事实）；`PARTIAL`（对"熟悉度驱动使用"的解释性主张，是作者/评审假设，非因果证据）。本论文**不能**填补审计 Class-1 的实证缺口（无易用性/满意度/偏好测量），但它把缺口边界说清楚：行为性不使用（non-use）在操作性考试中是可测且普遍的，而偏好/满意度仍未测。

### Class 2 — 行为改变（UI/格式/布局改变可观察行为）

- **使用行为有强烈的测验内时间结构（front-loading）**：支持使用在测验早期明显更高，尤其前几页；TTS 是唯一跨页持续使用的支持。物理页 10、20。原文："students' use of the supports was noticeably higher earlier in the test, particularly for the first few pages. The TTS supports had the most sustained use across pages relative to the other supports, for both subject areas."（物理页 10）；"They found the use of accommodations designed for ELs was low, and that use decreased as the test progressed. That study, and ours, suggests more work needs to be done to engage students in the use of supports, or design better supports that students will use."（物理页 20，引 Crotts-Roohr & Sireci 2017）。
- **子群-支持匹配**：SWD/SWD-EL 高用 TTS-entire（最高使用率 SWD-EL ELA 80%/Math 74%，SWD ELA 76%/Math 69%）；EL/GenEd 最常用 line reader（ELA 约半数、Math 约 40%）。物理页 10、14。
- **判定**：`PARTIAL`——这是单一固定 UI 内的**观察性**行为描述（无 UI 变体操纵、无因果归因）。对审计的用途：即使在同一仪器内，无障碍支持的参与行为也高度异构且随时间衰减；「使用了支持 = 需要该支持」的推断不可靠。

### Class 3 — 仪器信度与缺失（数据质量、操作化敏感性、缺失/完整性）

- **"使用"不是一个稳定量：三种操作化给出不同（甚至相反）结论**。表 6 的排序在三种定义下翻转：TTS-entire 在三种定义下均居前三，line reader 最常见但跨题使用稀疏。物理页 8–9、19。原文："The first definition can lead to the conclusion a support is being widely used, when in fact it is being used often by relatively few students. Thus, the second definition may be best for summarizing information on a lack of support use."（物理页 19）；"Line reader was the first or second most commonly used, but not used frequently over test items."（物理页 9）。作者明言"there is no 'best' way to define use overall"（物理页 19）。
- **日志数据需要质量筛查，且清洗阈值带信息代价**：因"data capture glitches or some students haphazardly and repeatedly clicking"造成正偏，作者删除"同一支持在单个题目上使用 >10 次"的动作（占分布最高 5%），约删去 **4% 的 student-by-item 交互**；但被删动作可能恰是有效反应（挫折/不熟悉所致）。物理页 6、21。原文："we deleted any student action that involved using the same support more than 10 times on an item. This process resulted in the deletion of about 4% of the student-by-item interactions."（物理页 6）；"The 4% of student actions we deleted seem to be the result of testing the system, but also could be due to students' frustration or unfamiliarity with a support... future research may dive deeper into aberrant use behaviors that may be valid student responses."（物理页 21）。
- **数据可得性是投递模式的设计属性**：纸笔与早期 CBT 根本不产生逐题使用数据；使用数据存在本身就是 CBT 平台的产物。物理页 5。原文："in paper and pencil tests and early computer-based tests, data were not captured to describe how students used accessibility supports throughout the test."
- **平台资格门禁有效（数据完整性）**：无未获批学生使用获批支持——"There were no students who used a support they were not eligible to use."（物理页 14）；学区层面"the percentage of students who used the designated support is never higher than the percentage eligible"（物理页 15）。
- **判定**：`SUPPORTED`（全部为研究报告的描述性操作与结果，范围限于本州 6 年级）。这是本文对审计的最强贡献：log 派生的使用率指标没有单一真值，结论随操作化与清洗决策变化。

### Class 4 — 学习/构念与 estimand（分数分布、构念等价、模式效应）

- **无任何分数证据**：研究明确无逐题/总分数据，因此使用↔成绩的关联在本设计中不可判；作者将其列为未来研究。物理页 6、21。原文："Only usage data were available to the researchers—item and total test score data for students were not available."（物理页 6）；"future research should explore reasons why students did or did not use the supports, as well as how well such use impacted performance on items and the test as a whole"（物理页 21）。
- **框架性关联**：作者把支持使用日志定位为"response processes 效度证据"的候选来源，但只演示了汇总/监控用途，未做构念验证。物理页 20。原文："Log data traditionally can be used to acquire validity evidence based on response processes (AERA et al., 2014; Padilla & Benitez, 2014)."
- **判定**：对 Class 4 无正面证据贡献（`UNRESOLVED` / 不适用）；可作限定语——"最适配某子群的 accommodation 恰好被该子群最常使用"（物理页 20）是描述性匹配，不是构念等价或分数效应声明。

## 边界与局限（作者声明 + 提取方补充）

- 作者声明的局限（物理页 20–21）：单一州、两个科目、一个年级（6 年级——因该年级学生对考试与技术更熟悉、EL 比例更高）；日志分析非直接观察/访谈；无题目文本复杂度、无残疾类型/英语水平数据；无完整题目呈现顺序（页面内多题顺序未知）；无全部支持数据（bundled accommodations 未探索）。
- 方法学边界（提取方）：描述性研究，无推断统计与效应量，无操纵；CAT 自适应 + 无时限是平台常量的一个特殊组合；Smarter Balanced 衍生平台，支持集（5 类）非全平台全集；正文无总 N（仅表格图像含样本量，无法复核）。
- 不可外推处：结果不能外推到其他年级/州/科目/平台/设备；「使用率」数字随操作化定义、清洗阈值、时间点（测验早段 vs 全卷）变化，任何单一数字（如"约一半学生用 line reader"）都必须携带定义与范围。

## 对审计的用途

- **支持/限定既有条目**：
  - 强化 `UIE-11`（B2，missingness 是行为/设计依赖的）：本州统考中，约半数考生对 universal support 的使用量为零，且这是常态而非异常——缺失是默认状态。间接支持审计决策含义 #5（"treat absent signals as the default state"）。
  - 平行于 `UIE-12`（B7，数据完整性是指针/设计决策）：4% 删除阈值与"被删动作可能有效"直接复现同一教训；另加投递模式决定数据可得性（纸笔 → CBT 才有逐题使用日志）。
  - 与 `UIE-22`（METHOD-010，log/paradata 作数据质量筛查）同类张力：使用日志需清洗阈值，但清洗与"aberrant use 可能是有效反应"的取舍无先验答案。
  - **限定审计 W4/queue 项 17 的 "low-actual-use-of-accommodations" 引用**：该行把 Lee et al. 2021 当作"住宿实际使用率低"的证据。本文显示此说需限定——对**已获批**的 TTS-entire，至少用过一次的比例是 61–84%（不低）；「低使用」主要指 (a) universal supports（全体开放，仅约 37–52% 使用）、(b) 未用/少用的获批个体与低使用学区、(c) 采用"至少用过一次"以下更严格定义时的估计。且"使用率"本身随操作化定义翻转（物理页 19）。引用时须带这些限定，否则构成 `OVERSTATED`。
- **未关闭的缺口**：不填补审计 Class-1 实证缺口（无满意度/偏好测量）；不提供任何 Class-4 分数/estimand 证据；不对阅读作答 UI 的事件完整度/重放保真作任何测量。

## 建议的新 UIE 条目草稿

- **UIE-31（Class 3）** claim: Log 派生的「支持使用率」无稳定真值——三种操作化（点击次数计数 / 至少用过一次 / 使用题目数）产生不同支持排序（表 6），且点击计数定义会把「少数人高频使用」呈现为「广泛使用」。pages: 物理页 8–9, 19。verdict: `SUPPORTED`（描述性）。scope: 单一州 6 年级 Smarter-Balanced 衍生 CAT（ELA+数学），2018 春；无分数数据。审计含义：任何「X 用了多少」的 UI/无障碍指标必须先固定操作化并报告敏感性。
- **UIE-32（Class 3）** claim: 使用日志需数据质量筛查，且清洗阈值携带构念相关代价——同支持单题 >10 次的动作被删（占分布最高 5%），删去约 4% 的 student-by-item 交互；作者自认被删动作可能包含反映挫折/不熟悉的有效反应。pages: 物理页 6, 21。verdict: `SUPPORTED`（报告的研究操作）。scope: 同 UIE-31；平行于 UIE-12 的"事件完整性与清洗是仪器决策"教训，延伸到 log 指标。
- **UIE-33（Class 1/2 边界）** claim: 在操作性大规模考试中，供给 ≠ 参与——全员开放的 universal support 仅约 37–52% 考生至少用过一次；最高使用率的获批 accommodation（TTS-entire）仍有 16–39% 获批者全程未用；使用行为测验内前载（front-loaded）且跨页衰减；作者假设熟悉度是主要驱动（未检验）。pages: 物理页 8, 10, 14, 20–21。verdict: `SUPPORTED`（观察性使用事实）；`PARTIAL`（熟悉度解释为假设）。scope: 同 UIE-31。审计含义：为「无障碍/可用性不能从供给推断」提供操作性证据，但**不**提供满意度/偏好测量，不关闭 Class-1 实证缺口。
