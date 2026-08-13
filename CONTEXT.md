# English Reading Process Evidence Context

本文件规定项目专用术语。术语用于区分观测、解释与验证层，避免把相似词混成同一构念。

## Project scope

**Runtime baseline**: 面向学习者运行、从交互输入到状态估计或输出的系统链；不含 LLM、生成式 AI 或 Agent，但可包含可复现的规则、统计、心理测量和传统机器学习方法。
_Avoid_: No-model system, purely deterministic system

**Research/experiment plane**: 围绕系统开展文献研究、编码、实验编排、合成数据、标注与分析的外部工作面；允许受治理的 AI/Agent。
_Avoid_: Runtime AI layer

**Canonical asset**: 已从历史材料恢复、标明证据强度并可供日常研究使用的项目文档、协议、索引或数据规范。
_Avoid_: Raw material, chat conclusion

**Recovery source**: 为恢复研究谱系而冻结保存的聊天、handoff 或迁移包；只用于来源追溯，不是日常研究资产。
_Avoid_: Canonical report

## Measurement chain

**Raw observable event**: 浏览器或系统直接记录、尚未加入行为或认知含义的事件。
_Avoid_: Student action, cognitive event

**State timeline**: 从原始事件确定性重建的 UI、对象、可见性和选择状态序列。
_Avoid_: Cognitive timeline

**Semantic action**: 能由事件与 UI 状态直接支持的任务层行为，如切题、划线、排除或答案修改。
_Avoid_: Strategy, cognition

**Behavior episode**: 有边界和类型的连续行为片段；边界质量与标签质量分别评价。
_Avoid_: Cognitive episode

**Focus evidence**: 对学生可能处理区域的带不确定性证据；不是视线或注意真值。
_Avoid_: Gaze, attention ground truth

**Evidence packet**: 把行为、时间、题目语义、前后文、候选解释和证据质量绑定在一起的最小推断输入。
_Avoid_: Feature row

**Process hypothesis**: 对 Search、Verification、Monitoring 等过程的可证伪候选解释，必须允许竞争解释和未知。
_Avoid_: Process truth

**Cognitive evidence**: 通过预先声明的独立效度证据支持、且限定适用人群和任务的认知解释。
_Avoid_: Model prediction, expert guess

**Validation Registry**: 记录行为到认知 mapping 的适用范围、证据、替代解释、状态与版本的权威登记。
_Avoid_: Q-matrix

**Student model**: 跨多个题目整合已验证证据后形成的技能或 latent-trait 表示。
_Avoid_: Single-event diagnosis

## Evidence and data roles

**Simulation truth**: 由 data-generating mechanism 写入合成样本的隐藏状态；只在该生成机制下成立。
_Avoid_: Human ground truth

**Human reference annotation**: 由盲化独立标注和裁决形成、服务于特定解释用途的人类参考标准。
_Avoid_: Absolute cognitive truth

**Production evidence**: 常规系统通过低干扰自然交互采集的 `COL-L0 + COL-L1` 证据。
_Avoid_: Research ground truth

**Research evidence**: 为验证 mapping 额外采集的 replay、stimulated recall、人类编码或经批准的独立传感证据。
_Avoid_: Production requirement

**NONRESEARCH_DEBUG_ONLY**: H1 smoke test 只用于发现工程缺陷的产物分类；不得用于训练、统计、论文或后续研究。
_Avoid_: Pilot data

## Stable namespaces

**`COL-L0..L2`**: 采集层级：被动交互、纸面原生显式交互、研究性显式认知报告。
_Avoid_: `L0..L2` without namespace

**`SYS-L0..L7`**: 从 logging 到 student model 的系统测量层。
_Avoid_: Collection L0/L1/L2

**`DATA-D0..D5`**: 外部参考、工程合成、半合成、真人 pilot、主研究和泛化的数据角色。
_Avoid_: Using D3 for a benchmark

**`BENCH-E0..E6`**: Instrumentation、Focus、Segmentation、Process、Construct Validity、Student Model 与 End-to-End 的顶层实验族。
_Avoid_: Historical E0–E10 as canonical IDs
