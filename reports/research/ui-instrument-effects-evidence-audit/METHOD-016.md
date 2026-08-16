# METHOD-016 提取笔记 — Arslan et al. 2020 (EMIP) D&D 题目特征效应实验

> 供「UI 仪器效应证据审计」（Wayfinder #5，GitHub Issue #5）最终综合使用。审计角色：E6 编辑综合（UIE-10）二手引用的原始实验，Class 2/4 最切题。全部页码为本地 PDF 物理页（= 印刷页 − 4；如 PDF p.1 = 印刷 96）。

## 头部

- **Source ID**: `METHOD-016`
- **本地路径**: `sources/library/papers/methods/2020_Arslan_DragDrop.pdf`
- **完整书目**: Arslan, B., Jiang, Y., Keehner, M., Gong, T., Katz, I. R., & Yan, F. (2020). The Effect of Drag-and-Drop Item Features on Test-Taker Performance and Response Strategies. *Educational Measurement: Issues and Practice*, 39(2), 96–106. DOI: `10.1111/emip.12326`.
- **书目核对**: catalog（`sources/catalog.yaml` METHOD-016 条目）与 PDF 首页一致的字段：标题、年份、venue（EMIP 39(2), 96–106）、DOI（PDF 水印 URL `10.1111/emip.12326` 一致）、6 位作者数量。**不一致处（不改 catalog，仅标注）**：两位作者姓名拼写不同——catalog 记 `Ying Jiang` / `Ting Gong`，PDF 首页为 **`Yang Jiang` / `Tao Gong`**（PDF p.1 作者行原文 "Burcu Arslan, Yang Jiang∗, Madeleine Keehner∗, Tao Gong, Irvin R. Katz, and Fred Yan"）。建议综合时以 PDF 首页为准核对 catalog。
- **与审计内其他 Arslan 文献的区分（重要）**: 本论文是 **476 名成人、数学 D&D、组间随机** 实验（PDF p.3），与 UIE-01/02 引用的 `B7`（Arslan et al. 2026, *Contemporary Educational Psychology*, 443 名八年级学生、ELA、组内设计）是**同一作者群的两篇不同研究**，不可混用；审计结论速览中「B7，OR=1.40」的效应量不属于本论文（本论文无 OR 类效应量）。本论文是 `E6` 编辑综合（UIE-10）所引 "Arslan et al., 2020" 的原始实验。

## 研究概览

- **研究问题**: (1) D&D 题目的表面设计特征是否以构念无关方式影响被试表现与答题过程；(2) 被试是否使用认知高效策略、题目设计是否影响策略选择。
- **样本**: 500 名成人（Amazon Mechanical Turk，≥高中同等学历；52.10% 学士）；**24 名因 process data-capturing issues 被排除**，最终 **476 名** 进入分析（女性 274、男性 201、其他 1；M_age = 32.26, SD = 4.88）(PDF p.3)。
- **设计**: **组间随机实验**（作者明示用组间而非组内，是为了贴近运营测验中「每名考生面对一致设计」的体验；PDF p.3）。随机分入 5 条件：Control N=98、Targets first N=95、Swapped content N=92、No problem statement N=93、Modified problem statement N=98（表 1，PDF p.4）。随机化平衡检验：性别 χ²(4)=4.479 p=.345、教育 χ²(12)=9.359 p=.672（PDF p.6）。
- **任务与材料**: 先答 10 道已发布 Praxis 单选中数学题（前测控制先验数学知识），再答 10 道分类型 D&D 数学题（所有被试同序；不可回退上一题；每题至少 5 次 D&D 动作；二进制评分——全部 target 正确得 1 分，否则 0；作者明示「本研究的目的是检验不同 D&D 设计是否以构念无关方式影响表现，而非评估数学能力」；PDF pp.3–4）。**题目内容在所有条件间完全一致**（"The content of the D&D item variants was identical across conditions"）(PDF p.4)。Cronbach's α：control .68 / targets first .65 / swapped content .61 / no problem statement .69 / modified problem statement .74，总体 .69 (PDF p.4)。
- **四个操纵**（相对 control，control = 大尺度运营测验常见设计：sources 在上、to-be-solved 数学对象为 sources、题干含问题陈述、陈述含 1 个比较数 × 3 条语句；PDF pp.4–5）:
  1. **Targets first（空间布局）**: targets 置于题干后、sources 前（纯表面布局变化；预期不影响分数）。
  2. **Swapped content（source/target 内容对调）**: 比较语句变 sources、数学对象变 targets（3 sources × 5 targets）；检验策略受物理控制功能还是认知功能驱动。
  3. **No problem statement**: 题干删去问题陈述，由 target 标题传达决策信息。
  4. **Modified problem statement**: 陈述含 3 个不同比较数（如 less than 11 / equal to 12 / greater than 15），增加心智计算量（作者框架为构念相关难度变化）。
- **变量**:
  - **产品分数（estimand）**: 每题 0/1，10 题总分（表 1，PDF p.4）。
  - **过程指标**（定义于 PDF p.5）: First pause = T(首次拖动 source) − T(item-loaded)；Transition pause = T(放下第 n 个 source) − T(开始拖动第 n+1 个 source)；Dragging time = T(放下第 n 个 source) − T(开始拖动第 n 个 source)；另计每题 D&D 动作数与题目完成时间（对数变换）。
  - **策略分类**（PDF pp.5–6）: 从动作序列清洗（剔除未完成拖动与修订/移动动作；80% 题目以最少 5 动作完成，仅 20% 序列被清洗，平均动作数 5.34, SD .96, 最大 29）后，分 source-focused / target-focused / mixed。策略类估计仅基于 3,070 条序列（4,718 条中的 65.07%；1,562 条 [33.11%] 为 mixed、87 条 [1.84%] 无法归类；PDF p.6）。
  - **缺失/数据质量指标**: process-data 捕获失败排除（24/500）、完成时间 IQR 离群排除（8%）、策略分析的序列子集。
  - 统计：线性/广义线性混合模型（lme4），condition 固定效应 + 被试/题目随机截距，control 为参照；分数模型含 age 与前测分协变量（ΔAIC 判定，PDF p.6）。

## 核心发现（按四类主张分组）

### Class 2（行为改变）— 最强证据：表面设计操纵移动过程指标与策略分布

1. **所有四个设计操纵都移动了至少一个过程指标**；同一内容、仅改表面特征即可改变动作/时序分布 (PDF pp.6–8)。这是 UIE-10 引用的核心实证。
   - 动作数：仅 Swapped content 显著更多，B = .208, SE = .056, t(472) = 3.755, p < .001；其余条件无差异 (PDF p.7)。
   - 完成时间（对数，控制动作数；剔除 8% IQR 离群）：Swapped content B = .155, SE = .045, t(468) = 3.409, p < .001；Modified problem statement B = .132, SE = .045, t(463) = 2.974, p = .003；Targets first B = .070, p = .121；No problem statement B = −.042, p = .350 (PDF p.7；数值表 2，PDF p.8)。
   - First pause：Modified problem statement B = .130, SE = .059, t(462) = 2.191, p = .029（显著更长）；No problem statement B = −.115, p = .055（边际更短）；Targets first B = .059, p = .320；Swapped B = .079, p = .189 (PDF pp.7–8)。
   - Transition pause：Targets first B = .073, SE = .036, t(487) = 2.054, p = .041；Modified problem statement B = .104, SE = .035, t(485) = 2.963, p = .003；Swapped B = .026, p = .462；No problem statement B = .000, p = .999 (PDF pp.7–8)。
   - Dragging time：仅 Swapped content 显著更长，B = .264, SE = .036, t(474) = 7.398, p < .001；Modified problem statement B = .065, p = .063 (PDF pp.7–8)。
   - 引文: "participants spent significantly more time on items in the swapped content and modified problem statement conditions compared to the control condition when number of D&D actions was controlled for" (PDF p.7)。
2. **策略分布被设计移动**：target-focused（认知较不高效）对 source-focused 的对数优势比——Swapped content B = 4.690, SE = .248, z = 18.918, p < .001；No problem statement B = .922, SE = .218, z = 4.233, p < .001；Targets first B = .0005, p = .998；Modified problem statement B = .284, p = .206 (PDF p.7)。除 Swapped content 外各条件最常用策略均为 source-focused（图 3，PDF p.8）；但注意作者说明 Swapped content 条件下算法中的 target-focused 与其余条件的 source-focused 认知过程相同（PDF p.7）。
3. **「任务类型权变」在本论文不可判**：本研究只用了分类型（categorization）D&D 数学题，未变化任务类型；UIE-01（B7，ordering vs categorization 方向性差异）的权变结论必须由 B7 支持，本论文不能替代也不能反驳。但本论文显示「具体哪个过程指标被移动」取决于设计特征种类（布局→transition pause；内容对调→dragging time/动作数/完成时间；题干信息量→first pause/transition pause/分数）。

### Class 4（学习/构念与 estimand）— 分数被部分设计操纵移动，且方向/构念性质因特征而异

1. **分数被内容/题干组织特征移动，但不被纯空间布局移动**：
   - Modified problem statement（题干比较数 1→3，作者框架为构念相关难度）：分数显著更低，B = −.450, SE = .218, z = −2.064, p = .039 (PDF p.6)。
   - Swapped content（source/target 内容对调，作者明确判定为构念无关）：分数边际更低，B = −.428, SE = .221, z = −1.932, p = .053，预测概率约低 5 个百分点 ("the predicted probability of score in the swapped content condition was almost 5 percentage points lower than the predicted probability of score in the control condition", PDF p.7)。作者结论：该操纵 "could affect test-taker performance in a construct-irrelevant way since lower scores and more item completion time were not related to the construct, but to the design of the items" (PDF p.9)。
   - Targets first（纯空间布局）：分数无差异，B = −.162, p = .462；完成时间 B = .070, p = .121；策略 B = .0005, p = .998。作者："surface-level spatial layout manipulation did not affect scores or item completion time, suggesting that making such a design change would probably not affect test-taker performance in a construct-irrelevant way, at least with this type of item content" (PDF p.8)。
   - No problem statement：分数 B = .163, p = .467、完成时间 B = −.042, p = .350 均无差异 (PDF p.7)。
2. **过程–产品解离（指标动、分数不动）**：Targets first 与 No problem statement 条件下过程指标已改变（transition pause 分别 B=.073 p=.041；target-focused 策略 B=.922 p<.001），产品分数与完成时间均未动 (PDF pp.7–8, 9)。这为「过程指标变化不必然意味着 estimand 变化」提供反方向证据（与 UIE-02 中 B7「drop-down 分数更高但交互更多」的解离方向相反）。
3. **同内容、同分数构念，仅表面特征差异即可移动分数分布**：Swapped content 的 ~5pp 分数差与 Modified problem statement 的显著分数差是设计驱动的 estimand 位移；作者据此给出设计建议：source/target 内容安排要匹配心理表征（"Decisions about which information to use as sources and which to use as targets should consider the alignment between mental and external representations of the problem"），并明示增加题干比较数可用于「以构念相关方式提高难度」（PDF p.10 Implications）。

### Class 3（仪器信度与缺失）— 过程数据完整性依赖仪器与清洗决策

1. **过程数据捕获失败直接造成被试级缺失**：24/500（4.8%）因 process data-capturing issues 被排除出**全部**分析（"Twenty-four participants were excluded from data analyses due to process data-capturing issues"）(PDF p.3)。即事件日志不完整 = 整被试剔除，而非局部补缺失。
2. **完成时间分析的清洗决策**：8% 的题目完成时间被按 IQR 离群剔除（"We first excluded outliers (8%) that were outside the interquartile range"）(PDF p.7)。
3. **策略类估计建立在选中的子集上**：33.11% 序列为 mixed、1.84% 无法归类，策略分析仅覆盖 65.07% 的序列 (PDF p.6)；且分类前清洗掉修订/未完成拖动动作（只取每个 source/target 的首次完整动作）——**行为空间本身被算法设计截断**（"did not include any partial D&D events or any later revisions to initial dropped locations", PDF pp.5–6）。策略类推断是对选择性子集的推断。
4. **信度大致跨设计变体保持**：α .61–.74（各条件）与 .69（总体）被作者判定 "satisfactory in all five experimental conditions" (PDF p.4)。注意：这是 10 题、每条件 n≈92–98 的 α，仅能说明内部一致性未随设计变体崩塌，不能当作信度等价证据（Swapped content 最低 .61，与分数边际降低方向一致，但作者未讨论）。
5. 作者未报告事件采样率、日志格式或捕获失败的根因，也未量化跨浏览器/设备捕获一致性——仪器级可靠性细节仍是白盒缺口（与本审计 Class 3 总体结论一致）。

### Class 1（可用性/偏好）— 无贡献

本论文**没有测量**可用性、满意度或偏好；Implications 部分是专家设计建议（如 "Presenting targets first or sources first makes no difference to performance. Therefore, either version can be used depending on other constraints"）而非用户偏好证据 (PDF p.10)。Class-1 实证可用性主张保持 `UNRESOLVED`，本论文不改变该状态。

## 边界与局限

- **作者自述局限**（PDF p.10, "Limitations and Future Directions"）: (1) 被试为 MTurk 成人，对学龄学生在运营测验中的表现与策略效应可能不同，需以学龄被试复现；(2) 数学题目未必推广到其他领域（作者认为 Implications 可作为分类型 D&D 题的一般原则）；(3) 只研究系统性策略，mixed（非系统）策略机制未探究。
- **设计边界**：组间设计（分数效应含被试间方差；靠随机化 + 前测协变量控制）；题目相对容易且不依赖高深数学；部分条件（targets first、swapped content、modified PS 的时序分析）作者明示为 exploratory（PDF pp.4–5）；策略分类算法简化（修订被剔除），且部分类含 "partial" 序列规则（28%/20% 的 partial 判定，PDF pp.5–6）。
- **领域/格式边界**：数学分类型 D&D，**不是阅读理解作答 UI**，也不是阅读任务；到本项目双栏「左文右题」baseline 的一切迁移为 `PROJECT-INFERENCE`。机制（mental–external representation mismatch、Fitts' law 距离、题干信息负荷）具一般性，但具体量级与方向不可直接外推。
- **任务类型权变不可判**（见 Class 2 第 3 条）：本实验未操纵任务类型。
- **效应量形式**：只报告混合模型 B 系数（logit / log-seconds），无 OR、无 d、无标准化效应量；与 B7 的 OR=1.40 不可直接比较。
- **外部信源核对**：摘要级结论与正文一致（摘要 PDF p.1 的 (a)(b) 两结论与 Results/Discussion 相符）；无 `ABSTRACT-ONLY` 标记项。

## 对审计的用途

### 支持/反驳/限定既有 UIE 条目

- **UIE-10（E6 编辑综合，原 `PARTIAL`）→ 可升级**。原 verdict 的唯一理由即「Arslan et al. 2020 未本地持有、实证主张二手」。现原始实验已本地持有并读毕：E6 的编辑断言「仅改题目表面设计、内容不变，显著改变过程数据指标」直接由本论文支持（内容跨条件完全一致 PDF p.4；四个操纵均移动至少一个过程指标 PDF pp.6–8）。建议 verdict 升级为 `SUPPORTED`（scope：成人、数学分类型 D&D、组间设计；"surface design" 需限定为内容/组织/题干特征——纯空间布局只动 transition pause 未动分数）。E6 编辑中「构念无关过程数据方差来源包括内容、措辞、显示设计」部分被支持（内容组织与题干信息量确实移动过程数据；纯显示布局效应弱）。
- **UIE-01/02（B7）**：本论文提供**收敛但不替代**的 Class 2 证据；且提供与 B7 相反方向的「过程–产品解离」（指标动、分数不动，见 Class 4 第 2 条）——强化「过程指标与产品分数的关系方向不固定」这一总体结论（UIE-02 的 scope 边界本来就有此句）。**必须防止综合时把两篇混淆**：B7=八年级 ELA 组内、METHOD-016=成人数学组间。
- **UIE-28（METHOD-013 边界注「不能替代 gated 的 Arslan 2020 格式实验」）**：该 gate 已解除——METHOD-016 即为被引格式操纵实验；METHOD-013 描述性 NAEP 过程数据与 METHOD-016 操纵实验的互补关系可明确写出。
- **UIE-23（WCAG 2.2 SC 2.5.7 拖动约束）**：本论文提供直接实证——D&D 反应格式本身携带过程效应（本论文）与潜在分数效应（swapped content ~5pp 边际）——「single-pointer 替代路径本身是不同反应格式、携带不同过程指标」的注记由本论文直接支持。
- **UIE-24（reflow/zoom，滚动约束）**：本论文有两条直接相关证据——(a) 需要滚动的两个题 transition pause 普遍更长（"transition pauses were generally longer for the two items that required scrolling the screen"，PDF p.7）；(b) Implications 明确建议最小化 sources 与 target 标题距离、避免滚动（"test takers should not have to scroll to see the sources and targets; instead, it is better to choose a version that minimizes the distance between the sources and the target headings so that no scrolling is required"，PDF p.10），理由含 Fitts' law 距离效应（dragging time B = .264 归因于屏上距离，PDF pp.8–9）。对双栏滚动 passage+question baseline 的含义：滚动需求会改变交互时序分布。
- **Class 1 结论（审计第 149 行 `UNRESOLVED`）**：本论文未测量可用性/偏好，状态不变。
- **审计第 173/184/245 行**：其中「E6 最强单一论断二手化、待 Arslan 2020 获取」的待决项可勾除；「Arslan 2020 是 Class 2/4 最切题实验、居 Acquisition queue 之首」的表述在综合时可改为「已读毕并入库」。
- **第 9 行结论速览**的「B7 OR=1.40」保持 B7 归属，勿与本论文混淆。

### 建议新增 UIE 条目草稿（编号接续 UIE-30）

- **UIE-31**（Class 2 + 4）：操纵题目表面特征（内容对调 / 题干信息量 / 空间布局），内容恒定，可同时移动过程指标与产品分数；分数移动既可为构念无关（swapped content B=−.428, p=.053，预测概率 ~5pp 低，作者判定构念无关）也可为构念相关（题干比较数 1→3，B=−.450, p=.039）。Pages: PDF pp.1, 6–9。暂定 verdict: `SUPPORTED`（限成人、数学分类型 D&D、组间随机实验）。Scope: 不是阅读 UI；到阅读 baseline 的迁移为 `PROJECT-INFERENCE`。
- **UIE-32**（Class 2，过程–产品解离反方向）：纯空间布局（targets first）与删除问题陈述（no problem statement）移动过程指标（transition pause B=.073, p=.041；target-focused 策略 B=.922, p<.001）但不移动分数（p=.462/.467）与完成时间（p=.121/.350）。Pages: PDF pp.7–9。暂定 verdict: `SUPPORTED`。Scope: 同 UIE-31；强化「过程指标变化不能直接推出 estimand 变化」。
- **UIE-33**（Class 3，过程数据完整性与清洗）：4.8% 被试因过程数据捕获失败整被试剔除；完成时间分析剔除 8% IQR 离群；策略估计仅基于 65.07% 的序列（33.11% mixed + 1.84% 不可归类排除）；策略分类前算法剔除修订/未完成动作（行为空间被算法截断）；α 跨设计变体 .61–.74。Pages: PDF pp.3, 5–7, 4。暂定 verdict: `SUPPORTED` as reported study operations。Scope: 单研究操作；证明过程指标估计量天然建立在选择性子集上，且完整性是仪器属性。
- **UIE-34**（Class 2/4，距离与滚动）：source–target 屏上距离与滚动需求改变交互时序——dragging time 仅在 swapped content（距离更大）显著更长（B=.264, p<.001，作者归因 Fitts' law）；需滚动的两个题 transition pause 更长；作者建议 no-scroll 布局。Pages: PDF pp.7–10。暂定 verdict: `SUPPORTED` within study（Fitts' law 归因是作者解释；滚动–transition 观察为描述性）。Scope: 对双栏滚动布局 baseline 的直接约束——滚动需求进入行为空间与时间分布。

## 备注

- 本笔记为最终综合的输入工件；未修改 catalog、checksums、审计主文件、crosswalk 或任何其他文件。
- 唯一待综合者拍板项：catalog 两位作者姓名拼写（Yang/Tao vs Ying/Ting）与 PDF 首页不一致，建议核对后以 PDF 为准修正 catalog（属于 catalog 变更流程，不在本笔记内执行）。
