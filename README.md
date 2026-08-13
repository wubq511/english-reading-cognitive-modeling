# English Reading Cognitive Modeling

本项目研究：在尽量不干扰学生自然作答的前提下，利用英语阅读理解网页中的交互过程证据，恢复可观察的行为过程，并检验这些证据在什么条件下能够支持阅读过程、认知状态和跨题技能判断。

当前首先建立并评测一个**运行时不含大语言模型、生成式 AI 或 AI Agent** 的 baseline。规则、统计模型、心理测量模型和传统机器学习可以作为候选，但算法胜负必须由本项目 benchmark 决定。AI/Agent 可以用于研发、实验编排、合成数据辅助和候选标注；它们不是真人认知真值，且不得进入 baseline 的运行时推断链。

## 当前状态

截至 2026-08-14，本项目已把三段网页研究会话、两份 handoff 和既有文献报告恢复为本地 canonical 知识层。当前**没有**可运行系统、benchmark 结果、真人 pilot 或正式实验数据。最成熟的成果是：

- A/A+/B/C/D/E 与 UI 交互文献的深读资产；
- 部分可观测、分层、可回溯的系统研究框架；
- 题目无关的 measurement/validation 设计；
- 明确允许 `UNKNOWN`、保留 competing hypotheses 的测量边界；
- AI 研究工具与真人研究的治理门禁。

Phase 3/4 在网页会话中只达到草案或“准备开始”状态，不能当作已实现或已完成研究。完整状态见 [CURRENT_STATE](reports/project_state/CURRENT_STATE.md)。

## 新研究员或 Agent 的入口

1. 阅读 [AGENTS.md](AGENTS.md) 和 [CONTEXT.md](CONTEXT.md)。
2. 运行 `scripts/papers doctor`。必需全文不齐时不得开始依赖全文的研究。
3. 阅读 [当前状态](reports/project_state/CURRENT_STATE.md)、[研究问题](reports/project_state/RESEARCH_QUESTIONS.md)、[路线图](reports/project_state/ROADMAP.md) 与 [人工行动队列](reports/project_state/MANUAL_ACTIONS.md)。
4. 系统设计从 [SYSTEM_DESIGN](reports/synthesis/SYSTEM_DESIGN.md) 开始；不要直接从历史聊天或迁移包接续。
5. 涉及 AI 或真人参与者时，分别先通过 [AI 研究工具政策](reports/protocols/AI_RESEARCH_TOOLING_POLICY.md) 与 [真人研究门禁](reports/protocols/HUMAN_RESEARCH_GATES.md)。

项目级完整性检查运行：

```bash
scripts/verify
```

## 目录

| 路径 | 用途 | 是否是日常权威入口 |
| --- | --- | --- |
| `reports/project_state/` | 当前状态、问题、路线图 | 是 |
| `reports/synthesis/` | 已恢复并核验边界后的系统与研究综合 | 是 |
| `reports/protocols/` | 实验、AI、真人研究与数据治理规则 | 是 |
| `reports/research/` | 论文/标准/官方来源的专项审计与获取队列 | 是，用于专项问题 |
| `reports/provenance/` | 来源政策、冲突、恢复记录与交叉索引 | 发生争议时使用 |
| `reports/literature/a-e/` | A–E 论文深读固定资产 | 是，作为文献资产 |
| `reports/literature/ui-interaction/` | UI 行为文献固定资产 | 是，作为文献资产 |
| `papers/` | 本地论文目录、校验值与全文缓存 | 是 |
| `webchat_raw_materials/` | 冻结的恢复证据，只在追溯矛盾时回查 | 否；公开 Git 排除 |

历史 `interation` 拼写和 `chatgpt_A-E` 来源命名已在第二阶段物理重构中移除；旧路径与旧 basename 仍由 provenance crosswalk 保留。

## 不可跨越的证据边界

```text
observable event
  -> reconstructed UI state
  -> semantic behavior / episode
  -> contextual evidence
  -> process hypothesis
  -> validated cognitive evidence
  -> cross-item student model
```

任何一层都不能因为模型拟合、预测准确率或叙述听起来合理而自动跳到下一层。`viewport != attention`、`pointer != gaze`、`dwell != difficulty`、`revisit != confusion`。证据不足时输出 `UNKNOWN`，不是强迫生成完整画像。

## 论文协作

公共 Git 只跟踪书目、DOI、版本、权利状态、下载来源、校验值和工具，不默认分发第三方 PDF。每位协作者执行：

```bash
scripts/papers doctor
scripts/papers sync
```

自动同步只允许使用 catalog 中明确记录的合法下载地址；需要订阅或人工获取时，工具会给出论文 ID、DOI、目标路径和人工动作。详见 [papers/README.md](papers/README.md)。

## 发布状态

计划中的公开仓库为个人账号 `wubq511` 下的 `english-reading-cognitive-modeling`，但尚未创建或发布。公开前必须完成权利、隐私、密钥、链接和历史审计，并在完整报告后再次取得项目负责人的明确批准。

## License scope

项目自有代码采用 Apache-2.0，自有研究报告/协议/文档采用 CC BY 4.0，自建书目元数据和校验值在权利允许范围内采用 CC0。第三方论文、标准、数据、历史聊天和真人研究数据不被本项目重新授权；精确范围见 [LICENSES/README.md](LICENSES/README.md)。
