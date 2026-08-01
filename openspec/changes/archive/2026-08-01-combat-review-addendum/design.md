## Context

Second addendum in the combat review thread, following `combat-review-cleanup` (PR #25). Unlike the melee thread's addendum (which had one moot item and one real fix), all three items here are new and correct.

## Decisions

### REVIEW-015: split the Combat Flow diagram's blended box, using existing terminology

The prior diagram (from `melee-combat-flow-diagram`, PR #24) labeled Attack Roll through Penetration as one "Combat Resolution" box citing `DMG-009` through `DMG-017`. This blurred a real ownership distinction already established elsewhere in this document: `CBT-005` (Successful Impacts) is the canonical owner of the Attack Roll threshold — `16-damage-system.md` DMG-011 explicitly cites `CBT-005`'s threshold rather than defining its own — while `DMG-012` onward (component selection, Geometry Check, Damage Roll, Component State Change, Penetration) is unambiguously Component Damage System territory. REVIEW-015's suggested split (`Attack Roll` as its own step, then hand off to `Component Damage System`) matches that existing ownership exactly, and its wording ("Successful Impacts") is `CBT-005`'s own rule title — not a new synonym for "Attack Die" or "Impact," so it doesn't trigger the same rejection as the "Impact Attempt" proposals. Applied as suggested, with the diagram citing `DMG-012` through `DMG-017` (not `DMG-009`, which is the overview/TOC rule itself, not a resolution step).

### REVIEW-016: correct to apply now, would have been wrong to apply in combat-review-cleanup

`combat-review-cleanup` (as REVIEW-006) rejected this exact one-sentence version of `CBT-008` because, at that time, the Combat Flow diagram's "Combat Resolution" box was a single unlabeled blob — `CBT-008`'s itemized DMG- citations were the *only* place in `11-combat.md` a reader saw the actual step sequence (assign component → Resistance check → Damage Roll → possible Dead). Removing them then would have removed the only signposting available.

REVIEW-015 (this change) fixes that by giving the diagram its own accurate, itemized "Component Damage System" box. With that box now present a few lines below `CBT-008`, restating the identical DMG-012→017 sequence in `CBT-008`'s prose would create the exact duplication this whole review thread exists to remove — two descriptions of the same step list, several lines apart, in the same document. Applying REVIEW-016 *immediately after* REVIEW-015, in the same change, is what makes it correct: order matters here, not just content.

### REVIEW-017: Summary generalized to match the shipped ranged/melee unification

Straightforward — `simplify-melee-combat` already unified how ranged and melee generate Impacts, but this document's own closing Summary never caught up, still describing weapons in ranged-only terms ("shoot," "fire"). Applied the review's suggested wording, which already uses established terms (Attack Dice, Impact Strength) rather than inventing new ones.

## Risks / Trade-offs

None — accuracy and duplication-removal edits, no rule ID or mechanic changes.

## Open Questions

None outstanding.
