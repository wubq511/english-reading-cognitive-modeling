# METHOD-039 全文证据提取笔记 — Woodcock, Howard & Ehrich (2020)

> 本文件是 `ui-instrument-effects-evidence-audit` 的输入笔记（Acquisition queue 已定位未读 → 已通读），只读不改审计主文件。页码一律为本地 PDF 物理页（1–8；印刷页 80–87，两者相差 79）。

## 头部

- **Source ID**: `METHOD-039`
- **Local path**: `sources/library/papers/methods/2020_Woodcock_ItemFormatEffects.pdf`
- **Bibliographic record (catalog)**: Woodcock, S., Howard, S. J., & Ehrich, J. (2020). *A within-subject experiment of item format effects on early primary students' language, reading, and numeracy assessment results.* School Psychology 35(1), 80–87. DOI 10.1037/spq0000340.
- **PDF 首页核对**: 标题、作者（Woodcock, Griffith University；Howard, University of Wollongong；Ehrich, Macquarie University）、期刊（School Psychology 2020, Vol. 35, No. 1, 80–87）、DOI（10.1037/spq0000340）与 catalog 一致，无出入。仅一处可加注：期刊现名 *School Psychology*（原 *School Psychology Quarterly* 更名），不影响条目。
- **核验方式**: 全文 `pdftotext -layout` 通读（8 物理页），无 `ABSTRACT-ONLY` 项。

## 研究概览

- **研究问题**: 常用题目格式（multiple choice / open-ended / error detection and correction / explain；数字题另加 low literacy）是否显著改变标准化测验中学生的成绩、题难度与能力区分度——即"作答方式"是否改变"被测量的能力估计"（Class 2/4 格式操纵一手证据）。
- **样本**: 89 名 Grade 3 学生（8–9 岁），澳大利亚某都市区 5 所小学；57.3% 女生；全部英语母语；无纳入/排除标准以贴近普通课堂；家长书面知情同意。缺勤：8 人缺 1 科（语言 6、阅读 2），2 人缺 2 科（数学+阅读），相应分析样本缩减（PDF p.3）。
- **设计**: 被试内实验（within-subject），内容等价的格式操纵 + 反平衡（counterbalanced）。题目取自 NAPLAN 退役真题；每题保留原版并生成仅格式不同的变体（three-step 创建流程，团队逐题讨论修订）；Schoolhouse Test 4 随机为每题选一个变体并编成 89 份唯一试卷，条件与顺序交错以消除 order effects（PDF pp.3–4）。
- **任务与材料**: 纸笔、团体施测，3 次 45 分钟（每科一次，连续 3 天；顺序 language conventions → numeracy → reading，与 NAPLAN 施测时长/顺序平行；缺勤学生次日补考）。Language Conventions 50 题（拼写/语法/标点；格式：MC、open、error correction——用 proofreading 替代 explain）；Reading Comprehension 36 题（格式：MC、open、error correction 基于 T/F 原题、explain）；Numeracy 35 题（格式：MC、open、explain、low literacy——删除非必要文字、尽量用数字替代）。low literacy 是 MC 的变体（PDF p.4）。
- **评分**: 受训研究者按答案键做二分（对/错）判定；随机 10% 双人复评，>99% 一致率（PDF p.4）。
- **变量**:
  - 产品分数: 各格式正确率比例（proportional accuracy，repeated-measures ANOVA）；
  - 潜变量指标: 每格式/领域分别跑二分 Rasch（RUMM 2030），得题难度（logits）、person separation index (PSI) 信度、misfit 比例；对 Rasch 题难度做 repeated-measures ANOVA（PDF p.5）；
  - 过程指标: 无（无反应时、无交互日志、无眼动）；格式→认知过程差异仅为 CLT 理论推断（PDF p.2, p.6）。
- **假设**: (a) MC 成绩最高（猜测抬升）、open 次之、explain 最低；(b) 数字题 low-literacy MC 会给出更高的能力估计（PDF p.3）。
- **分析清理**: 移除极端分（满分/零分，n=2）与 misfitting 题后再拟合；各条件 Rasch 样本 N=65–83（PDF p.5, Table 2）。

## 核心发现（按四类主张分组）

### Class 1 — 可用性 / 偏好

- **无任何可用性、满意度或偏好证据**。全文无 self-report、无偏好测量、无工具可用性评估。对 Class 1 零贡献（全文核查，无页可钉——记为空缺而非发现）。

### Class 2 — 行为改变（格式/布局改变可观察行为与过程指标）

- **不构成 Class 2 直接证据**。操纵是格式级行为操纵，但结果变量只有正确率与 IRT 参数；论文并未观测任何过程指标（无 RT、无事件日志、无眼动/鼠标轨迹）。格式→过程差异（recognition vs recall、WM/元素交互负荷、mental search、图写与书写表达要求）是 CLT 理论推断（PDF p.2, p.6），未测量。
- 若项目要用它推断"格式改变认知过程"，应标 `PROJECT-INFERENCE`（理论路径合理但无过程测量），不能作为已观测行为证据。

### Class 3 — 仪器信度与缺失

- **发现 3.1（`SUPPORTED`）: 测量信度与题级数据质量随反应格式系统性变化**。MC 各条件信度边缘（PSI .68–.73，部分低于 .70 阈值）且 misfit 最高（25%–48%）；explain/error-correction 条件信度最高、misfit 最低（PSI .70–.88，misfit 12%–34%）；open response 居中偏低（numeracy PSI .60/40% misfit；language PSI .72/29%；reading misfit 15% 为最低）。PDF p.5（Table 2）、p.6。
  - 引文: "multiple-choice conditions typically showed marginal reliability, with the person separation index (PSI) ranging from .68 to .73 (acceptable levels should exceed .70)... and the highest levels of item misfit, ranging from 25% to 48% of these items."（PDF p.6）
  - MC misfit 主源: 低能力学生与高能力学生在这些题上表现相近——题未能区分能力层（PDF p.6）。
- **发现 3.2（`SUPPORTED`）: 格式对数据质量的作用不是单调的**——numeracy 中 low-literacy MC（内容等价、去冗余文字）misfit 低于同内容 MC（29% vs 48%），但两者 PSI 均略低于可接受线（.66 vs .68）。PDF p.6。
  - 引文: "the low-literacy multiple-choice questions showed less item misfit (29%) than did otherwise identical multiple-choice questions (48%), although the reliability of both was slightly below acceptable levels (PSIs of .66 and .68, respectively)."（PDF p.6）
- **发现 3.3（范围边界，非发现）: 该文不贡献"格式→缺失率"证据**。缺失仅管理性缺勤（8 人缺 1 科、2 人缺 2 科，PDF p.3），无格式驱动的缺失/漏答分析；且全样本正确率分析未报告逐条件缺失。缺失维度仍由 UIE-11/12/27 覆盖。

### Class 4 — 学习 / 构念与 estimand

- **发现 4.1（`SUPPORTED`）: 内容等价、被试内反平衡下，反应格式移动产品分数分布**。成绩层级 MC > open > error-correction/explain：
  - Language conventions: F(2,166)=63.08, p<.001, ηp²=.44；MC 62.4%(24.9) > open 45.7%(26.9) > error 38.4%(26.0)（PDF p.4, Table 1）；
  - Reading: F(2,170)=29.03, p<.001, ηp²=.26；error-correction(T/F) 45.4%(21.7) > MC 40.0%(24.2) > open 27.9%(24.5) > explain 19.2%(22.7)，各条件两两显著（PDF pp.4–5）；
  - Numeracy: F(3,261)=18.68, p<.001, ηp²=.18；MC 44.7%(22.0) ≈ low-literacy 43.7%(25.5)（ns），两者均 > open 31.2%(25.5) > explain 20.1%(21.7)（PDF p.5）。
  - 引文: "difficulty increased and accuracy decreased from multiple-choice to open-response to error-correction and explain questions."（abstract, PDF p.1）
- **发现 4.2（`SUPPORTED`）: 格式移动潜变量难度估计（Rasch logits），最大约 2 logit 位移**：
  - LC: F(2,58)=30.83, p<.001, ηp²=.52；MC −1.17(1.90) < open .43(2.04) ≈ error .95(1.77)（PDF p.5）；
  - Reading: F(2,52)=8.83, p=.001, ηp²=.26；MC −.80(1.48) ≈ error-TF −.81(1.47) < open .17(1.71) < explain 1.02(1.25)（PDF p.6）；
  - Numeracy: F(3,87)=12.29, p<.001, ηp²=.31；MC −.69(1.72) ≈ low-lit −.76(1.48) < open .12(1.60) < explain 1.05(1.56)（PDF p.6）。
  - 引文: "rather an issue of item format effects on difficulty and discrimination even when focus and content were otherwise equated."（PDF p.6）
- **发现 4.3（`SUPPORTED`）: 分数水平与测量质量解耦——高分格式测量质量最差，低分格式区分度最好**。MC（成绩最高）信度边缘、misfit 最高；explain（成绩最低）信度/区分度最好（PDF pp.6–7）。
  - 引文: "Reliability and discrimination of student ability levels were largely reduced in those conditions with higher student performance... the lowest levels of item misfit, and the highest levels of discrimination were generally found when students were required to explain their answers."（PDF p.6）"heightened performance did not necessarily indicate a better performing scale (e.g., in terms of reliability, item discrimination)."（PDF p.7）
  - 反向约束: 不能把"格式效应致分数更高"解读为"该格式测得更准"——方向相反。
- **发现 4.4（`SUPPORTED` 作为已报告阴性结果）: 降低数字题非必要文字负荷（low-literacy MC）未提升成绩也未降低难度**——与作者假设 (b) 及 Howard et al. (2017) 相关证据相反。numeracy 成绩 43.7% vs MC 44.7%（ns）、难度 −.76 vs −.69 logits（ns）（PDF p.1 abstract、p.5、p.7）。
  - 引文: "in contrast to expectations, the low-literacy items did not significantly differ from their multiple-choice analogues."（PDF p.5）
  - 含义: "减少构念无关需求"的住宿式操纵不一定移动估量；作者推测该效应可能随年龄/题目复杂度显现（PDF p.7）。
- **发现 4.5（`PARTIAL`，作者推断）: 格式会改变实际被测量的知识/技能（构念层面论证）**。作者主张格式与内容、统计属性并列，是构念定义的一部分；MC 允许识别/猜测、open/explain 额外引入图写与书写表达、阅读 comprehension 在 open 格式下卷入 decoding/linguistic processing 等（PDF p.6）。
  - 引文: "the current adoption of disparate item formats may inadvertently and inconspicuously modify the knowledge, skills, and abilities actually being assessed."（PDF p.7）
  - 判定: 这是论文的论证性结论，无独立构念效度验证（无放声思考、无外部效标、无跨格式构念等价检验）；作为"格式改变被测量构念"的事实前提是 `OVERSTATED`，作为格式实验的设计动机与研究建议是合理推断。

## 边界与局限

- **人群**: 仅 Grade 3（8–9 岁）澳大利亚都市区、英语母语学生；作者明示结果不可外推到其他年龄组（PDF p.7）。无纳入/排除标准，样本贴近普通课堂但 N=89 偏小；Rasch 各条件 N=65–83，作者自评 ANOVA 与二分 Rasch（>30）功效足够，但不足以做子组分析（如特殊需要学生），复现需更大更广样本（PDF p.7）。
- **工具**: 纸笔、团体施测、45 分钟/科（未操纵时限，施测安排平行 NAPLAN）；无数字 UI、无任何过程/交互数据。Reading 的 error-correction 格式实为 T/F 衍生题，跨格式比较需注意该条件构念更简（PDF pp.4–5）。
- **内容等价性**: 作者承认格式操纵中内容难免有细微改变，且"内容变化 vs 格式变化"的贡献无法在设计内分离（PDF p.7）。这是被试内格式实验的固有边界。
- **领域**: 语言/阅读/数字三维度；作者指出模式可能随领域（如 science）、能力、测验经验、gender 变化（PDF p.6–7）。
- **对审计的转移边界**: ①格式级（response format）证据，不是 UI/布局/导航级——纸笔界面无数字 UI 可类比；②成绩与 IRT 估计移动 ≠ 过程指标移动（无过程测量）；③英文 NAPLAN 材料、8–9 岁人群，向成人/大学读者界面外推属 `PROJECT-INFERENCE`。

## 对审计的用途

**支持/强化既有条目**:
- **强化 UIE-02**（`B7`: 反应格式改变产品分数，OR=1.40）: METHOD-039 是第二个独立的被试内、内容等价格式实验证据，且扩展到阅读/语文/数学三维度 + IRT 难度/区分度——格式移动 estimand 不再只有 `B7` 一个数字评估样本。
- **强化 Class 3 的"信度是仪器设计函数"**（UIE-11..15 讲缺失/完整性）: 本文填补"测量信度"维度——PSI 与 misfit 随格式变化（发现 3.1/3.2），即同一内容换格式即换数据质量画像。
- **部分填补 Class 4 缺口**（审计 p.179: "no locally held source demonstrates that a specific variant change in a reading MC answer UI changes the measured construct or the estimand of a skill estimate"）: 在格式级（非 UI 级）证明阅读测验中格式变体改变成绩与 Rasch 难度/区分度估计；UI 布局级缺口仍开。
- **呼应 UIE-16**（`E8`: 意图的题型标签 ≠ 保证的作答过程）: 意图的"低识字化"操纵未实现预期效果（发现 4.4），同构于"操纵意图 ≠ 实现效果"。
- **互补 UIE-27**（`METHOD-012`: 投递模式移动阅读估量，d=.16–.22）: 模式级证据 + 本文格式级证据，两层合起来覆盖"仪器变体移动估量"；本文还提示模式/格式效应的方向性不能简单外推（发现 4.4 与相关证据方向相反）。
- **呼应 UIE-30**（`METHOD-015`: 设备效应因题型而异——计算机有利于 MC 而非 TEI）: 本文区分度模式随领域变化（阅读/语文 MC 区分良好、数学 MC 不佳，PDF p.6），是"格式效应随领域/题型条件化"的又一实例。
- **不可用于 Class 2**: 无过程指标，不能支持"格式改变过程指标"类主张。

**建议新增 UIE 条目草稿**:

| 条目 | Claim | 页码 | 暂定 verdict | Scope boundary |
| --- | --- | --- | --- | --- |
| UIE-31 | 内容等价、被试内反平衡下，反应格式移动产品估量：正确率层级 MC > open > error-correction/explain（ηp²=.44/.26/.18），Rasch 难度位移最大约 2 logit（如 reading MC −.80 vs explain 1.02）。 | PDF p.1 (abstract), pp.4–6, Table 1 | `SUPPORTED`（范围内） | Grade 3（8–9 岁）澳大利亚英语母语生，纸笔 NAPLAN 退役题；格式级而非 UI/布局级；无过程指标；English reading/numeracy。 |
| UIE-32 | 测量信度与题级数据质量是反应格式的函数：高分格式（MC）PSI .68–.73、misfit 25–48% 最差；低分格式（explain/error-correction）PSI .70–.88、misfit 12–34% 最好——分数水平与测量质量解耦。 | PDF p.5 (Table 2), p.6 | `SUPPORTED`（范围内） | 同上；各条件 Rasch N=65–83；reading 的 error-correction 为 T/F 衍生题。 |
| UIE-33 | 减少构念无关文字负荷（numeracy low-literacy MC）未提升成绩也未降低难度（43.7% vs 44.7% ns；−.76 vs −.69 logits ns）——住宿式需求缩减的阴性结果，与相关证据（Howard et al. 2017）方向相反。 | PDF p.1 (abstract), p.5, p.7 | `SUPPORTED`（作为范围内报告的 null） | 仅 numeracy、Grade 3；作者推测效应可能随年龄/复杂度出现；不能外推为"需求缩减永远无效"。 |

**其他可吸收点**: ①区分度/信度随领域变化的模式（reading/language MC 区分良好、numeracy MC 不佳）可并入 UIE-30 的条件化叙事；②"高分格式 ≠ 好量表"（发现 4.3）应作为 Class 4 反向约束写入综合，防止"格式效应致高分→格式更好"的误读；③作者对"格式改变被测量构念"的论证（发现 4.5）仅可作动机引用，不可作事实前提。
