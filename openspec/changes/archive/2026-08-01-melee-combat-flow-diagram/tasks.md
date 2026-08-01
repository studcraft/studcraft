## 1. Apply REVIEW-010, adapted

- [x] 1.1 `docs/11-combat.md` "Combat Flow": add the Delivery Method fork (ranged Line of Sight + Range vs. melee Physical Contact, citing MEL-001/MEL-014) before Generate Attack Dice.
- [x] 1.2 Collapse the detailed resolution steps into one "Combat Resolution" box citing `16-damage-system.md` DMG-009 through DMG-017, instead of re-listing them or adding a separate new diagram elsewhere.

## 2. REVIEW-009 — confirm not applicable

- [x] 2.1 Confirm the wording REVIEW-009 wants to refine only existed in REVIEW-001's rejected suggestion, never shipped — no action needed, reasoning recorded in `design.md`.

## 3. Verify

- [x] 3.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 3.2 Confirm only one top-level combat-flow diagram exists in `11-combat.md` (not a second one added elsewhere).
