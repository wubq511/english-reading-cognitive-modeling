# METHOD-019 全文证据提取笔记 — Clinton (2019)

## 头部

- **Source ID**: `METHOD-019`
- **本地路径**: `sources/library/papers/methods/2019_Clinton_DigitalVsPaper.pdf`（38 页）
- **完整书目**: Clinton, V. (2019). *Reading from paper compared to screens: A systematic review and meta-analysis*. Journal of Research in Reading, 42(2), 288–325. DOI: 10.1111/1467-9817.12269
- **catalog 核对**: `sources/catalog.yaml` 条目（authors/title/year/venue/DOI/local_path）与 PDF 首页完全一致，无出入。
- **审计角色**: 审计文件 C3 检索记录（L45）将其列为 gated 命中；L175/L186/L245 三处均声明 Clinton/Delgado/Schwabe 等模式效应元分析在全文获取前「结论不得以任一方向断言」。本笔记落定 **Clinton 侧**结论（Delgado 2018 仍 gated）。审计任务给的角色是「Class 4 模式效应方向」。
- **提取警示（重要）**: `pdftotext -layout` 丢失了元分析统计表中的**负号**（如 95% CI `[ .37, .12]` 实为 `[−.37, −.12]`）。本笔记所有效应量的**方向一律以正文叙述文字为准**（正文明确 "negative effect" / "worse for screens" / "no difference" / "better calibrated … from paper"），数值符号已按正文还原为负号。正文（p.19 等）与各表底部 random-model 行存在轻微数值出入（如整体 g：正文 .25 vs 表 2 底部 .26；reading time p：正文 .45 vs 表 5 底部 .69），属原文内部不一致，本笔记以正文为准并如实记录差异。

## 研究概览

- **研究问题**: RQ1 纸 vs 屏幕阅读对 reading assessment performance（literal / inferential / general）的影响；RQ2 对阅读过程（reading time、metacognition/calibration）的影响；RQ3 结果是否随体裁（narrative/expository）与年龄（child/adult）变化。PDF p.7。
- **样本**: 元分析。29 篇报告、33 项研究（全部为随机分配实验或 within-subjects counterbalancing）。performance k = 33, n = 2,799；reading time k = 14, n = 1,233；calibration k = 11, n = 698。PDF p.8、p.9（Table 1 区域）。
- **设计**: 系统综述 + 元分析。随机效应模型；效应量 Hedges' g；异质性 I²；moderator 用 Qbetween + R²（每类至少 6 个效应量才做）；出版偏倚用 funnel plot + Egger's test；outlier 用 one-study-removed。PDF p.18–19。
- **纳入标准**: 2008 年之后发表（不含 Noyes & Garland 2008 / Wang et al. 2008 已覆盖文献）；随机分配（或 within-subjects counterbalancing）；被试有基本阅读技能（非学阅读阶段）；**不报告残疾（含视力障碍）**；文本长于一句；母语阅读；以英文发表；受监督环境（教室/实验室）；纸/屏幕条件文本相同。PDF p.7。
- **任务与材料**: 阅读 comprehension 测评（MC、开放题、free recall；编码为 literal/inferential/general），同文本纸 vs 屏幕两种媒体；过程指标为 reading time 与 calibration（性能预测与实际表现之差）。文本多为说明文（expository k = 22 > narrative k = 7，体裁分布不均）。PDF p.9–17（Table 1）、p.23。
- **变量**: 产品分数 = comprehension performance（Hedges' g，**正 g = 屏幕更好**）；过程指标 = reading time（正 g = 屏幕更长）、calibration（方向标注见 F2-4 内部矛盾说明）；moderators = 体裁、年龄、literal/inferential 分测。**无缺失率/数据完整性指标**——元分析层面无 missingness 证据。
- **检索/编码质量**: 2016.10–11 七库检索（2,042 hits）→ 51 篇全文 → 29 篇报告；作者联络补充 + 前后向 snowballing；编码由作者 + 独立助理复核 25%（k = .93）。PDF p.8。

## 核心发现（按四类主张分组）

### Class 4 — 学习/构念与 estimand（产品分数）

- **F4-1｜投递模式移动阅读产品分数分布：屏幕总体负效应，幅度小（g = −.25）。** k = 33, SE = .06, 95% CI [−.37, −.12], p < .001, I² = 70.35（异质性高，支持随机效应 + moderator 分析）。正文 "reading text from screens had a small, but significant negative effect on performance scores compared to reading from paper, g = .25, k = 33, SE = .06, 95% CI = [−.37, −.12], p < .001"（负号已还原；表 2 底部 random-model 行为 g = −.26, CI [−.33, −.19]，与正文略有出入）。PDF p.19。
- **F4-2｜体裁是显著 moderator：纸优效应集中在说明文（g = −.32），叙事文本无媒体差异（g ≈ −.04）。** Qbetween(1) = 6.86, p = .01, R² = .13。Expository: g = −.32, k = 22, SE = .08, 95% CI [−.48, −.16], p < .001（屏幕更差）；Narrative: g = −.04, k = 7, SE = .07, 95% CI [−.18, +.11], p = .64（无差异）。正文 "reading performance for expository texts was worse for screens compared to paper, g = .32 … no difference in reading performance by medium for narrative texts, g = .04 … p = .64"。作者警示体裁分布不均削弱稳健性（expository 远多于 narrative）。3 项含两种体裁且可分体裁的研究（Kretzschmar et al. 2013; Mangen et al. 2013; Margolin et al. 2013）内部也呈现「说明文负效应大于叙事」的模式。PDF p.23。
- **F4-3｜年龄（child vs adult）不是显著 moderator。** Qbetween(1) = .07, p = .80, R² = .04；child k = 7 子模型 g = −.18, p = .49（ns）；adult k = 26 子模型 g = −.21, p < .001。作者归因：成人样本几乎全是大学生（"digital natives"），与儿童同样熟悉屏幕阅读；Kretzschmar et al. 2013 的老年（M = 66.8 岁）vs 青年（M = 25.7 岁）组内对比也未发现年龄差异。PDF p.24。
- **F4-4｜literal 与 inferential 分测均为屏幕负效应，且 literal（更易任务）效应量略大——与「屏幕更伤难任务」预期相反。** Literal: g = −.33, k = 19, SE = .08, 95% CI [−.48, −.18], p < .001, I² = 67.13；Inferential: g = −.26, k = 13, SE = .05, 95% CI [−.36, −.17], p < .001, I² = 0.00。正文 "contrary to expectations that screens would be more detrimental for challenging tasks than easier tasks"。3 项同质研究（Singer & Alexander 2017a; Singer Trakhman et al. in press; 2018）：main idea 无媒体差异，但**细节 recall 纸更好**——作者用「屏幕阅读干扰细节编码」解释，而 literal 测量基于文本记忆。PDF p.24。
- **F4-5｜效率推断（讨论层，非独立测量）：阅读时间无差异 + 纸 performance 更好 ⇒ 纸阅读「更高效」。** "reading from paper appears to be more efﬁcient in terms of performance outcomes than reading from screens"。这是作者对两个独立元分析结果的合成推断，非直接测量。PDF p.30。
- **F4-6｜出版偏倚与稳健性（performance）**: funnel 对称；Egger 截距 β = 1.29, p = .20（无偏倚证据）；one-study-removed 移除任一项不改变结果。PDF p.19。

### Class 2 — 行为改变（阅读过程指标）

- **F2-1｜阅读时间（过程指标）对投递模式总体不敏感：g = .08（无差异），但异质性极高。** k = 14, SE = .20, 95% CI [−.32, +.48], p = .45, I² = 92.47。funnel 不对称但 Egger 截距 β = .14, p = .96——作者归因于异质性而非出版偏倚。one-study-removed 无异常。PDF p.26–27。
- **F2-2｜阅读时间的方向可被**评估通道/作答方式**颠倒（单一异常值）：Kim & Kim 2013 屏幕阅读时间显著更短（g = −1.72, CI 跨负区间, p < .001），作者归因于答题 psychomotor 差异——屏幕条件用鼠标圈答 MC、纸条件用铅笔圈答，导致纸条件耗时更长。** 正文 "the different psychomotor demands of assessment in Kim and Kim (2013) were responsible for the substantially longer reading times in the paper than the screen condition"。同一研究因此被排除于时间方向结论之外。PDF p.28。
- **F2-3｜阅读时间方向在「纯文本 vs 含视觉表征」研究间相反——布局/图文结构假设（未检验）。** 纯文本研究纸阅读时间更长（Chen & Catrambone 2015; Singer Trakhman et al. 2018/in press）；含图表/插图研究屏幕时间更长（Connell et al. 2012; Daniel & Woody 2013）。作者提出「图文布局跨媒体不同→注意力分配不同」的可能解释，并明言 "There are not clear empirical ﬁndings to support this possible explanation; therefore, this would be a potential direction for future research"。PDF p.28。
- **F2-4｜校准（metacognitive performance 预测准确性，过程指标）对投递模式敏感：屏幕校准更差、更过度自信，g = .20。** k = 11, SE = .07, 95% CI [.07, .33], p = .002, I² = 19.65（低异质性）。正文 "reading text from screens caused less calibrated and more overconﬁdent predictions of performance than reading from paper, g = .20"。**方向说明**：正文明确正效应量 = 纸校准更好（"better calibration for paper compared to screens (i.e., positive effect sizes)"，PDF p.29）；但**表 6 标题标注为 "positive Hedges' g indicates better calibration with screens"（PDF p.29），与正文及摘要（"better calibrated (more accurate) judgement … from paper"）直接矛盾**——内部不一致，本笔记以正文/摘要为准，表头标注存疑。PDF p.29。
- **F2-5｜校准方向例外（反向证据保留）**: 11 项研究中仅 Singer Trakhman et al. (2018) 方向相反（非异常值）。作者推测其设计差异——纸条件被要求用铅笔追踪阅读、屏幕条件用放大光标——追踪工具可能改善屏幕条件聚焦（"this possibility is only conjecture without empirical ﬁndings to support it"）。PDF p.29。
- **F2-6｜偏好可改写过程指标方向（间接、研究级）**: Ackerman & Goldsmith 2011 Exp 2 参与者对纸偏好显著更强 → 阅读时间方向与其它同材料研究相反（"one would opt to spend more time reading from a preferred medium"）；校准准确性在**偏好媒体**上更好（Lauterman & Ackerman 2014）——"calibration is not as dependent on medium per se, but from which medium one would prefer to read"。PDF p.28、p.30。
- **F2-7｜行为机制解释（讨论层，未测量）**: (a) 走神假设——屏幕更难聚焦 → 校准差 → performance 差（引用 Mizrachi 2015 报告难聚焦、Muir & Hawes 2013 屏幕分心，但无本元分析数据）；(b) 情境线索假设——电子媒体=休闲阅读线索、纸=学习线索，引用 Sidi et al. 2017 词问题实验（非文本理解，作者注明 "Although not explicitly tested with text comprehension"）。PDF p.30–31。

### Class 3 — 仪器信度与缺失

- **F3-1｜本元分析不报告任何缺失率/数据完整性指标**（纳入研究为受监督实验，无作答缺失率信息）。无 missingness 证据——不构成缺失证据，也不排除缺失率受投递模式影响（METHOD-012/UIE-27 已证明 ACT 中 omission 模式依赖）。
- **F3-2｜样本层面排除「无障碍增强可受益群体」**: 纳入标准排除自报残疾者（含视力障碍）——"electronic text can be enhanced to ease reading for individuals with visual impairments" 是作者给出的排除理由。无障碍住宿是否移动分布，在本元分析中既无证据也无反证。PDF p.7、p.31（Limitations 重申）。
- **F3-3｜测量信度普遍缺失（仪器质量）**: 作者列举 9 项研究未报告 performance measure 信度（Ackerman & Goldsmith 2011; Ackerman & Lauterman 2012; Chen et al. 2014; Daniel & Woody 2013; Green et al. 2010; Kim & Kim 2013; Lauterman & Ackerman 2014; Porion et al. 2016; Taylor 2011），呼吁未来研究报告信度。PDF p.31。
- **F3-4｜作答通道（answering items）的电子化可能独立于阅读媒体引入难度**: 两项纳入研究作者自报局限 "answering performance items electronically may have been more difﬁcult than on paper"（Kim & Kim 2013; Mangen et al. 2013，Table 1 Limitations 列）——即评估 UI/作答层本身是潜在混淆源，作者未将其从阅读媒体效应中分离。PDF p.13。
- **F3-5｜null result 可能是检验力不足**: 多项研究小样本（Table 1 多列 "small sample size"）；作者明言若干 null 结果 "could likely be due to a sample size too small to detect an effect rather than no differences between media"。PDF p.32。

### Class 1 — 可用性/偏好

- **F1-1｜本元分析未测量可用性/满意度**；唯一偏好证据是历史综述引用（Dillon 1992 "noted a preference for reading paper books over electronic"）与上述 F2-6 的偏好对过程指标的调节作用。无满意度/易用性主张。PDF p.5、p.28–30。

## 出版偏倚与稳健性（元分析自身质量）

- **performance**: funnel 对称，Egger β = 1.29, p = .20；one-study-removed 无异常。PDF p.19。
- **reading time**: funnel 不对称，Egger β = .14, p = .96 → 归因异质性（I² = 92.47）而非偏倚。PDF p.27。
- **calibration**: funnel 大致对称，Egger β = 1.61, p = .16；one-study-removed 无异常。PDF p.29。
- **正文 vs 表格数字出入**: 整体 performance 正文 g = −.25 / SE = .06 / CI [−.37, −.12] vs 表 2 底部 g = −.26 / SE = .04 / CI [−.33, −.19]；reading time 正文 p = .45 / CI [−.32, +.48] vs 表 5 底部 p = .69 / CI [−.31, +.47]。以正文为准记录。

## 边界与局限

- **人群边界**: 仅母语阅读者；排除学习阅读者、自报残疾者（含视力障碍）；成人样本几乎全为大学生；child k = 7 与 adult k = 26 分布不均（年龄 moderator 检验力弱）。PDF p.24、p.31。
- **任务/材料边界**: 2008–2018 受监督实验，同一文本纸/屏两条件；**时间压力（time pressure）未被编码为 moderator**（虽纳入含时限研究如 Ackerman & Lauterman 2012，但其标题语义即 "under time pressure"），设备类型未作为 moderator（Chen et al. 2014 的 tablet 与 monitor 条件被合并）；体裁分布不均（expository k = 22 vs narrative k = 7）。PDF p.23、p.18。
- **语言边界**: 仅英文发表文献（作者自述）。PDF p.31。
- **作者自声明的局限**: 检索限于英文；排除残疾/视力障碍与学阅读群体；多项纳入研究未报信度；样本量偏小致检验力不足。PDF p.31–32。
- **不可外推处**: 本元分析操作的是**投递模式（medium: paper vs screen）**，不是作答 UI / 反应格式 / 布局 / 导航 / 反馈的变体；无任何 within-screen UI 变体证据。屏幕侧设备/软件 UI 细节在纳入研究中不可控，是效应量的混合来源。
- **与 Delgado et al. (2018) 的关系（审计重点）**: Clinton 2019 全文**未引用** Delgado et al. (2018)（检索零命中）——两篇同期独立元分析。样本时间窗部分重叠（Clinton 2008–2018 vs Delgado 按元数据级信息 2000–2017），具体重叠条目**需在 Delgado 侧全文核对**（Delgado 仍 gated）；Clinton 侧能确认的是其 moderator 集合（体裁/年龄/literal-inferential）与 Delgado 的差异点（Delgado 是否含 time limit moderator，属 Delgado 侧事实，不在本笔记断言）。

## 对审计的用途

**落定 Clinton 侧悬置**（审计 L175/L186/L245 曾将其列为「不得断言」的 gated 文献）:

- 投递模式（纸 vs 屏幕）**确实移动阅读 comprehension 产品分数分布**，但方向与幅度是任务条件性的：说明文负效应 g = −.32（屏幕更差）、叙事零效应 g ≈ −.04、literal −.33 / inferential −.26、年龄无调节、总体 −.25。这为「instrument change ⇒ estimand change」前提（审计 L177 的 Class-4 主线）提供一个全文级、随机分配实验的元分析锚点。
- **与 METHOD-020 (Schwabe 2022, 叙事 d = 0.10 等价零) 一致而非冲突**: Clinton 叙事子样本 g ≈ −.04（p = .64，无差异）与 Schwabe 的叙事等价零结论**方向一致**——Schwabe 笔记中「Delgado/Clinton 的负效应主要来自说明文」的判断在 Clinton 侧得到直接证实（expository g = −.32 且是唯一显著方向）。审计 L175 的「方向张力」现在可表述为三档并存：说明文语境纸优（Clinton g = −.32）→ 叙事/非速度语境零（Clinton g ≈ −.04 与 Schwabe d = 0.10 双锚）→ 高速度标准化阅读测试屏优（METHOD-012/UIE-27, d = .16–.22）。**不可把任一方向的单一记录当作普适模式效应**；Clinton 未检验 time limit moderator，是它与 METHOD-012 语境差异的未解析接口。
- **限定 UIE-27（METHOD-012, ACT 屏优 d = .16–.22）**: UIE-27 的 scope boundary 应补一句「投递模式效应方向依赖任务语境——说明文/成人实验语境为纸优小效应（g ≈ −.25~−.32, Clinton 2019），叙事/非速度语境为零（Clinton; Schwabe 2022），高速度标准化测试语境为屏优（ACT）」。UIE-27 仍是唯一的 operational 大样本证据，本笔记不削弱它，只限幅其可外推性。
- **对 Class 2/3 的贡献**: Clinton 提供「**过程指标对投递模式的敏感度不一致**」的证据——reading time 对模式不敏感（g = .08, ns, 但 I² = 92.47），而 calibration（元认知校准）敏感（g = .20, p = .002）。对审计含义：过程指标集合中哪些对仪器变体敏感、哪些不敏感，本身是变体依赖的；且**作答通道（鼠标圈答 vs 铅笔）可颠倒过程指标方向**（F2-2），与 UIE-01/02（B7）「反应格式改变过程指标」的证据形成模式级对照。
- **对 Class 1 的贡献**: 无新增可用性实证；偏好对过程/校准的调节（F2-6）支持审计 L149「偏好影响行为」但仍是间接、非直接可用性测量。

**建议新 UIE 条目草稿**:

- **UIE-32（建议）｜投递模式（纸 vs 屏幕）移动阅读产品分数分布，方向由体裁决定：说明文屏幕显著更差（g = −.32, k = 22, p < .001），叙事无媒体差异（g ≈ −.04, k = 7, p = .64），总体小负效应（g = −.25, k = 33, n = 2,799, p < .001）；literal（g = −.33）与 inferential（g = −.26）均负，年龄（child/adult）无调节。**
  - 证据: `METHOD-019`, 总体 PDF p.19；体裁 PDF p.23；年龄 PDF p.24；literal/inferential PDF p.24。
  - 暂定 verdict: `SUPPORTED`（其范围内：2008–2018 随机分配实验元分析，成人/儿童，说明文为主）。
  - Scope boundary: 操作的是投递模式而非作答 UI 变体；屏幕侧 UI 细节不可控；未编码 time limit / 设备 / 速度；英文发表文献；排除残疾与学阅读者；体裁分布不均。与 METHOD-012/UIE-27（ACT 屏优）及 METHOD-020（叙事等价零）并列时，方向由任务语境决定，不作普适断言。
- **UIE-33（建议）｜过程指标对投递模式的敏感度不一致：阅读时间对模式无总体差异（g = .08, p = .45, I² = 92.47）且方向可被作答通道颠倒（Kim & Kim 2013 屏幕鼠标圈答 vs 纸铅笔圈答 → 屏幕时间显著更短，g = −1.72）；校准（性能预测准确性）则显著恶化（屏幕更过度自信，g = .20, p = .002, I² = 19.65）。**
  - 证据: `METHOD-019`, reading time PDF p.26–27；Kim & Kim PDF p.28；作答通道研究级局限 PDF p.13；校准 PDF p.29；表 6 方向标注矛盾 PDF p.29。
  - 暂定 verdict: `SUPPORTED`（其范围内：实验语境）；「作答 UI 通道可颠倒时间类过程指标方向」为 `PARTIAL`（单研究异常值 + 作者归因性解释）。
  - Scope boundary: 阅读时间 = 全文级（总时长），非区域/段级可见性时间；校准为自报性能预测偏差，非 UI 行为指标；不涉及作答 UI 变体；表 6 方向标注与正文矛盾，引用时以正文为准。

## 笔记元信息

- 提取范围：全文 38 页通读（`pdftotext -layout`），关键数据用按 form-feed 分页 + 正文叙述文字交叉核对；无 `ABSTRACT-ONLY` 条目。
- 页码均为 PDF 物理页（PDF 物理页 1 = printed 288）；统计表负号因提取工具丢失，方向以正文为准（见头部警示）。
- 未修改 catalog、checksums、审计主文件、crosswalk 或任何其他文件。
