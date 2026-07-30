## Context

`delete-me-review.md` is scoped differently from the three prior review files in this thread — it explicitly asks for a repo-wide consistency pass ("Standardize Terminology... across the documentation," "Verify that each subsystem owns only its intended responsibility," "Every document should reference this flow consistently") rather than commenting on one specific document. Treated accordingly: re-verified all 15 `docs/*.md` files against each of the four review items, not just `11-combat.md`/`12-melee.md`.

## Decisions

### VEH-014 (REVIEW-019): found by grepping every document for terms already known to have a single canonical owner

Checked every mention of "weapon system" across `docs/` for one already known to have exactly one owner (`WPN-008`, cross-referenced correctly by `CBT-006`). `VEH-014` had none — it restated the concept a third time with zero cross-reference, missed by `ruleset-consistency-fixes` Finding 10 because that finding's search was scoped to `10-weapons.md`/`11-combat.md` specifically, not the wider `docs/` tree. Fixed the same way as every other instance of this bug class in this repo: cross-reference the owning rule(s), don't restate.

### Diagram unification (REVIEW-020): correct the labeling bug while unifying

While aligning `11-combat.md`'s diagram with the canonical vocabulary, found that its "Attack Roll (CBT-005)" step mislabeled the rule ID — `CBT-005`'s actual title is "Successful Impacts"; "Attack Roll" is `DMG-011`'s title for the same mechanic (which explicitly cites `CBT-005` as owning the threshold). REVIEW-020's suggested canonical flow already lists both as separate sequential steps ("Attack Roll" → "Successful Impacts"), which resolves the mislabel cleanly.

Neither step gets an inline citation in the diagram, matching the pattern already used by the diagram's other same-document steps ("Generate Attack Dice," which `CBT-004` owns): `CBT-004` and `CBT-005` sit a few lines above in the same document, so a citation adds nothing a reader can't already see. Only steps that jump to a *different* document are cited inline (`Delivery Method` → `12-melee.md`; `Component Damage System` → `16-damage-system.md`) — an inline `(CBT-005)` on "Successful Impacts" while its same-document neighbors went uncited would have been a new, smaller inconsistency introduced while fixing a bigger one. Applied this exact structure to all three diagrams:
- `11-combat.md` Combat Flow — added the missing "Successful Impacts" step, fixed the mislabel.
- `16-damage-system.md` DMG-009 "Combat Resolution Overview" — this diagram pre-dated `simplify-melee-combat` entirely (no Delivery Method, "Generate Impacts" instead of "Generate Attack Dice," "Select Component" instead of "Select Target Component" — the latter not even matching `DMG-012`'s own title). Brought fully in line with the other two.
- `12-melee.md` Design Philosophy diagram — "Generate Impact" corrected to "Generate Attack Dice," matching `MEL-003`'s own rule text. Left "Standard Combat Resolution" as a single collapsed label rather than exploding it into the full Attack Roll/Successful Impacts/Component Damage System chain — `MEL-005` already spells that out in full; repeating it in the Design Philosophy diagram would recreate the exact duplication this pass exists to remove, just inside the same document instead of across documents.

### REVIEW-018 (terminology) and REVIEW-021 (language pass): verified, no further action

Every term REVIEW-018 lists was checked with a targeted grep across all `docs/*.md` for competing definitions or unreferenced restatements; all resolved to a single canonical owner already, mostly thanks to prior findings (`ruleset-consistency-fixes`, `remove-materials-document`, the melee/combat review changes). REVIEW-021's two named examples ("physically removed" vs. "removed from the model," "determines" vs. "defines") were checked and found to be legitimate contextual variation, not synonym drift describing the same mechanic twice — no change made. Recording the check itself here, since "we looked and found nothing else wrong" is worth documenting the same as a fix, per this repo's iterative review convention.

## Risks / Trade-offs

None — cross-reference and diagram-wording edits only, no rule ID or mechanic changes.

## Open Questions

None outstanding. This closes out the `delete-me-review.md`/`delete-me-combat-comments.md`/`delete-me-melee-comments.md` review thread; no further addenda expected unless the user provides one.
