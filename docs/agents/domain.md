# Domain context for project skills

本仓库使用单一 domain context：根级 [`../../CONTEXT.md`](../../CONTEXT.md)。Agent 在生成 map、spec、ticket、分支、实验或报告时必须使用其中稳定术语。

重大架构和治理决定保存在 [`../adr/`](../adr/)；与任务相关的 ADR 必须在冻结 spec 前读取。不要在 Issue 或 Skill 中创建竞争术语表。新术语先更新 `CONTEXT.md`，必要时通过 ADR 解释迁移，再更新引用面。
