## 1. Verify blast radius before touching any rule ID

- [x] 1.1 Grep the full repo for `MEL-[0-9]` cross-references from outside `docs/12-melee.md` — confirm only `10-weapons.md` WPN-002 references a specific MEL- ID (MEL-003).
- [x] 1.2 Map the RFC's proposed content to the existing MEL-001–MEL-012 IDs by subject, not by the RFC's own sequential numbering — confirm no existing ID's meaning gets silently reassigned.

## 2. Repurpose existing MEL- rules in place

- [x] 2.1 MEL-001: rename "Melee Range" → "Physical Contact" (fixing a pre-existing title/body mismatch); cross-reference MEL-013.
- [x] 2.2 MEL-002: rename "Eligible Targets" → "Component Targeting"; cross-reference DMG-012; absorb MEL-010's duplicate vehicle-component target list.
- [x] 2.3 MEL-003: rename "Attack Dice" → "One Weapon, One Impact"; change from per-striking-end to per-independently-wielded-weapon counting; add the "attacker declares which end strikes" rule for multi-ended weapons and cross-reference WPN-021 for that end's Impact Strength.
- [x] 2.4 MEL-004: rename "Simultaneous Combat" → "Simultaneous Resolution"; cross-reference CBT-010 instead of restating it.
- [x] 2.5 MEL-005: rename "Successful Impacts" → "Standard Combat Resolution"; cross-reference DMG-011 through DMG-017 instead of restating the 4/5/6 threshold.
- [x] 2.6 MEL-006 (Multiple Combatants): confirmed unaffected — left unchanged.
- [x] 2.7 MEL-007 (Weapons): cross-reference WPN-015 (decorative elements) and MEL-013 (functional striking end requirement).
- [x] 2.8 MEL-008: rename "Improvised Weapons" → "Unarmed Combat"; add explicit Impact Strength 1.
- [x] 2.9 MEL-009 (Shields): tighten wording to match Component Damage System framing.
- [x] 2.10 MEL-010: reduce "Component Attacks" to a thin cross-reference to MEL-002/DMG-012.
- [x] 2.11 MEL-011 (Physical Representation): add CORE-016/DMG-006 cross-references.
- [x] 2.12 MEL-012 (Interaction with Combat Rules): confirmed unaffected — left unchanged.

## 3. Add genuinely new rules (not RFC-numbered, appended at next available IDs)

- [x] 3.1 MEL-013 — Functional Striking End: sized 1×1–4×4 like a muzzle, determines Impact Strength (WPN-021), explicitly NOT required to be round (unlike WPN-002's muzzle requirement).
- [x] 3.2 MEL-014 — Weapon Reach: melee reach determined by Weapon Length (WPN-003), the melee equivalent of WPN-005's ranged formula.

## 4. Update docs/10-weapons.md and docs/14-glossary.md

- [x] 4.1 WPN-001, WPN-002: update `12-melee.md` citations from MEL-003 to MEL-013.
- [x] 4.2 WPN-021 (Impact Strength): generalize from muzzle-only to "muzzle or functional striking end," citing MEL-013.
- [x] 4.3 `14-glossary.md`: add "Functional Striking End" and "Weapon Reach" entries; update "Impact Strength" (was muzzle-only) and "Weapon Range" (clarify ranged-specific, cross-reference "Weapon Reach").

## 5. Update Purpose / Design Philosophy / Summary

- [x] 5.1 `12-melee.md` Design Philosophy: replace the vague "Fast/Simultaneous/Physical/Easy" list with the RFC's actual flow diagram (Weapon → Physical Contact → Generate Impact → Standard Combat Resolution).
- [x] 5.2 `12-melee.md` Summary: rewrite to state melee is a special case of the standard combat system, listing what actually differs (contact/reach, per-weapon Attack Dice, simultaneous resolution) vs. what's fully shared (resolution sequence).

## 6. Verify

- [x] 6.1 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 6.2 Run `openspec validate "simplify-melee-combat" --strict` and confirm valid.
- [x] 6.3 Reread the full `docs/12-melee.md` end to end to confirm every cross-reference resolves and no old MEL rule content was silently lost or duplicated.
