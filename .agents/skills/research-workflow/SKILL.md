---
name: research-workflow
description: Route an explicitly requested project effort to Wayfinder, Spec, Tickets, or Implement without confusing scientific research with software work. Use only when the user invokes this workflow or asks which stage an effort is in.
disable-model-invocation: true
---

# Research Workflow Router

This is a **user-invoked router**, not an execution shortcut. Determine the current state and tell the user the one next explicit command. Do not silently run the next stage.

## Start

1. Run the repository preflight required by `AGENTS.md`.
2. Read `docs/agents/research-workflow.md` and `docs/agents/issue-tracker.md` completely.
3. Read the supplied GitHub Issue, map, spec, experiment file, or ticket. If no artifact was supplied, use the current conversation and canonical project state.

## Route by uncertainty, not by activity type

Research can contain code, and implementation can contain literature or data work. Route by what is missing:

- An important decision is unresolved or the path is still foggy → `/wayfinder` in Claude Code or `$wayfinder` in Codex.
- Decisions are resolved, but no reviewable contract is frozen → `/to-spec` or `$to-spec`.
- A spec is frozen, but the work is not divided into independently verifiable evidence slices → `/to-tickets` or `$to-tickets`.
- The user named one executable, ready GitHub ticket → `/implement <issue>` or `$implement <issue>`.
- New evidence invalidates a frozen decision or contract → reopen Wayfinder; do not patch the contradiction inside a ticket.

Never route a broad phase, map, spec, or whichever ready ticket happens to be first directly to Implement.

## Output

Return exactly these fields, concisely:

```markdown
State: WAYFINDING | SPEC | TICKETS | IMPLEMENT | BLOCKED | DONE
Evidence: <artifact and gate that prove the state>
Missing: <the one contract/gate still absent, or None>
Next: <one explicit command with an issue/path argument>
Why: <one sentence>
```

If state is `BLOCKED`, name the external dependency, canonical owner, and condition that would unblock it. If state is `DONE`, cite merged/verified evidence; an unpushed local change is not done.
