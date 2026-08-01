## Why

`editorial-reviews-cleanup` (#31) shipped ten edits across `docs/16-damage-system.md`, `docs/10-weapons.md`, `docs/12-melee.md` and `docs/14-glossary.md`. Reviewing the merged diff found three defects, all introduced by that change's own insertions rather than pre-existing.

None affects a rule's meaning. All three are placement or dead-weight problems that make the shipped text read worse than it should.

| # | Defect | Cause |
|---|---|---|
| 1 | `DMG-004`'s closing paragraph now reads as though it belonged to Example 7 | #31 inserted Example 7 ahead of a paragraph that discusses Examples 3 and 4, leaving it three examples away from its subject |
| 2 | `10-weapons.md`'s Summary no longer ends on its strongest line | #31 placed the new architectural line before two weaker closers instead of after them |
| 3 | `editorial-reviews-cleanup`'s `weapon-construction` delta contains a scenario that cannot fail | `WPN-018` and `WPN-019` force a Weapon Body's longest dimension and its firing axis to coincide, so the scenario describes a build the rules already forbid |

## What Changes

- `docs/16-damage-system.md` — move DMG-004's closing paragraph ("A brick-built shield (Resistance 3)...") from the end of the rule to directly after Example 4, the last example it discusses. Text unchanged. It will sit between Examples 4 and 5, which is its original position: it was written as the closer for Examples 3 and 4, and was displaced three times as Examples 5, 6 and 7 were each inserted ahead of it.
- `docs/10-weapons.md` — reorder the Summary's three closing prose lines so the architectural line ends the block. Text unchanged.
- `openspec/changes/editorial-reviews-cleanup/specs/weapon-construction/spec.md` — delete the scenario "Length is measured along the firing axis". The requirement prose above it keeps the firing-axis wording, which is where the content belongs.

## Impact

No rule ID, no numeric value, and no sentence wording changes. Every task is a move or a deletion.

**On editing another change's spec delta.** Defect 3 lives in `editorial-reviews-cleanup`'s delta file. That change is merged but not yet archived, so its delta has not been folded into `openspec/specs/weapon-construction/spec.md` and the vacuous scenario has never reached the living spec. Correcting the delta now is the only way to stop it arriving there at archive time. The alternative — leaving it and remembering to drop it during `archive-cut` — depends on a future reader noticing a scenario that looks plausible.

**Why a separate change rather than an amendment to #31.** While that branch was open, amending it was the right shape and was drafted that way. #31 has since merged, so its proposal, tasks and verification now describe work that shipped. Retroactively appending an amendment section would rewrite the record of a completed change. These three fixes are their own unit of work and get their own change, branch and PR.

Not applied — proposal only.
