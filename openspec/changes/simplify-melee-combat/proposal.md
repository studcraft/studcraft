## Why

`docs/12-melee.md` predates the current Impact/Component-Damage architecture and still carries its own parallel definitions of concepts the rest of the ruleset already owns: Attack Dice generation, the 4/5/6 success threshold, and simultaneous-resolution mechanics. Melee should be a special case of the standard combat system — differing only in *how* an Impact is generated (physical contact instead of Line of Sight + Range), never in how it's *resolved*. Duplicating resolution logic in two documents is exactly the class of bug `ruleset-consistency-fixes` and `remove-materials-document` already fixed elsewhere in this repo (weapons/combat overlap, materials/damage-system overlap) — melee.md never got the same treatment.

Source: `delete-me-melee-org.md` (an RFC, discarded after use).

## What Changes

The RFC's own numbering (`MEL-001` through `MEL-009`) does not match this repo's existing `MEL-001` through `MEL-012` rule IDs — applying it literally would have silently reassigned IDs that other documents (`10-weapons.md` WPN-002) already cross-reference, and would have silently dropped `MEL-006` (Multiple Combatants), `MEL-007` (Weapons), and `MEL-012` (Interaction with Combat Rules) without saying so. Every rule below is placed at its **existing** stable ID, not the RFC's sequential position; content that has no existing counterpart gets a genuinely new ID (`MEL-013`, `MEL-014`) instead of reusing a number already in use.

- **MEL-001** (was "Melee Range", body was always about contact): renamed to **Physical Contact**, matching what it already said.
- **MEL-002** (was "Eligible Targets"): renamed to **Component Targeting**, now cross-referencing `16-damage-system.md` DMG-012 instead of restating targeting rules independently; absorbs the target-list content that used to be duplicated in MEL-010.
- **MEL-003** (was "Attack Dice"): renamed to **One Weapon, One Impact** — the core mechanic change. A melee weapon generates exactly 1 Attack Die per *independently wielded weapon*, not per *striking end*. A weapon with multiple striking ends (e.g. a double-ended staff) still generates only 1 Attack Die; the attacker declares which end strikes, and that end's size determines Impact Strength.
- **MEL-004** (was "Simultaneous Combat"): renamed to **Simultaneous Resolution**, now a cross-reference to `11-combat.md` CBT-010 (which already used melee as its own illustrative example) instead of an independent restatement.
- **MEL-005** (was "Successful Impacts", the 4/5/6 threshold restated on its own): renamed to **Standard Combat Resolution** — the RFC's central claim made explicit: every melee Impact resolves through the exact same DMG-011–DMG-017 sequence as a ranged Impact.
- **MEL-006** (Multiple Combatants): left unchanged — the RFC didn't address it, and it isn't duplicative of anything else in the ruleset.
- **MEL-007** (Weapons): kept, lightly tightened to cross-reference WPN-015 (decorative elements) and the new MEL-013 (functional striking end requirement).
- **MEL-008** (was "Improvised Weapons"): renamed to **Unarmed Combat**, and now explicitly states Impact Strength 1 — a gap in both the old rule and the RFC (see design.md).
- **MEL-009** (Shields): kept, tightened wording to match the Component Damage System framing.
- **MEL-010** (was "Component Attacks", duplicated MEL-002's target list for vehicles specifically): reduced to a thin cross-reference to MEL-002/DMG-012.
- **MEL-011** (Physical Representation): kept, added CORE-016/DMG-006 cross-references.
- **MEL-012** (Interaction with Combat Rules): left unchanged — still accurate, still the meta-rule justifying this whole consolidation.
- **MEL-013 — Functional Striking End** (new): formalizes the construction concept `10-weapons.md` WPN-001/WPN-002 already named but never defined — a melee weapon's striking end is sized 1×1–4×4 like a muzzle (determining Impact Strength, WPN-021) but, unlike a muzzle, is **not** required to be round.
- **MEL-014 — Weapon Reach** (new): a melee weapon's reach is determined by its Weapon Length (`10-weapons.md` WPN-003) — the melee equivalent of WPN-005's `Range = Weapon Length × 2` for ranged weapons.
- `docs/10-weapons.md`: WPN-001/WPN-002 update their `12-melee.md` citations from MEL-003 to MEL-013 (the concept moved). WPN-021 (Impact Strength) generalized to cover muzzles *or* functional striking ends — it was written muzzle-only and never accounted for melee, a pre-existing gap this proposal closes since MEL-005 now routes melee through the exact same Geometry Check that reads Impact Strength.
- `docs/14-glossary.md`: added "Functional Striking End" and "Weapon Reach" entries; updated "Impact Strength" (was muzzle-only) and "Weapon Range" (clarified as ranged-specific, cross-referencing the new "Weapon Reach").

## Capabilities

### Modified Capabilities
- `weapon-construction`: `Requirement: Impact Strength From Muzzle Size` generalized to cover functional striking ends as well as muzzles — the mechanism (size determines strength) is unchanged, only its applicability widens to melee weapons, which previously had no defined Impact Strength source at all.

## Impact

- `docs/12-melee.md` shrinks from 12 independently-defined rules with real duplication to 14 rules (12 kept/repurposed at stable IDs + 2 new), most of which are now a sentence or two pointing at the single owning rule elsewhere.
- No change to any ranged-combat rule value, threshold, or sequence.
- One real mechanic change (confirmed via the RFC, not silently introduced): melee Attack Dice are now counted per independently-wielded weapon, not per striking end. A double-ended staff generates 1 Attack Die (previously 2); the attacker chooses which end strikes for Impact Strength purposes.
- One gap closed that neither the shipped ruleset nor the RFC addressed: melee weapons now have a defined Impact Strength source (functional striking end size, MEL-013/WPN-021), and unarmed attacks are explicitly Impact Strength 1 (MEL-008) — without this, melee's Geometry Check (DMG-014) had nothing to compare against Resistance.
