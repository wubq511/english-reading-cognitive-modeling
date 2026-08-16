# EXP-001 — Replay-fidelity and engineering-oracle simulations

Status: `READY`

All outputs from this experiment are `simulation-only` engineering evidence.

## Question and claim boundary

- Research question: Can a small deterministic DATA-D1 fixture expose event loss, duplication, arrival reordering, final-state-only oracle blind spots, and ambiguity among `wall_time`, `mono_ms`, and session-local `sequence`?
- Allowed claim: The specified metrics and oracles recover the corruption written into this frozen fixture and demonstrate the stated counterexamples under this data-generating mechanism (DGM).
- Claims this experiment cannot support: prevalence in real sessions; cross-browser/device performance; construct, ecological, or human validity; universal metric thresholds; production readiness.
- Falsification / failure condition: any expected injected defect is missed, an un-injected defect is reported, the final-state blind spot is not reproduced, or `sequence` does not recover the frozen within-session order.

## Inputs and gates

- Data role and dataset IDs: `DATA-D1-REPLAY-ORACLES-V1`, synthetic engineering fixture embedded by the generator and described in `simulation_config.json`.
- Required source IDs: `REPLAY-001`, `REPLAY-002`, `REPLAY-003`, `REPLAY-004`, `REPLAY-005`, `REPLAY-006`, `REPLAY-007`, `REPLAY-008`, `REPLAY-009`, `REPLAY-010`, `REPLAY-011`.
- Human-research gate: `N/A`
- Sensitive-modality gate: `N/A`
- AI research tooling gate: `G0` (AI-assisted implementation and QA only; the executed generator and all oracles are deterministic non-AI code).

## ADEMP and frozen comparison

- Aim: exercise engineering failure detection and clarify ordering-field roles.
- DGM:
  - Scenario 1 injects exactly one missing event, one duplicate instance, and one adjacent arrival-order inversion into an eight-event canonical trace.
  - Scenario 2 compares a two-step trace (`A` then `B`) with a one-step trace (`B`) that has the same final state.
  - Scenario 3 injects a wall-clock rollback, timestamp ties, and transport reordering into one five-event session.
- Estimands: unique-event coverage; missing and duplicate counts; inversion and adjacent-descent counts; first stream divergence; final/full-state and process-trajectory equivalence; inversion count for each ordering field.
- Baseline: final-state equality alone and transport arrival order.
- Candidate methods: stable event identity plus session-local sequence checks; prefix/state-trajectory oracle; wall, monotonic, and sequence ordering comparisons.
- Split and leakage controls: not applicable; the complete fixture is engineering synthetic data and its injected truth is frozen before execution.
- Metrics and versions: `replay-fidelity-oracles/v1`, owned by `reports/research/replay-fidelity-metrics-and-engineering-oracles.md`.
- Compute/time budget: one deterministic standard-library Python run, under one minute.
- Seeds / repetitions: no randomness and no Monte Carlo estimand; one exact run. Monte Carlo uncertainty is not applicable to a deterministic counterexample fixture.

## Exit gate

- Required checks: unit tests pass; generated assertions all pass; run manifest records source/config/data/output hashes; output is labelled `simulation-only`.
- Negative and null-result handling: any mismatch remains visible in `results.json`; the run is `INVALID` rather than selectively omitted.
- Decision rule: mark the run `COMPLETE` only when all predeclared expected outcomes match. This supports implementation selection for BENCH-E0 but does not freeze universal thresholds.

## Provenance

- Owner: `smiling-wei`
- Review record: pending teammate review in GitHub issue #7.
- Supersedes / superseded by: none.
