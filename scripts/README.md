# Stable command entrypoints

`scripts/` 只放研究工作流的稳定命令入口和仓库治理工具。当前 `bootstrap`、`sources`、`logs` 与 `verify` 是有效入口；版本化第三方 CLI 必须遵守根级 `AGENTS.md` 的 `vendor_imports/tools/` 约定。

未来实验脚本应调用 `src/` Module 的公开 Interface，并负责配置、I/O 与 manifest 编排；不要在脚本中复制核心测量或建模实现。
