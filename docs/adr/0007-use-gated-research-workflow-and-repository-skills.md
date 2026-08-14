# ADR 0007: Use a gated research workflow and repository-distributed skills

Status: Accepted
Date: 2026-08-14

## Context

Project phases mix literature, human decisions, data work, experiments, UI instrumentation and code. Dividing collaboration into “research tasks” and “implementation tasks” would misroute hybrid work and allow broad phases to become unauditable tickets. Team members also use both Codex and Claude Code, so relying on separately installed personal skills would produce version and behavior drift.

## Decision

Use the state machine owned by [`../agents/research-workflow.md`](../agents/research-workflow.md): Wayfinder resolves uncertainty, Spec freezes a verifiable contract, Tickets divide it into evidence slices, and Implement executes one user-selected ready ticket.

Every collaboration artifact has a GitHub Issue. Scientific experiment specs remain versioned `EXP-*` files, with Issues as publication/status surfaces rather than duplicate scientific owners.

Store one tracked physical skill set under `.agents/skills/`. The five public entry points are explicit-only on both platforms. Bootstrap generates ignored, platform-native Claude Code mappings under `.claude/skills/` that resolve to the same physical directories; mappings are never a second tracked skill copy. Supporting skills retain on-demand model invocation.

Namespace every adapted project skill with `ercm-` (English Reading Cognitive Modeling), including support skills. This prevents the project variants from colliding with globally installed upstream skills while keeping one memorable router, `ercm-workflow`.

## Consequences

- Phase names remain roadmap/navigation units; members claim bounded decision or evidence-slice Issues.
- Research code and implementation research are both valid; routing depends on missing contract, not activity type.
- GitHub gives a shared map, assignment and dependency view without becoming a second scientific truth store.
- macOS/Linux use generated directory symlinks; Windows uses generated directory junctions. Ignoring these derived mappings prevents platform-specific file types from polluting Git status.
- Repository skill updates are code/governance changes and must pass evals, repository verification and activity-log gates.

## Supersedes

This decision supersedes the “do not add `.agents/skills` or `.claude/skills` without observed bootstrap failure” portion of the 2026-08-14 bootstrap audit. Skills are now justified by the explicit cross-member workflow requirement, not as unconditional startup hooks.
