# 证据提取笔记 — METHOD-017

> 供「UI 仪器效应证据审计」（Wayfinder #5）综合使用。本文档只记录本 source 的全文证据，不修改审计主文件、catalog、checksums 或任何其他文件。

## 头部信息

- **source ID**: `METHOD-017`
- **本地路径**: `sources/library/papers/methods/2025_Ogut_UniversalByDesign.pdf`
- **完整书目（以 PDF 首页为准）**:
  - 作者: Burhan Ogut (American Institutes for Research); Michelle Yin & Hoa Vu (Northwestern University); Juanita Hicks & Ruhan Circi (American Institutes for Research)
  - 标题: *Universal by Design: Unveiling the Effectiveness of Accommodations and Universal Design Features through Process Data*
  - 年份: 2025
  - Venue: *Educational Measurement: Issues and Practice*, Winter 2025, Vol. 44, No. 4, pp. 18–32
  - DOI: 10.1111/emip.70007
- **书目核对**: catalog.yaml 中 METHOD-017 条目的标题/年份/venue/DOI 与 PDF 首页一致；**作者名与 PDF 首页不符**：catalog 写 "Burak Ogut / Mei Yin / Huyen Vu / Jennifer Hicks"，PDF 首页为 "Burhan Ogut / Michelle Yin / Hoa Vu / Juanita Hicks"（Ogut first name 拼写、Yin 用 Michelle、Vu 用 Hoa、Hicks 用 Juanita）。按任务纪律不修改 catalog，仅在此标注。
- **页码约定**: 本笔记页码一律为 PDF 物理页（文件共 15 页）；物理页 = 打印页 − 17（如物理页 5 = 打印页 22）。全文（摘要→参考文献）均已通读，无 `ABSTRACT-ONLY` 标注项；supplementary file 未本地获取，凡依赖其内容的细节本笔记不引用。

## 研究概览

- **研究问题**:
  1. ET（extended time）住宿使用与 SWDs 成绩是否相关（p.2）；
  2. UD 特征使用（scratchwork / text-to-speech / equation editor）与 SWDs 与 SWODs 成绩是否相关（p.2）；
  3. UD 特征与成绩的关系是否因 SWDs 是否使用 ET 而异（p.2）。
- **样本**: NAEP 2017 Grade 8 Mathematics 全国代表性数据，约 148,100 名学生（p.7）；分析主用 process data 中一个 assessment block（约 28,000 学生；其中 SWDs n=2,790，SWODs n=25,370），form 级数据（约 2,800 学生）仅作参照（p.7–8）。SWDs 定义为 IEP ∪ 504 计划（p.8）。
- **设计**: 观察性/准实验性回顾性数据分析（非随机；无干预分配）。统计方法为 logit 回归 + inverse probability weighting (IPW) + doubly robust (DR) 三种模型对比，以缓解选择偏差（p.10）。
- **任务与材料**: NAEP 2017 八年级数学，一个 block 含 15 个 item（矩阵抽样，每学生 2 个 block，各 30 分钟、ET 资格者可延至 90 分钟）（p.7）。注意：**学科是数学，不是阅读**。
- **变量**:
  - 产品分数（outcome）: item 级 0/1 正确（block 满分 25）（p.8; p.4 Table 2 note）。
  - 过程指标（usage）: ET 使用 = block 内"第一个到最后一个动作"总时长 > 30 分钟（学生级变量）；scratchwork 使用 = 打开后活跃 ≥ 2 秒；TTS 使用 = 至少一句话被朗读；equation editor 使用 = 激活后按键输入 > 2 秒（后三者是 student-by-item 级变量）（p.8–9）。
  - 缺失/完整性指标: NAEP 纳入率（SWDs 89%、ELLs 90%）；SWDs 参与率 12%，其中 2% 无住宿参与、10% 带住宿参与（p.7）。
  - 协变量: 学生人口学、家长教育、item 特征（难度、可读性指数等）、学校特征（p.9）。

## 核心发现（按四类主张）

### Class 4 — 学习/构念与 estimand（本论文主要贡献）

1. **ET 住宿使用移动 SWDs 分数分布：item 正确率 +3.5 至 +4.2 个百分点，三模型一致显著**。logit 边际效应 .0345 (SE .006)、IPW .0417 (SE .006)、DR .0419 (SE .007)，均 p<.01，n=24,420 item 观测（Table 3, p.5；结果文本 p.11 "a positive association between extended time usage and test performance among SWDs, with the use of extended time showing a 3.5 to 4.2 percentage point increase in the likelihood of correctly answering a test item"）。ET 即"时间投递模式"变体，是审计维度中投递模式/设备的直接实例。

2. **同一 UD 特征的效果依赖是否同时启用 ET（住宿组合改变"特征—分数"关系）——TTS 与 scratchwork 的证据方向在 ET 用户与非 ET 用户中分离**（p.12）:
   - TTS: 非 ET 用户 SWDs 三模型一致显著正相关（logit .024**, IPW .025*, DR .027**，即 +2.4–2.7pp）；ET 用户 SWDs 三模型全不显著（Table 6 Panels C/D, p.8；结果文本 p.12 "TTS usage was consistently associated with higher performance across all three models, with differences ranging from 2.4 to 2.7 percentage points"）。
   - Scratchwork: 非 ET 用户 IPW +3.5pp (p<.05)，ET 用户 IPW +2.7pp (p<.1)；两者 logit/DR 均不显著（Table 5, p.7；结果文本 p.12）。
   - 作者解释为"compensatory strategy"（无时间住宿时 UD 特征起补偿作用，p.12），但明确承认子群间差异可能是未观测特征（残疾类型/严重度）造成（p.12）。

3. **equation editor 使用与 item 正确率全模型、全子群显著负相关**（p.9 Table 7；结果文本 p.12）: SWDs DR −.213 (SE .009)、SWODs DR −.341 (SE .008)；ET 用户 SWDs DR −.244、非 ET 用户 SWDs DR −.190，均 p<.01。作者解释为认知负荷/界面导航困难/工具与题目需求错配，并承认"these mechanisms cannot be definitively tested with the available data"（p.12）。注意：系数是 UD 特征中最大的，且方向为负。

4. **TTS 对无住宿 SWODs 呈负相关**（p.8 Table 6 Panel B）: IPW −.016 (SE .005, p<.01)、DR −.009 (SE .004, p<.1)，logit 不显著；SWDs Panel A 三模型均不显著。作者将 SWODs 负相关解释为 TTS 可能构成"distraction"（摘要 p.1；结果 p.11–12）。

5. **UD 特征使用者的原始分数整体偏低（描述性）**（p.6 Table 4）: SWDs UD 用户 raw score 5.78 vs 非用户 5.68；SWODs 9.24 vs 9.01；且 UD 用户在人口学上系统性偏向男性、Black、Hispanic 等（p.11）。方向性风险：无因果设计时"特征使用与低分相关"可被误读为特征有害，作者用 IPW/DR 部分校正，但残余内生性仍不可排除（p.12）。

### Class 3 — 仪器信度与缺失

6. **住宿资格 ≠ 实际使用：仅 31.2% 的 ET 合格 SWDs 实际使用 ET**（p.11 "only 31.2% of SWDs (calculated as 530/(530+1140)) who are eligible for extended time actually utilize this accommodation"；Table 1 资格分布 p.3：SWDs 1,670=59.9% 有资格，SWODs 440=1.7%）。资格（IEP/504 行政记录）与基于日志的实际使用（>30 分钟，p.8）是不同构念；资格→使用存在系统性缺口，构成住宿路径的"测量差异 + 可比性"问题。

7. **过程指标的使用定义依赖显式阈值（数据质量筛查）**（p.8–9）: scratchwork ≥ 2 秒活跃、equation editor 激活后 > 2 秒输入、TTS ≥ 1 句被朗读；作者说明 2 秒阈值"balancing the need to exclude accidental openings while capturing brief but intentional use"，并援引 process-data 文献的最小时间阈值惯例（Michaelides & Ivanova 2022; Wise et al. 2010）（p.9）。阈值选择直接改变"使用"这一测量的内容和结果——这正是不做阈值敏感性分析就无法定案的信度问题。

8. **纳入率与参与边界**（p.7）: NAEP 2017 G8 math 纳入率 SWDs 89%、ELLs 90%（NAGB 目标 ≥85%）；SWDs 中 2% 无住宿参与、10% 带住宿参与。作者据此声明结论"primarily generalizable to SWDs who participated in the NAEP with accommodations"（p.7）——即排除无住宿参与的 SWDs，外推边界是显式声明的。

### Class 2 — 行为改变

9. **UD 特征可得性伴随高使用率，但本研究无 UI 操纵、无行为基线对比**（p.6, p.11）: 66% SWDs 与 56% SWODs 至少使用一种 UD 特征（Table 4 派生，p.11 文本给出计算）。过程日志被用作"使用行为"的操作化（p.1 摘要 "process data capture insights into how students interact with the assessment"），但设计是观察性的，无法区分"特征存在引发使用行为"与"学生按需选择"，也无布局/格式操纵下的行为前后对比。对 Class 2 只能算 `PARTIAL` 支持（特征可得性→高使用率），无因果行为改变证据。

### Class 1 — 可用性/偏好

10. **无满意度/偏好测量；仅有机制性推测**（p.12–13）: 论文没有收集偏好、满意度、感知可用性或 self-report 数据。TTS 对 SWODs 的负相关被解释为"potential distractions"（p.1），equation editor 负相关被归因于"cognitive overload / challenges with navigating the interface"（p.12），但作者明言机制"cannot be definitively tested"。对 Class 1 无直接贡献，Class 1 在审计中维持 `UNRESOLVED`。

## 边界与局限

- **人群边界**: 美国八年级、NAEP 2017 G8 数学；SWDs=IEP∪504（两类支持强度差异大）。ET 分析仅限 SWDs（SWODs 中仅 1.7% 有 ET 资格，p.3/p.11）。结论只外推到"带住宿参与 NAEP 的 SWDs"（p.7）。
- **任务边界**: 数学，非阅读——迁移到项目（自然英语阅读 UI）需谨慎；UD 特征（equation editor 尤其）是数学特有工具。TTS/scratchwork 的机制讨论依赖认知负荷理论，方向可借鉴，效应量不可直接照搬。
- **设计边界**: 观察性非随机；使用是自选行为，无干预分配；IPW/DR 依赖无未观测混杂假设（作者承认"residual endogeneity cannot be entirely ruled out"，p.13）。
- **作者声明局限**（p.12）: (1) NAEP 的 SWDs 定义合并 IEP 与 504 两类差异群体；(2) ET×UD 子群样本小、统计功效受限；(3) 残余内生性不可排除。
- **测量边界**: ET 使用用">30 分钟"阈值代理（p.8），与资格声明非同一构念；UD 使用阈值（≥2 秒等）是研究者自选，未做敏感性分析。
- **不可外推处**: 低 stakes（NAEP）≠ 高 stakes；一次测验一个学科；2017 年平台；无不同 UI 版本间的对照（无 A/B 或格式操纵）。

## 对审计的用途

审计主文件（`reports/research/ui-instrument-effects-evidence-audit.md`）中对 METHOD-017 的既有引用（grep 确认）:
- 行 62: S5 检索命中（"Ogut et al. 2025 EMIP … — gated"）；
- 行 103: Wiley publisher bot-wall（transport-level 拒绝）；
- 行 175: Class-4 段落——"The directly on-point study — Ogut et al. (2025), evaluating universal-design accommodations through process data — was located but is gated"，并据此推论"an accommodation … moves the process distribution for that subgroup, so process-indicator comparability between the standard and accommodated paths cannot be assumed and must be measured"；
- 行 183: accessibility coverage——"the empirical accommodations literature (Ogut et al. 2025; Taylor & Banerjee 2023; Lovett & Lewandowski 2015) is located but gated"。

本笔记能：**（a）把行 175 的推论从"未读文献的预期"升级为已钉页的实证**——TTS×ET 交互（发现 2）与 ET 主效应（发现 1）直接显示住宿/特征组合会移动"特征—分数"关系与分数分布；(b) **为行 183 的 accessibility 条款（UIE-23..25 无实证背书）补充实证**，但需限定在数学任务；(c) 为 B7/反应格式条目提供"同特征在不同住宿组方向相反"的反向证据库。对既有 30 条 UIE 条目无直接反驳，均属支持/限定。

### 建议的新 UIE 条目草稿

| # | Claim（中文主张） | Pages | 暂定 verdict | Scope boundary |
| --- | --- | --- | --- | --- |
| UIE-31 | 投递模式变体（时间扩展）移动产品分数分布：ET 住宿使用使 SWDs item 正确率 +3.5–4.2pp，logit/IPW/DR 三模型一致（p<.01） | p.5, p.11 | `SUPPORTED` | 仅 SWDs、数学、低 stakes；观察性 |
| UIE-32 | 住宿/特征组合改变"特征—分数"关系：TTS 只在未用 ET 的 SWDs 中三模型一致正相关（+2.4–2.7pp），对 ET 用户无效应——standard vs accommodated 路径的指标可比性不能假定 | p.8, p.12 | `SUPPORTED` | 观察性；子群差异可能由未观测特征驱动 |
| UIE-33 | 工具型 UI 特征可伴随大幅负向分数移动：equation editor 使用与 item 正确率全模型显著负相关（SWDs DR −.213，SWODs DR −.341） | p.9, p.12 | `SUPPORTED` | 机制未测（作者自认）；数学特有工具；自选使用 |
| UIE-34 | 无障碍特征对非目标（无住宿）群体可为干扰：TTS 与 SWODs 成绩负相关（IPW −.016**, DR −.009*） | p.8, p.11–12 | `SUPPORTED` | 无直接可用性测量，机制为推测 |
| UIE-35 | 住宿资格≠实际使用，日志定义的使用与行政资格是不同构念：仅 31.2% ET 合格 SWDs 实际使用；住宿路径存在系统性 take-up 缺口 | p.3, p.8, p.11 | `SUPPORTED` | 单次测验；阈值（>30 分钟）为研究者自选 |
| UIE-36 | 过程指标"使用"的定义依赖显式阈值（≥2 秒/≥1 句），阈值即数据质量筛查，改变"使用"的测量与结果 | p.8–9 | `SUPPORTED` | 未做阈值敏感性分析；supplementary 细节未获取 |
| UIE-37 | 特征可得性伴随高使用率（66% SWDs / 56% SWODs 用至少一种 UD 特征），但无 UI 操纵证据，不能推因果行为改变 | p.6, p.11 | `PARTIAL` | 观察性使用数据，无布局/格式操纵 |

共建议新增 7 条（UIE-31..37）：Class 4 四条（31–34）、Class 3 两条（35–36）、Class 2 一条（37，PARTIAL）。Class 1 无新条目，维持 `UNRESOLVED`。

## 提取验证记录

- 全文通读：`pdftotext -layout` 输出 953 行（摘要→参考文献），逐页（物理页 1–15）复核关键段落与表格位置。
- SHA-256 与 catalog 一致性：未复算（catalog 已核验）；作者名字段差异已标注于头部，未改 catalog。
- 本笔记之外未修改任何文件。
