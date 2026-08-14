# Runtime source skeleton

`src/` 只容纳被研究系统的可执行实现。当前尚未开始 runtime 实现，因此本轮不创建语言包、算法类或假接口。

开始实现时按 `reports/synthesis/SYSTEM_DESIGN.md` 的测量链建立深 Module；每个 Module 用一个小 Interface 隐藏内部复杂度，调用方和测试都只跨该 Interface。不要为了“以后可能替换”提前创建只有一个 Adapter 的抽象层。

预期依赖方向为：

```text
raw measurement -> state reconstruction -> behavioral abstraction
                -> contextual evidence -> validity gate -> student model
```

约束：

- baseline runtime 不调用 LLM、生成式 AI 或 Agent；研究辅助实现不放入本目录；
- 上游只产出可观察或确定性派生事实，不能把认知标签写回 raw/state；
- 原始事件 append-only，所有派生输出必须携带 schema、实现和配置版本；
- 候选算法在 benchmark 前保持可替换，不在目录名中提前宣布 winner；
- 新建 Module 时同时增加对应测试、最小 Interface 说明和失败模式。

具体实现开始前，应先更新架构决策或任务规范，再创建实际代码目录。
