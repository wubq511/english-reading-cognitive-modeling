# METHOD-025 提取笔记：PISA 2015 Results (Volume V): Collaborative Problem Solving

## 头部信息

- **Source ID**: METHOD-025
- **本地路径**: `sources/library/papers/methods/2017_OECD_CollaborativeProblemSolving.pdf`（310 物理页）
- **完整书目**: OECD (2017), *PISA 2015 Results (Volume V): Collaborative Problem Solving*, PISA, OECD Publishing, Paris. ISBN (PDF) 978-92-64-28552-1. DOI: 10.1787/9789264285521-en
- **catalog 核对**: 与 `sources/catalog.yaml` METHOD-025 条目（authors/年份/标题/venue/DOI/许可 CC BY-NC-SA 3.0 IGO）一致，无出入。
- **页码约定**: 本笔记全部引用 **PDF 物理页**（pdftotext 的 `-f/-l` 编号）。物理页 = 印刷页 + 2（已逐页校准，如物理 50 页脚为印刷 48）。

## 模式效应焦点核验（任务核心结论）

> **「模式效应量化内容未在此卷」。**

- 检索记录（审计主文件 W6）称本卷含「PISA 2015 field trial 中 65/103 题模式等价、38 题难度漂移」。**全文逐项搜索未找到任何此类量化分析**：无 `mode effect`/`equat`/`DIF`/`item parameter drift` 结果表，数字 `65`/`103`/`38` 全文检索均不指向任何等值统计量。
- 本卷仅有的相关陈述在 `WHAT IS PISA?`（物理页 28–29，印刷 26–27）：
  > "For the first time, PISA 2015 delivered the assessment of all subjects via computer. Paper-based assessments were provided for countries that chose not to test their students by computer, but the paper-based assessment was limited to questions that could measure trends in science, reading and mathematics performance. New questions were developed for the computer-based assessment only. A field trial was used to study the effect of the change in how the assessment was delivered. Data were collected and analysed to establish equivalence between the computer- and paper-based assessments."
  - 即：只声明 field trial 被用于研究投递方式变化效应、并采集数据建立 CBT/PBT 等价，**无任何等值结果数据**。CBT 版 66 种测试形式、PBT 版 30 种笔纸形式（物理页 28–29）。
- **CPS 域无 CBT/PBT 模式效应问题的结构性原因**（物理页 85，印刷 83）："The PISA 2015 collaborative problem-solving assessment is interactive and hence could only be delivered in a computer-based format."——CPS 只能机考，本卷涉及的模式相关讨论仅限于「机考依赖 ICT 熟悉度」。
- **「65/103、38 题」真实来源回查指向**：本卷 References 引用 `OECD (2017b), PISA 2015 Technical Report`（物理页 66，印刷 64）为方法细节 owner；等值/模式效应量化分析应到 Technical Report（及 field trial 专项报告）回查，**不得再以本卷作为该数字的 primary source**。

## 研究概览

- **研究问题**: 15 岁学生协作解决问题（collaborative problem solving, CPS）能力在国际间的表现、与核心学科及个体问题解决的关系、ICT 经验与机考成绩的关系。这是**首轮国际大规模 CPS 测评**的结果报告卷。
- **样本**: PISA 2015 约 540,000 名学生（72 国）；其中 57 国参加 computer-based assessment，52 国参加 CPS 测评（32 OECD + 20 partner）（物理页 68，印刷 66；物理页 20，印刷 18）。
- **设计**: 大规模横断面国际测评结果报告（observational/cross-sectional），**非实验**；无随机分配、无对照条件操纵。
- **任务与材料**: 6 个 CPS 单元、117 个 items（物理页 68，印刷 66）；3 个 30 分钟 cluster；学生与 computer agents 在 chat 界面 + 任务空间（按钮、记分卡）中交互（物理页 57，印刷 55）。全部 items 为多选/移动图标/点击选项，**无 free-response**（物理页 68）。样例单元 XANDAR 全部分解于物理页 55–65（印刷 53–63）。
- **变量**:
  - 产品分数: CPS 成绩（5 级熟练度，IRT 单维标尺，117 items 定难度；物理页 68–69，印刷 66–67）。
  - 过程指标: 本卷**不含**过程日志/行为序列分析（XANDAR 各 item 的答题路径描述是题目设计说明，非实证过程数据）。
  - 缺失指标: CPS 测评**无 item 缺失**（强制作答设计，见下）；问卷 non-response 在 Annex A1 有处理声明（物理页 175，印刷 173）。

## 核心发现（按四类主张）

### Class 1 可用性/偏好

- **无系统可用性/满意度数据**。本卷没有关于界面可用性、满意度或偏好的任何实证测量。
- 轶事性唯一相关点（物理页 51，印刷 49，Box V.2.1）：学生在认知实验室中**无法区分 human agent 与 computer agent**——
  > "Anecdotal evidence from students indicates that they were unable to distinguish which of the agents was the human agent, likely because their responses were all prepared."
  - 判定：`PARTIAL`——轶事证据、无系统测量；仅说明 agent 对话式 UI 的拟人一致性。
- 公开样例单元供在线体验（物理页 55，印刷 53）："The interactive nature of the unit Xandar can best be appreciated by trying to solve the items oneself."——仅为传达性描述，无可用性测量。

### Class 2 行为改变

- **核心证据：仪器替换（computer agent → human agent）的分数差异「统计显著但很小、实际无关」**（物理页 50–51，印刷 48–49，Box V.2.1；转述卢森堡大学 Herborn, Mustafic & Greiff, forthcoming 教室研究）：
  - 做法：4 个 PISA CPS 单元把 1 个 computer agent 换成 human agent 搭档（human 从预备反应集中选择，被试所见与被试作答界面相同）；只对被试评分；作答前告知被试对方是人还是电脑。
  - 结果原句："A statistically significant yet small difference in scores was observed between students who interacted with a computer agent and students who interacted with a human agent; this difference was deemed too small to be relevant from a practical standpoint."
  - 判定：`PARTIAL`——**无效应量数值、无样本量/检验统计量**（来源是 "forthcoming" 手稿转述）；方向（谁高谁低）也未给出。可作为「仪器变体移动分数分布」的量级参考（小且实际无关），但不可引用具体数字。
- **仪器行为标准化（收敛设计）**（物理页 57，印刷 55）：agent 对学生的任意作答以收敛方式回应，保证后续刺激一致——
  > "No matter which response a student selects for a particular item, the computer agents respond in a way so that the unit converges. All students are hence faced with an identical version of the next item."
  - 判定：`SUPPORTED`（设计层面陈述）——agent/UI 行为被设计为「响应不变性」，消除学生选择对后续刺激的反馈效应，使行为测量可比。
- **强制作答设计**（物理页 68，印刷 66）："students were required to respond to each item before moving onto the next item and could not skip or omit items."——UI 禁止跳过/省略，直接改变作答行为空间（见 Class 3）。
- **ICT 使用频率 × 机考成绩**（物理页 86，印刷 84，横断面）：校内 ICT 使用最多组比最少组 CPS 平均**低 29 分**（OECD 平均；部分国家 >50 分）；顶组学生成为 top performer 的几率仅及其他学生 **60%**。作者明确声明非因果（见 Class 4 边界）。
- **教师评价相关性**（物理页 50，印刷 48）：教师对学生协作技能的主观评价与学生在虚拟单元（computer agent 版与 human agent 版）的成绩「显著且中度相关」。

### Class 3 仪器信度与缺失

- **CPS 设计将 item 缺失率结构性归零**（物理页 68，印刷 66）：强制作答 + 无 free-response + 117 items。作答前不可前进，故除整体离场/缺考外不存在 item-level missingness——这是**仪器设计决定缺失机制能否存在**的直接例证（对审计 missingness 类主张有对照价值：一个选择「强制+连续」而非「可跳答+可回看」的 UI，缺失率恒为 0，但这同时抹去了缺失率作为行为指标的信息量）。
- **问卷 non-response 处理**（物理页 175，印刷 173，Annex A1）："Unless otherwise indicated, no adjustment is made for non-response to questionnaires in analyses included in this volume."——问卷分析不做 non-response 调整，估计基于有效作答子样本；表 A1.1（在线）报告各变量覆盖比例，并提示"Where this proportion shows large variation across countries/economies or across time, caution is required when comparing results on these dimensions."（国家间/时点间覆盖差异大时需谨慎比较）。
- **报告层缺失符号**（物理页 20，印刷 18，Reader's Guide）：`c`（<30 学生或 <5 学校，估计不可靠）、`m`（数据缺失）、`w`（国家撤回）——报告惯例，非分析调整。
- **测量模型与信度**：IRT（2PL/GPCM + WLE），Annex A1（物理页 172，印刷 170）；CPS 标尺定位于 117 items（物理页 68–69）。本卷**无信度系数、无 DIF、无 CBT/PBT 等值统计**。
- **可比性保障机制**：agent 行为受控以隔离个体 CPS 能力（物理页 50，印刷 48："allows the assessment to control the behaviour of the other agents in order to isolate the collaborative problem-solving ability of the student being evaluated"）+ 收敛设计（物理页 57）——仪器层面的跨被试标准化。

### Class 4 学习/构念与 estimand

- **构念效度（仪器可外推性）证据**（物理页 51，印刷 49，Box V.2.1；Herborn et al., forthcoming 认知实验室）：
  > "students' performance in the original and re-formatted units, both of which took place in a virtual, computer-based setting, was a moderately good predictor of their performance in the face-to-face collaboration units with another human."
  - 即：虚拟 agent 化测评成绩是面对面真人协作表现的「中等程度预测因子」（"moderately good predictor"）；教师评价与虚拟单元成绩显著中度相关（物理页 50）。
  - 判定：`PARTIAL`——无相关系数数值、无样本量，转述未出版手稿；支持「UI/仪器变体（agent 替代真人、虚拟替代面对面）不摧毁分数与真实构念的关联」，但量级未钉死。
- **分数分布受仪器 × 个体交互影响（ICT 经验）**（物理页 86–88，印刷 84–86）：
  - 自报 ICT 使用：顶 vs 底四分位差 **29 分**（物理页 86）。
  - 自报 ICT 能力：顶 vs 底四分位差 **11 分**；低 ICT 能力（指数 < −1.00）学生成为 low performer 几率高 **19%**、平均低 **18 分**（物理页 87，印刷 85）。
  - 但 ICT 能力对 CPS 成绩的解释量仅 **0.6% 方差**（物理页 88，印刷 86："ICT competence explains only 0.6% of the variation in collaborative problem-solving performance"）。
  - 方向无法判定（物理页 88，印刷 86："the direction of the association cannot be ascertained from this analysis"）。
  - 判定：`PARTIAL`——相关性明确但效应极小、方向不明；可作为「机考平台经验对产品分数的贡献小但存在、且混淆因果」的参考。
- **构念区分性（背景）**：CPS 相对成绩与 2012 个体问题解决相对成绩 r² = 0.23（物理页 84，印刷 82）——支持 CPS 测出独立构念，但属构念效度背景，与 UI 变体无关。

## 边界与局限

- **横断面非实验**：ICT 相关全部为观察性相关，作者明确声明非因果（物理页 86，印刷 84："Because of the cross-sectional and non-experimental nature of the variation in ICT use, the relationship between ICT use and performance in collaborative problem solving is not necessarily one of cause and effect."）。
- **未出版手稿转述**：Box V.2.1 全部实证（agent vs human、教师评价、面对面预测）源自 "forthcoming" 手稿（Herborn, Mustafic and Greiff; Herborn et al.，物理页 66，印刷 64 References），无效应量、样本量、统计细节；结论为 OECD 转述，不可当作已出版同行评审证据。
- **领域/人群边界**：仅 15 岁在校生、仅 CPS（interactive、只能机考）；不能外推至 science/reading/math 或纸笔/其他格式测评；本卷无任何阅读测评内容。
- **无过程日志数据**：本卷不含按键/导航/时间等过程指标实证分析，审计关注的阅读 UI 过程证据不在此卷。
- **方法细节外移**：scaling、等值、field trial 量化分析均在 `PISA 2015 Technical Report (OECD, 2017b)`（本卷多次引用，物理页 66、172），本卷只承载结果报告。

## 对审计的用途

- **修正 W6/C9 的来源归属**：审计主文件 W6 把「65/103 题模式等价、38 题难度漂移」的 primary source 指向本卷——**不成立**。本卷只承载「field trial 用于建立 CBT/PBT 等价」的过程声明（物理页 28–29），量化结果需回查 `PISA 2015 Technical Report`。C9 将本卷命中为 PISA mode effects 证据的主要来源，同样需要限定为「过程声明层面」。
- **支持 UIE-26（METHOD-011 TME 综述条目）**：本卷证实 PISA 2015 全学科 CBT 化、PBT 仅限趋势题、以 field trial 回应模式切换（物理页 28–29）；CPS 因 interactive 只能机考（物理页 85）——补充「模式效应威胁在 OECD 的制度化应对是 field trial + 等值，而非 UI 层控制」的政策层背景。
- **为 missingness 类主张提供对照设计**：CPS 强制作答（物理页 68）说明「UI 可以设计为消灭缺失率」，审计中若涉及「缺失率作为行为/数据质量指标」的主张，此卷是反向对照（缺失率=0 的设计如何牺牲缺失率信息量）。

## 建议新增 UIE 条目草稿

1. **UIE-NEW-A「强制作答消除 item 缺失」**：CPS UI 要求每 item 必答、不可跳过/省略，117 items 无 item 缺失（物理页 68）。Class 3。暂定 `SUPPORTED`（设计层面）。Scope：interactive 机考设计；反向含义——缺失率被设计归零时丧失缺失率行为信息。
2. **UIE-NEW-B「仪器行为收敛设计保障可比性」**：agent 对任意作答收敛回应，所有学生面临相同后续刺激（物理页 57）。Class 3。暂定 `PARTIAL`（设计声明，无行为数据验证）。Scope：CPS 类 agent 交互测评。
3. **UIE-NEW-C「agent 替换真人仅小幅移动分数」**：computer agent → human agent 分数差异统计显著但很小、实际无关（物理页 50–51）。Class 2/4。暂定 `PARTIAL`（转述未出版手稿、无效应量）。Scope：预备反应集受限的协作任务；不覆盖自由作答场景。
4. **UIE-NEW-D「虚拟 agent 化成绩是面对面协作的中等预测因子」**：虚拟单元成绩与面对面真人协作表现中度相关（物理页 51）。Class 4。暂定 `PARTIAL`。Scope：CPS 构念效度；无 r 数值。
5. **UIE-NEW-E「机考平台经验对产品分数贡献极小且因果不明」**：自报 ICT 使用/能力与 CPS 成绩差 29/11 分，但解释量仅 0.6% 方差，方向不明（物理页 86–88）。Class 4。暂定 `PARTIAL`。Scope：15 岁学生、CPS；横断面相关非因果。
6. **UIE-NEW-F「问卷 non-response 不调整的报告实践」**：本卷问卷分析不做 non-response 调整，覆盖差异大时需谨慎（物理页 175）。Class 3。暂定 `SUPPORTED`（报告实践层面）。Scope：PISA 卷宗惯例。

## 未决项 / 待回查

- 「65/103、38 题」量化模式效应：回查 `PISA 2015 Technical Report (OECD, 2017b)` 或 field trial 专项报告，再行钉实。
- Box V.2.1 转述研究若已发表（Herborn, Mustafic & Greiff），应取得原文以补效应量。
