# 提取笔记 — METHOD-033 | Moon et al. 2022, Split-Attention in Computer-Based Assessment

## 头部

- **source ID**: `METHOD-033`
- **本地路径**: `sources/library/papers/methods/2022_Moon_SplitAttention.pdf`（28 页，SHA-256 见 `sources/catalog.yaml`，本次未改动）
- **完整书目**（与 `sources/catalog.yaml` 及 PDF 首页核对一致，无出入）:
  - Moon, J. A., Lindner, M. A., Arslan, B., & Keehner, M. (2022). Investigating the Split-Attention Effect in Computer-Based Assessment: Spatial Integration and Interactive Signaling Approaches. *Educational Measurement: Issues and Practice*, 41(2), 90–117. DOI: 10.1111/emip.12485
  - PDF 首页打印页 pp.90–117；**页码约定**：本笔记正文引用一律用 PDF 物理页，并在首次出现处给出打印页对照。映射：物理页 = 打印页 − 89（物理页 1 = 打印 90，… 物理页 28 = 打印 117）。该映射由 `pdfinfo` 总页数 28 与页脚打印页号核对得出。

## 研究概览

- **研究问题**：计算机化评估（CBT/CBA）中，减少 split-attention 的两类多媒体设计操纵——(a) 空间整合（spatial integration：把图例文字嵌入图形内部）与 (b) 交互式信号（interactive signaling：悬停某答案选项时高亮图中对应部分）——是否提升解题效率（以 time on task 为代理）并影响成绩；效果是否随先验知识（prior knowledge）变化（物理页 2–4，打印 91–93）。
- **设计**：混合 2×2 随机实验。spatial integration 为被试内变量（nonintegrated vs integrated）；interactive signaling 为被试间变量（nonsignaled vs signaled）。24 个形式经 balanced Latin square 配平，被试随机分配；基线 = nonintegrated & nonsignaled（物理页 4–5，打印 93–94）。
- **样本**：397 名 Amazon Mechanical Turk 美国成人（20–45 岁，M = 32.2, SD = 5.0），$7 报酬，2019 年 11 月三周内分批投放；nonsignaled n = 182、signaled n = 215；一个 signaled 形式因技术错误分到 40 人（作者注释不影响配平，物理页 5/12，打印 94/101）。人口学见 Table C1（物理页 27，打印 116）。
- **任务与材料**：12 道几何单项选择 MC 题（图形+图例+选项，正文明确存在"图形↔图例"与"图形↔选项"两个 split-attention 来源，物理页 4，打印 93）；另测 10 题 Praxis I PPST 数学先验知识测验（α = 0.74；本次样本，物理页 5，打印 94）。程序：练习项（signaled 条件强制至少试用 hover 一次才能进入实验），12 题固定顺序、不可回看、无时间限制、每题必答（物理页 6，打印 95）。
- **变量**：
  - 产品分数：每题 dichotomous 正确/错误（GLMM binomial）。
  - 过程指标：time on task（秒，log 变换 LMM，主因变量；定义为题出现到点击"下一题"按钮的时间）；hover frequency（Poisson）；hover time（log 变换 LMM）。
  - 缺失/质量指标：disengaged 参与者剔除、快速猜测（rapid guessing）观测剔除、上阈值（超长时长）观测剔除、7 人 hover 数据技术性缺失（详见 Class 3）。

## 核心发现（按四类主张分组）

### Class 2 — 行为改变（本论文最核心、证据最强的一类）

- **F2-1 空间整合显著降低解题时间（过程指标），且效应随先验知识增强**：log-time 上 spatial integration 主效应 γ1 = –0.27, t = –5.07, p < .001；原始描述均值 nonintegrated vs integrated = 74.7s vs 55.4s（nonsignaled 条件）、67.8s vs 46.2s（signaled 条件）（Table 1, 物理页 7，打印 96；模型结果物理页 7 正文与 Table 2 物理页 8，打印 97）。先验知识主效应 γ3 = 0.07, t = 4.70, p < .001（高 PK 者花更长时间）；integration × PK 交互 γ5 = –0.02, t = –2.83, p = .005——**高先验知识者从空间整合中获益更多**。英文原文："spatial integration significantly increased item-solving efficiency indicated by reduced time on task, especially for test takers who had higher prior knowledge"（摘要，物理页 1，打印 90）；"the time on task difference between nonintegrated and integrated items increased with increasing levels of prior knowledge"（物理页 8，打印 97）。
- **F2-2 交互式信号（hover）单独不改变行为，只在空间整合项内生效**：signaling 主效应 γ2 = –0.08, t = –1.40, p = .163（单独可用 hover 功能不显著降时）；integration × signaling 交互 γ4 = –0.12, t = –2.71, p = .007——**hover 的时间收益仅出现在 integrated 项**（物理页 7，打印 96；讨论物理页 10，打印 99）。英文原文："the hover feature was only effective in items with spatial integration (see Figure 2a)"（物理页 7，打印 96）。
- **F2-3 新 UI 功能的自发采用率极高，且与条件化使用并存**：signaled 条件 208 人中 206 人至少用 hover 一次；每项平均 hover 8.3 次（SD = 4.8）、每项累计 hover 31.3 秒（SD = 32.0）（物理页 7，打印 96）。使用量随布局变化：integrated 项 hover 频率更低（γ1 = –0.11, z = –2.03, p = .042）、hover 时间更短（控制频率后 γ1 = –0.22, t = –2.42, p = .032）（物理页 7 正文、Table C3 物理页 28，打印 117）——**布局改变既改变目标行为（解题），也改变对 UI 辅助功能本身的使用量**。
- **F2-4 作者声明的机制**：spatial integration 减少"图例↔图形"的视觉搜索与心理整合；hover 减少"选项↔图形"的视觉搜索；但作者同时明确 **交互功能本身消耗额外的知觉/运动过程（hover 需要计划和执行鼠标动作），可能构成新的 extraneous load**："interacting with the hover feature takes additional time because participants have to plan and execute additional perceptual and motor processes such as hovering their mouse over an icon. This could also add a new source of extraneous load"（物理页 10，打印 99）。
- **F2-5（无自报类过程证据）**：本研究刻意用 time on task 代替自报认知负荷，"a decision made in order to more faithfully replicate typical test-taking procedures and build our conclusions on a more objective outcome"（物理页 5，打印 94）——与 `E6`/`B7` 的"过程指标需验证"框架一致，但本论文没有自我报告、眼动或出声思维验证通道。

### Class 4 — 学习/构念与 estimand

- **F4-1 布局操纵在时间维度有强效应，但在产品分数上无显著主效应（null 结果，须如实保留）**：spatial integration 对成绩 γ1 = 0.24, z = 1.67, p = .094；signaling 对成绩 γ2 = 0.20, z = 1.67, p = .094；integration × signaling 对成绩交互不显著 γ4 = –0.02, z = –0.17, p = .863（物理页 7–9，打印 96–98；Table 2 物理页 8）。描述均值 0.48/0.51/0.52/0.54（Table 1, 物理页 7）——**UI 变化移动过程指标的同时，成绩分布基本不动**：这是与 `B7`（格式移动成绩，OR=1.40）方向不同、互补的过程-产品分离证据。
- **F4-2 但对高先验知识子群，signaling 显著提升成绩（子群依赖的 estimand 移动）**：signaling × PK 交互 γ6 = 0.08, z = 2.04, p = .041（物理页 9，打印 98；Figure 3）。integration × PK 对成绩交互不显著 γ5 = 0.02, z = 0.64, p = .525。英文原文："the availability of the interactive signaling feature did improve performance in test takers who had higher prior knowledge"（物理页 10，打印 99）。
- **F4-3 作者对构念/效度含义的表述是条件化的、假设性的，不是实证结论**：认为整合手段"may also benefit construct validity if it can reduce and equalize asymmetric extraneous load arising from split attention effects"（物理页 10，打印 99）；总体框架是"减少构念无关 extraneous load → 改善 score interpretation 的 validity"（物理页 2–3，打印 91–92；物理页 10，打印 99）。且明确集成手段**不能补偿构念知识缺失**："integration aids cannot compensate for a lack of construct-relevant knowledge, but can improve item-solving efficiency"（物理页 10，打印 99）。**用本文断言"布局优化提升测验效度"属 `OVERSTATED`；本文支持的是"布局优化提升效率、对成绩无主效应、对高 PK 子群可能提升成绩"。**
- **F4-4 设计伦理/泄露边界**：hover 信号应用到所有选项（含干扰项），不泄露答案："applied to every answer option (regardless of whether it was the key or a distractor)"（物理页 3–4，打印 92–93）；并与 multimedia-signaling 与 assessment-signaling（提示正确答案）的语义差异做了明确区分（物理页 3，打印 92）。作者还将两种操纵声明为"broadly aligned with universal design"（物理页 5，打印 94）——这是**对齐声明，非实证**。

### Class 3 — 仪器信度与缺失

- **F3-1 时间类过程指标的分析样本由显式数据质量筛查决策塑造**：以每题平均时间 15% 为下阈值剔除快速猜测（引用 Wise & Ma, 2012）；34 名被试（34/397 ≈ 8.6%）因 ≥33% 响应为快速猜测被整体判为 disengaged，整组剔除 408 观测；另剔除 126 个快速猜测观测与 33 个超上阈值观测（mean + 2.5 SD of log-time）——时间分析最终用 4,197 / 4,764 观测；成绩分析只剔除 disengaged 与快速猜测（4,230 观测），**不剔除上阈值**（物理页 6，打印 95）。作者对不对称剔除的论证："taking longer time to solve an item should not necessarily deem a response to be likely invalid"（物理页 6，打印 95）。
- **F3-2 技术性缺失真实存在**：signaled 条件 7 名被试 hover 数据因技术问题不可用（208 → 201 人进入 hover 分析，物理页 5，打印 94；物理页 6，打印 95）。hover 分析从 2,308 观测减至 2,054（频率）/ 1,974（时间）。
- **F3-3 剔除规则是 item×condition 特异的**："All thresholds were defined separately for each item in the spatial integration and interactive signaling condition"（物理页 6，打印 95）——**同一过程指标的可比性取决于每格自定义的阈值**，跨条件直接比较时间分布时须注意这一点。
- **F3-4 报告不完备（对审计的 replicability 启示）**：正文与附录未报告鼠标采样率、hover 的精确命中判定、浏览器/设备等实现细节；这与审计文件对 `C6` 的同类批评一致（见审计 Limitations 段），`METHOD-033` 是"过程指标本身是仪器设计产物"的又一实例。

### Class 1 — 可用性/偏好

- **F1-1 无满意度/偏好量表**：本研究没有任何 self-report 可用性或偏好测度。唯一相关证据是 hover 功能的自发采用率（206/208 = 99.0%），作者仅以行为推断"participants ... likely found it useful for solving the items"（物理页 10，打印 99）——**这是行为推断，不是偏好证据**；用作偏好/满意度主张须标 `PROJECT-INFERENCE` 或 `OVERSTATED`。训练程序（signaled 条件须先试用 hover 才能进入实验）也说明 99% 采用率部分由强制试用+教程塑造，不能当作自然使用基线（物理页 6，打印 95）。

## 边界与局限

- **任务域边界（最重要的外推限制）**：单一题型（单选 MC）、单一布局、单一内容域（数学几何），非阅读、非语言理解。作者明确声明："we targeted a rather specific item type (single-selection multiple-choice), item layout, and content area (geometry)"（物理页 10，打印 99）。**任何"布局操纵影响阅读作答 UI"的迁移均为 `PROJECT-INFERENCE`**。
- **人群边界**：美国成人 MTurk（20–45 岁，教育程度集中在副学士/学士，Table C1 物理页 27）；非 K-12、非考试情境的在校学生。作者引用 MTurk 效度文献为其辩护，也列出 inattentiveness 的担忧（物理页 10，打印 99）。
- **测试情境边界**：无时间限制、可回看被禁止、每题必答、每格自定义数据清洗阈值（物理页 6，打印 95）——这些程序选择与真实大规模考试（有时间压力、有跳题策略）不同；time on task 在有时间限制下的含义会改变。
- **测量边界**：time on task 是作者自选的"更客观"效率代理，但作者承认精确认知机制需 eye-tracking 验证："the precise nature of the current exploratory findings should be further investigated in detailed eye-tracking research"（物理页 10，打印 99）。
- **成绩测度信度**：12 题实验测验 Cronbach's alpha = 0.68 不高，作者说明与题量少、几何概念异质有关，且强调单题观测才是分析单元（物理页 5，打印 94）。
- **作者未声明的边界**：hover 功能依赖鼠标定点（桌面设备），触屏/键盘导航/无障碍替代路径不在本文范围；signaling 条件内一个形式被技术错误分到 40 人（物理页 12 注释 1，打印 101）。

## 对审计的用途

- **支持并强化 `UIE-01/02`（`B7`，格式维度）**：`METHOD-033` 与 `B7` 同属 ETS 同一研究脉络（本文作者含 Arslan；引用了 Arslan et al. 2020），但在**布局/呈现维度**独立复现了"UI 变化显著移动过程指标、产品分数主效应弱/子群依赖"的模式（F2-1 vs F4-1/2）。据此可把 `B7` 的 process–product dissociation 从单一格式研究升级为跨维度模式（格式与布局皆然），并补强审计 Class 2 总述（审计文件 151–157 行）与 Class 4 的"产品分数可被 UI 移动"判断——不过 `METHOD-033` 的成绩主效应是 null，方向与 `B7` 相反，说明"分数移动"不是布局操纵的必然结果，只能作为子群/条件依赖现象陈述。
- **填补 Class 2 的"布局操纵"空白（审计文件 157 行明示的 gap）**：本地 corpus 此前无"操纵 layout 并测量因果行为效应"的实验；本文是第一个（几何 MC/CBT、被试内随机），把"布局改变行为"从纯 `PROJECT-INFERENCE` 提升为跨域 `SUPPORTED`。但注意：不是阅读 UI，迁移仍标 `PROJECT-INFERENCE`。
- **直接对话 `UIE-24`（WCAG SC 1.4.10 Reflow）与我们的 dual-pane baseline**：spatial integration 的本质是把"空间分离的双源信息"整合为"单源"；我们冻结的"左 passage + 右 question"双栏正是分离式布局原型，`METHOD-033` 提供了"分离布局本身带来可测量的过程代价（时间上升、高 PK 者更明显）"的实验证据；反过来，集成/折叠/就近呈现（如题目旁标注文本）是减少该代价的操纵，应纳入 baseline 变体选项的候选，并作为 `BENCH-E0` 可测的过程指标假设。
- **限定 `E6`/`STANDARD-001` 的框架引用**：本文的 validity 论断是条件化的（F4-3），不能作为"减少 split-attention 即提升效度"的经验依据；同时 `E6` 的"display design 是构念无关方差来源"在此得到一项随机实验的过程数据佐证（时间维度）。
- **对 Class 1 的作用**：强化审计结论"本地 corpus 无实证偏好证据"——本文连子群内的偏好测量都没有；hover 自发使用只是行为代理。
- **与队列中其他条目的关系**：与 `METHOD-032`（Ponce 2021 D&D 响应格式效应）同属"呈现/响应变体"实验簇；本文在数学域、Ponce 需另行确认域与题型后横向比较。

### 建议新增 UIE 条目草稿

1. **UIE-31（草案）** 布局的空间整合改变过程指标而不必然移动产品分数：嵌入图例文字的 integrated 布局显著降低解题时间（log-time γ = –0.27, t = –5.07, p < .001；74.7s→55.4s），效应随先验知识增强（integration × PK γ = –0.02, p = .005），但对成绩无显著主效应（γ = 0.24, z = 1.67, p = .094）。verdict：`SUPPORTED`。scope boundary：成人 MTurk、几何单选 MC、无时间限制 CBT、被试内随机；非阅读任务，迁移到阅读作答 UI 为 `PROJECT-INFERENCE`；null 成绩结果须与 `B7`（格式移动分数）并列呈现，不得合成"布局一定移动分数"。
2. **UIE-32（草案）** 交互式 UI 辅助功能（hover 高亮）的自发采用（206/208 ≈ 99%）与测量效应解耦：单独可用不降时（γ = –0.08, p = .163），仅在 integrated 项内生效（交互 γ = –0.12, p = .007），且对高先验知识者提升成绩（signaling × PK γ = 0.08, z = 2.04, p = .041）；交互本身构成额外知觉/运动负荷（作者明示）。verdict：`SUPPORTED`（行为/成绩两部分各自成立）。scope boundary：hover 依赖鼠标定点；其成绩交互为单一研究、探索性结论，跨子群外推须谨慎；"功能被使用 = 测量中性"不成立。
3. **UIE-33（草案，Class 3）** 时间类过程指标的分析分布由显式筛查决策塑造：8.6% 被试（34/397）因快速猜测被整体剔除（408 观测），逐项按 item×condition 自定义下阈值（15% 平均时间）与上阈值（mean+2.5SD），且时间与成绩分析采用不同剔除集（4,197 vs 4,230 / 4,764）；7 人过程数据因技术故障缺失。verdict：`SUPPORTED` as reported operations。scope boundary：单研究规则，不是统一标准；含义是"time on task 的样本、分布形状与跨条件可比性都是仪器+分析决策的产物"，呼应 `UIE-11/12/13` 的缺失依赖设计论，并提示 `BENCH-E0` 必须预先固定快速猜测/离群处理规则。

## 备注

- 本笔记仅作证据提取输入；未修改 `sources/catalog.yaml`、`sources/checksums.sha256`、审计主文件 `ui-instrument-effects-evidence-audit.md`、crosswalk 或任何其他文件。
- 页码全部经 `pdftotext -layout` 核对；无 `ABSTRACT-ONLY` 条目（全文已读）。表格数值（Table 1/2/C1/C2/C3）已逐格核对正文引用。
