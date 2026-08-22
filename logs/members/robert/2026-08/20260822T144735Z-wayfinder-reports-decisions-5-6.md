---
schema_version: 1
member_id: robert
timestamp: 2026-08-22T14:47:35Z
category: governance
summary: Wayfinder 决策答案改为仓库内决策记录（reports/decisions/），含 #5 回填与 #6 记录
supersedes: NONE
---

## Work completed

- 新建 reports/decisions/（README + wayfinder-5 回填记录 + wayfinder-6 决策记录）；新增 docs/adr/0008；同步更新 research-workflow.md ownership 表与关票审查节、ercm-wayfinder SKILL.md 不变量与 Invocation B 第 6 步、SOURCE_POLICY.md canonical 归属地图、reports/README.md 导航。

## Research or decision impact

- 治理变更：Wayfinder 决策答案的 canonical owner 由 Issue resolution 评论改为 reports/decisions/ 下的 Markdown 记录（ADR 0008），Issue 回归协作/讨论表面。#6 决议内容（V0–V5 候选变体集 + 8 条不变量合同 + 被否替代）随记录落档，输入 #8/#13。

## Verification

- scripts/skills doctor OK (physical=13)；scripts/skill-evals doctor OK (skills=5 evals=17)；scripts/verify OK (markdown_files=149 sources=111)；pytest tests/ 55 passed。

## Follow-ups

- 等待用户批准 push/PR；合并后在 #6 发布 resolution 摘要评论、关票并更新地图 #2 的 Decisions so far；原型谱系分支 kimi/robert/issue-6-ui-variant-prototype 待一并 push。
