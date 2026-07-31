## 1. Verify each REVIEW item against current shipped text

- [x] 1.1 REVIEW-001 (Define the Structural Unit): confirmed already satisfied by `DMG-003`'s existing "measured in plate layers... a standard brick is 3 plates tall."
- [x] 1.2 REVIEW-002 (Bricks and Plates Become Equivalent): confirmed already satisfied by the same `DMG-003` text plus `DMG-004` Example 3.
- [x] 1.3 REVIEW-004 (Transparent Components Should Follow Geometry): confirmed already satisfied by `docs/04-construction-standard.md` SCS-023.
- [x] 1.4 REVIEW-005 (Penetration Already Handles Multiple Transparent Layers): confirmed `DMG-017` is already fully generic; no addition needed.
- [x] 1.5 REVIEW-006 (Remove Material-Based Resistance): confirmed already satisfied by `DMG-008` ("No Material-Specific Mechanics").
- [x] 1.6 Confirmed the review's un-exceptioned "always Plates, never Bricks" wording would, if applied literally, undo `audit-round2-repairs`' fixed-piece exception for minifigs — not adopting that wording change.

## 2. REVIEW-003 (not yet applied — proposal only this round)

- [ ] 2.1 `docs/16-damage-system.md` DMG-004: add a multi-brick example (Bunker, 2 bricks thick → Resistance 6).
- [ ] 2.2 `docs/16-damage-system.md` DMG-004: add a transparent-component example (window built 1 plate thick → Resistance 1).

## 3. Verify (once section 2 is applied)

- [ ] 3.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [ ] 3.2 Confirm no rule ID added, removed, or renumbered.
