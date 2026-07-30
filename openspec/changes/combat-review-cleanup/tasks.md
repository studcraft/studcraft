## 1. Verify each review item against the current file before acting

- [x] 1.1 Reread the full current `docs/11-combat.md` and check each of the 15 review items against actual content, not assumed prior state.
- [x] 1.2 Confirm REVIEW-004, REVIEW-007, REVIEW-011, REVIEW-012 already resolved by `ruleset-consistency-fixes` (Finding 10/11) and `melee-combat-flow-diagram` (PR #24) — no action needed.
- [x] 1.3 Confirm REVIEW-005, REVIEW-008, REVIEW-010 correctly recommend no changes — no action needed.
- [x] 1.4 Confirm REVIEW-001, REVIEW-013, REVIEW-014, REVIEW-015 are general philosophy/architecture statements already substantially true of the current file — no concrete action needed.

## 2. Apply genuinely actionable items

- [x] 2.1 REVIEW-009: `CBT-011` — drop the Range/Attack Dice/Impact Strength/Firing Position list (duplicates `10-weapons.md`'s own Summary), keep the Impact Strength historical note.
- [x] 2.2 REVIEW-006: `CBT-008` — tighten wording, keep the DMG- citation signposting.
- [x] 2.3 Self-identified gap: `CBT-001` — add one sentence noting melee substitutes Physical Contact for steps 3–4 (Line of Sight, Weapon Range).

## 3. Reject repeated "Impact Attempt" proposal, with reasoning recorded

- [x] 3.1 REVIEW-002, REVIEW-003, REVIEW-012/014 (the "Impact Attempt" terminology and CBT-001 abstraction): rejected, same reasoning as the two prior rejections in the melee review threads — recorded in `design.md`.

## 4. Verify

- [x] 4.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 4.2 Confirm no rule ID added, removed, or renumbered in `docs/11-combat.md`.
