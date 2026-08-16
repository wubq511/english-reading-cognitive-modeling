# 实验规范

每个正式实验使用一个稳定目录 `EXP-<number>-<slug>/`，其中至少包含从 `../templates/EXPERIMENT_SPEC.md` 派生的设计文件。状态只使用 `PROPOSED`、`READY`、`RUNNING`、`COMPLETE`、`INVALID`；只有满足预先声明 exit gate 才能标记 `COMPLETE`。

不要在多个 experiment spec 复制共用 metric 或数据定义；共用定义应有单一 registry，spec 只记录稳定 ID 与版本。

## 当前实验规范

- [`EXP-001-replay-oracle-simulations`](EXP-001-replay-oracle-simulations/EXPERIMENT_SPEC.md)：面向议题 #7 的确定性 `DATA-D1`、`simulation-only` 反例；指标统一由 `reports/research/replay-fidelity-metrics-and-engineering-oracles.md` 维护。
