# Replay-fidelity metrics and engineering oracles

- Status: `DRAFT_FOR_REVIEW`
- Owner: `smiling-wei`
- GitHub decision issue: [#7](https://github.com/wubq511/english-reading-cognitive-modeling/issues/7)
- Experiment: `EXP-001`, run `2026-08-16-simulation-only-v2`
- Metric registry version: `replay-fidelity-oracles/v1`
- Evidence cutoff: 2026-08-16

## 1. Question and claim boundary

This report asks which engineering methods should be evaluated for BENCH-E0 to measure event completeness, deterministic reconstruction, replay equivalence, cross-browser/device fidelity, and failure localization.

The report can support a sourced options decision and a concrete experiment contract. It does **not** show that the current runtime is production-ready, that any threshold is universal, or that a faithfully replayed UI trace identifies a reader's cognitive state. The three included demonstrations are `simulation-only` DATA-D1 engineering fixtures.

## 2. Method and search boundary

The search combined backward/forward citation tracing and targeted searches for: deterministic browser capture/replay; GUI test oracles; cross-browser functional consistency; event ordering and clocks; telemetry duplication; page-lifecycle delivery; and failure-inducing trace reduction. Preference was given to original papers, publisher/author manuscripts, and official specifications. Seven full papers and four official specifications were downloaded or snapshotted, assigned stable IDs, hashed, and passed the repository's per-file format/hash checks.

Recent work was not excluded: `REPLAY-004` is a 2025 empirical GUI-oracle study; the High Resolution Time and WebDriver snapshots are 2026 Working Drafts. TimelyRep (2020, DOI `10.1002/stvr.1745`) and STAn (2023, DOI `10.1007/s10009-023-00719-8`) were screened but not used for full-text-dependent claims because a verified local full text was not obtained. This avoids treating metadata or a failed HTML download as a paper.

The repository-wide `sources doctor` still reports 70 missing historical sources outside this selected set. No claim in this report depends on those missing originals; the global gate remains an explicit project-level unresolved item.

## 3. Evidence table

| ID | Evidence and exact locator | What it establishes here | Limits |
| --- | --- | --- | --- |
| `REPLAY-001` | Xie & Memon (2007), PDF p. 1, Abstract | Oracle content and invocation frequency materially affect fault detection; weak oracles lose faults; some faults are visible only during a short execution window. | Four GUI systems from an older desktop era; does not prescribe a BENCH-E0 threshold. |
| `REPLAY-002` | Mickens, Elson, & Howell (2010), PDF pp. 1–3, Abstract and §3 opening | A final crash snapshot is insufficient for root-cause analysis; deterministic browser replay requires capturing external nondeterminism and event ordering. | JavaScript/browser assumptions and evaluation environment are historical. |
| `REPLAY-003` | Burg et al. (2013), PDF p. 1, Abstract and Introduction | Deterministic web replay captures and reuses user, network, and other nondeterministic inputs; the small user study's larger-task result was null. | Debugging tool, not a metric standard; small evaluation. |
| `REPLAY-004` | Yarifard et al. (2025), PDF p. 2, Abstract; pp. 3–4, §§1–2 | App-specific GUI invariants can augment crash-only/implicit oracles; reported fault-detection improvement was 18%–32% in the studied mobile-app test suites. | Mobile app mutation study; the percentage must not be transferred to this reading UI. |
| `REPLAY-005` | Lamport (1978), journal pp. 558–560 / PDF pp. 1–3, “The Partial Ordering” and “Logical Clocks” | Causal order is a partial order; logical clocks can extend order, while physical time alone is not a sufficient causal ordering rule. | Multi-process theory; a single session-local counter is a project specialization. |
| `REPLAY-006` | Zeller & Hildebrandt (2002), PDF p. 1, Abstract and Introduction | `ddmin` can reduce a failure-inducing input while preserving the failure; the Mozilla example reduced 95 actions to 3. | Requires a stable, automatable pass/fail predicate. |
| `REPLAY-007` | Mesbah & Prasad (2011), PDF pp. 1–4, §§2 and 4.1–4.2 | Cross-browser compatibility is a functional state/trace consistency problem, not merely screenshot similarity; state-machine equivalence is one usable differential oracle. | Old browser stack and finite-state abstraction; visual-only differences remain a separate class. |
| `REPLAY-008` | W3C High Resolution Time Level 3 (2026 WD), §§1 and 2.1 | Wall time may decrease or stay equal; monotonic time is intended for measurement but can be coarsened and is not a cross-execution global clock. | Working Draft; monotonic timestamps can still tie and are not event identities. |
| `REPLAY-009` | W3C WebDriver (2026 WD), §§15.7, 17.1–17.2 | Standard browser actions and screenshot endpoints provide a repeatable driver/observation surface. | Working Draft; a driver and screenshot API do not define semantic correctness. |
| `REPLAY-010` | OTLP 1.11.0, §“Known Limitations → Request Acknowledgements → Duplicate Data” | A client retry after a missing acknowledgement can create server-side duplicate telemetry. | OTLP is not this project's transport; it supplies a primary counterexample to “retry implies exactly once.” |
| `REPLAY-011` | W3C Beacon (2022 CR Draft), §1 Introduction, Example 1 | `visibilitychange` is the lifecycle trigger recommended over `unload`; lifecycle-aware send mitigates termination loss. | Queueing a beacon is not an end-to-end durable-delivery proof or an exactly-once guarantee. |

## 4. Findings

### 4.1 “Replay fidelity” is not one number

The literature supports separating at least four questions:

1. **Did the expected evidence arrive?** Stable identities and an expected sequence expose loss and duplication.
2. **Can the same ordered inputs reconstruct the same states?** Deterministic replay requires the relevant nondeterministic inputs, not only user gestures (`REPLAY-002`, PDF pp. 1–3; `REPLAY-003`, PDF p. 1).
3. **Did important intermediate states agree?** Xie and Memon found that some faults are observable only within a small execution window; therefore a thorough final check can be cost-effective without being universally sufficient (`REPLAY-001`, PDF p. 1).
4. **Is behavior equivalent across environments?** Functional state/transition consistency and user-observable rendering differences are related but non-identical (`REPLAY-007`, PDF pp. 2–4).

Consequently, a single final-state equality flag can report a false pass even when events were lost or the process path changed.

### 4.2 Metric registry `replay-fidelity-oracles/v1`

The following definitions are **PROJECT-INFERENCE**, derived from the source constraints and designed for BENCH-E0 evaluation. They are not claimed as universal published standards.

| Metric | Definition | Direction and diagnostic role |
| --- | --- | --- |
| Unique-event coverage | `|U_observed ∩ U_expected| / |U_expected|`, where `U` uses stable event IDs | Higher is better; isolates missing unique evidence. Report numerator and denominator. |
| Missing-event rate | `|U_expected − U_observed| / |U_expected|` | Lower is better; report missing IDs and sequence gaps, not only the rate. |
| Duplicate-instance rate | `(N_observed − |U_observed|) / N_observed` | Lower is better; preserve retry/arrival records while replay deduplicates by stable ID. |
| Order inversion rate | Pairwise inversions among first occurrences divided by `m(m−1)/2`, relative to the frozen reference order | Lower is better; exposes global reordering. Also report adjacent descents for local debugging. |
| Exact stream equivalence | Ordered normalized event tuples match exactly after declared deduplication rules | Binary strict oracle for deterministic fixtures. |
| Prefix/state-trajectory equivalence | All declared state projections agree after every replayed event | Strict process oracle; catches transient divergences hidden by final state. |
| Final semantic-state equivalence | Declared semantic projection of final reconstructed state agrees | Useful but insufficient alone; exclude volatile/render-only properties explicitly. |
| Timing interval error | On matched adjacent events, compare monotonic intervals; report MAE, P95, maximum, and monotonic violations | Lower is better; do not infer order from a tied or cross-execution monotonic value alone. |
| Cross-environment differential | Per browser/device: unreachable transitions, missing/extra semantic states, invariant violations, final projection mismatches, and separately visual diffs | Zero unexplained semantic differences is the deterministic-fixture target; visual tolerance must be specified per property. |
| First divergence | First event position/ID and first state field whose expected and actual values differ | Localization output, not an aggregate quality score. |

All metric outputs should use `PASS`, `FAIL`, `UNRESOLVED`, or `INVALID`. An unavailable expected event set must not be silently converted to 100% coverage; it is `UNRESOLVED`. A run with source/config/input drift is `INVALID`.

### 4.3 Layered engineering oracles

**PROJECT-INFERENCE:** BENCH-E0 should combine, rather than choose only one of, these oracle layers:

| Layer | Minimum checks | Blind spot if used alone |
| --- | --- | --- |
| O1 Structural ingestion | schema/version, session/producer ID, stable event ID, sequence continuity, duplicate instances, append-only provenance | Does not prove state transitions are correct. |
| O2 Ordered replay | deterministic sort/dedup policy; exact normalized event stream; capture of declared external inputs | Can reproduce an incorrect state reducer perfectly. |
| O3 Prefix transition | invariant and state-projection checks after each event; first divergence | Higher storage/execution cost; only sees properties included in the projection. |
| O4 Final semantic state | answer history outcome, eliminate/restore outcome, submission and other declared semantic fields | Misses compensating errors and alternate paths ending in the same state. |
| O5 Timing | monotonic interval error, lifecycle gaps, clock anomalies | Timing agreement does not prove semantic correctness. |
| O6 Cross-environment differential | same fixture/actions across supported browser/device matrix; semantic state/transition diff plus separate screenshot diff | A common bug across all environments can pass a differential oracle. |

App-specific invariants are a promising supplement because implicit crash-only oracles miss non-crashing faults (`REPLAY-004`, PDF pp. 3–4). They remain fallible specifications: each invariant needs an owner, scope, rationale, and negative test.

### 4.4 Ordering-field roles

High Resolution Time explicitly distinguishes wall and monotonic clocks: wall clocks may be adjusted backwards, while monotonic clocks are for measurement and do not provide a universal cross-execution time (`REPLAY-008`, §§1, 2.1). Lamport separately shows that observable/causal order and physical time are not interchangeable (`REPLAY-005`, journal pp. 558–560).

**PROJECT-INFERENCE:** retain all three fields, with different roles:

| Field | Primary role | Do not use it as |
| --- | --- | --- |
| `sequence` | Session- and producer-local total order; deterministic replay key; gap detection | A duration or a cross-producer causal order without an explicit merge contract. |
| `mono_ms` | Within one execution/time-origin: elapsed time, interval plausibility, latency | Stable identity, total order under ties, or a cross-restart clock. |
| `wall_time` | UTC calendar anchor, human-readable audit, approximate cross-system alignment | The sole replay order or duration clock. |

For multiple producers/contexts, include `producer_id` and either a frozen aggregator sequence or an explicit causal/merge rule. Preserve transport `arrival_index` separately; never overwrite raw arrival evidence when deriving replay order.

### 4.5 Delivery, duplication, and lifecycle

OTLP documents the fundamental retry ambiguity: if acknowledgement is missing, resending may duplicate data (`REPLAY-010`, §“Duplicate Data”). Beacon recommends `visibilitychange` over `unload` for mobile/background lifecycle transitions (`REPLAY-011`, §1 Example 1), but this does not establish durable server acknowledgement.

**PROJECT-INFERENCE:** a BENCH-E0 candidate should therefore test:

- stable `event_id` idempotency across retry;
- local durable buffer and explicit acknowledgement/watermark behavior;
- page background, termination, offline/reconnect, and collector timeout faults;
- raw arrival multiplicity plus a deterministic deduplicated replay view;
- observed gaps as `UNKNOWN/UNRESOLVED` evidence, not reconstructed user actions.

“At least once plus idempotency” is a testable candidate contract; “exactly once” should not be claimed merely because retries exist.

### 4.6 Cross-browser/device oracle

WebDriver supplies standard actions and observation endpoints, including screenshots (`REPLAY-009`, §§15.7, 17), but it is a driver rather than a truth definition. Mesbah and Prasad model functional compatibility through state/transition behavior and explicitly distinguish DOM/trace differences from visible differences (`REPLAY-007`, §§2, 4).

**PROJECT-INFERENCE:** run the identical frozen fixture and action schedule on every supported environment and compare:

1. event capture and ordering metrics;
2. reachable semantic states and transitions;
3. declared GUI/state invariants;
4. final semantic projection;
5. screenshots/layout as a separate, tolerance-bound channel.

Do not let screenshot equality substitute for event/state equivalence, or DOM equality substitute for user-observable correctness.

### 4.7 Failure localization

Every failure should first report the event ID/sequence, state field, environment, and oracle layer at the first divergence. If a deterministic predicate can be replayed automatically, apply `ddmin` to the trace while preserving the same failure signature. Zeller and Hildebrandt's Mozilla case reduced 95 actions to 3 (`REPLAY-006`, PDF p. 1), demonstrating the diagnostic value of a reproducible pass/fail predicate rather than prescribing a fixed reduction rate.

## 5. Simulation-only demonstrations

The frozen design is in `experiments/specs/EXP-001-replay-oracle-simulations/`; bulk output is in ignored run artifacts. The result hash is `6c527fd5d26594f91dd272529b920914066a2995ddc1ad2b41f5d550214ae237`.

| Simulation (`simulation-only`) | Frozen manipulation | Observed result | What it demonstrates—and does not demonstrate |
| --- | --- | --- | --- |
| Event loss / duplicate / disorder | Canonical sequence `1..8`; arrival `1,2,3,5,5,7,6,8` | Missing `[4]`; duplicate instances `1`; inversions `1`; adjacent descents `1`; coverage `7/8 = 0.875`; first divergence at position 4 | The v1 metrics exactly recover injected corruption in this DGM. It says nothing about real loss prevalence. |
| Final-state Oracle blind spot | Reference answer path `A→B`; candidate path `B` | Final state equal; event stream unequal; state trajectory unequal; final-only false negative `true` | Final equality is insufficient for process fidelity. It does not validate a cognitive interpretation of either path. |
| Three ordering fields | Arrival `1,3,2,5,4`; wall rollback/tie; monotonic tie | Inversions: arrival `2`, wall-only `2`, monotonic-only `1`, sequence `0` | Fields have different roles; `sequence` recovers this frozen within-session total order. It is not a universal cross-producer ordering proof. |

All 10 predeclared checks passed, so this exact run is `COMPLETE`. The run was executed from a dirty worktree and records commit `9ef61368f881ead0f4fb63b6a95862598749769a`; that provenance is intentional and prevents the run from being mistaken for a release artifact.

## 6. Decision implications for issue #7

Recommended answer to carry into #8 as experiment gates, not locked product truth:

1. Evaluate the layered O1–O6 oracle stack; do not collapse replay fidelity into final-state equality.
2. Require stable `event_id`, `session_id`, `producer_id`, session-local `sequence`, `mono_ms`, `wall_time`, schema/version, and preserved arrival provenance as candidate evidence fields.
3. Use `sequence` for within-session deterministic replay, `mono_ms` for elapsed-time checks, and `wall_time` for calendar audit.
4. For frozen deterministic DATA-D1 fixtures, require exact recovery of injected counts and zero unexplained semantic mismatches. Treat this as a project engineering gate, not a literature-derived universal threshold.
5. Leave empirical tolerances for real browsers/devices open until BENCH-E0 supplies distributions, negative cases, and repeated runs.
6. Report final state, prefix trajectory, event structure, timing, and cross-environment differentials separately, with first divergence and optional `ddmin` reduction.
7. Preserve `UNKNOWN/UNRESOLVED` when expected evidence is unavailable; synthetic recovery cannot create missing truth.

## 7. Limitations and open questions

- The browser replay and cross-browser papers are foundational but use older platforms. Their principles motivate candidate checks; they do not establish current browser support.
- High Resolution Time and WebDriver are 2026 Working Drafts and may change.
- The 2025 invariant study concerns mobile apps and mutation testing, not this reading UI.
- The simulations are deterministic counterexamples, not performance, stochastic recovery, cross-browser, or field-loss studies.
- No verified TimelyRep/STAn full text was used; their metadata cannot carry detailed formal claims here.
- The project still needs #8 to freeze the actual benchmark matrix, supported environments, state projection, negative fixtures, repetitions, and tolerance rules.
- Global source preflight remains red because 70 historical sources unrelated to the selected #7 evidence are absent in this clone.

## 8. Meeting presentation outline (8–10 minutes)

### Slide 1 — Why issue #7 matters (45 s)

- BENCH-E0 must show that raw UI evidence survives capture, transport, reconstruction, and replay before downstream inference.
- Decision question: which metrics and Oracles should #8 freeze as experiment gates?

### Slide 2 — Main evidence (75 s)

- Deterministic replay needs event order plus external nondeterministic inputs (`REPLAY-002`, `REPLAY-003`).
- Oracle strength and invocation timing change fault detection; final checks can miss transient faults (`REPLAY-001`).
- Recent app-specific invariant evidence shows value beyond crash-only Oracles (`REPLAY-004`, 2025), without transferring its effect size to our UI.

### Slide 3 — Recommended metric stack (75 s)

- Completeness: unique coverage, missing rate, duplicate rate.
- Ordering: inversion rate, adjacent descents, first divergence.
- Equivalence: exact stream, prefix trajectory, final semantic state, timing error.
- Cross-environment: state/transition/invariant differences and separate visual differences.

### Slide 4 — Why one final-state Oracle fails (60 s)

- Show `A→B` versus `B`.
- Same final answer; different stream and trajectory.
- Message: final state is necessary for some questions, never sufficient for replay fidelity.

### Slide 5 — Which time field does what? (75 s)

- Simulation result: wall `2` inversions, monotonic `1`, sequence `0`.
- `sequence`: replay order; `mono_ms`: elapsed time; `wall_time`: calendar audit.
- Multi-producer merge remains an explicit #8 contract item.

### Slide 6 — Layered Oracles and failure localization (75 s)

- O1 structure → O2 ordered replay → O3 prefix state → O4 final semantic → O5 timing → O6 cross-environment.
- First divergence first; then `ddmin` when a stable predicate exists.

### Slide 7 — Decision and remaining gates (60 s)

- Adopt the metric/oracle options as #8 experiment gates.
- Do not freeze real-world tolerances yet.
- Explicitly retain `UNKNOWN/UNRESOLVED`, negative/null results, and `simulation-only` labels.

### Backup slide — Provenance and caveats

- 11 local verified sources; exact source IDs and locators.
- 3 simulations, 10/10 checks; output SHA shown above.
- Global historical-source gate remains red; selected #7 evidence is locally verified.

## References

- `REPLAY-001` — Qing Xie & Atif M. Memon. [Designing and Comparing Automated Test Oracles for GUI-based Software Applications](https://doi.org/10.1145/1189748.1189752). TOSEM, 2007.
- `REPLAY-002` — James Mickens, Jeremy Elson, & Jon Howell. [Mugshot: Deterministic Capture and Replay for JavaScript Applications](https://www.usenix.org/conference/nsdi10-0/mugshot-deterministic-capture-and-replay-javascript-applications). NSDI, 2010.
- `REPLAY-003` — Brian Burg et al. [Interactive Record/Replay for Web Application Debugging](https://doi.org/10.1145/2501988.2502050). UIST, 2013.
- `REPLAY-004` — Ali Asghar Yarifard et al. [Extraction and Empirical Evaluation of GUI-level Invariants as GUI Oracles in Mobile App Testing](https://doi.org/10.1016/j.infsof.2024.107531). Information and Software Technology, 2025.
- `REPLAY-005` — Leslie Lamport. [Time, Clocks, and the Ordering of Events in a Distributed System](https://doi.org/10.1145/359545.359563). Communications of the ACM, 1978.
- `REPLAY-006` — Andreas Zeller & Ralf Hildebrandt. [Simplifying and Isolating Failure-Inducing Input](https://doi.org/10.1109/32.988498). IEEE TSE, 2002.
- `REPLAY-007` — Ali Mesbah & Mukul R. Prasad. [Automated Cross-Browser Compatibility Testing](https://doi.org/10.1145/1985793.1985870). ICSE, 2011.
- `REPLAY-008` — W3C. [High Resolution Time Level 3](https://www.w3.org/TR/hr-time-3/). Working Draft, 24 March 2026.
- `REPLAY-009` — W3C. [WebDriver](https://www.w3.org/TR/webdriver2/). Working Draft, 02 July 2026.
- `REPLAY-010` — OpenTelemetry. [OTLP Specification 1.11.0](https://opentelemetry.io/docs/specs/otlp/).
- `REPLAY-011` — W3C. [Beacon](https://www.w3.org/TR/beacon/). Candidate Recommendation Draft, 03 August 2022.
