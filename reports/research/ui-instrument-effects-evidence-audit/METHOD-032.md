# Evidence Extraction Notes — METHOD-032

Source ID: `METHOD-032`
Local path: `sources/library/papers/methods/2021_Ponce_DragDropResponseEffects.pdf`
Full bibliographic record (as in `sources/catalog.yaml`, cross-checked against PDF p.1 — 一致，无出入):
Ponce, H. R., Mayer, R. E., & Loyola, M. S. (2021). Effects on Test Performance and Efficiency of Technology-Enhanced Items: An Analysis of Drag-and-Drop Response Interactions. *Journal of Educational Computing Research*, 59(4), 713–739. DOI: 10.1177/0735633120969666. （PDF 首页版权行标注 "The Author(s) 2020"；catalog 的 aliases 里年份写 2020 系文件命名历史，catalog 主条目 year=2021 与印刷信息一致，无需修改。）

Page locators 一律为 PDF 物理页（本文件 27 页，PDF p.N = 印刷页 N+712）。

---

## 研究概览

- **研究问题**：(a) 给在线测试添加 drag-and-drop 界面是否影响作答准确率？(b) 是否影响作答速度？(PDF p.2)
- **理论框架**：CTML / working memory hypothesis——D&D 减少界面操作对工作记忆的占用，使学生更快作答而不改变题目难度（PDF p.3, pp.6–7）。四个假设：H1 准确率等价；H2 D&D 更快；H3 D&D 点击更少；H4 两版 stems/responses 注视时长相似（认知加工相同）（PDF p.7）。
- **设计**：三个独立随机被试间实验（between-subject，按 CLPT 预试成绩 + 性别分层随机），格式操纵 = 同一批题目的 conventional（键入数字/字母）vs drag-and-drop 版本，内容完全一致，只改作答程序。无时间限制，低利害（告知不影响成绩）。
- **样本**：智利 Santiago 三所小学。E1 四年级 84 人随机（42/42，预试池 148）；E2 六年级 90 人（45/45，池 128）；E3 八年级 86 人（43/43，池 140）。排除未完成者后最终 N：E1 40/40、E2 38/41、E3 41/41。全西班牙语母语。
- **任务与材料**：E1 四道句子排序题（满分 22）；E2 四道图形组织器题（时间线/因果/对比/前后，满分 31）；E3 两道完形填空 + 两道图形组织器（满分 23）。HTML5 自建应用，23 英寸屏，Tobii Pro X2-60 眼动仪（60 Hz）+ Tobii Studio。
- **变量**：产品分数 = 响应准确率（% correct）；过程指标 = 响应时间（秒，眼动仪记录）、鼠标点击数（response AOI 上的左键次数，Greiff et al. 2017 框架下作为"执行答案所需行为/认知活动量"代理，Tullis & Albert 2013）、总注视时长（stems/responses AOI，秒）。无任何主观满意度/偏好测量。
- **最小必需点击数设计控制**：E1 传统 22 vs 交互 12；E2 传统 31 vs 交互 14；E3 特意设计为传统 23 vs 交互 23 **相同**，以分离"操作数差异"与"执行层差异"（PDF p.7, pp.10, 16, 18）。
- **排除与缺失操作记录**：E1 4/84 未完成 → 40/40；E2 11/90 未完成（视频检查发现多数"只是按结束按钮"，未做最后一项）→ 38/41；E3 4/86 未完成 → 41/41，另 1 人眼动仪未记录时间（应用内结果仍捕捉）。时间/点击分析各移除极端离群值 1–2 人；多数组非正态，用平方根变换或 Mann-Whitney U（PDF pp.11–13, 16, 19–20）。

---

## 核心发现（按四类主张分组）

### Class 2 — 行为改变（本论文最强贡献）

- **C2-1 反应格式一致改变响应时间（过程指标）**：三实验 D&D 均显著更快——E1 451 vs 527 s, t(77)=2.11, p=.038, d=−0.47；E2 863 vs 1046 s, t(77)=3.49, p=.001, d=−0.82；E3 629 vs 741 s, t(79)=2.74, p=.008, d=−0.61。合并（z 分）F(1,233)=23.274, p<.001, d=−0.62。效率增益 14.4% / 17.5% / 15.1%，换算 60 分钟考试节省 8.6–10.5 分钟。**SUPPORTED**。PDF pp.12, 16, 20, 21, 22。引文：*"the drag-and-drop interfaces in Experiment 1, 2, and 3 were in average 14.4%, 17.5% and 15.1% more efficient than the conventional interfaces"*（PDF p.22）。
- **C2-2 反应格式改变鼠标点击数（行为/认知努力代理）**：E1 t(76)=5.50, p<.001, d=−1.18（21.4 vs 29.6）；E2 t(76)=7.01, p<.001, d=−1.59（27.9 vs 45.6）；E3 非正态用 Mann-Whitney U=528, z=2.76, p=.006, d=−0.71（中位数 34 vs 37）。合并 F(1,231)=75.133, p<.001, d=−1.13。点击减少 27.7% / 38.8% / 17.3%。**SUPPORTED**。PDF pp.13, 17, 20, 21, 22。
- **C2-3 E3 最小必需点击数相同（23 vs 23）时 D&D 实际点击数仍更低**：差异（34 vs 37 中位数）不能归因于必需操作数，而包含执行冗余/纠错成分——对"以事件最小集约束格式等价"的设计思路是直接反证。**SUPPORTED**。PDF pp.18, 20。
- **C2-4 注视时长（认知加工指标）大多无差异，行为改变定位在执行层而非加工层**：E1 合并 AOI t(68)=0.35, p=.727, d=0.08；E2 stems t(74)=0.893, p=.378, d=−0.20、responses t(73)=0.627, p=.532, d=−0.15；E3 stems t(76)=1.504, p=.137, d=−0.34、graphic-organizer AOI t(75)=1.25, p=.216, d=−0.28——全部 n.s.；**唯一显著例外**是 E3 完形填空 word-list AOI 注视显著减少，t(76)=4.59, p<.001, d=−1.04（62 vs 104 s），作者归因于传统版在单词列表与文本框之间匹配数字的"界面物流"注视。作者自判 H4 "partially supported"。**SUPPORTED for the execution-vs-processing localization; PARTIAL for H4 as a whole**。PDF pp.13, 17, 20–21。引文：*"These findings support hypothesis 4 and show that a drag & drop interface did not affect how students process the items in order to figure out how to respond, whereas ... implementing a drag & drop interface did affect the ease with which students executed their responses"*（PDF p.13，E1）。
- **年级一致性（moderation）**：合并分析中年级 × 格式对准确率 F(2,235)=0.475, p=.622、时间 F(2,233)=0.581, p=.560、点击 F(2,231)=2.237, p=.109，均无显著交互——效应模式跨 4/6/8 年级稳定。**SUPPORTED**。PDF p.21。

### Class 3 — 仪器信度与缺失

- **C3-1 未完成/排除率与格式的关系在论文内未检验（证据缺口）**：E1 4.8%、E2 12.2%（11/90，多数未做最后一项直接按结束按钮）、E3 4.7%；论文只按条件报告最终 N，未按格式报告缺失率，无法判定格式是否改变完成率。E2 的高未完成及其"末项跳过"模式值得注意（可能含位置/疲劳效应）。**UNRESOLVED (in-paper gap)**。PDF pp.11, 16, 19。
- **C3-2 传感器层数据缺失与数据质量处理是常态**：E3 1 人眼动仪未记录时间（应用内结果可捕捉，PDF p.20）；E2 注视数据丢失 1 conv + 2 D&D（PDF p.17）；时间/点击数据多数组 Shapiro-Wilk p<.05 非正态，需平方根变换或非参数检验；E1 每组各移除 1 个极端点击离群值（PDF pp.12–13）。**SUPPORTED as reported operations**。PDF pp.12–13, 17, 20。
- **C3-3 信度/统计功效推论是作者层面的外推，非直接测量**：实践贡献段声称 D&D 提高单位时间题量 → 更大统计功效 → 更高信度（引 Speer et al. 2016），但论文未直接测量信度或功效。**PROJECT-INFERENCE (authors' inference)**。PDF p.23。

### Class 4 — 学习/构念与 estimand

- **C4-1 反应格式不移动平均产品分数（三个随机实验 + 合并全 null）**：E1 t(78)=0.65, p=.518, d=0.15（.530 vs .499）；E2 t(77)=1.23, p=.222, d=0.22（.652 vs .596）；E3 t(80)=0.126, p=.900, d=−0.03（.617 vs .622）；合并 F(1,235)=1.100, p=.295, d=0.14。**SUPPORTED within study**。PDF pp.12, 16, 20, 21。
- **C4-2 格式 × 能力交互移动子群体分数分布（平均 null 掩盖的亚组效应）**：补充分析（仅合并数据可做，作者明示单实验内样本不足）：低表现学生（预试 z<−0.5）D&D 准确率显著更高，M=.516 vs .418, F(2,76)=7.022, p=.010, d=0.57；高表现学生（z>0.5）无差异，.708 vs .692, F(2,76)=0.125, p=.725, d=0.08。年级 × 条件交互均 n.s.。作者明确标注为初步证据与猜测：*"These conjectures warrant further study"*。**SUPPORTED as exploratory subgroup finding**。PDF pp.21–22。
- **C4-3 构念级解释声明（非直接证据）**：理论贡献段称 D&D 使 *"test performance is a better reflection of what the learner knows rather than a reflection of the challenges of using an unfriendly interface (Greiff et al., 2017)"*——这是作者的机制解释，由 C2/C4 数据支持方向但未直接验证构念效度。**PROJECT-INFERENCE (authors' interpretation)**。PDF p.23。
- **与 Arslan 系/B7 的方向关系（对照，非本论文发现）**：B7（`B7`，2026）中 drop-down 高于 D&D（OR=1.40）；本论文 D&D ≡ conventional（分数无差）。表面冲突可调和：本论文 conventional 是键入数字/字母而非 drop-down；任务类型（句序/图形组织器/完形填空 vs ordering/categorization）、年龄（4/6/8 年级 vs grade 8）、语言（西语 vs 英语）均不同。两篇合并的意义恰是：格式效应在过程层面存在且方向一致（交互减少），但在产品层面的存在与方向是任务/样本依存的。作者文献综述引 Kong et al. (2018)：电脑 vs 平板响应时间无差异，TEI 中唯独 drag-and-drop 项目设备间无差异（PDF p.5）；引 Wang et al. (2008) 元分析：11 研究 42 实验纸笔 vs 计算机阅读成绩无显著差异，年级与测试类型非显著 moderator（PDF p.5）。

### Class 1 — 可用性/偏好

- **无贡献**：论文没有任何主观满意度、偏好或感知易用性测量；点击数被作为"effort"的行为代理（PDF p.10），不是偏好证据。仅动机语境提及低利害测试（PISA/TIMSS）下疲劳与完成动机问题（PDF p.2），不构成可用性证据。**不产生 Class 1 条目**。

---

## 边界与局限

- **人群边界**：智利三所小学 4/6/8 年级，西班牙语母语，低利害实验室测试（明确告知不影响成绩），与高利害英语成人/学龄阅读作答 UI 不可直接外推。
- **任务边界**：仅阅读理解题（句序、图形组织器、完形填空），不是 MC 作答格式；无时间限制；D&D 界面与 conventional 界面不是最小差异对照（E1 中 D&D 无文本框、句子自动重排；E1 的 stems/responses AOI 在 D&D 中不可分离，仅合并分析，PDF p.13）。
- **"conventional = paper-based design"的措辞限制**：三个实验的 conventional 版都是电脑上键入数字/字母，仅"对应纸笔题的外观"（PDF p.8）；本论文不是纸笔 vs 计算机的对照，是同一投递模式内的格式对照。
- **工具边界**：桌面 23 英寸屏 + 实验室眼动仪，非自然作答环境；作者自述未来需研究触摸屏（PDF p.24）。
- **作者自限**：*"These experiments involved a particular type of test (i.e., reading comprehension test items) and a particular set of participant samples (fourth, sixth, and eighth-graders in Chile), so further work is needed to determine whether the effects can be replicated"*（PDF p.24）。
- **探索性分析**：低/高表现亚组分析仅合并数据，样本量不足以在单实验内检验（PDF p.21）；d 符号约定：时间/点击用负号表示 D&D 更优，准确率用正号。
- **笔误提示（不影响数据）**：E3 响应时间结果段末写作 "These findings support hypothesis 3"，按假设编号应为 hypothesis 2（PDF p.20）；E2 结果段将 H3 检验写为 "These findings support hypothesis 3" 处实际对应点击（PDF p.17），编号本身对应正确。
- **阴性/反证保留**：C4-1 的 null 分数结果、C2-4 中多数注视 n.s.、E2 高未完成率、C3-1 的格式→缺失率未检验缺口，均保留如上。

---

## 对审计的用途

**支持**：
- 支持 `UIE-01`（`B7`）的 Class 2 主线：独立的三实验随机对照复制"反应格式改变过程指标"，方向在句序/图形组织器/完形填空三类任务中一致，且年级无交互——补强"格式效应非均匀"论点的同时给出一个稳定方向的任务族（本论文三类均 D&D 更快、点击更少）。
- 支持 `UIE-10`（`E6`"surface design 改变过程指标"）从第二手变为第一手实证支撑（但注意 `E6` 引的是 Arslan 2020，本论文是另一独立证据源，非替代）。
- 支持 Class 3 框架"缺失是设计/行为/样本依存的"：E2 未完成率 12.2%、E3 眼动仪记录失败、非正态需变换。

**限定/反驳**：
- 限定 `UIE-02`（`B7` 的 OR=1.40 "格式移动产品分数"）：本论文证明格式变更可以不移动平均产品分数（合并 d=0.14, p=.295）——"格式移动估量"不能作为普适前提，必须逐任务/逐人群检验。但 `C4-2` 又证明平均 null 可掩盖子群体移动（低表现 d=0.57），因此"平均无差异"也不能当作构念等价证据。两条结合强化审计既有结论：格式与分数的关系是任务与子群体依存的，冻结基线前必须 H2-gated 实证。
- 限定 `UIE-27`（`METHOD-012` 模式效应 d=.16–.22）：本论文是 within-mode 格式级证据且方向为 null——模式/格式级仪器效应都不能一概而论，需逐变体测量。
- 对 Decision implications #2（按任务类型选格式并记录最小事件数）：`C2-3`（E3 最小点击数相等仍减少实际点击）说明"事件最小集"约束不足以保证执行层等价，事件记录还需包含冗余/纠错成分。

**建议新增 UIE 条目（4 条草稿，编号接 UIE-30）**：

1. **UIE-31（Class 2，暂定 `SUPPORTED`）**：反应格式（drag-and-drop vs 键入数字/字母）在三种阅读理解任务（句序/图形组织器/完形填空）中一致改变执行层过程指标：响应时间合并 d=−0.62、鼠标点击合并 d=−1.13（均 p<.001），效率增益 14.4–17.5%；年级 × 格式交互全部 n.s.（p=.560–.622）。Pages: PDF pp.12–13, 16–17, 20–22。Scope: 智利 4/6/8 年级西语阅读理解，桌面眼动仪实验室，无时间限制低利害；非 MC 作答 UI；D&D 方向性在 `B7` 的 categorization 任务中不成立（任务依存）。
2. **UIE-32（Class 4，暂定 `PARTIAL`）**：同一格式变更不移动平均产品分数（合并 d=0.14, p=.295，三实验独立 null），但格式 × 能力交互移动子群体分数分布：低表现学生 D&D 显著更高（d=0.57, p=.010），高表现无差异（d=0.08, p=.725）——平均估计掩盖亚组移动。Pages: PDF pp.12, 16, 20–22。Scope: 探索性合并分析，作者自标 warrant further study；亚组定义为 CLPT 预试 z 分 ±0.5 阈值。
3. **UIE-33（Class 3，暂定 `PARTIAL`/`UNRESOLVED`）**：完成率/数据缺失是格式、样本与传感器依存的：E1 4.8% / E2 12.2% / E3 4.7% 未完成排除，E2 多数未完成者直接按结束按钮跳过末项；E3 眼动仪单点记录失败；时间/点击分布非正态需变换或非参数检验——但论文未按格式报告缺失率，格式→缺失率关系在论文内 `UNRESOLVED`。Pages: PDF pp.11, 16, 19–20。Scope: 运行级操作记录；不支撑"格式改变缺失率"的因果主张。
4. **UIE-34（Class 2/4，暂定 `SUPPORTED`）**：最小必需操作数相等的格式变更仍减少实际交互量：E3 传统与 D&D 最小点击同为 23，实际点击数仍显著更低（中位数 34 vs 37, U=528, z=2.76, p=.006, d=−0.71）——格式差异含执行冗余/纠错成分，事件最小集约束不保证执行层等价。Pages: PDF pp.18, 20。Scope: 完形填空 + 图形组织器，八年级；对 `BENCH-E0` 事件最小集设计与 `B7` 的 superfluous-event 构造有直接含义。
