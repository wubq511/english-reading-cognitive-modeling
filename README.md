# English Reading Cognitive Modeling

本项目研究：在尽量不干扰学生自然英语阅读作答的前提下，UI 过程证据能以什么精度、校准度和效度支持行为恢复、过程假设、认知解释和跨题技能判断。

研究分阶段进行：先实现并优化运行时不含 LLM、生成式 AI 或 Agent 的 baseline，得到可复现的能力上限与失败边界；再以相同数据、split 和 metric 研究 AI 的纵向增强与横向拓展。AI/Agent 当前即可用于受治理的文献、合成数据、实验编排、候选标注和 QA，但不能自造真人认知真值。

## 当前状态

项目的唯一动态状态入口是 [CURRENT_STATE.md](reports/project_state/CURRENT_STATE.md)。路线图只定义依赖顺序和 exit gate，不在 README 复制会过时的 phase 状态。

## 新研究员或 Agent

```bash
scripts/bootstrap
scripts/verify
```

`bootstrap` 是克隆后的唯一初始化命令：安装仓库 hooks，处理人工下载收件箱，恢复允许自动获取的外部来源并 fail closed 地验证本地研究环境。随后按 [AGENTS.md](AGENTS.md) 的顺序阅读项目上下文；Claude Code 通过根级 `CLAUDE.md` 软链读取同一规则。

## Canonical navigation

| Path | Single responsibility |
| --- | --- |
| `CONTEXT.md` | 项目术语 |
| `reports/project_state/` | 当前状态、研究问题、路线图和人工行动 |
| `reports/synthesis/` | Baseline 系统与测量设计 |
| `reports/protocols/` | 实验、AI、真人与数据治理 gate |
| `reports/research/` | 有范围的一手来源专项审计 |
| `reports/provenance/` | 来源权威、知识 owner、矛盾和路径谱系 |
| `reports/literature/` | 已沉淀的文献深读资产 |
| `sources/` | 外部论文、标准、题目、第三方数据及其 catalog/checksum |
| `src/` | 未来 baseline runtime 实现；当前只有边界规范 |
| `experiments/` | 实验设计、模板和 run 复现契约 |
| `data/` | 项目生成、采集或派生数据 |
| `artifacts/` | 可重建运行输出，不是 canonical 结论 |
| `webchat_raw_materials/` | 本地冻结追溯证据；非日常入口，公共 Git 排除 |

同一事实的 canonical owner 和变更防腐流程见 [SOURCE_POLICY.md](reports/provenance/SOURCE_POLICY.md)。其他文件应链接 owner，不维护竞争版本。

## Source collaboration

需要人工获取的论文统一放入：

```text
tmp/pdfs/
```

Agent 负责核实身份、版本、来源、权利和 hash，更新 `sources/catalog.yaml` 后运行 `scripts/sources inbox`。只有正式目标再次验证成功，工具才删除收件箱副本；未知文件会保留并要求 Agent 审查。完整流程见 [sources/README.md](sources/README.md)。

公共 Git 默认只发布来源 metadata、checksum、获取说明和权利状态，不发布第三方原件。创建公开仓库、push、Release 或逐文件分发必须在最终审计后再次获得用户明确批准。

## Evidence boundary

```text
observable event
  -> reconstructed UI state
  -> semantic behavior / episode
  -> contextual evidence
  -> process hypothesis
  -> validated cognitive evidence
  -> cross-item student model
```

任何一层都不能因为模型拟合、预测准确率或叙述合理而自动跳到下一层。`viewport != attention`、`pointer != gaze`、`dwell != difficulty`、`revisit != confusion`；证据不足时输出 `UNKNOWN`。

## License scope

项目自有代码采用 Apache-2.0，自有研究报告/协议/文档采用 CC BY 4.0，自建书目元数据和校验值在权利允许范围内采用 CC0。第三方来源、历史聊天和真人研究数据不被本项目重新授权；精确范围见 [LICENSES/README.md](LICENSES/README.md)。
