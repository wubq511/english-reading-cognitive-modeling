# 认知目标与可观测性矩阵

> Status: `SOURCE-RECOVERED DESIGN`
> 人工验证：未开始

本矩阵先问“观测中有没有信息”，再问“哪种模型最好”。可观测性不足时，增加模型复杂度不能创造缺失信息。

## 输出类别

- `DIRECT`: 由事件定义直接支持的行为事实。
- `BEHAVIORAL`: 从事件与 state timeline 可靠派生的行为。
- `PROBABILISTIC`: 有信息但存在多个解释，输出分布/置信与 alternatives。
- `VALIDATION-REQUIRED`: 只有经独立 response-process evidence 才能使用认知名称。
- `UNIDENTIFIABLE`: 当前 observation model 下没有足够信息区分。
- `UNKNOWN`: 当前样本证据不足；不代表目标理论上永远不可识别。

## 矩阵

| 目标 | 直接观测 | 主要备选解释 / 失效模式 | 初始类别 | 需要的验证 |
| --- | --- | --- | --- | --- |
| 使用了选项排除 | 排除开关 | 意外开关 | `DIRECT` | 事件 QA |
| 答案更改 | 答案历史 | 意外点击 | `DIRECT` | replay QA |
| 文章/题目已显示 | UI 状态 | 已显示不等于已处理 | `DIRECT` | 埋点（instrumentation）QA |
| 文章回访 | 重建的 viewport/scroll | layout/scroll 伪迹 | `BEHAVIORAL` | 边界标注 |
| 证据区回访 | 回访 + 题目 EvidenceMap | EvidenceMap 可能与学生证据不匹配 | `BEHAVIORAL` | 题目审计 |
| 阅读焦点区域 | viewport、pointer、selection、action history | 眼睛可能在无事件时移动；inactive pointer | `PROBABILISTIC` | 粗粒度回忆与可选独立传感器研究 |
| 证据搜索 | 作答前的导航/回访 + 相关性 | 验证、记忆刷新、正常重读 | `VALIDATION-REQUIRED` | 盲法回忆/编码、按题分层检验 |
| 答案验证 | 候选答案后的相关回访 | 搜索、难度、监控 | `VALIDATION-REQUIRED` | 同上 |
| 监控/不确定性 | 更改、比较、回访 | 策略性检查或意外动作 | `VALIDATION-REQUIRED` | 明确报告 + 外部关联 |
| 难度/困惑 | 长/不规则处理、回访、错误 | 投入度、验证、分心、文本长度 | 通常 `UNKNOWN` | 独立报告与结果证据 |
| 排除选项 C 的原因 | 排除序列 + 邻近证据 | 日志中没有语义推理 | 通常 `UNIDENTIFIABLE` | 定向报告可能恢复部分案例 |
| 句子解释 | 已访问/高亮文本 | 内部语义表征缺失 | 仅凭 trace 为 `UNIDENTIFIABLE` | 访谈/评估任务 |
| 推理技能掌握 | 多次作答 + 已验证证据 | 题目难度、语言知识、策略异质性 | 间接，`VALIDATION-REQUIRED` | 多题 + 独立评估 + 模型检查 |
| 误解 | 系统性错误行为 | 猜测、局部误解、界面错误 | `VALIDATION-REQUIRED`，通常未知 | 设计诊断题 + 独立证据 |

## 可识别性检验

对每个 target 先尝试构造两个不同 latent states 产生同一 observable trace 的反例。如果合理反例在当前 UI 下无法区分，则该 target 不能强制分类；需要增加独立证据、限制用途或标 `UNIDENTIFIABLE`。

## 粒度策略

Focus 先评估 coarse region/paragraph，再根据数据决定是否进入 sentence。Webcam、cursor 或统计模型的点级输出不自动授权更细语义粒度。目标粒度的晋级依据是 held-out calibration、selective risk、cross-device stability 和 construct evidence，而不是视觉上“轨迹看起来对”。

## 必需的不确定性输出

每个非直接输出至少包含：

```yaml
label_distribution: {}
unknown_probability: 0.0
evidence_quality: low | medium | high
alternatives: []
applicability_scope: []
mapping_version: string
```
