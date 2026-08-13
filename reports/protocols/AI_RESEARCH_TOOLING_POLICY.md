# AI 研究工具使用政策

> 状态：ACTIVE
> 版本：1.0
> 生效日期：2026-08-14
> 适用范围：本项目的无 AI/Agent baseline、合成数据、实验编排、人工与 AI 标注、质量控制及结果报告

## 1. 核心边界

本项目所说的“无 AI、无 Agent”只约束**被研究系统的 runtime baseline**，不禁止在研发和实验过程中使用 AI/Agent。

| 平面 | 定义 | AI/Agent 边界 |
| --- | --- | --- |
| Runtime baseline | 面向学习者运行、从输入证据到状态估计/反馈输出的系统推断链 | **不得使用** LLM、生成式 AI 或 Agent；允许预先声明、可复现的规则、统计模型和传统机器学习方法 |
| Research/experiment plane | 文献研究、编码、实验编排、合成数据、候选标注、QA、敏感性分析和报告辅助 | **允许且鼓励**使用 AI/Agent，但必须遵守本政策的 provenance、验证和人工责任要求 |

AI 产物一律视为**待验证的研究工件**，而非天然可信的证据。测量效度取决于证据与理论能否支持特定用途下的分数解释，不能由单一一致率或模型自洽性替代（[AERA/APA/NCME, *Standards for Educational and Psychological Testing*](https://www.testingstandards.net/open-access-files.html)）。

## 2. 决策状态

### 2.1 LOCKED：不可在日常实验中自行放宽

1. **Runtime baseline 不含 AI/Agent。** 若未来要研究 AI 增强，必须作为独立实验臂，与无 AI baseline 分开实现、标识和报告。
2. **AI 不是真人认知真值。** 任何 AI 生成的过程数据、访谈、stimulated recall、认知/元认知标签或解释，都不能单独作为真人认知状态、情绪、策略或学习机制的 ground truth。
3. **参考标准来自独立人类证据链。** 正式认知标签使用 `human reference annotation` 或 `adjudicated reference standard`；不得把专家共识描述为可直接观察的绝对真值。人类 reference set 必须独立于待评估系统和 AI 标注器。
4. **合成标签仅是 simulation truth。** 它只能证明方法在已声明 data-generating mechanism（DGM）下能否回收设计者写入的状态，不能证明真人服从该 DGM。
5. **逐任务验证。** 每一种构念、标签、语言、任务、数据源、目标人群、codebook 版本和 AI pipeline 都必须分别验证；其他数据集上的高性能不得外推。
6. **完整 provenance。** 未满足第 7 节最小字段的 AI 工件不能进入正式分析。
7. **人类数据保护。** 未经相应同意、审查和数据处理安排，不得向外部 AI API 发送可识别的访谈、录屏、音频、Webcam、gaze 或个体级过程日志。

### 2.2 DEFAULT：默认允许的研究用途

AI/Agent 可以用于：

- 生成 schema、时间戳、缺失、重复、乱序、噪声和极端路径等工程测试数据；
- 在人类已冻结的状态机/DGM 之上生成表面语言或行为变体；底层状态与 oracle 必须由独立规则预先确定；
- 实验编排、代码实现、候选假设和敏感性分析；
- 候选证据片段抽取、重复/冲突检查、codebook 歧义提示和 negative-case 搜索；
- 作为与人类标注并列的独立“第三臂”；
- active-learning 候选排序、低置信或疑难样本召回；
- 生成候选解释和 QA 报告，由具名人类研究者作最终接受/拒绝决定；
- 跨模型、跨 prompt、跨运行和跨时间漂移测试。

默认允许不等于结果可直接进入正式研究结论。所有输出仍受 LOCKED 边界和相应 gate 约束。

### 2.3 EXPERIMENT GATE：验证通过后才能启用

以下用途必须针对当前任务通过第 6 节 gate：

- 自动接受任一类 AI 标签；
- 用“一名人类 + AI”替代两名独立人类；
- 用 AI 标签训练正式下游分类器或估计正式效应；
- 用 AI 扩大正式定量/定性分析样本；
- 用 AI 标注教育过程日志、访谈、stimulated recall 或课堂对话中的认知/元认知状态；
- 根据 AI 标注结果自动改变学习者状态估计或研究决策。

通过 gate 的授权只适用于已冻结的 `task × population × language × codebook × model/prompt pipeline` 组合，不可横向复用。

### 2.4 PROHIBITED：禁止用途

- 让 AI 单独充当 ground truth、reference standard 或最终 adjudicator；
- 用同一模型或高度同源的模型家族生成“学生过程”、标注过程并评价系统，形成循环论证；
- 把 prompt/codebook 写入的规则生成成数据，再以系统成功回收这些规则作为构念效度、生态效度、真人效度或干预效果证据；
- 在用于 prompt/codebook 调优的数据上报告最终性能；
- 只报告 accuracy、总体一致率或模型重复运行的自洽率，而不报告逐类和逐群体误差；
- 把 AI 合成样本与真人样本混合后不保留来源字段或分别报告；
- 用两个 AI 的一致意见代替独立人类证据。多个模型可能共享训练数据、对齐目标和系统性偏差，其一致不等于独立验证；
- 未经授权公开或向第三方服务上传敏感的人类原始数据。

## 3. 合成过程数据的能力边界

### 3.1 可以支持的声明

合成数据可以验证：

- 数据 schema、序列、时间、缺失、重复、乱序和存储/传输管道；
- 确定性规则、状态转换、数据库 invariant、oracle 和 metric 实现；
- 方法在明确 DGM 下的回收率、误差、功效和边界条件；
- 极端或罕见工程场景下的鲁棒性；
- “若世界按这些假设生成，方法会怎样”的敏感性问题。

模拟实验必须按 ADEMP 明确 `Aims, Data-generating mechanisms, Estimands, Methods, Performance measures`，并报告 Monte Carlo 不确定性（[Morris, White, and Crowther, 2019](https://doi.org/10.1002/sim.8086)）。

### 3.2 不能支持的声明

合成数据不能单独验证：

- 真人行为或认知状态的 prevalence、方差、尾部和条件相关结构；
- 行为特征到认知构念的映射是否成立；
- 内容效度、构念效度、生态效度或外部效度；
- 真人分类校准、因果效应或教学干预效果；
- stimulated recall 是否忠实反映当时认知；
- 系统在真实学生、语言水平、文本类型和设备环境中的真实性能。

LLM 合成回答的均值可能接近真人而方差和高阶关系明显失真，且相同 prompt 会随措辞和时间改变；因此“表面像真人”不能作为分布保真证据（[Bisbee et al., 2024](https://doi.org/10.1017/pan.2024.5)）。递归依赖模型生成数据还会优先损失真实分布尾部，真人 anchor data 不得被合成数据替代（[Shumailov et al., 2024](https://doi.org/10.1038/s41586-024-07566-y)）。

### 3.3 必须采用的隔离措施

1. 先冻结 DGM、状态空间、参数范围和 oracle，再生成表面过程数据。
2. 生成器与待评估测量器逻辑隔离；不得让测量器读取隐藏状态或生成 prompt。
3. 若使用 LLM，LLM 只负责 surface realization；隐藏状态和预期结果由非 LLM 规则生成并单独保存。
4. 至少包含无 LLM 规则生成组，并对不同模型家族、prompt 和采样参数做敏感性分析。
5. 合成数据与真人数据使用不同 dataset ID、目录和结果表；不得静默混报。
6. 使用真实、冻结且未用于调优的人类 anchor set 检查 synthetic-to-real gap。

## 4. Blinded multi-annotator protocol

本协议适用于过程日志、访谈、stimulated recall、课堂对话及其他认知/元认知标签。

### 4.1 构念与 codebook

每个标签必须预先记录：

- 构念定义与允许的解释范围；
- 纳入、排除和反例；
- 最小证据单位及所需上下文窗口；
- `unknown / insufficient evidence / not applicable` 的使用条件；
- false positive 与 false negative 的后果；
- 证据等级：`direct self-report`、`observable behavior`、`inferred`。

每个标签必须绑定可回查的 transcript span、时间戳或日志事件。没有充分证据时必须标 `unknown`，不得强制分类。

### 4.2 人类 calibration 与数据切分

1. 至少两名具备相关领域训练的人类 coder 在 calibration set 上独立标注并迭代 codebook。
2. 认知/元认知等高解释性构念应配置第三名具备领域资格的 adjudicator。
3. `development / validation / locked test` 按 participant、session 或 collection wave 分组切分；同一人的相邻事件不得随机分到不同集合。
4. codebook 的实质修改要求受影响数据重新独立标注，并产生新版本。

### 4.3 盲法与裁决

- 人类 coder 不得看到系统预测、AI 标签或其他 coder 标签。
- AI 使用与人类相同的 frozen codebook，但不得看到 locked test 的人类标签或 adjudication。
- adjudicator 查看原始证据和匿名化的人类分歧，不查看系统/AI 输出。
- 保存所有 adjudication 前独立标签、理由、证据锚点和最终裁决；不得只保存共识结果。
- AI 可以解释其标签供事后误差分析，但 AI explanation 不是其推断正确的证据。

### 4.4 AI 第三臂与必报比较

在同一 locked test 上分别报告：

- human A vs human B；
- 每名 human vs adjudicated reference；
- AI vs adjudicated reference；
- baseline system vs adjudicated reference。

human–AI agreement 不得代替 human–human reliability。已有真实课堂对话研究中 human–ChatGPT 的总体 Cohen's kappa 为 0.560，低于 human–human 的 0.646；元认知标签分别只有 0.271 与 0.565，说明依赖隐含意图和上下文的构念尤其需要人类判断（[Shin, 2025](https://doi.org/10.1111/jcal.70089)）。

## 5. 验证指标与误差分析

每次验证至少报告：

- 样本和各标签 prevalence、完整 confusion matrix；
- 每类 precision、recall/sensitivity、specificity、F1 及 bootstrap 95% CI；
- human–human 和 human–AI 的 Cohen's kappa 或 Krippendorff's alpha，同时报告原始 agreement；类别高度不平衡时增加 Gwet AC1 等稳健指标；
- 以 participant/session 为 cluster 的置信区间，避免把同一学生的多个事件误当独立样本；
- 按英语水平、母语、任务、文本难度、设备、会话长度和其他预注册群体切片的误差；
- AI 错误是否与群体属性、上下文长度和 label prevalence 系统相关；
- 使用 AI 标签后，下游效应方向、效应量和研究决策相对 human-reference 分析是否改变；
- run-to-run、prompt-to-prompt、model-to-model 和 time-to-time 漂移。

可靠性与一致性研究的样本、rater、程序、统计量和不确定性应按 GRRAS 完整报告（[Kottner et al., 2011](https://doi.org/10.1016/j.ijnurstu.2011.01.016)）。只看总体分数会掩盖失败：27 个社会科学任务的 LLM median F1 为 0.707，但其中 9 个任务至少有一项 precision 或 recall 低于 0.5（[Pangakis, Wolken, and Fasching, 2023](https://arxiv.org/abs/2306.00176)；同行评审版：[Pangakis and Wolken, 2025](https://doi.org/10.1609/icwsm.v19i1.35883)）。

访谈标注还必须检验**非随机误差**。在大规模开放访谈中，LLM 错误被发现与受访者人口属性系统相关并可改变效应方向，简单的人类标注监督模型反而更准确、偏差更低（[Ashwin, Chhabra, and Rao, 2025](https://doi.org/10.1177/00491241251338246)）。

## 6. Task-specific experiment gate

不存在适用于所有构念的科学统一 kappa 或 F1 阈值。每项任务必须在查看 locked test 之前，根据错误后果预注册可接受损失和等价范围。以下是本项目的最低流程政策，不应表述为外部文献的普适定律。

### G0 — Candidate / QA only（默认起点）

- AI 标签只能用于候选、QA、排序或误差发现；
- 不得计入正式 prevalence、效应估计或研究结论；
- 所有正式标签仍由人类 reference protocol 产生。

### G1 — Task validation

进入下一 gate 前必须满足：

1. frozen codebook、pipeline 和 participant-level locked test 已建立；
2. 报告第 5 节全部指标及置信区间；
3. 至少完成重复运行、语义等价 prompt 扰动和第二模型家族的稳定性检查；
4. 无法排除重大群体偏差、系统性过报/漏报或下游结论翻转时，判定为未通过；“差异不显著”不能自动解释为等价；
5. 模型/模型快照、prompt、codebook、输入表示或后处理任一实质变化，必须建立新 pipeline version 并重过 gate。

Prompt 细微变化可能显著改变标签分布和准确性，因此 prompt 是测量器的一部分而非可忽略的实现细节（[Atreja et al., 2025](https://doi.org/10.1609/icwsm.v19i1.35807)）。

### G2 — Limited automatic acceptance

只有具体标签同时满足以下条件，才能仅对该标签自动接受：

- 对 adjudicated locked test 的关键逐类指标，其 95% CI 下界落在预注册可接受损失内；
- 相对第二名人类对 adjudicated reference 的同一指标，95% CI 支持“不差超过 5 个百分点”的初始非劣界；该 5% 是本项目的保守起始 policy，必须在 pilot 后按实际错误后果复核；
- 预注册群体的误差差异均落在各自等价范围内；样本不足以证明则不通过；
- 用 AI 标签得到的主要效应方向、效应量和决策与 human-reference 分析落在预注册等价范围内；
- 未通过的类别、`unknown`、低置信和分布外样本全部回退给人类。

自动接受后仍必须按 label 和 subgroup 分层随机人类审计。审计样本量按要排除的错误率和置信度计算，不得随意固定百分比；active learning 排序不能替代随机审计。

### G3 — Reduced human burden

只有在至少两个独立真人 collection wave 上重复通过 G2，才可考虑用“一名人类 + AI”替代双人全量标注。仍须：

- 保留人类随机审计与专家 adjudication；
- 为高风险、认知/元认知、低频和分布外标签保留双人标注；
- 每个新 wave 做漂移检查；
- 一旦指标、群体误差或下游结论越界，立即回退至 G0/G1。

## 7. AI provenance 最小字段

每次 AI 运行必须保存机器可读记录，至少包含：

```yaml
artifact_id: string
artifact_role: synthetic_generation | annotation | qa | orchestration | analysis
created_at: ISO-8601
operator: person-or-agent-id

provider: string
model_family: string
model_id: exact-provider-model-id
model_snapshot_or_digest: string-or-unknown
access_date: YYYY-MM-DD
endpoint_or_runtime: string

prompt_id: string
prompt_version: string
prompt_sha256: string
system_prompt_sha256: string-or-not-applicable
codebook_version: string-or-not-applicable
codebook_sha256: string-or-not-applicable

input_dataset_id: string
input_dataset_version: string
input_sha256: string
split: development | validation | locked_test | not_applicable
output_sha256: string

temperature: number-or-not-exposed
top_p: number-or-not-exposed
seed: number-or-not-supported
max_output_tokens: number-or-not-exposed
other_parameters: object

attempt_count: integer
retry_policy: string
preprocessing_version: string-or-none
postprocessing_version: string-or-none
human_review_status: pending | accepted | rejected | amended
human_reviewer: id-or-null

data_classification: synthetic | deidentified_human | identifiable_human
external_transfer_basis: approval-id-or-not-applicable
software_environment_or_container_digest: string
cost_and_usage: object-or-not-available
```

必须同时保留完整 prompt、原始响应和解析后结果；hash 不是内容归档的替代品。若 provider 不提供模型快照、seed 或其他字段，明确记为 `unknown/not-supported`，不得伪造可复现性。NIST Generative AI Profile 要求管理数据来源、内容 lineage、评估条件和生命周期风险，可作为记录与变更控制基线（[NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1)）。

## 8. 报告与变更控制

- 所有正式结果明确区分 `human-observed`、`human-annotated`、`AI-assisted` 和 `synthetic`。
- 报告 AI 是否影响了研究问题、codebook、数据生成、分析和文字解释，不得只在致谢中笼统披露。
- 在正式研究前冻结 runtime baseline、DGM、codebook、AI pipeline、主要终点、gate 和分析计划。
- LOCKED 规则的改变必须先形成可审查的设计决策并由项目负责人批准；不得先改变实践再补文档。
- AI 产出的理论连接和解释只能作为候选。LLM 即使面对不合适理论也可能给出表面可信的论证，因此正式解释必须由研究者回到原始证据审查（[Wachinger et al., 2024](https://doi.org/10.1177/10497323241244669)）。

## 9. 一句话执行规则

> AI/Agent 可以显著增强本项目的研发与实验外环，但不得进入无 AI baseline 的 runtime 推断链。AI 生成的数据和标签只能支持工程或模拟条件下的声明；正式认知参考标签必须来自盲化、独立的人类标注与裁决。AI 可以作为经过逐任务验证的第三臂、QA 或 active-learning 工具，不能单独作为真值或最终裁决者。
