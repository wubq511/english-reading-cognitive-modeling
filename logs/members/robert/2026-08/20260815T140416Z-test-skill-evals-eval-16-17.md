---
schema_version: 1
member_id: robert
timestamp: 2026-08-15T14:04:16Z
category: code
summary: 修复 test_skill_evals 硬编码 eval 计数（16→17）
supersedes: NONE
---

## Work completed

- PR #17 的 CI 三 check 全挂：tests/test_skill_evals.py:18 硬编码断言 eval 总数为 16，ercm-wayfinder 新增 eval id 5 后实际为 17。本地 skill-evals doctor 只跑结构校验不跑 unittest，未能提前抓到。已把计数改为 17。

## Research or decision impact

- 无研究影响；CI 门禁恢复绿色。教训：evals.json 变更必须跑完整 unittest 套件而非仅 doctor。

## Verification

- python3 -m unittest discover -s tests：55 tests OK；scripts/verify OK markdown_files=115 sources=86。

## Follow-ups

- 推送后确认 PR #17 CI 转绿。
