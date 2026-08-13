# Existing Literature Validation Audit

Status: `CURRENT`
Audit date: 2026-08-14
Scope: high-leverage claims sampled from the existing A/A+/B/C/D/E/UIB corpus

## Purpose and decision rule

This audit checks the restored reports against the locally held paper originals. It does not treat either the prior ChatGPT analysis or the migration package as evidence. The unit of review is a project claim, not a paper summary.

Labels:

- `SUPPORTED`: the local paper directly supports the claim within the paper's studied population, task, variables and design;
- `PARTIAL`: the paper supports only part of the claim or only a narrower setting;
- `PROJECT-INFERENCE`: a defensible design inference made by this project, but not a finding reported by the cited paper;
- `OVERSTATED`: the current wording exceeds the evidence and must not be used as a factual premise;
- `UNRESOLVED`: the local source is insufficient for a decision.

Page locators below refer to PDF pages unless explicitly described as printed pages. The authoritative file identity is the SHA-256 in `papers/catalog.yaml`.

## Findings

| ID | Claim under audit | Evidence checked | Verdict | Canonical boundary |
| --- | --- | --- | --- | --- |
| LIT-A1-01 | MSRM can estimate multiple latent dimensions from process sequences. | `A1`, Eq. 2 and the simulation plus two empirical studies; see pp. 3–4 and the discussion. | `SUPPORTED` for a pre-specified finite-state task. | The transition→dimension relation and correct/incorrect sign are inputs fixed before analysis. The paper does not validate a reading-skill map, discover dimensions from raw UI events, or establish that scrolling and annotation actions have cognitive correctness. Calling the relation a "process-data analogue of a Q-matrix" is a `PROJECT-INFERENCE`. |
| LIT-AP1-01 | Probability-based transition effectiveness avoids all expert judgment and gives a non-circular cognitive truth. | `A_PLUS_1`, Eq. 1–2 and empirical application; pp. 7–9. State effectiveness is the fraction of sequences containing the state that end in success; transition effectiveness is the change between successor and current state effectiveness. | `OVERSTATED` if used as construct truth; `SUPPORTED` only as an outcome-conditioned indicator. | The indicator reduces one form of manual step scoring, but still inherits the terminal success definition and observed task distribution. It may support engineering comparison or predictive measurement; it cannot by itself prove that an action is cognitively effective. The circularity warning in the synthesis is a project measurement critique, not an author-reported result. |
| LIT-B11-01 | An answer-preceding reread pattern is associated with higher immediate quiz accuracy after measured covariate adjustment. | `B11`, methods, Results 3.1–3.2 and limitations; pp. 1–8. The study reports 263 Japanese high-school EFL learners, 56 units, adjusted OR 1.28 (95% CI 1.07–1.53), and explicitly describes the design as correlational. | `SUPPORTED` within the BookRoll/open-book setting. | This is not causal evidence and does not identify learner intent. The authors say revisits may reflect confusion or distraction; long-term retention and cross-context generalization were not established. In this project, a backward scroll is therefore a candidate reread/evidence-search event, never a strategy label by itself. |
| LIT-C2-01 | Cursor position can be treated as gaze or point-level attention truth. | `C2`, temporal alignment, cursor-behaviour table and conclusion; pp. 4–9. Cursor lagged gaze by at least about 250 ms and about 700 ms on average; inactive behaviour occupied 58.8% of time and had much larger gaze–cursor distance than action behaviour. | `OVERSTATED`; the negation is `SUPPORTED`. | Cursor is contextual auxiliary evidence whose value varies by action and user. It cannot replace eye tracking or justify a global fixed attention weight. Transferring web-search figures to this project's dual-pane English-reading UI would itself require a local study. |
| LIT-D5-01 | Low-level UI events benefit from task/object abstraction before process analysis. | `D5`, abstract, §1 and method; pp. 1–6. The paper explicitly treats raw interaction events as unsuitable for direct process use and proposes online task identification, categorisation and object-instance relations. | `SUPPORTED` as an architecture/method precedent. | The evaluated domains are organizational application tasks, not English reading or cognition. The paper supports separating raw events from higher-level task events; it does not validate this project's semantic labels, reading boundaries or psychological interpretation. |
| LIT-E7-01 | Trace data and think-aloud are interchangeable ground truth channels. | `E7`, abstract, Table 5 and discussion; pp. 1, 12–19. The study involved 44 university students; matched processes occurred for 17.18% of identified time segments, either one channel alone contributed around 45%, and different co-occurring processes appeared for 27.17%. | `OVERSTATED`; non-interchangeability and complementarity are `SUPPORTED`. | Neither channel is an error-free view of cognition. Exact percentages are task- and coding-specific and must not become priors for this project. They support independent-channel triangulation, preserved disagreement and abstention, not forced adjudication. |
| LIT-UIB15-01 | Interaction logs alone recover general human reasoning with approximately 60–79% accuracy. | `UIB-015`, study setup, coding comparison and limitations. The study used WireVis, ten financial analysts and four coders, with a transcript derived from instrumented sessions as the comparison reference. | `PARTIAL` and domain-bound. | Reported recovery rates concern findings, methods and strategies in a highly instrumented visual-analytics task. The paper notes that the reference may not perfectly reflect internal reasoning and that visually inferred methods can remain invisible to coders. The percentages cannot be generalized to natural reading or treated as cognitive-label accuracy. |

## Corrections fixed for canonical use

The high-level synthesis is scientifically conservative and remains usable with these clarifications:

1. `raw event -> semantic behavior` is an engineering abstraction boundary, not a cognition claim.
2. `behavior -> process evidence` remains probabilistic and task-conditioned.
3. Reading-skill mappings, correct/incorrect transitions and Q-matrices are hypotheses requiring independent expert and empirical validation; they are not learned truths merely because a model fits.
4. Outcome-conditioned effectiveness is allowed as a benchmark target, but must be named as such and separated from construct validity.
5. Cursor, viewport, dwell, reread and trace/verbal channels are partial observations. The system must retain competing interpretations and `UNKNOWN`.
6. All quoted effect sizes and percentages remain source-specific descriptive evidence, not default parameters for the new system.

## Consequences for the baseline experiment

- Start with deterministic semantic events whose meaning is fixed by the UI contract, such as `question_opened`, `answer_selected`, `option_eliminated` and paragraph visibility intervals.
- Benchmark segmentation and replay recovery before fitting a latent model.
- Evaluate reread-like and pointer-derived features by ablation against response-only and viewport-only baselines.
- Build a blinded human reference set for any cognitive annotation. Keep the participant account, each coder's label and model output separate.
- Report predictive increment, calibration and cross-item/cross-person generalization separately from construct-validity evidence.
- Treat a model that recovers synthetic generator parameters as a software/statistical recovery result, not evidence of human cognition.

## Files checked

- `papers/library/a-e/A/A1_2025_Han_MSRM.pdf`
- `papers/library/a-e/A/A+1_2026_Wang_TEM.pdf`
- `papers/library/a-e/B/B11_2025_Wijerathne_RereadBeforeAnswer.pdf`
- `papers/library/a-e/C/C2_2012_Huang_UserSeeUserPoint.pdf`
- `papers/library/a-e/D/D5_2024_Rebmann_TaskLevelEvents.pdf`
- `papers/library/a-e/E/E7_2023_Fan_SRLTraceThinkAloud.pdf`
- `papers/library/ui-interaction/UIB-015-recovering-reasoning-processes-from-user-interactions.pdf`

## Remaining audit debt

This is a high-leverage claim audit, not a re-review of all 62 PDFs. Before a claim becomes a frozen model assumption or primary study hypothesis, its exact source passage, study design, population, task, estimator and limitations must be registered in the claim ledger. `needs_metadata` and rights fields in `papers/catalog.yaml` remain separate acquisition-governance debt and do not change the scientific verdicts above.
