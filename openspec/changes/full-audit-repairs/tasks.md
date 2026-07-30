## 1. Design decisions (confirmed with user before any edit)

- [x] 1.1 A-01: Dead is always a physical removal — no casualty marker, no lie-down exception.
- [x] 1.2 A-02: Resistance measured in plate layers (1 brick = 3 plates).
- [x] 1.3 A-04: Reaction fire reworded as target-symmetry, not implemented as a mechanic.
- [x] 1.4 A-05: Melee simultaneous-resolution no longer implies an automatic free counter-attack.
- [x] 1.5 A-06: Shields reduced to interposed/targetable component only (DMG-007), no separate bonus.
- [x] 1.6 A-07: Cover reduced to "hidden = not a legal target" (DMG-012), partial/heavy levels removed.

## 2. A-03 — resolved via wording clarification, no design decision needed

- [x] 2.1 `docs/10-weapons.md` WPN-002: muzzle size list reworded as illustrative, not a ceiling — sized only by the Weapon Front Footprint.
- [x] 2.2 `docs/10-weapons.md` WPN-021: table extended with "no maximum" note; explains the platform-size tradeoff that prevents unconditional invulnerability.
- [x] 2.3 `docs/12-melee.md` MEL-013, `docs/14-glossary.md` (Muzzle, Muzzle Size, Functional Striking End entries): synced to the same "no fixed maximum" wording.

## 3. Contradictions (A-08, A-09, A-10)

- [x] 3.1 `docs/11-combat.md` CBT-013: Armour redefined as Resistance's colloquial name, not a separate mechanic.
- [x] 3.2 Spelling unified to "Armour" in `docs/16-damage-system.md` and `docs/15-geometry-layers.md` (previously "Armor").
- [x] 3.3 `docs/14-glossary.md`: added missing "Armour" entry.
- [x] 3.4 `docs/07-movement.md` MOVE-004: removed the incorrect "12 studs = three Unit Base lengths" justification.
- [x] 3.5 `docs/10-weapons.md` WPN-016: synced to post-Impact-Strength wording; dropped phantom Armour/Cover mechanic references.

## 4. Omissions (B-01 through B-12)

- [x] 4.1 `docs/07-movement.md` MOVE-004, `docs/08-vehicles.md` VEH-004: Move costs 1 AP.
- [x] 4.2 `docs/11-combat.md` CBT-001: Attack costs 1 AP per weapon system.
- [x] 4.3 `docs/08-vehicles.md` VEH-008 through VEH-011: rotation costs 1 AP, matching MOVE-008.
- [x] 4.4 `docs/02-core-rules.md` CORE-006: "Stand up" cross-references DMG-019 (Repairs).
- [x] 4.5 `docs/16-damage-system.md` DMG-019: states its own cost (1 AP), self- or adjacent-unit repair.
- [x] 4.6 `docs/09-transport.md` TRN-005/TRN-006: AP comes from the embarking/disembarking unit's own pool and constitutes its own activation; embark now scales 1 AP per UB (was a flat 1 AP), matching disembark.
- [x] 4.7 `docs/03-game-flow.md` FLOW-002: added the uneven-forces alternation rule.
- [x] 4.8 `docs/02-core-rules.md` CORE-001: stated the Unit Base `W × D` orientation convention explicitly.
- [x] 4.9 `docs/07-movement.md`: acknowledged the vehicle-terrain rules gap (no invented system).
- [x] 4.10 `docs/02-core-rules.md` CORE-005: acknowledged the structure-damage/collapse rules gap (no invented system).
- [x] 4.11 `docs/09-transport.md` TRN-010: clarified penetration can reach closed-transport passengers via DMG-007/DMG-017.
- [x] 4.12 `README.md`, `system/documentation-standards.md`: explained the `13-*.md` numbering gap.

## 5. Duplications (C-01 through C-05)

- [x] 5.1 `docs/08-vehicles.md` VEH-001 / `docs/04-construction-standard.md` SCS-003: merged the divergent vehicle footprint tables into one (in VEH-001); SCS-003 cross-references it.
- [x] 5.2 `docs/05-construction-components.md` CMP-004/005/006: cross-reference VEH-009/011/010 for pivot behavior instead of restating it.
- [x] 5.3 `docs/07-movement.md` Doors/Ramps/Interactive Terrain sections: cite CORE-007 for the 1 AP cost, matching every other document.
- [x] 5.4 `docs/10-weapons.md` WPN-010: cross-references CORE-015 (Hands) instead of repeating the one/two-handed equipment list.
- [x] 5.5 C-04 (Attack Dice/threshold triple declaration): confirmed already resolved by existing citation pattern — no change needed.

## 6. Minor (D-01 through D-07)

- [x] 6.1 `docs/11-combat.md` CBT-002, `docs/10-weapons.md` WPN-012: Line of Sight viewpoint unified to "the attacker's point of view" (CORE-008's wording).
- [x] 6.2 `docs/16-damage-system.md` DMG-017: clarified "successfully affects" means passing the Geometry Check, independent of the Damage Roll.
- [x] 6.3 `docs/16-damage-system.md` DMG-018: added a note confirming infantry-always-qualifies-for-free-rotation is intentional.
- [x] 6.4 `docs/12-melee.md` MEL-014: reworded Weapon Reach as a description of the Physical Contact check's outcome, not a separately-consulted value.
- [x] 6.5 `docs/05-construction-components.md` CMP-002: unified "motorized" to "powered" (matching VEH-013); `docs/08-vehicles.md` VEH-013: clarified it covers wheels/tracks/walkers/hover.
- [x] 6.6 `docs/14-glossary.md`: added the missing Version header and closing quote.
- [x] 6.7 `docs/02-core-rules.md` CORE-012: stated explicitly that Wounded carries no gameplay penalty.

## 7. Not changed

- [ ] 7.1 D-08 (stray `delete-me-*.md` files): not tracked by git, not a ruleset change — left for the user.

## 8. Spec delta

- [x] 8.1 `openspec/specs/component-damage/spec.md`: checked whether any formalized requirement encoded the audit's findings, not just doc prose. Found one: "Geometry Defines Resistance" formally asserted "1 brick → Resistance 1," matching A-02's bug. Added a MODIFIED delta correcting it to plate layers (brick = 3 plate layers).
- [x] 8.2 Confirmed "Impact Strength From Muzzle Size" and "Muzzle Placement Validity" (weapon-construction) do NOT encode A-03's ceiling bug — their `SHALL` text and "e.g." examples were already open-ended; no delta needed there.
- [x] 8.3 Confirmed "Component State Progression"'s `DESTROYED` scenario already said "no destroyed component remains on the battlefield" — A-01 only needed doc-level fixes (CORE-013/MEL-011 contradicted an already-correct formal spec); no delta needed there either.

## 9. Verify

- [x] 9.1 Run `python3 scripts/lint_ruleset.py` after every batch of edits and confirm no structural issues.
- [x] 9.2 Confirm no rule ID added, removed, or renumbered anywhere in `docs/`.
