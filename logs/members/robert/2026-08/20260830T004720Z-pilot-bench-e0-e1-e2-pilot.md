---
schema_version: 1
member_id: robert
timestamp: 2026-08-30T00:47:20Z
category: documentation
summary: pilot前最小范围自决：只做BENCH-E0+信号冒烟，E1/E2移至pilot后
supersedes: NONE
---

## Work completed

- 1) 从可逆性判据完成分析并决定：pilot 前只做记录+重建+回放（BENCH-E0），加内部 H0 数据上的切分/焦点信号存在性冒烟（go/no-go）；行为切分、焦点估计、思路推断的正式模块与 benchmark 移到 pilot 后；2) GitHub #10 速览记录该决定及依据与条件，#2 速览同步拍板状态（仅剩 #4 篇幅取舍待负责人）；3) reports/project_state/ROADMAP.md 依赖链与 Phase 5 节同步收窄（原 Phase 4 implementation + BENCH-E0/E1/E2 改为 BENCH-E0 + 信号冒烟）

## Research or decision impact

- 研究路线变化：E1（焦点）/E2（切分）正式 benchmark 从 pilot 前移到 pilot 后用 D3 数据完成。依据：采集不可逆、派生可重算；切分候选方法需真实数据定胜负；pilot 出口只需 E0 层指标。保护条件：#8 日志合同须含时间分辨率要求并通过破坏注入测试；信号冒烟不达标先改日志合同再放行外部 pilot。未改变任何科学结论

## Verification

- scripts/verify PASS（local, markdown_files=159, sources=111）；GitHub #2/#10 已读回核对

## Follow-ups

- 待负责人确认仅剩 #4 篇幅取舍（半小时×6篇隐含四六级短篇）；#11 机构路线按成员意见挂起；#8 合同起草时落实时间分辨率条款；pilot 前安排内部信号冒烟
