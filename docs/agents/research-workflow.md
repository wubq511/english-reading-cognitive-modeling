# Research Workflow Contract

Status: `CURRENT`

本文件是 Wayfinder → Spec → Tickets → Implement 状态机的唯一 owner。Skill 负责执行各阶段，本文件负责阶段含义、artifact ownership 和 transition gate。

## First principle

本项目不能按“研究”与“实现”二分：文献决策可能需要代码验证，软件 ticket 可能需要数据研究，实验会同时产生协议、代码、数据和报告。可靠边界不是活动类型，而是当前缺少哪一类可验证承诺：

```text
uncertainty
  -> decision
  -> frozen contract
  -> executable evidence slices
  -> verified evidence/result
  -> reviewed project claim
```

Phase 是依赖与 exit gate 的导航层，不是可直接领取的工作单元。多人并行的最小单元是一个 decision ticket 或 evidence-slice ticket。

## State machine

| State | What is missing | Canonical artifact | Exit gate | Next explicit skill |
| --- | --- | --- | --- | --- |
| `WAYFINDING` | 路径中仍有高代价未知、分歧或不可逆选择 | GitHub parent map + decision sub-issues | frontier 与 in-scope fog 均为空；每个决定有证据、替代项和边界 | `ercm-to-spec` |
| `SPEC` | 已知决定尚未成为可审查契约 | Implementation spec Issue、`EXP-*`，或 hybrid parent | 行为/estimand、输入、输出、gate、验证和 out-of-scope 已冻结 | `ercm-to-tickets` |
| `TICKETS` | 契约尚未分解为单上下文、独立可验的结果 | GitHub evidence-slice sub-issues + native dependencies | spec 覆盖完整；每个 slice 有 owner、claim boundary、gate 和验收 | `ercm-implement <issue>` |
| `IMPLEMENT` | 一个明确 ready slice 尚未产生可审查证据 | 指定 ticket + branch/commit/run/report/data artifact | ticket 验收、项目 gate、review、日志、CI/merge 条件满足 | close or next ticket |
| `BLOCKED` | 外部权利、来源、伦理、权限或上游证据缺失 | Issue blocker + canonical gate owner | 明确 unblock evidence 到位 | return to prior state |
| `DONE` | 无 | merged artifact + required CI + reviewed result | 证据可复现；状态 owner 已更新（若改变项目状态） | none |

状态只能由证据证明，不能由 Agent 宣告。未 push 的本地 commit、未冻结实验、未获得的全文和未审批真人活动都不是 `DONE`。

## Artifact ownership

| Information | One owner | GitHub Issue role |
| --- | --- | --- |
| Wayfinder destination/fog/decision topology | map Issue | canonical map |
| One decision and its resolution | `reports/decisions/wayfinder-<issue>-*.md` (ADR 0008) | discussion/assignment surface; resolution summary links the record |
| Software/UI instrument behavior contract | implementation spec Issue | canonical spec |
| Scientific experiment design | `experiments/specs/EXP-*` | publication, owner, review and status index; no duplicate full spec |
| Hybrid contract | parent spec Issue + linked implementation Issue + `EXP-*` | relationship and collaboration surface |
| Executable work and acceptance | evidence-slice Issue | canonical assignment/status contract |
| Run truth | run manifest and immutable artifacts | links/status only |
| Reviewed scientific conclusion | canonical `reports/` owner | links/discussion only |
| Dynamic phase completion | `reports/project_state/CURRENT_STATE.md` | links/status summary only |

An Issue may summarize what its audience needs, but it must link the owner and must not maintain a second independently editable copy of scientific rules or current phase status.

## Transition rules

### Decision closure review

A decision child closes only through a human review path: the Agent presents a review briefing in chat — work list, headline findings, file guide, open residuals; briefing content is owned by `ercm-research` step 9, procedure by `ercm-wayfinder` Invocation B — and obtains the user's sign-off before landing the decision record under `reports/decisions/`, posting the resolution summary comment linking it, and closing the ticket. A resolution the reviewer of record has not seen is not a resolution, and a ticket closed without review does not count toward the Wayfinder → Spec exit gate. Located-but-unread evidence keeps the ticket open by default; closing earlier is the user's explicit call.

### Wayfinder → Spec

- The destination is a reviewable contract, not “finish Phase N”.
- No open, unblocked decision remains; no in-scope fog remains.
- Closed decisions record evidence, alternatives, uncertainty and downstream implications.
- External unknowns that cannot be resolved now are either explicit spec gates or out of scope, never silently assumed.

### Spec → Tickets

- Implementation specs are approved for decomposition.
- Experiment specs have stable `EXP-*` IDs and an explicit frozen/reviewed state; `PROPOSED` is not executable.
- Hybrid specs keep implementation and experiment acceptance separate and link both through one parent.
- Every spec requirement has exactly one owning ticket or is explicitly out of scope.

### Tickets → Implement

- The user names the exact ticket.
- Ticket is sufficiently specified, unassigned or assigned to the same member, and has no open native blocker.
- External gates are satisfied, not merely documented.
- Parent contract remains current and approved/frozen.

### Selection assistance before assignment

When the user invokes Wayfinder with only a map or Implement without one exact ticket, the Agent provides a read-only decision aid rather than silently choosing or merely refusing:

1. derive the verified decision or execution frontier using [`issue-tracker.md`](issue-tracker.md);
2. show at most three titled Issue URLs with readiness, gates, downstream unlocks and fit with the user's stated goal;
3. recommend one option and explain when an alternative is the better choice;
4. stop before assignment, labels, branches, artifact changes or execution;
5. continue only after the user explicitly names the ticket in a new invocation.

The recommendation is advisory evidence for the human choice. It is not a ticket claim, workflow transition or authorization to execute.

### Implement → Evidence or reopen Wayfinder

- Expected, null, negative and invalid outcomes are all recorded honestly.
- If evidence only answers the ticket, complete the normal review path.
- If evidence invalidates a frozen decision, spec, metric, interface or claim boundary, do not patch downstream tickets ad hoc: create/reopen a decision ticket, record supersession and re-enter Wayfinder.

## UI and experimental-instrument lane

The answer UI is both software and a measurement instrument. Its design can alter reading behavior, observability, missingness, latency and construct interpretation; it cannot be treated as neutral frontend polish.

UI work therefore crosses the state machine as a dedicated lane:

1. **Decision map** — settle natural-reading constraints, required actions, instrumentation granularity, accessibility, device/browser scope, contamination risks and candidate variants.
2. **Implementation spec** — freeze interaction/state/event contracts and replay invariants. UI appearance may vary only where the experiment contract permits it.
3. **Engineering validation** — developer tests and H1 `NONRESEARCH_DEBUG_ONLY` smoke checks may find defects only; their data never selects a scientifically “better” UI.
4. **Instrument reliability experiment** — `BENCH-E0` tests logging completeness, deterministic reconstruction, replay fidelity and cross-browser/device behavior before cognitive claims.
5. **H2-approved UI study** — only after ethics and data gates, compare prespecified variants on usability, task behavior, missingness, measurement reliability and downstream estimands. Freeze assignment, outcomes and analysis before collection.
6. **Confirmation boundary** — exploratory pilot data may select/refine a UI but cannot confirm the same selection effect. Confirmation uses held-out participants/items or a later preregistered study.
7. **Baseline freeze** — record the selected non-AI runtime UI/version before AI vertical or horizontal extensions. AI arms use the same data/split/metric unless their horizontal claim explicitly requires a new contract.

Visual preference alone, completion time alone, or model accuracy alone cannot establish that one UI is a better measurement instrument.

## Collaboration and publication boundary

- Every map, decision, spec publication and evidence slice has a GitHub Issue so members can discover, discuss and assign it.
- Native sub-issues/dependencies define topology; labels define role/status, not scientific truth.
- Wayfinder and Implement may rank and recommend a verified frontier, but neither assigns or works a ticket from that recommendation. The user must name one decision child for Wayfinder or one execution ticket for Implement before any mutation.
- Creating Issues and labels follows the user's standing decision for this workflow. Public push, PR, Release or third-party-file distribution still requires the authorization stated in `AGENTS.md`.
