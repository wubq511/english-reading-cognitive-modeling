# Agent Bootstrap Governance

Status: `CURRENT`
Audit date: 2026-08-14
Decision scope: repository-owned initialization when Codex or Claude Code first opens, resumes, or takes over this project

## Conclusion

The current root instructions are already sufficient for the stated operational goal: a conforming Codex or Claude Code Agent receives the bootstrap rule automatically at session start and actively runs `scripts/bootstrap` before project work. The collaborator does not need to know or remember the command. Codex reads `AGENTS.md` before work; Claude Code reads the root `CLAUDE.md` symlink to the same file at session start.

Therefore the recommended **current** design is the minimal contract already present:

```text
AGENTS.md: first task step is scripts/bootstrap
CLAUDE.md -> AGENTS.md: same rule reaches Claude Code
scripts/bootstrap: idempotent setup, source preflight and activity-log identity notice
tracked Git hooks: source continuity plus staged activity-log enforcement
```

The only remaining probabilistic layer is whether a model follows the loaded instruction. Project `SessionStart` hooks remove that model-choice dependency, but add first-use trust, vendor-specific configuration, repeat execution and maintenance cost. No failure evidence currently shows that the instruction route is insufficient. Do **not** add `.codex/hooks.json` or `.claude/settings.json` only for architectural completeness; add them if bootstrap omission is observed or if initialization must occur independently of the Agent's reasoning.

If that stronger requirement later becomes real, the reliable hardening design is:

```text
canonical operation: scripts/bootstrap (idempotent)
shared hook adapter: one repository script with Codex/Claude-compatible JSON output
Codex lifecycle trigger: .codex/hooks.json -> SessionStart
Claude Code lifecycle trigger: .claude/settings.json -> SessionStart
behavioral fallback: AGENTS.md + CLAUDE.md -> AGENTS.md
post-bootstrap continuity: repository-local Git hooks
```

This hardening is stronger than an instruction, while preserving the mandatory trust boundary. `.agents/skills/` and `.claude/skills/` are useful for reusable, model-invoked workflows; neither is an unconditional session-start trigger.

## Is the existing first-step instruction enough?

Yes, for an Agent-mediated workflow and the current evidence.

1. The instruction is not hidden in an optional README. Codex documents that it reads `AGENTS.md` before doing work; Claude Code documents that it loads root `CLAUDE.md` at the start of every session.
2. `CLAUDE.md -> AGENTS.md` removes rule drift: both Agents receive the same first step.
3. `scripts/bootstrap` is idempotent, so “run at the start of every task” safely covers first clone, later pull, resume and a newly discovered inbox file.
4. The Agent can explain the result in ordinary conversation, including an exact `tmp/pdfs/` action. A human does not have to inspect hook logs or remember a recovery command.
5. After the first successful bootstrap, tracked Git hooks cover checkout, merge, pre-commit activity logs and pre-push continuity.

The instruction route is not a hostile-client enforcement mechanism. An Agent can ignore instructions, a different product might not load either rule filename, and a user can bypass local Git hooks. Those are real limitations, but a repository `SessionStart` hook is also not universal: it is vendor-specific, may be disabled, and cannot run silently before workspace/hook trust. For this research repository, source-dependent tools already fail closed, so there is no current justification for paying the additional complexity merely to remove a residual model-compliance risk.

One small wording improvement is justified if the parent task is already editing `AGENTS.md`: require the Agent to **announce that project preflight is running and report `OK` or the exact unresolved item**. That addresses the user's information requirement without adding another execution mechanism.

## What the official mechanisms actually guarantee

| Surface | What loads from a repository | Can execute automatically at session start? | Important boundary |
| --- | --- | --- | --- |
| Root `AGENTS.md` | Codex reads it before doing work and builds an instruction chain once per run | No deterministic command execution; it can instruct the model to run a command | It is behavioral guidance, not an execution hook ([OpenAI: AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)) |
| Root `CLAUDE.md` | Claude Code reads it at the start of every session | No deterministic command execution | Anthropic explicitly describes it as context rather than enforced configuration; a symlink to `AGENTS.md` is supported ([Anthropic: project memory and AGENTS.md interop](https://code.claude.com/docs/en/memory)) |
| `.codex/hooks.json` | Codex loads project hooks from the trusted `.codex/` config layer | Yes: `SessionStart` supports `startup`, `resume`, `clear`, and `compact` | Hooks are enabled by default, but each non-managed command definition is hash-reviewed and skipped until trusted ([OpenAI: Codex hooks](https://learn.chatgpt.com/docs/hooks)) |
| `.claude/settings.json` | Claude Code loads shareable project settings and hooks | Yes: `SessionStart` runs for new and resumed sessions, locally and in Claude Code web | Interactive sessions hold hooks until workspace trust is accepted; project hooks are executable repository content ([Anthropic: hooks](https://code.claude.com/docs/en/hooks), [Anthropic: cloud setup versus SessionStart](https://code.claude.com/docs/en/claude-code-on-the-web)) |
| `.agents/skills/<name>/SKILL.md` | Codex discovers repository skills from the working directory up to the repository root | No | Codex explicitly or implicitly selects a skill from its description; discovery does not mean invocation ([OpenAI: skills and `.agents/skills`](https://learn.chatgpt.com/docs/build-skills)) |
| `.claude/skills/<name>/SKILL.md` | Claude Code discovers project skills | No | Skills are user- or model-invoked and load on demand, not unconditionally at session start ([Anthropic: Claude Code skills](https://code.claude.com/docs/en/slash-commands)) |

Therefore “support `.agents` and `.claude`” must not be implemented as two look-alike startup folders. The official lifecycle locations differ:

- Codex startup hooks belong in `.codex/hooks.json`; `.agents/` is currently the repository skill-discovery convention.
- Claude Code startup hooks belong under `hooks` in `.claude/settings.json`; Anthropic explicitly says there is no standalone `.claude/hooks.json` ([Anthropic: configuration troubleshooting](https://code.claude.com/docs/en/debug-your-config)).

## Trust boundary and first-use behavior

### Codex

Codex supports project-level `SessionStart` command hooks. Commands run with the session working directory, and the official guidance recommends resolving repository scripts through the Git root because Codex may start in a subdirectory. `SessionStart` stdout or `hookSpecificOutput.additionalContext` becomes model-visible developer context; `systemMessage` is surfaced in the UI/event stream ([OpenAI: SessionStart input and output](https://learn.chatgpt.com/docs/hooks)).

However, Codex will not run a newly cloned or changed project command hook until the user reviews and trusts its exact definition. It records trust against the hook hash and tells the user to inspect it with `/hooks`. This is intentional supply-chain protection, not an obstacle to work around. The repository must not recommend `--dangerously-bypass-hook-trust` for normal collaboration.

If the hook is not yet trusted, root `AGENTS.md` remains the fallback: Codex reads it before work, so its first-task rule can require the Agent to announce and run `scripts/bootstrap` itself.

### Claude Code

Claude Code accepts shareable project hooks in `.claude/settings.json`; `SessionStart` is the documented mechanism for project setup that should run both locally and in cloud sessions. A hook can emit `additionalContext` to Claude and `systemMessage` to the user ([Anthropic: SessionStart](https://code.claude.com/docs/en/hooks)).

Interactive Claude Code withholds settings-file hooks until the user accepts workspace trust. After trust, the repository hook can run without a separate remembered command. There is one security-sensitive exception: current Claude Code `-p`/SDK sessions treat the folder as trusted and may run committed `.claude/settings.json` hooks without an interactive dialog. Anyone scripting non-interactive Claude over an unfamiliar repository must inspect `.claude/` first or disable hooks for that run ([Anthropic: workspace trust](https://code.claude.com/docs/en/hooks#workspace-trust)).

The existing root `CLAUDE.md -> AGENTS.md` symlink is the correct single-source instruction arrangement for macOS/Linux. Anthropic also documents `@AGENTS.md` as the Windows-compatible fallback where symlink creation is unavailable ([Anthropic: AGENTS.md interoperability](https://code.claude.com/docs/en/memory#agentsmd)).

## Optional hook hardening design

The design below is ready if observed behavior later establishes that instructions are being skipped. It is not the current recommendation.

### 1. Keep one idempotent operation

`scripts/bootstrap` remains the only owner of repository setup and source preflight. Hooks, instructions, and humans call it; none reimplement its logic.

Add one thin, repository-owned session adapter, for example `scripts/agent-session-start`, whose only responsibilities are:

1. consume or ignore the hook JSON received on stdin;
2. run `scripts/bootstrap` from the Git root;
3. preserve the complete bootstrap output for diagnosis without flooding model context;
4. emit a short JSON result understood by both Codex and Claude Code;
5. always allow the session to continue so the Agent can repair an inbox/source problem.

The fifth property is important. A failing source gate must not end the session before the Agent can inspect and import `tmp/pdfs/`. The adapter should return a concise warning and model instruction such as “bootstrap incomplete; resolve the reported source requirement before source-dependent research,” while source-dependent tooling and pre-push remain fail-closed.

A portable result shape is:

```json
{
  "continue": true,
  "systemMessage": "Project preflight needs attention; the Agent will report the exact item.",
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Run or repair the project bootstrap before source-dependent work. Report the exact unresolved item to the user."
  }
}
```

On an already-configured, healthy clone, the adapter should be quiet or provide only a very short `additionalContext`. On the first successful configuration and on every failure, it should use `systemMessage` so the human sees what happened. This avoids turning every resumed session into notification noise.

### 2. Add the Codex trigger

Use `.codex/hooks.json` with a synchronous `SessionStart` command. Resolve the adapter from `git rev-parse --show-toplevel`, set a bounded timeout, and expose a short `statusMessage` while it runs. Match `startup|resume|clear`, but not `compact`: the hook is idempotent and should catch changed source state after a resume, while compaction is not a new workspace entry and should not repeatedly hash the source corpus.

Codex hooks are enabled by default. A collaborator still has to trust the project hook once, and again when its definition changes; that review is the irreducible Codex first-use action ([OpenAI: hook locations, trust, and defaults](https://learn.chatgpt.com/docs/hooks)).

### 3. Add the Claude Code trigger

Use the same matcher and adapter under `hooks.SessionStart` in `.claude/settings.json`. Reference the root with `$CLAUDE_PROJECT_DIR`, set the same bounded timeout and `statusMessage`, and keep the JSON output contract identical. Project settings are shareable through Git and Claude Code documents SessionStart as the cross-local/cloud setup mechanism ([Anthropic: project settings](https://code.claude.com/docs/en/configuration), [Anthropic: SessionStart](https://code.claude.com/docs/en/hooks#sessionstart)).

Do not add `.claude/hooks.json`; Claude Code does not discover that file. Do not copy the project rules into `.claude/CLAUDE.md`; retain the root symlink so there is one rule owner.

### 4. Retain behavioral fallback and recovery path

Keep the first instruction in `AGENTS.md` as the explicit `scripts/bootstrap` requirement, and require the Agent to tell the user when automatic preflight is unavailable, skipped for trust, or incomplete. This covers:

- older Codex/Claude versions without the current hook behavior;
- a user or administrator who disabled hooks;
- a Codex project hook awaiting `/hooks` review;
- an interactive Claude workspace awaiting trust;
- another Agent product that reads `AGENTS.md` but implements neither vendor hook format.

An optional `project-bootstrap` skill can document manual recovery, but it must remain a convenience only. Duplicating it under `.agents/skills` and `.claude/skills` adds maintenance surface without improving first-entry guarantees. If such a skill is later justified, both thin adapters should point to the same canonical script and protocol rather than duplicate the procedure.

## Acceptance criteria if hooks are later implemented

The implementation should be accepted only when all of the following are demonstrated in disposable clones or isolated config homes:

1. Codex discovers `.codex/hooks.json`, requests trust for a new definition, and runs the adapter after trust.
2. Claude Code interactive mode requests workspace trust and then runs the project `SessionStart` hook.
3. A healthy first run configures repository-local Git hooks and visibly reports first-time success.
4. A repeated run is idempotent and quiet.
5. An unknown file in `tmp/pdfs/` produces a user-visible warning and model-visible exact recovery instruction without terminating the session.
6. Starting either Agent in a repository subdirectory still resolves the root adapter.
7. Compaction does not rerun the expensive source preflight.
8. Hook-disabled or untrusted startup still leaves `AGENTS.md`/`CLAUDE.md` instructions available as the fallback.
9. `scripts/verify` checks the two hook configurations, their shared adapter path, and the `CLAUDE.md -> AGENTS.md` single-source invariant.

## Decision

Keep the minimal cross-Agent mechanism now: root `AGENTS.md`, root `CLAUDE.md -> AGENTS.md`, and idempotent `scripts/bootstrap`. Make the rule explicitly require a concise user-visible preflight result. Do not add `.codex/`, `.claude/settings.json`, `.agents/skills`, or `.claude/skills` for startup solely because those extension points exist.

Escalate to paired project-level `SessionStart` hooks only after either of these triggers:

- a supported Agent demonstrably starts work without running the loaded bootstrap instruction; or
- a workflow requires bootstrap to execute before and independently of the model's first reasoning step.

If escalation occurs, use one shared adapter and both vendor hook files; treat trust approval—not manual bootstrap—as the unavoidable human first-use step. Keep `.agents/skills` and `.claude/skills` out of the startup-critical path because skill discovery is conditional model behavior, not lifecycle execution.
