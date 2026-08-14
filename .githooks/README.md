# Repository hooks

这些 hooks 由 `scripts/bootstrap` 通过仓库本地 `core.hooksPath` 启用。`pre-commit` 执行成员日志门禁，checkout/merge/push hooks 执行来源和仓库门禁。机制唯一说明分别见 [`../logs/README.md`](../logs/README.md) 和 [`../sources/README.md`](../sources/README.md)；不要在这里复制流程。
