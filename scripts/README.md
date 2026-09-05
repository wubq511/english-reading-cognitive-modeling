# Stable command entrypoints

`scripts/` 只放研究工作流的稳定命令入口和仓库治理工具。当前 `bootstrap`、`skills`、`workflow`、`sources`、`logs` 与 `verify` 是有效入口；Windows 使用对应 `.cmd` 包装。版本化第三方 CLI 必须遵守根级 `AGENTS.md` 的 `vendor_imports/tools/` 约定。

- `skills install|doctor`：生成并校验 `.agents/skills` 到 Git 忽略的 `.claude/skills` 的跨平台单源映射，同时校验显式调用策略。
- `skill-evals doctor`：按 skill-creator schema 校验五个显式入口的行为 eval 覆盖。
- `workflow labels-check|labels-install`：核对或幂等安装 GitHub workflow label manifest；`labels-install` 会修改公开仓库，只能在明确授权的 workflow 发布范围内运行。
- `verify`：默认校验本地完整研究工作区；`verify --public` 只校验可提交的公开快照，不要求本地 raw/PDF 原件。`pre-push` 默认走完整模式；仅当用户明确声明本次提交不需要本地原件时，可对该次 push 设置 `ERCM_VERIFY_MODE=public`。该一次性选项不改变 catalog 中的 `required`、rights 或 provenance 状态。

未来实验脚本应调用 `src/` Module 的公开 Interface，并负责配置、I/O 与 manifest 编排；不要在脚本中复制核心测量或建模实现。
