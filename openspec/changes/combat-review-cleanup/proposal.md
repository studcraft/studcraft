## Why

`delete-me-combat-comments.md` is a 15-item external review of `11-combat.md`, framed as "Combat should become a thinner orchestrator." Most of what it asks for was already done by `ruleset-consistency-fixes` (Finding 10/11) and the melee work (PRs #22/#24) before this review was read — this change verifies that against the actual current file, applies the small number of items that are genuinely still open, and rejects the one recurring suggestion ("Impact Attempt" terminology) that keeps resurfacing across all three review files for the same reason each time.

## What Changes

**Applied:**
- **REVIEW-009** — `CBT-011` (No Damage Values) dropped its "Weapons only define: Range / Number of Attack Dice / Impact Strength / Firing Position" list, which duplicated `10-weapons.md`'s own Summary section (Length → Range, Muzzle Count → Attack Dice, Muzzle Size → Impact Strength) almost exactly. Replaced with a direct pointer to that Summary, keeping the one piece of unique content (the historical note on Impact Strength/WPN-021 not being a "hidden stat").
- **REVIEW-006** — `CBT-008` (Defender Resolution) tightened from a longer sentence to a more direct hand-off, without dropping any of its DMG- citations (unlike the review's own minimal one-liner suggestion, which would have lost the step-by-step signposting).
- **Self-identified gap** (not directly requested by any REVIEW item, found while verifying REVIEW-003 and REVIEW-004 against the current file): `CBT-001` (Attack Sequence) states "every attack follows the same procedure" but its own steps 3–4 ("Verify Line of Sight," "Verify Weapon Range") are ranged-specific — melee substitutes a single Physical Contact check (`12-melee.md` MEL-001/MEL-014). Added one clarifying sentence rather than rewriting the sequence.

**Confirmed already resolved, no further action:**
- REVIEW-001 (general ownership philosophy), REVIEW-004 (CBT-003/004 duplication with Weapons), REVIEW-007 (CBT-009 duplication with DMG-006), REVIEW-011 (CBT-013/Armour), REVIEW-012 (Combat Flow diagram) — all already fixed by `ruleset-consistency-fixes` Finding 10/11 or `melee-combat-flow-diagram` (PR #24), verified against the current file rather than assumed.
- REVIEW-005, REVIEW-008, REVIEW-010 — reviewer explicitly recommended no changes (CBT-005, CBT-010, CBT-012); confirmed correct.
- REVIEW-013, REVIEW-015 — general philosophy statements with no concrete wording target; already substantially true of the current file.
- REVIEW-014 — its 4-layer diagram (Weapon → Delivery Method → Combat System → Component Damage System → Physical Consequences) is already substantially present in the Combat Flow diagram shipped by PR #24, which additionally keeps "Generate Attack Dice" visible as its own step (more precise than collapsing it into "Combat System").

**Rejected:**
- **REVIEW-002, REVIEW-003, REVIEW-012's/REVIEW-014's "Impact Attempt" phrasing** — this is the third time across the three review files (`delete-me-melee-comments.md` REVIEW-001, REVIEW-009; now here) that "Impact Attempt" is proposed as a replacement for "Attack Die." Rejected again, same reasoning: `10-weapons.md` WPN-006 already owns "Attack Die" as the construction-side term for the pre-resolution unit a weapon generates; introducing "Impact Attempt" as a second synonym for the identical concept adds terminology drift instead of removing it. REVIEW-003's broader suggestion to replace `CBT-001`'s concrete 8-step list with an abstract 6-step one is rejected on the same grounds as the terminology point, plus its own: `CBT-001`'s current steps already function as a named-step index into `CBT-002` through `CBT-009` (mirroring the same TOC pattern already used by `16-damage-system.md` DMG-009) — abstracting the step names would reduce traceability without removing any actual duplication, since there wasn't any left to remove.

## Impact

- `docs/11-combat.md`: `CBT-001`, `CBT-008`, `CBT-011` edited. No rule ID added, removed, or renumbered.
- No change to any measured rule value, dice mechanic, or resolution sequence.
