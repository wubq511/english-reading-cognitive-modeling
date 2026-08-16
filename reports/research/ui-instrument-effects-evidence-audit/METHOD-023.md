# METHOD-023 全文证据提取笔记

> 用途：Wayfinder #5「UI 仪器效应证据审计」Acquisition queue 条目（已定位未读 → 本篇读完）。审计角色：Class 3 产品层缺失/参与度证据。
> 页定位一律为 **PDF 物理页**（本 PDF 物理页 = 印刷页 + 1，已验证：物理页 4 = 印刷页 3，物理页 6 = 印刷页 5）。
> 全文阅读范围：物理页 4–27（摘要至 Discussion 与设计建议）+ 目录；Annexes（物理页 29–32，题目样例）未逐页细读，未引用其内容。

## 头部

- **source ID**: METHOD-023
- **本地路径**: `sources/library/papers/methods/2024_OECD_ItemDisengagement.pdf`
- **书目**（与 `sources/catalog.yaml` METHOD-023 条目一致，未改动 catalog）:
  - Avvisati, F., Buchholz, J., Piacentini, M., & Vargas-Madriz, L. F. (2024). *Item characteristics and test-taker disengagement in PISA* (OECD Education Working Papers No. 312, EDU/WKP(2024)7). OECD Publishing. DOI: `10.1787/7abea67b-en`
- **核对结果**: catalog 条目（标题/作者/年份/venue/DOI/本地路径/SHA）与 PDF 首页、DOI 页脚一致；无出入。

## 研究概览

- **研究问题**: 哪些题目特征（item characteristics）与低 stakes 大规模测评中的两种脱离作答（disengagement）指标——rapid guessing（快速猜测）与 breakoff（提前弃测）——相关联；据此为命题人提供降低脱离的题目/试卷设计建议。
- **数据**: PISA 2018 阅读测试（低 stakes，群体施测的 CBT）；仅限计算机施测国家（响应时间是 rapid guessing 定义的前提）；67 个国家和地区，499,387 名学生，约 1,700 万条题目作答，233 道题（245 道中排除 12 道同屏题目，仅每屏取一题）。两阶段分层抽样，各国目标样本约 6,300 人。
- **设计**: 观察性/相关性设计（operational assessment 数据分析），**非随机实验**。三层 logistic 回归（rapid guessing；学生/学校随机截距，学校层聚类标准误）+ Weibull 比例风险生存模型（breakoff；item position 为离散时间变量）。两国样数据集分别建模后跨 67 样本取平均，报告 OR/HR。**不加权**，作者明示结论首先描述的是"数据产出与质量如何受脱离影响"，外推依赖模型有效性。
- **任务与材料**: 1 小时 PISA 2018 阅读 CBT；多阶段自适应（two routing points）；每生作答 3 个 testlet（33–40 题）。考生在第一天与第二小时之间轮换（各一半学生在第一/第二小时作答阅读）。
- **脱离指标的操作化**:
  - *Rapid guessing*：题目层、按各次访问累计总响应时间、仅非缺失作答；低于某截断值（cut-off）判为快速猜测。**该阈值以公式图形渲染，文本层不可提取（`pdftotext -layout` 与 `-raw` 均为空白）**；PISA 2018 常用惯例为短响应时间阈值，但本文具体数值未能在本地文本层核实，如需引用应回查 PISA 2018 技术报告或图片渲染。缺失作答（omitted + non-reached）与无有效响应时间的作答一律编码为缺失并从 rapid-guessing 分析中排除（物理页 12）。
  - *Breakoff*：non-reached 定义为会话末尾连续 ≥2 题无作答；其中第一题若在 60 分钟会话的前 45 分钟内到达（即距时限 ≥15 分钟），判定为"absence of time pressures"下的弃测起点；proper breakoff = 时限前 ≥15 分钟出现连续无作答（物理页 12、18）。
  - 注意：rapid guessing 与 breakoff 均以**作答结果（响应时间/缺失模式）**推断，属仪器层/作答层指标，非过程日志 UI 事件指标。
- **自变量（surface item characteristics，均分类变量）**: 反应格式（open-ended 25% / hot spot & match 4% / matrix & complex multi-selection 17% / simple multiple-choice 54%）；图片/图形（无 24% / 1 张 49% / ≥2 张 27%）；Interactive Material（需翻页/标签/网页交互，48%）；阅读刺激长度（1–200 词 24% / 201–500 词 64% / 501+ 词 12%）；是否 unit 内第一题（21%）。控制：题内精确位置（RG 用二次多项式，survival 用时间变量）、题目难度（PISA 水平 1–5/6）、其他领域插补成绩（PV1 与是否实考指示）、考试时段（第一/二小时）、性别。

## 核心发现（按四类主张分组）

### Class 3 — 仪器信度与缺失（本论文主要贡献层）

1. **脱离的发生率（产品层缺失规模）**：约 7.4% 学生出现 rapid guessing、8.0% 出现 breakoff（部分人两者皆有）；按题目作答计，约 1.6% 被判为 rapid guesses，另约 1.6% 因 breakoff 缺失（物理页 15）。原文："rapid guessing and breakoffs were observed for 7.4% and 8.0% of students ... about 1.6% of them were identified as rapid guesses, and another 1.6% were missing because of breakoff."
2. **缺失类型与行为机制（非随机缺失的直接证据）**：缺失主要由 non-reached（时间不够）驱动，尤其第一小时；第二小时学生更多选择 omit 某些题以赶进度。相当比例的 non-reached 属于时限前 ≥15 分钟就弃测的学生（breakoff）（物理页 18–19）。缺失率随测试推进单调上升，且位置存在峰值（反映该位置题目特征）（物理页 18）。**结论：PISA CBT 阅读的缺失不是随机仪器故障，而是题目格式/位置/时段相关的行为产物**。
3. **两类脱离指标近乎正交**：跨国家 rapid guessing 率与 breakoff 率相关系数接近 0——"test-taker disengagement tends to manifest itself in different forms across countries"；不同国家优先出现不同形态（拉美 breakoff 高、RG 低；香港/韩国 RG 高、breakoff 低）（物理页 16、25）。同类证据：post hoc 调整所用指标间相关低，导致"score adjustment 结果依赖指标选择、引入不可取的任意性"（引 Buchholz et al. 2022；物理页 7）。
4. **不同缺失/脱离在计分中的不同处理 → 对可比性与参数恢复的威胁**：PISA scaling 中因 breakoff 导致的缺失与任何 non-reached 同样处理（物理页 16；该句"are treated as [x]"的 [x] 以图形渲染、文本层缺失，具体处理方式未能从文本核实）；breakoff 高比例威胁均值分解释与题目参数无偏恢复（"Breakoffs are also a strong threat to the unbiased recovery of item parameters"）。rapid-guess 的"有效"作答按对/错**进入计分**，其分数效应可正可负（"Their effect on scores may be positive ... or negative"），同样威胁题目参数无偏恢复（物理页 16）。
5. **跨国家相关模式**：国家层 RG 率与阅读成绩线性相关 ∈ [−0.2, 0.2]（无关）；breakoff 率与成绩相关约 −0.5（低分国家更易弃测）（物理页 16）。

### Class 2 — 行为改变（UI/格式/布局改变可观察行为与过程指标）

> 注：本文无随机操纵，所有"效应"为**控制变量后的关联（OR/HR）**，作者在方法部分明示不加权、模型内解释；因果解读须谨慎。但格式→脱离行为的关联方向与量级是操作化大规模测评中可复现的最强证据。

1. **反应格式是 rapid guessing 的最强预测因子**：simple MC 触发 RG 的几率是 open-ended 的 **23.10 倍**（Baseline OR=23.100, SE 0.348；Lagged OR=21.702），是 matrix/multi-selection 的约 13 倍；matrix/multi-selection 相对 open-ended 为 OR 1.673；hot spot/match 为 1.204（物理页 19–20，Table 3.1）。原文："simple multiple-choice items being more than 20 times more likely to trigger rapid guessing behaviour compared to open-response items, and more than 13 times more likely than complex multiple-choice items." 所有题目特征变量在两种模型均显著（p < .05）。
2. **格式对 breakoff 的方向相反（格式-行为 contingency）**：hot spot/match 使 breakoff 风险升为 1.282 倍（HR 1.282, SE 0.044）；simple MC 与 matrix/multi-selection 使 breakoff 降至 0.425 / 0.268（物理页 22，Table 3.2）。作者解释复杂/新颖格式（hot spot 等）的 breakoff 效应可能源于学生不熟悉（"it is possible that this effect results from the unfamiliarity of students with such formats"）（物理页 24）。
3. **刺激长度（任务 UI 负载）**：501+ 词 RG OR 2.028、breakoff HR 1.797；201–500 词 OR 1.706 / HR 1.417（均相对 1–200 词）（物理页 20、22）。
4. **多媒体与交互（content UI 元素）方向分裂**：图片增多 **增加** RG（Single OR 1.259、Multiple OR 1.360）——与既往文献相反（作者推测是增加刺激复杂性）；交互材料 **降低** RG（OR 0.785）但 **增加** breakoff（HR 1.104）（物理页 20、22、24）。
5. **位置/时段效应**：第二小时作答 RG 几率是第一小时的 2.459 倍（Lagged 模型降至 1.717，且"前次 RG"系数 6.417 表明 RG 有惯性）；unit 首题 RG 降约 2.5 倍（OR 0.386）但 breakoff 升 2.19 倍（HR 2.192）；breakoff 基线风险随位置指数增长（Weibull 参数 4.783）（物理页 20–22）。
6. **难度与性别（控制变量，部分可视为考生×题目交互）**：难度越高 RG 越多（L5/6 OR 3.061）；breakoff 在难度 L3 峰值（HR 2.385），L4/5/6 回落；女生两类脱离均更低（RG OR 0.302，breakoff HR 0.902）（物理页 20–22）。

### Class 4 — 学习/构念与 estimand（产品分数、构念等价、模式/格式效应移动分数分布）

1. **格式吸引的猜测直接进入产品分数（estimand 污染的结构性路径）**：PISA 将 rapid-guess 的有效作答按对/错计入计分，而 simple MC 格式以 OR≈23 的强度吸引 RG——即**作答 UI 格式（点选式简单 MC）会系统性增加被计分的猜测性作答比例**，其分数效应方向未知（可正可负）（物理页 16、19–20）。这是"格式移动估测量"的间接但规模化的证据；注意是相关性，非操纵实验。
2. **时间压力下的行为替代损害表现分数**：学生对"未达卷尾"无惩罚、对"答错（含猜错）"有惩罚，因此把第二小时的省略换成第一小时开始的 RG 作答会拉低成绩（"if students substitute rapid-guess answers ... for missing responses ... their performance suffers"）（物理页 23）。
3. **对均值分解释与等值的威胁**：breakoff 高发国（拉美 19–22%）的未完成部分在 scaling 中与非 reached 同处理，作者提示高 breakoff 比例"may still cast questions on the interpretation of mean scores"（物理页 16）。
4. **设计建议层（interface/test-design 变更需先实验验证）**：作者建议帮助时间管理（施测前安抚"无惩罚"、增加休息、把 2×60 分钟改为 3×40 分钟）、屏幕闲置后弹出"可跳过"软提醒等；并明确写：**"The effect of such changes to the interface or test design on [engagement] behaviour and, ultimately, data quality, should ideally be investigated thoroughly prior to their introduction in the main study, through pilot studies and/or field-trial experiments"**（物理页 25）——即接口/设计变更在引入前须经实验验证，与审计"冻结前必须先证 UI 变体等价"的决策一致。
5. **题目设计权衡（无免费午餐）**：简单 MC 有良好心理测量属性与低成本，但吸引 RG；复杂/新颖格式降 RG 却增 breakoff；作者建议"组合"特征（unit 首题配最简单格式）（物理页 25）。

### Class 1 — 可用性/偏好

- 无直接可用性/满意度/偏好数据。间接相关：格式不熟悉被推测为 breakoff 诱因（"response formats that are unfamiliar or the subject of insufficient practice during tutorials risk disrupting students"），属作者解释性推断而非偏好测量（物理页 24–25）。

## 边界与局限

- **作者自陈局限**（物理页 24）：仅 PISA 2018 阅读；其他领域（数学/科学）中图片、交互导航、刺激长度的作用可能不同；部分特征仅出现在少数题目（hot spot/match 仅 4%），其结果可能反映这些题目更 idiosyncratic 的特性。
- **设计层面**：观察性、非操纵；多阶段自适应设计使题目特征与学生能力相关（作者用其他领域插补成绩控制，但因果解读仍受限）；**未加权重**，SE 为模型 SE；跨国家平均呈现，国家间异质性（补充材料）未在正文展开。
- **指标层面**：rapid guessing 阈值数值在本地文本层不可提取（公式图形），引用该阈值需另核 PISA 技术报告；breakoff 定义依赖"≥15 分钟余量"与"≥2 题连续"的约定，指标选择本身影响结论。
- **测量对象边界**：RG/breakoff 是**作答结果层**指标（响应时间/缺失模式），不是光标/注视/事件流过程日志；其"脱离"构念效度依赖响应时间与缺失行为=脱离的假设（作者引用 Wise 2017 等，未在本论文内验证）。
- **对审计不可外推处**：本文不涉及 UI 布局变体（分栏、滚动、字体、无障碍）或投递设备变体，只覆盖**作答格式/刺激负载/位置/时段**四个题目层表面特征；不能把"格式→RG"直接外推为"任何 UI 变体→行为分布移动"，但能支持"答案 UI 形态影响作答行为分布与缺失率"这一前提。

## 对审计的用途

- **支持/强化既有条目**：
  - **UIE-11**（`B2`，缺失是行为/设计依赖而非随机）：METHOD-023 在 PISA CBT 阅读上提供同一结论的大规模独立证据（1.6% RG + 1.6% breakoff 缺失、缺失类型与格式/位置/时段相关）——Class 3 直接强化。
  - **UIE-01/02**（`B7`，格式改变过程指标与产品分数，方向随任务类型翻转）：METHOD-023 在操作化阅读测评中复现"格式→行为"关联（simple MC RG OR 23.1 vs open-ended；hot spot/match breakoff HR 1.28），且同样呈**格式-行为 contingency**（简单格式引 RG、复杂格式引 breakoff）——与 B7 的任务类型 contingency 呼应；但本文是相关性非实验，只能作互补，不能替代 Arslan 2020 的操纵证据。
  - **UIE-22**（`METHOD-010`，过程通道可做数据质量筛查）：两者属不同筛查通道（RT 阈值 vs 光标指标），METHOD-023 另证不同筛查指标（RG 与 breakoff）近乎正交（跨国家 r≈0）——**单一筛查指标不可互换**，补强 UIE-22 的筛查语义。
  - **UIE-26/27**（投递模式效应）：METHOD-023 在同一 CBT 模式**内部**显示格式/负载移动脱离与缺失，补足模式层证据之下的题目层证据；其"未达卷尾无惩罚、答错有惩罚"的行为替代机制与 UIE-27（ACT 模式效应集中在后期题目、与 speededness 一致）机制相容。
  - **UIE-29**（介质改变行为）：METHOD-023 增加了"数字阅读测试内部题目表面特征"维度。
- **回答/限定待决问题**：审计 Class 4 缺口"无本地源证明阅读 MC 作答 UI 的具体变体改变被测量构念或 estimand"——METHOD-023 **不能关闭**该缺口（无操纵、无直接分数对比），但它提供了最强的前提证据：格式吸引被计分的猜测性作答（OR 23.1），且作者明确要求接口/设计变更须先经 pilot/field-trial 实验（物理页 25），与审计"冻结前先证变体等价"一致。
- **引用说明**: 审计主文件与 register 当前均无 METHOD-023 条目（grep 未命中），本篇为首次入库笔记；现有 UIE-01..30 编号不受影响，新增条目建议接续 UIE-31 起编号（见下）。

## 建议的新 UIE 条目草稿

1. **UIE-31（Class 2/3，暂定 `SUPPORTED`）** — claim: 在操作化低 stakes 阅读 CBT（PISA 2018，67 国，约 50 万学生）中，答案格式与题目表面特征系统移动脱离作答与缺失率：simple MC 的 rapid guessing 几率是 open-ended 的 23.10 倍（OR=23.100, SE 0.348）；hot spot/match 使 breakoff 风险 ×1.282；501+ 词刺激使 RG ×2.028、breakoff ×1.797；交互材料降 RG（OR 0.785）但升 breakoff（HR 1.104）。pages: 物理 19–20（Table 3.1）、22（Table 3.2）。scope: PISA 2018 CBT 阅读题目层表面特征；观察性关联（非随机操纵），格式效应方向随格式-行为组合翻转，不可外推至布局/设备变体。
2. **UIE-32（Class 3，暂定 `SUPPORTED`）** — claim: 大规摸阅读测评的产品层缺失是格式/位置/时段依赖的行为产物而非随机故障：1.6% 题目作答被判 rapid guess、另 1.6% 因 breakoff 缺失（7.4%/8.0% 学生）；缺失以 non-reached（时间不足）为主、第二小时以 omit 替代；breakoff 缺失在 scaling 中与非 reached 同处理，rapid-guess 有效作答按对/错进入计分（分数效应可正可负）。pages: 物理 15–16、18–19。scope: PISA 2018 阅读 CBT；缺失类型在计分中的具体处理（"treated as [x]"）本地文本层缺失，需另行核实。
3. **UIE-33（Class 3，暂定 `SUPPORTED`）** — claim: 脱离筛查指标不可互换：跨国家 rapid guessing 率与 breakoff 率相关≈0（不同国家呈现不同主导形态）；post hoc 分数调整的结果依赖所选的脱离指标（指标间相关低），引入分数构造的任意性。pages: 物理 7、16、25。scope: 国家层相关 + 文献引用（Buchholz et al. 2022）；属"指标选择影响调整结果"的方法论证据，非 UI 变体证据。
4. **UIE-34（Class 4，暂定 `PARTIAL`，框架事实 `SUPPORTED` + 因果链 `PROJECT-INFERENCE`）** — claim: 因为 rapid guesses 被按对/错计分且 simple MC 以 OR≈23 吸引 RG，答案格式选择会系统性改变产品分数中"猜测性作答"的成分（格式→estimand 组成移动）；作者据此要求接口/试卷设计变更（休息安排、跳过提醒、会话长度）在引入前须经 pilot 与 field-trial 实验验证。pages: 物理 16（计分事实）、19–20（OR）、23（行为替代机制）、25（pilot 要求）。scope: "猜测进入计分"为支持的事实；"格式必然移动分数分布"是本文未直接检验的推断（观察性），分数效应方向未决（作者明示可正可负）。

## 关键原始引文（英文，锚点）

- "simple multiple-choice items being more than 20 times more likely to trigger rapid guessing behaviour compared to open-response items, and more than 13 times more likely than complex multiple-choice items."（物理页 19）
- "rapid guessing and breakoffs were observed for 7.4% and 8.0% of students who sat the PISA reading test in 2018, respectively ... about 1.6% of them were identified as rapid guesses, and another 1.6% were missing because of breakoff."（物理页 15）
- "valid answers which are classified, based on response-time information, as rapid guesses, are treated as either correct or incorrect and used in scoring. Their effect on scores may be positive ... or negative."（物理页 16）
- "Breakoffs are also a strong threat to the unbiased recovery of item parameters" / "Rapid guessing also poses a significant threat to the unbiased recovery of item parameters."（物理页 16）
- "The effect of such changes to the interface or test design on [engagement] behaviour and, ultimately, data quality, should ideally be investigated thoroughly prior to their introduction in the main study, through pilot studies and/or field-trial experiments."（物理页 25）
- "response formats that are unfamiliar or the subject of insufficient practice during tutorials risk disrupting students and are associated with higher risks of breakoff, with only limited benefits for reducing rapid guessing behaviour."（物理页 25）
