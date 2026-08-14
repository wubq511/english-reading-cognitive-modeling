# Project Documentation

`docs/` 只存放项目和仓库如何协作、运行与维护的说明；科研问题、证据、综合结论和实验协议仍由 `reports/` 管理。

## Project management

- [`project-management/AGENT_BOOTSTRAP.md`](project-management/AGENT_BOOTSTRAP.md)：Codex/Claude 首次进入项目时的预检机制、信任边界和可选 SessionStart 加固方案。
- [`project-management/SOURCE_DISTRIBUTION.md`](project-management/SOURCE_DISTRIBUTION.md)：协作者如何在不把第三方原件提交到公共 Git 的前提下恢复相同来源版本。
- [`agents/research-workflow.md`](agents/research-workflow.md)：Wayfinder → Spec → Tickets → Implement 的状态机与 artifact ownership。
- [`agents/issue-tracker.md`](agents/issue-tracker.md)：GitHub Issue、sub-issue、dependency、claim 与 publication 操作契约。
- [`../logs/README.md`](../logs/README.md)：按成员记录研究/修改语义、append-only 更正和本地/远端提交门禁。

动态研究状态不在这里维护；以 [`../reports/project_state/CURRENT_STATE.md`](../reports/project_state/CURRENT_STATE.md) 为准。研究事实与外部来源仍遵守 [`../reports/provenance/SOURCE_POLICY.md`](../reports/provenance/SOURCE_POLICY.md)。
