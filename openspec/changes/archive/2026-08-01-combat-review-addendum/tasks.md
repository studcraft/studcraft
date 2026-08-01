## 1. Apply in dependency order

- [x] 1.1 REVIEW-015: split the Combat Flow diagram's "Combat Resolution" box into "Attack Roll (CBT-005)" then "Component Damage System (DMG-012 through DMG-017)", matching actual rule ownership.
- [x] 1.2 REVIEW-016: reduce `CBT-008` to a one-sentence hand-off, now that the diagram (1.1) carries the itemized step sequence — applying this before 1.1 would have removed the only signposting in the document; applying it after does not.
- [x] 1.3 REVIEW-017: reword the Summary's weapon-property list to cover melee (delivery method, Attack Dice, Impact Strength) instead of ranged-only language ("shoot," "fire").

## 2. Verify

- [x] 2.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 2.2 Confirm no rule ID added, removed, or renumbered in `docs/11-combat.md`.
- [x] 2.3 Confirm `CBT-008`'s "see the Combat Flow diagram below" points in the correct direction (the diagram follows it in document order).
