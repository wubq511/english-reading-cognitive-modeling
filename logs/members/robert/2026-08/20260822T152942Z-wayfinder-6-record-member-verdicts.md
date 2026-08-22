---
schema_version: 1
member_id: robert
timestamp: 2026-08-22T15:29:42Z
category: research
summary: Wayfinder #6 决议记录按成员逐变体判决修订——V1/V2/V4 移出候选集、V3 保留、V5 双显示模式
supersedes: NONE
---

## Work completed

- 修订 reports/decisions/wayfinder-6-baseline-ui-variants.md：候选变体集由 V0+V1..V5 收缩为 V0+V3+V5；V1 纵向堆叠、V2 侧栏导航、V4 拖拽排除移入「被否替代」并附原证据锚点、判决理由、独立核查与重开条件；V5 由「可见倒计时」修订为「可见计时（倒计时/正计时两种显示模式）」；不变量 8 中 SC 2.5.7 改为条件条款、SC 1.4.10 补充桌面缩放触发说明；下游含义与评审谱系同步更新。

## Research or decision impact

- 冻结集变为 V0（参照）+ V3 篇章分页 + V5 可见计时；V3 是否采用由后续实验实测决定。计时政策（限值、默认显示模式）、V3 翻页 schema 取舍、设备范围终案仍流向 #8；成员「桌面优先」取向记录为 #8 设备范围冻结的输入而非结论。有意识的放弃：冻结集不再含反应格式操纵（V4 证据锚点最强但被否，理由与重开条件已记录）。

## Verification

- scripts/verify OK (markdown_files=151 sources=111)。

## Follow-ups

- 等待成员对修订版记录整体 sign-off 及 push/PR 授权；之后按既定序列：push 两分支、records 分支开 PR、合并后 #6 发 resolution 摘要评论并关票、更新地图 #2 的 Decisions so far、报告新 frontier。
