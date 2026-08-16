# Experiment specifications

每个正式实验使用一个稳定目录 `EXP-<number>-<slug>/`，其中至少包含从 `../templates/EXPERIMENT_SPEC.md` 派生的设计文件。状态只使用 `PROPOSED`、`READY`、`RUNNING`、`COMPLETE`、`INVALID`；只有满足预先声明 exit gate 才能标记 `COMPLETE`。

不要在多个 experiment spec 复制共用 metric 或数据定义；共用定义应有单一 registry，spec 只记录稳定 ID 与版本。

## Current specifications

- [`EXP-001-replay-oracle-simulations`](EXP-001-replay-oracle-simulations/EXPERIMENT_SPEC.md): deterministic DATA-D1 `simulation-only` counterexamples for issue #7; metrics are owned by `reports/research/replay-fidelity-metrics-and-engineering-oracles.md`.
