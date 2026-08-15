# 资产地图（Asset Map）

| 资产 | 用途 | 权威性/使用方式 | 公开 Git 默认 |
| --- | --- | --- | --- |
| 根目录 `README.md`、`AGENTS.md`、`CONTEXT.md` | 定位、规则与术语 | canonical；`CLAUDE.md` 导入 `AGENTS.md`，经由跨平台 `@AGENTS.md` shim | 包含 |
| `docs/project-management/` | Agent 启动、来源同步与仓库协作 | canonical 项目操作 | 包含 |
| `docs/agents/` + `.agents/skills/` | 研究工作流状态机、GitHub tracker 契约与随仓库分发的 Agent 流程 | canonical 工作流文档 + 可执行的 Agent 指南；Claude 映射不含第二份副本 | 包含 |
| `logs/` | 各成员的研究/变更意图、验证与后续事项 | canonical 的 append-only 协作历史；精确 diff 保留在 Git | 包含；排除敏感或受许可的内容 |
| `reports/project_state/` | 当前状态与计划 | canonical | 包含 |
| `reports/synthesis/` | 恢复的系统/研究设计 | canonical，带主张标签 | 按 CC BY 4.0 政策包含 |
| `reports/protocols/` | AI/真人/实验门禁 | canonical | 包含 |
| `reports/research/` | 科学一手来源审计与精确的研究获取队列（acquisition queue） | canonical 范围内的研究 | 包含 |
| `reports/provenance/` | 审计轨迹与 crosswalk | canonical 溯源 | 包含，排除敏感内容 |
| `reports/literature/a-e/` | 详细的论文深读 | 派生研究资产；高风险主张需对照 PDF 核验 | 来源链接清理后包含 |
| `reports/literature/ui-interaction/` | UI 论文笔记 | 派生研究资产 | 重命名/链接清理后包含 |
| `sources/catalog.yaml` | 稳定的外部来源身份、类型、版本、路径、获取渠道、权利与精确字节 | canonical 机器索引 | 在 `LICENSES/README.md` 的元数据许可范围内包含 |
| `sources/checksums.sha256` | 精确的本地来源版本 | 完整性 | 包含 |
| `sources/library/` | 第三方论文、标准、研究材料与数据集 | 一手外部证据/输入 | 排除，除非逐项完成权利清除并单独批准 |
| `src/` | baseline runtime 实现边界 | 未来代码；目前仅为规范性骨架 | 包含 |
| `experiments/` | 实验规范与 run manifest 模板 | canonical 实验设计层 | 包含 |
| `data/` | 项目生成、派生或真人数据 | 由数据角色治理 | 包含文档；生成/真人数据按政策排除 |
| `artifacts/` | 可复现的 run 输出 | 非 canonical 的机器输出 | 排除大批量/敏感 runs；仅包含经审阅的小型 manifest |
| `webchat_raw_materials/chatgpt_chathistory/` | 完整恢复 transcript | 最高等级的历史项目状态证据 | 排除；本地冻结 |
| `webchat_raw_materials/handoff/` | 精简的会话 handoff | 历史派生证据 | 排除；本地冻结 |
| `webchat_raw_materials/chatgpt_migration_package/` | GPT 生成的迁移提案/参考 | 最低等级的恢复权威 | 排除；本地冻结 |
| 未来的 `data/human/` | H2/H3 参与者数据 | 受限研究数据 | 始终排除 |
| 未来的 `data/synthetic/` | 工程/仿真数据 | 仅限仿真（simulation-only），需溯源 | 许可/体积审查后有选择地包含 |

## 已完成的物理重组

2026-08-14 历史报告路径被移至 `reports/literature/*`；历史名称 `papers/chatgpt_A-E` 与 `papers/ui_interation_behavior` 先成为中立的本地库。之后一次经确认的来源边界迁移把容易误导的 `papers/` 根目录替换为类型化的 `sources/library/{papers,standards,study-materials,datasets}` 路径。catalog、校验值、crosswalk、导航与工具一并更新；既有来源字节得到保留。

人工获取的论文 PDF 现在只通过 `tmp/pdfs/` 进入。catalog 身份与目标字节核验通过后，`scripts/sources inbox` 移除临时副本；未解决的文件留在收件箱。

仍开放：任何删除之前先确定 UIB-088 的来源与首选同作品 PDF 版本。

重命名迁移不会删除任何 canonical 来源。收件箱清理需单独授权，且只在核验导入后发生。
