# Repository skill set

`.agents/skills/` is the only tracked physical source for project skills. Codex discovers it directly; after bootstrap, Claude Code consumes generated, Git-ignored mappings under `.claude/skills/`.

Every adapted project skill uses the `ercm-` namespace (English Reading Cognitive Modeling). This keeps it distinct from globally installed upstream skills. Do not add an unprefixed project skill.

The five public workflow entry points are user-invoked only:

- `ercm-workflow`
- `ercm-wayfinder`
- `ercm-to-spec`
- `ercm-to-tickets`
- `ercm-implement`

Their supporting skills retain model invocation so an explicitly started stage can use them when needed. Workflow and tracker semantics are owned by `docs/agents/`; skill files contain stage procedures, not a second project policy.

Several supporting skills and the original stage designs are adapted from Matt Pocock's skills under the MIT License. See `LICENSES/MATT-POCOCK-SKILLS-MIT.txt`.
