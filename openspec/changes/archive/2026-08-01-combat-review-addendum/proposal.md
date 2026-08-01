## Why

A second addendum to `delete-me-combat-comments.md` (REVIEW-015 through REVIEW-017), following `combat-review-cleanup` (PR #25). Unlike the repeated "Impact Attempt" proposals rejected three times across this review thread, all three items here are genuinely new and, on inspection, correct.

## What Changes

- **REVIEW-015 applied** — the Combat Flow diagram's "Combat Resolution" box bundled `CBT-005`'s Attack Roll (a Combat-owned mechanic) together with `DMG-012`–`DMG-017`'s component-targeting/damage steps (Component Damage System-owned) under one label. Split into two boxes matching actual rule ownership: **Attack Roll (CBT-005)**, then **Component Damage System (DMG-012 through DMG-017)**. This uses `CBT-005`'s own existing title ("Successful Impacts" is the rule; "Attack Roll" is what it resolves) rather than the "Impact Attempt"/"Successful Impact" vocabulary the review's own wording suggested — no new terminology introduced, just a more accurate split of an already-correct diagram.
- **REVIEW-016 applied (now, not when first proposed as REVIEW-006)** — `CBT-008` reduced to a one-sentence hand-off, dropping its DMG- citation list entirely. This wasn't right when `combat-review-cleanup` considered it (then called REVIEW-006): at that point the Combat Flow diagram's "Combat Resolution" box was a single vague blob, so `CBT-008`'s detailed steps were the only place a reader saw the DMG-012→017 sequence spelled out. Now that REVIEW-015 (above) gives the diagram its own accurate, itemized "Component Damage System" box, `CBT-008` restating the same list would duplicate the diagram sitting a few lines below it. Applying REVIEW-016 now, immediately after REVIEW-015, removes that duplication instead of creating it.
- **REVIEW-017 applied** — the document's closing Summary still read as ranged-only ("How far they shoot," "Where they can fire") despite `simplify-melee-combat` having unified ranged and melee generation. Reworded to "How an attack is delivered (ranged or melee)," "How many Attack Dice it generates," "The Strength of each Impact" — covers pistols, cannons, swords, spears, and unarmed attacks without a melee-specific carve-out.

## Impact

- `docs/11-combat.md`: Combat Flow diagram, `CBT-008`, and the Summary edited. No rule ID added, removed, or renumbered.
- No change to any measured rule value, dice mechanic, or resolution sequence — this corrects documentation accuracy (who owns which step) and removes a duplication that only existed because of the order these two changes needed to happen in.
