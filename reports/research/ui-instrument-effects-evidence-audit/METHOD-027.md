# METHOD-027 提取笔记：Mangen, Walgermo & Brønnick (2013) 纸 vs 屏阅读理解

> 本文档是「UI 仪器效应证据审计」（Wayfinder #5）的逐篇一手证据提取笔记，作为审计资产 `ui-instrument-effects-evidence-audit.md` 的输入。页码一律为本地 PDF 物理页（= 期刊页 − 60）。

## 头部

- **Source ID**：`METHOD-027`
- **本地路径**：`sources/library/papers/methods/2013_Mangen_PaperVsScreen.pdf`
- **完整书目**：Mangen, A., Walgermo, B. R., & Brønnick, K. (2013). Reading linear texts on paper versus computer screen: Effects on reading comprehension. *International Journal of Educational Research*, 58, 61–68. DOI: 10.1016/j.ijer.2012.12.002
- **catalog 核对**：与 `sources/catalog.yaml`（ID `METHOD-027`，行 1850–1868）完全一致：作者、标题、venue（IJER 58, 61–68）、年份 2013、DOI 一致；PDF 首页（PDF p.1）再次核对一致。无出入，不改 catalog。
- **审计角色**：Class 4 模式实验一手证据；Acquisition queue B 组第 13 项（`human-tasks/wayfinder-5-ui-instrument-effects.md` 行 28，已入库）。

## 研究概览

- **研究问题**：挪威学校情境下，阅读技术界面（纸质 vs 电脑屏幕）对阅读理解的影响；作者明确把本研究定位为对「挪威国家阅读测评计划将采用的评分系统」的直接测试开发启示（PDF p.3）。
- **样本**：n = 72，挪威两所城市学校十年级学生（15–16 岁），43% 女性，作者描述为「middle-class Caucasian…homogenous with respect to socio-economic status and ethnicity」（PDF p.3）。
- **设计**：随机对照实验（RCT）。先做阅读理解 / word reading / 词汇三个 pretest（PDF p.3）；四周后 main survey 在班内随机分两组：Group 1 屏幕读 PDF、Group 2 纸读。**关键设计：两组都数字化作答**（"Both groups answered questions digitally/on screen", PDF p.4）——只有阅读呈现模态在两组间不同，作答格式恒定。
- **任务与材料**：两篇真实文本（一篇叙事 narrative、一篇说明 expository，各 1400–2000 词，约 4 页；摘要 PDF p.1 写 1400–2000，方法段 PDF p.3 写 1400–1600），纸屏格式与页数一致（PDF p.3）。每题 MC 为主、附少量短答 CR（12–20 题），按 PISA 五类理解过程归并为三类 aspect categories：access and retrieve / integrate and interpret / reflect and evaluate（PDF p.3）。作答时可回看文本；数字组可上下滚动并可在 PDF 与题目之间切换（PDF p.3）。时限 1 小时（PDF p.4）。
- **仪器**：15 英寸 LCD、60 Hz、1280×1024，Adobe Reader 9.4（Windows XP），学校日常用机；纸面 A4、黑色 14 pt Times New Roman、100% 缩放（PDF p.4）。
- **变量**：
  - 产品分数：main survey 阅读理解测试分（组间回归 outcome）。
  - 过程指标：**无任何过程/行为日志**——不记录滚动、不记录阅读时间、无导航数据。
  - 缺失指标：无逐题作答缺失数据；全员在时限内提交（PDF p.4）。
- **分析**：sequential regression（分块：词汇、word reading、阅读理解 pretest → 性别 → reading modality 哑变量），标准化 β；多重共线性/杠杆/异方差/残差正态性均已检查（PDF p.4）。

## 核心发现（按四类主张）

### Class 4 — 学习/构念与 estimand（本论文主贡献）

- **F4.1 阅读投递模态移动阅读理解分数分布（方向：纸 > 屏）**。在控制词汇、word reading、阅读理解 pretest 与性别后，reading modality 标准化 β = −.216, p = .025；加入该变量使解释方差增加 ΔR² = 4%（p = .025），总 R² = .42（PDF p.4 正文、PDF p.5 Table 2）。作者表述："reading modality was found to be statistically significant (b = −.216, p = .025) indicating that students who read texts digitally were more likely to receive lower scores on the reading comprehension tests compared to the students who read the texts on paper"（PDF p.5）。论文未报告主效应 Cohen's d；效应量以 β 与 ΔR² 为准，不另做换算。
- **F4.2 体裁不调节模态效应（阴性/反假设结果）**。作者假设说明文受模态影响大于叙事（PDF p.3 假设 2），未获支持：narrative vs expository × modality 交互 F(1,70) = .142, p = .707（PDF p.5）。即：在该样本与题目下，模态效应跨体裁方向一致。
- **F4.3 作者对政策/测验的结论句**："we should not assume that changing the presentation format for even short texts used in reading assessments will not have a significant impact on reading performance"（PDF p.7）——呈现格式变更即便对短文本也默认会移动表现，是作者给测试开发的政策结论。
- 机制解释（作者自己的、未测试的候选，不得当事实用）：滚动导致的「空间不稳定」损害文本心理表征（PDF p.5）；纸的固定空间/触觉线索支持文本空间表征，屏受限为「一次只见一页」（PDF p.6）；同屏双窗口（文本 + 题目）切换构成额外认知负担，而纸组是跨媒介切换（PDF p.6）；LCD 发光视觉疲劳（PDF p.6–7）。作者明确说数据无法判定这些机制（见 C3.2）。

### Class 3 — 仪器信度与缺失

- **F3.1 完成率：全员按时提交，无作答缺失**。时限 1 小时，"All students who took part in the experiment submitted their tests within this time limit"（PDF p.4）。样本小且任务负荷低，只说明该情境无缺失。
- **F3.2 过程通道完全缺失 → 效应机制不可判定（对审计的关键方法学例证）**。作者未记录数字组是否、在多大程度上使用滚动："We have no data showing whether or not, and to what extent, the students in the computer condition used the scrolling option when reading the texts. Hence, it cannot be eliminated that students in the computer condition scrolled during reading, and that this scrolling negatively impacted their comprehension performance"（PDF p.5）；未测量阅读时间（PDF p.6）；"It is impossible to determine from the data of the current study whether visual fatigue contributed to the poorer reading comprehension performance in the computer condition"（PDF p.7）。→ 没有过程日志，模态效应的机制归因只能停留在推测；作者建议未来用眼动等在线测量（PDF p.7）。
- **F3.3 随机化分组明显不平衡**：Paper n = 25 vs Computer n = 47（Table 1，PDF p.5）。pretest 组间无显著差异（vocabulary t(70) = −.41, p = .88；word-chain t(70) = .25, p = .80，PDF p.4），说明随机化平衡良好，但 25:47 的不平衡降低统计功效、扩大标准差影响，需随结论保留。
- **F3.4 题目信度**：本研究与 pretest 所有文本 Cronbach's alpha > .75（PDF p.4）。只覆盖产品分信度，不覆盖过程通道。

### Class 2 — 行为改变

- **F2.1 直接行为证据：无**。本研究没有任何交互日志/过程指标，不能直接证明「屏阅读改变行为分布」。
- **F2.2 设计事实（行为空间本身不同）**：数字组面对的是「可滚动 + 单页可见」的呈现，纸组是「整文在手」的固定布局；两组都数字化作答。作者对数字组"were able to scroll up and down the pages, and change between the PDF and answering questions"（PDF p.3）的描述说明：同一任务下，阅读媒介决定了可观察行为空间（滚动 vs 翻页/无滚动）——这正是本项目 baseline 要记录的 scroll 事件在文献中的呈现侧对应物。
- 候选行为机制（讨论层，未测）：滚动空间不稳定性（PDF p.5）、单页可见性限制整体概览（PDF p.6）、同屏窗口切换（PDF p.6）。这些是作者的解释假说，`PROJECT-INFERENCE` 级别，不得当作已证行为效应。

### Class 1 — 可用性/偏好

- **无贡献**。论文未测量满意度、偏好、主观负荷或可用性。唯一相关的是讨论中转述 Ackerman & Goldsmith (2011) 的他人发现——「纸质被感知为更适合费力的学习，屏幕被感知为适合浅层速读」（PDF p.6，转述，非本研究数据），不属于一手证据，不进入审计。

## 边界与局限

- **人群**：挪威 15–16 岁中产白人学生，n = 72，两所学校；单一国家、单一 SES/族群。
- **任务/材料**：线性叙事 + 说明文本各一篇（约 4 页、1400–2000 词），PISA 式 MC + 少量 CR；作答全部数字化；1 小时时限（低压力、非速度性）。
- **仪器**：2013 年的 15" LCD + Adobe Reader 9.4 PDF 呈现；现代设备、电子墨水（Kindle 类）、高分屏不可外推。纸面 A4 14 pt Times 与屏 PDF 100% 缩放在视觉呈现上并不完全等价（作者未报告实际屏上字体渲染尺寸）。
- **作者声明的局限**：未测阅读时间、未记录滚动、无法判定视觉疲劳/工效学贡献（PDF p.5–7）；文本较短，作者建议在更长文本上复制（PDF p.6）；建议结合客观阅读时间与眼动在线测量（PDF p.6–7）。
- **统计边界**：25:47 不平衡分组（F3.3）；效应量只有 β 与 ΔR²（无 d）；机制解释全部未测试。
- **不可外推处**：这是**投递模态（纸 vs 屏）**证据，不是作答 UI 变体（反应格式/布局/反馈）证据；不能由此推出「屏上作答 UI 的任一变体会移动分数」，只能推出「阅读呈现方式本身（含滚动、单页可见性）足以移动分数分布」。
- 后续相关一手证据（不在本笔记提取范围，供审计交叉引用）：同作者组的 Støle, Mangen & Schwippert (2020) 大样本儿童纸/屏实验已入库为 `METHOD-030`，是检验本研究效应在更大样本/不同年龄段上稳健性的直接后续。

## 对审计的用途

### 对既有 UIE 条目与待决问题的关系

- **支持 UIE-27（METHOD-012，ACT）**：审计结论速览中的「投递模式（纸/屏）会移动阅读分数分布」现获得第二个一手证据，且是 RCT（更强的因果设计）。互补性：METHOD-012 是操作性大规模考试的等值证据（d = .16–.22、速度性效应）；METHOD-027 是受控实验（β = −.216、ΔR² = 4%），并证明**在同一作答模式（全数字作答）内，仅阅读呈现不同即可移动分数**——这比 METHOD-012 更直接地切中「阅读 UI 呈现是测量仪器的一部分」这一主张。
- **与 UIE-29（METHOD-014 Goodwin）互补**：METHOD-014 显示纸/数字在过程行为层（划线、注释量）的差异；METHOD-027 显示产品分层的差异。两条证据分别覆盖行为与 estimand 两个层面。
- **与 UIE-01/02（B7，反应格式）区分**：B7 是同一 UI 内反应格式（D&D vs dropdown）的操纵；METHOD-027 是投递模态操纵、作答格式恒定。两者共同支持「仪器/呈现层的选择会移动分数分布」，但各自 scope 独立，不能互相替代。
- **与 UIE-11/12（缺失是设计依赖的）一致**：METHOD-027 的 F3.2 提供镜像证据——过程通道的**不存在**（无日志）本身就是设计决策的后果，直接导致机制不可判定。
- **与审计 Limitations 中「gated mode-effect 研究」的关系**：审计已标注 Delgado 2018 / Clinton 2019 等 meta 未读、不得断言方向；METHOD-027 是这些 meta 中的一个一手研究，本地已持有全文，可支撑「至少有一个 RCT 显示屏阅读劣势」的方向性事实，但不得当作 meta 结论。
- 审计正文当前对 METHOD-027 的唯一引用是 C5 检索记录（"gated"）；本笔记将该条目转为已读，**审计主文件与 acquisition queue 的更新属审计资产 owner 职责，本笔记不代改**。

### 建议新 UIE 条目草稿

- **UIE-31（草案，建议纳入）**：阅读投递模态（纸 vs 屏 PDF）在作答格式恒定的随机对照实验中移动阅读理解分数分布：屏组显著更低（标准化 β = −.216, p = .025；ΔR² = 4%；总 R² = .42；PDF p.4–5）；叙事/说明体裁不调节（F(1,70) = .142, p = .707；PDF p.5）；作者政策结论：短文本的呈现格式变更也不得默认不影响表现（PDF p.7）。暂定 verdict：`SUPPORTED`（研究自身种群/任务/变量/设计范围内）。Scope boundary：挪威 72 名 15–16 岁学生、两所城市学校、线性叙事+说明文本各一篇（约 4 页）、PISA 式 MC+CR、1 小时时限、2013 年 LCD/Adobe Reader vs A4；投递模态证据（不是作答 UI 变体证据）；n 小、分组不平衡 25:47、机制未判定。
- **UIE-32（草案，建议纳入）**：过程通道缺失使模态效应机制不可判定：作者未记录滚动使用、阅读时间与视觉疲劳，明确声明无法归因（"We have no data showing whether or not…used the scrolling option", PDF p.5；"It is impossible to determine from the data…", PDF p.7）；作者建议未来用眼动等在线测量（PDF p.7）。暂定 verdict：`SUPPORTED` as reported study operations / limitation；对本项目是 Class-3 决策输入——任何不记录过程通道的模态对比只能给出方向、无法给出机制。Scope boundary：同上；这是「研究操作缺陷」的文档，不是 UI 效应本身。
