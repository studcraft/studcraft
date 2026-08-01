## Context

`simplify-melee-combat` merged as PR #22. `delete-me-melee-comments.md` is an external review of that shipped document, not a fresh RFC — it assumes the current `MEL-001`–`MEL-014` numbering and comments against it directly (unlike the original RFC, which had a numbering mismatch problem; this review has no such issue since it references `MEL-013` and "current MEL-010" by their actual, correct IDs).

## Goals / Non-Goals

**Goals:** Apply correct review feedback; explicitly reject incorrect feedback with reasoning, rather than silently ignoring or blindly applying it.

**Non-Goals:** Re-litigating decisions already settled in `simplify-melee-combat` (e.g. striking-end sizing, per-weapon Attack Dice counting) — this review didn't challenge those, and neither does this change.

## Decisions

### REVIEW-001 (Attack Die → "Impact attempt") rejected

The review's stated reasoning — "melee should not define dice mechanics; dice already belong to the Combat System" — doesn't match how the *already-shipped, already-reviewed* ranged side actually works. `10-weapons.md` WPN-006 (Rate of Fire) defines Attack Dice **count** as a function of weapon construction (muzzle count), explicitly in the weapons document, not the combat document; `11-combat.md` CBT-004/CBT-005 own dice **resolution** (the 4/5/6 threshold). `MEL-003` (One Weapon, One Impact) already follows this exact split: it defines count (per independently-wielded weapon), and delegates resolution entirely to `MEL-005` → `16-damage-system.md` DMG-011+. Renaming melee's generated unit from "Attack Die" to "Impact attempt" while `WPN-006` keeps calling the identical ranged concept "Attack Die" would create a **new** cross-document terminology inconsistency — exactly the class of bug this repo's review process exists to prevent, not produce. Rejected with this reasoning recorded here rather than silently ignored, since the review was otherwise high-quality and deserves a real answer.

### REVIEW-005 (delete MEL-010) applied with a modification: repurpose, don't delete

The review is factually correct that `MEL-010` adds no rule beyond `MEL-002` post-`simplify-melee-combat`. Its literal recommendation — delete the rule entirely — conflicts with `system/documentation-standards.md`'s "rule identifiers should remain stable" convention, applied consistently throughout this repo's history (`WPN-007`, `SCS-018`, `CMP-002`/`VEH-013`/`MAT-010`, `DMG-008`, and `MEL-010` itself was *already* a repurposed cross-reference rather than a fresh deletion when `simplify-melee-combat` shipped). Deleting it outright would leave a silent numbering gap and risk confusing a future reader who finds `MEL-010` cited somewhere (changelogs, old discussions) with no explanation.

**Resolution:** `MEL-010` becomes an explicit "Merged into Component Targeting" marker — one sentence stating there's no separate rule here, pointing to `MEL-002`. This satisfies the review's correct observation (no duplicate rule remains) without violating the repo's ID-stability convention. Same reasoning as `DMG-008`'s "no gap, repurpose in place" earlier in this repo's history, just with genuinely no replacement mechanic to attach — the marker's only content is the pointer itself.

### REVIEW-002, 003, 004, 006 applied as suggested

All four are straightforward editorial tightening with no architectural implications:
- REVIEW-002 adds a connecting rationale (energy-transfer surface) between muzzle and striking end — pure clarity, no behavior change.
- REVIEW-003 removes comparison examples that were correct but redundant with the rule's own universal statement.
- REVIEW-004 removes a qualifier ("if exposed") already implied by the rule's own "visible" requirement.
- REVIEW-006 tightens `MEL-012`'s wording to state the document's scope in one sentence instead of three clauses.

### REVIEW-007, 008 — no action

Both are praise of already-shipped content (the flow diagram, the ranged/melee unification framing) with no "suggested wording" block, unlike every actionable review item. Nothing to apply.

### No `specs/` delta included

`docs/12-melee.md` has never been formalized as an OpenSpec capability (no `openspec/specs/melee/` exists), and none of this change's edits touch a requirement already formalized elsewhere (e.g. `weapon-construction`'s Impact Strength requirement, modified by `simplify-melee-combat`, is untouched here — REVIEW-002's addition is descriptive prose in `docs/12-melee.md` only). Per `system/proposal-review.md`'s Delta vs. Direct Edit guidance, this is ordinary direct-edit territory. `openspec validate --strict` cannot pass without at least one delta regardless of a change's actual capability impact — that is a tooling limitation for zero-mechanic-impact editorial changes, not a reason to skip the proposal itself. `system/workflow.md` is unambiguous: every `docs/*.md` change requires an OpenSpec proposal, no exceptions, independent of size. This proposal exists to satisfy that rule and to record the accept/reject reasoning; `openspec validate --strict` is expected to fail on the missing delta and that failure is not being treated as a blocker for this specific change.

## Risks / Trade-offs

None beyond the noted `openspec validate --strict` limitation above.

## Open Questions

None outstanding.
