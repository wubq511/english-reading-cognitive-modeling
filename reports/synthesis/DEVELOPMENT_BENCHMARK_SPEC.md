# 开发数据集与基准规范

> Status: `DRAFT RECOVERED FROM RAW CHAT`
> 目前不存在任何数据集、实现、运行或结果。

本文件只恢复网页会话中已有且科学边界合理的 Phase 3 设计。迁移包新增的 ADEMP/DOE 工具链、T0–T18、DVC/Snakemake/Hydra/MLflow 等不自动进入本规范；每项需独立论证。

## 1. 开发数据角色

### `DATA-D1` 工程合成

人工控制事件和 UI truth，用于 schema、ordering、replay、state reconstruction、missing/duplicate/out-of-order、visibility、resize/zoom、annotation history 和 answer history。

它不能用于任何 cognition claim。

### `DATA-D2` 经验校准的半合成

```text
versioned item package
  + synthetic student parameters
  + probabilistic behavior policy
  + browser-like raw event renderer
```

真实外部数据只为 duration、transition、revisit、navigation、heterogeneity 等提供带限制的先验。不同 UI/任务间不可直接搬运分布。

若 LLM 参与，只能在预先冻结的 rule/DGM 上生成 surface variants 或候选 edge cases；隐藏状态和 oracle 必须独立生成。详情见 AI policy。

### 认知场景压力测试

刻意让 Search、Verification、Difficulty、Memory Refresh 等不同假设产生相似观测，用来检查模型能否正确 abstain，而不是制造高分类分数。

## 2. 基准家族

| ID | 问题 | 最小输出 |
| --- | --- | --- |
| `BENCH-E0` | raw→state/replay 是否忠实 | 不变量失败、replay 差异、丢失率 |
| `BENCH-E1` | coarse focus 能恢复多少 | macro-F1、Brier、log loss、ECE、risk–coverage、未知检测 |
| `BENCH-E2` | continuous actions 如何分段 | 边界 P/R/F1、位移、segment IoU、split/merge、标签准确率 |
| `BENCH-E3` | process/strategy 是否可恢复与复现 | 每类指标、歧义、稳定性、可复现性 |
| `BENCH-E4` | behavior 名称是否具有认知含义 | 人工参照一致性、效度证据、亚组错误 |
| `BENCH-E5` | process evidence 是否改善 student model | 仅作答增量、校准、外部关联、泛化 |
| `BENCH-E6` | 每层证据的真实边际价值 | 冻结端到端消融、成本/延迟/隐私 |

`BENCH-E0/E2` 的 engineering oracle 与 `BENCH-E4` 的 human reference 不可混为同一 truth。

## 3. 稳定划分策略

至少报告：

- random trial split（仅作为低门槛诊断）；
- leave-student-out；
- leave-item-out；
- leave-passage-out；
- leave-item-type-out（样本允许时）；
- student × passage double holdout；
- observability extrapolation（只研究能力边界，不作为主要排名）。

同一 participant/session/testlet 的相邻 episode 不得跨 train/test 泄漏。

## 4. 候选门槛，而非胜者

- 焦点：weighted heuristic、Bayesian/DBN、HMM、HSMM、supervised temporal、graphical smoother。
- 滚动分段：gap/scrollend rule、change-point、HMM、HSMM、hybrid。
- 个性化：global、per-user、hierarchical prior + adaptation。
- 推断时机：online filter vs offline smoother。
- 学生模型：response-only 与多个 process-aware 候选。

它们必须在同 dataset、split、label/reference、budget 和 metrics 下比较。当前没有任何 winner。

## 5. 晋级原则

模块晋级前必须：

1. 冻结数据版本、split、metric、budget 和 baseline；
2. 报告不确定性、per-class/per-item/per-student 与 subgroup errors；
3. 在至少一个非随机泛化 split 上成立；
4. 对可 abstain 输出报告 risk–coverage；
5. 证明增量不是 leakage、任务 metadata shortcut 或生成器循环；
6. cognition 命名另过 `BENCH-E4`，不能由低层性能自动授权。

具体数值阈值尚未通过真实数据/误差成本确定，保持 `EXPERIMENT-GATE`。

## 6. 可复现性最低要求

每个 run 保留 code commit、environment、data/catalog hash、split manifest、config、seed、metric implementation、output hash 和 provenance。当前尚未决定是否需要 DVC、MLflow、Snakemake 或其他工具；先用最小可重现接口，不把工具选择误当研究成果。
