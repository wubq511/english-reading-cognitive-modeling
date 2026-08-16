# METHOD-029 提取笔记 — Kong, Seo & Zhai (2018) 屏纸阅读元分析

> 本文档是 `reports/research/ui-instrument-effects-evidence-audit.md` 的 Acquisition queue（W1，`METHOD-029`）全文提取笔记，供最终综合使用。只读不改审计主文件、catalog、checksums 与 crosswalk。页码均为本地 PDF 物理页（PDF 共 12 页，物理页 = 印刷页 − 137；`141` 页脚在满页表格页丢失，边界经相邻页脚插值确定）。

## 结论速览

- **核心结论**：投递模式（屏 vs 纸）在阅读理解分数上有小而显著的纸优势（Hedges' g = −0.21，95% CI [−0.38, −0.03]，p = .02；47 个效应量 / 16 项研究 / 被试 n = 4831）；阅读速度无显著差异（g = 0.48，[−0.15, 1.11]，p = .11）但异质性极高（I² = 93.36%）且仅 8 项研究、低功效。三个 moderator（年份、国家、屏幕类型）在 0.05 水平均不显著；年份系数呈趋势性递减（b = 0.26，p = .09–.10，纸优势随时间缩小，作者自认不可作断言）。
- **怎么得出的**：`pdftotext -layout` 通读 12 页全文，摘要、方法、结果（表 1/2a/2b/3a/3b/4/5a/5b）、讨论、局限逐条核验并钉物理页。
- **对审计的直接意义**：这是本地第一份全文核验的「纸优势」方向元分析证据，为审计此前挂起的方向性张力（审计主文件第 177、186 行）的成人实验性阅读一侧解封；但方向与 `METHOD-012`（ACT，线上 > 纸，d = .16–.22）相反——投递模式移动 estimand 已由两份全文核验来源确认，方向情境依赖，禁止单方向断言。
- **未决项**：与 Delgado 2018 / Clinton 2019 的效应量数值对比仍需其全文（本地未持有）；K-12（Wang 2008）与高风险机考（UIE-27）两条线方向未统一；表 5a 截距存在排版/提取歧义（见 Class 4）。

## 头部

- Source ID: `METHOD-029`
- Local path: `sources/library/papers/methods/2018_Kong_ScreenVsPaper.pdf`
- Catalog 条目（`sources/catalog.yaml`，已核验）与 PDF 首页一致，无需标注差异：title "Comparison of reading performance on screen and on paper: A meta-analysis"；authors Yiren Kong, Young Sik Seo, Ling Zhai；year 2018；venue "Computers & Education 123, 138–149"；DOI 10.1016/j.compedu.2018.05.005（PDF 首页刊头 p.1 与 DOI 一致）。

## 研究概览

- **研究问题**：(1) 屏读与纸读在阅读理解与阅读速度上是否有差异？(2) 发表年份、研究国家、屏幕类型是否调节该差异？（PDF p.1）
- **设计**：元分析（RVE，robust variance estimation 随机效应 + Tipton 小样本校正）。检索 2000–2016（检索日 2016-01-28），初始 416 篇 → 纳入标准筛出 19 + 前向引用追踪 9 = 28 篇 → 17 篇含足够统计信息纳入（16 期刊 + 1 学位论文）（PDF p.3、p.5）。
- **样本**：17 项研究；阅读理解 47 个效应量 / 16 项研究 / 总样本 n = 4831；阅读速度 19 个效应量 / 8 项研究 / n = 1359（PDF p.5；汇总表 4 见 PDF p.9）。被试构成：11 项大学生、4 项 K-12、1 项在职、1 项混合年龄；国家：美国 6、斯堪的纳维亚 4、欧洲其他 4、以色列 2、韩国 1；屏幕类型：电脑 14、便携阅读设备（Kindle 等）5；研究年代：9 项在 2013 前（PDF p.5；逐项特征见表 1，PDF p.4）。
- **任务与材料**：阅读理解 = 测验/quiz 分数（明确排除 recall 任务）；阅读速度 = 阅读时间（PDF p.3）。文本以说明性为主（10 项 expository、3 项 narrative、4 项未注明），长度约 300–2000 词，多数约 1000 词；文本类型与长度未作 moderator 纳入（PDF p.3、p.5）。
- **变量**：产品分数 = 阅读理解成绩（元分析结果指标）；过程/绩效指标 = 阅读速度；缺失指标：无（元分析不含缺失率/信度/DIF 数据，见 Class 3）。
- **效应量方向约定**（PDF p.5）：阅读理解 g 为正 = 屏优于纸；阅读速度 g 为正 = 屏读更慢（纸更快）。
- **Moderator**：年份（2013 等分位二分）、国家（美国 vs 其他）、屏幕类型（电脑 vs 其他 eBook/eReader）。gender、grade、样本量、抽样方式、研究设计因亚组失衡未纳入（PDF p.5）。编码者信度：8 个领域 Cohen's Kappa 均值 0.95（范围 82%–100%）（PDF p.3）。

## 核心发现（按四类主张）

### Class 1 — 可用性/偏好

- **无直接证据**。论文不测量可用性、满意度或偏好；偏好仅作为解释性推测出现在讨论中：「Quite possibly, the advantage of reading on paper could be accounted for by readers' extensive experience of reading on paper, which shapes their preference for reading on paper and strengthened their use of reading on paper strategies」（PDF p.10）。该句是作者的机制猜测，非元分析结果指标。
- 引言综述提到态度/偏好研究（Chou 2012；Young 2014；Connell et al. 2012，PDF p.2），属叙事性文献引用，不进入元分析。
- 对审计：Class 1 无贡献，维持审计结论「Class-1 实证可用性主张 UNRESOLVED」不变。

### Class 2 — 行为改变（UI/格式/布局改变可观察行为与过程指标）

- **阅读速度（可观察绩效/时间指标）：无显著平均屏纸差异，但异质性极高、低功效**。g = 0.48，95% CI [−0.15, 1.11]，p = .11（正号 = 屏读更慢），τ² = 0.85，I² = 93.36%，19 个效应量 / 8 项研究（PDF p.8 结果、p.9 表 4）。作者自述速度样本过小：「The number of studies (N = 8) in this meta-analysis is relatively small, compared with what has been recommended: Larger than 10 (Higgins & Green, 2011); at least 40 (Hedges et al., 2010; Tipton, 2013a)」（PDF p.11）。**null 不能读作「时间指标等价」——它是低功效 + 极高方差**。
- 讨论中补充：「our results showed reading speed on paper or on screen was not affected by increased cognitive load」（PDF p.10）——速度对介质不敏感，与认知负荷解释并行。
- 对审计：时间类/速度类过程指标对投递模式的响应是「平均 null、研究间方差极大」，警示以单一时间指标判定仪器等价不可靠。注意阅读文献把 speed 当绩效结果，与审计 Class-2「过程指标」语义存在边界歧义，已在 UIE-32 草稿中显式标注。

### Class 3 — 仪器信度与缺失

- **无直接贡献，缺口明确**：元分析不含任何缺失率、作答完整性、信度比较或 screen-DIF 数据——全部在汇总分数层面。不能为本类提供支持。
- 最接近的部分是元分析自身的数据质量检查（非作答缺失）：
  - 发表偏倚：Egger 回归无偏倚证据——阅读理解 z = −1.26, p = .21；阅读速度 z = −0.75, p = .45（PDF p.6）。但讨论承认漏斗图「gave us mixed results」（PDF p.10）。
  - Fail-safe N（表 2a/2b，PDF p.6）：阅读理解 Rosenthal 188 / Orwin 47 / Rosenberg 34；阅读速度 271 / 19 / 267。讨论引用 Orwin 口径「47 more studies for reading comprehension and 19 more for reading speed would be needed to reduce possible publication bias」（PDF p.10），相对纳入研究数（16/8）较高，作者据此认为发表偏倚可能性低。
  - rho 0–1.00 敏感性分析结果稳健（表 3a/3b，PDF p.9；脚注 PDF p.6）。
- 异质性的 Class-3 含义：「screen」作为投递类别本身高度异质（见 Class 4），任何把「屏」当单一仪器类别的可比性陈述都受此限制。

### Class 4 — 学习/构念与 estimand（投递模式移动分数分布）

- **核心发现：投递模式（屏 vs 纸）移动阅读理解分数分布，纸优势小且显著**。g = −0.21，95% CI [−0.38, −0.03]，p = .02，SE = 0.08，τ² = 0.11，I² = 73.23%（PDF p.6 结果、p.9 表 4）。原文：「the mean difference in reading comprehension between reading on screen and reading on paper was −0.21 with a 95% CI of (−0.38, −0.03), p = .02, meaning that readers had significantly higher comprehension scores when reading on paper than reading on screen」（PDF p.6）。摘要（PDF p.1）：「reading on paper was better than reading on screen in terms of reading comprehension」。
- **中高异质性**：I² = 73.23%——汇总估计是高度异质分布的均值，效应并非均匀存在于所有研究/情境（PDF p.6）。
- **Moderators 均不显著**（PDF p.9 正文、p.10 表 5a/5b）：
  - 阅读理解（表 5a，PDF p.10，Model 3）：Year b = 0.26 [−0.05, 0.57], p = .09；Country b = 0.06 [−0.52, 0.65], p = .80；Type（电脑 vs 其他屏）b = 0.22 [−0.42, 0.86], p = .41。原文：「none of the potential moderators turned out to be significant at the 0.05 level. Namely, the summary effect sizes in reading comprehension between reading on screen and reading on paper remained the same, regardless of publication year, country of study, and types of on-screen media」（PDF p.9）。
  - 阅读速度（表 5b，PDF p.10，Model 3）：Year b = 0.20, p = .61；Country b = −1.02, p = .14；Type b = 0.23, p = .39。表注明示 Model 2/3 的 moderator df < 4，「the results should not be trusted」（PDF p.10）——速度侧 moderator 分析按论文自己的标准不可信。
  - 表格歧义：表 5a 截距打印为「0.35」但 95% CI [−0.57, −0.13]、p = .01 与之矛盾；一致解读为 b = −0.35（2013 前基线纸优势更大，Year 正系数 0.26 使 2013 后效应趋近 −0.08，与「递减轨迹」叙述吻合）。此为排版/提取歧义，未改动 catalog；引用该截距数值时须注明。
- **递减轨迹（趋势，非显著）**：讨论指出 p = .10 的差异检验（2013 前 vs 后）「indicates that the magnitude of the difference in reading comprehension between paper and screen follows a diminishing trajectory」，但作者明确「we cannot make a claim directly based on this」（PDF p.10）——对「当前 UI 时代纸优势已消失」的任何断言都 OVERSTATED。
- **方向张力（对审计最相关）**：Kong（纸 > 屏，g = −0.21，实验性学术阅读，多为大学生）与 `METHOD-012`/UIE-27（ACT 机考 > 纸笔，d = .16–.22，高风险限时操作化考试）方向相反。投递模式移动 estimand 已由两份全文核验来源独立确认，但方向随情境（速度敏感性、任务 stakes、样本学段）反转，禁止单方向断言。
- **屏幕类型 null 的含义边界**：Type moderator 不显著（comp b = 0.22, p = .41；df = 4.78 仅略高于 4）是低功效 null（屏类下仅 5 项研究用 Kindle 等便携设备），**不能**当作「设备间等价」证据，不削弱 `METHOD-015`/UIE-30 的设备可比性 burden-of-proof。

## 边界与局限

- **人群**：11/17 大学生，4 K-12，1 在职，1 混合年龄（PDF p.5）——主要不是 K-12；审计主文件第 177/186 行把 Kong 归入「K-12 mode-effect 元分析」组，本笔记予以修正：Kong 更接近「成人阅读媒介元分析」线（Delgado/Clinton），且其方向（纸优势）与 Delgado/Clinton 报告方向一致（数值对比仍需各自全文）。
- **任务/材料**：学术性、说明性文本为主，约 300–2000 词（多数 ~1000）；排除 recall；不含 hypertext/导航型数字阅读——不适用 B-tier（PISA 超文本导航）迁移。研究时期 2000–2016，屏技术已过时（表 1 含 CRT 时代设备，PDF p.4）。
- **方法局限（作者自述，PDF p.11）**：年份等分位二分任意；「美国 vs 其他」分类理由不足；设计（实验 vs 非实验）与 gender 因亚组失衡未测；pilot 研究只含 2000 年后研究；速度侧仅 8 项研究（推荐 ≥10–40）；文本类型与长度未作 moderator。
- **统计局限（本笔记补充）**：I² = 73.23%/93.36% 高异质性；表 5a 截距排版歧义；速度侧 Model 2/3 df < 4 论文自认不可信（PDF p.10）；Kim & Kim (2013) 为潜在离群值但作者保留（PDF p.5）；漏斗图「mixed results」（PDF p.10）。
- **不可外推处**：不能外推到当前平板/手机阅读 UI、超文本导航任务、高风险考试速度敏感性情境；「纸优势」不能当作「屏 = 更差」的普遍命题（ACT 反向证据）；速度 null 不能当等价证据。

## 对审计的用途

### 支持/反驳/限定既有 UIE 条目与待决问题（引用见审计主文件第 68、177、186 行）

1. **解封审计第 186 行的方向挂起（对 Kong 部分）**：审计此前「Kong et al. 2018 ... must not be asserted in either direction until acquired」。现在本地全文核验：成人实验性阅读线方向 = 纸优势（g = −0.21, p = .02）。审计第 177 行的「directional tension across levels」应更新为：成人实验性阅读线方向已定（纸优势，与 Delgado/Clinton 报告方向一致），K-12 线（Wang 2008）与操作化高风险线（UIE-27，机考优势）仍需分别保持未决/反向——方向不能跨情境统一。
2. **修正 Kong 的分组**（审计第 177 行把 Kong 与 Wang 并列 K-12 small/null 组）：11/17 大学生，显著纸优势——应移入成人阅读媒介线。
3. **强化 UIE-27 / 第 177 行的「instrument change ⇒ estimand change」前提**：投递模式移动阅读理解 estimand 现在有实验性元分析（g = −0.21）与操作化大样本（d = .16–.22）两份全文核验来源，方向相反但「模式变体移动分数分布」成立。审计决策 implications（第 199–205 行）的基线冻结论证不受影响，反而更稳；「方向不可一概而论」需写入 claim budget。
4. **限定 UIE-30（跨设备可比性 burden of proof）**：Kong 的屏幕类型 moderator null 是低功效 null（df = 4.78），不构成设备等价证据，不削弱 UIE-30。
5. **Class 1 / Class 3 无贡献**：偏好仅解释性推测（Class 1 维持 UNRESOLVED）；无缺失率/信度/DIF 数据（Class 3 缺口保持）。

### 建议新增 UIE 条目草稿

**UIE-31（Class 4，暂定 `SUPPORTED`，meta 范围内）** — 投递模式（屏 vs 纸）移动阅读理解分数分布：g = −0.21 [−0.38, −0.03], p = .02，纸 > 屏；47 ES / 16 研究 / n = 4831；I² = 73.23%。Scope boundary：2000–2016 研究，多为大学生与说明性学术文本（~300–2000 词），测验/quiz 分数（recall 排除）；方向与 UIE-27（ACT 线上 > 纸）相反——投递模式移动 estimand 成立，方向情境依赖，禁止单方向断言。Pages: PDF pp.1, 5–6, 9（结果 p.6，汇总表 4 p.9）。

**UIE-32（Class 2，暂定 `PARTIAL`）** — 阅读速度/时间指标无显著平均屏纸差异（g = 0.48 [−0.15, 1.11], p = .11）但 I² = 93.36% 且 k = 8（n = 1359）远低于推荐——null 是低功效 + 高方差，不是等价证据；以时间类指标判定仪器等价不可靠。Scope boundary：阅读文献把 speed 当绩效结果，与 Class-2「过程指标」语义存在边界歧义；时间类指标对模式效应方向/存在性均不可作强断言。Pages: PDF pp.8–9, 11。

**UIE-33（Class 4，暂定 `PARTIAL`）** — 屏纸差异的 moderator（年份、国家、屏幕类型）在 0.05 均不显著；年份 b = 0.26, p = .09–.10 呈递减趋势（纸优势随时间缩小，作者自认不可作断言）；屏幕类型（电脑 vs eReader）b = 0.22, p = .41 为低功效 null（df = 4.78；速度侧 df < 4 论文自认不可信）。Scope boundary：null 与趋势均不构成设备等价或「纸优势已消失」证据；表 5a 截距有排版歧义（打印 0.35 vs CI [−0.57, −0.13]）。Pages: PDF pp.9–10。
