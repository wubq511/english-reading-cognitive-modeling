# PROTOTYPE — Wayfinder issue #6: baseline answer-UI variants

**Question answered**: which single-factor answer-UI candidate variants are worth freezing, and which interaction/state/event/accessibility properties must stay invariant across them.

**Status**: throwaway decision-support artifact. Not a measurement instrument, not the runtime UI, not evidence that any variant improves measurement or participant outcomes. Reactions to it are design decisions, not research data (`NONRESEARCH` by construction: synthetic content, no persistence, no network, no participants).

## Run

Open `index.html` in any desktop browser (double-click, or `open index.html`). No build, no server, no dependencies. Switch variants with the floating bottom bar, `←`/`→`, or the `?v=0..5` URL parameter. "Events" opens the live canonical-V1 raw-event stream and the state re-derivable from it.

**图文说明（先读这个）**：`explainer.html` — 每个变体的单因子差异、证据锚点具体内容与核实路径、不变量合同与被否替代的逐条理由。截图在 `shots/`。

## Variants (each differs from V0 by exactly one factor)

| Key | Name | Single factor vs V0 | Evidence anchors |
| --- | --- | --- | --- |
| V0 | Baseline dual-column | — reference: locked design (`reports/synthesis/SYSTEM_DESIGN.md` §2) | UIE-15 |
| V1 | Stacked layout | side-by-side columns → vertically stacked panes | UIE-24, UIE-34, UIE-37 |
| V2 | Sidebar navigation | number row → persistent question-list sidebar | UIE-03, UIE-04, UIE-56 |
| V3 | Paginated passage | continuous scroll → discrete pages (page turns emit no canonical event — observability compression is the point) | UIE-12, UIE-56 |
| V4 | Drag-to-eliminate | elimination via drag-to-tray **plus** the SC 2.5.7 single-pointer alternative | UIE-01/02, UIE-23, UIE-31/35, UIE-58 |
| V5 | Visible countdown | no timer → visible countdown, no enforcement | UIE-25, UIE-46/50, UIE-61 |

Passage and items are synthetic, written for this prototype; they are not Candidate Bank items and support no item-level claim.

Provenance: built 2026-08-22 for the resolution of GitHub issue #6 under map issue #2. To be captured on a throwaway branch after the human decision; never merged to main as-is.
