## Why

`delete-me-audit.md` is a 35-finding audit of `docs/` against `README.md`/`CODE_OF_DESIGN.md`/`AGENTS.md`: 10 direct contradictions, 12 omissions, 5 duplications, 8 minor issues. Several were genuinely blocking (no AP cost for Move or Attack, a Dead-state contradiction, components that could be built unconditionally invulnerable). This change applies fixes for 34 of the 35 findings; the 35th (D-08, stray `delete-me-*.md` files in the repo root) isn't a ruleset change and is left for the user.

Six findings required a real design decision rather than a consistency fix — each was confirmed with the user before writing anything:

- **A-01 (Dead state)**: minifigures are always physically removed on reaching Dead — no casualty marker, no "lie down and stay." `DMG-006`'s "no dead component remains on the battlefield" wins outright; `CORE-013`/`MEL-011` no longer contradict it.
- **A-02 (Resistance unit)**: Resistance is measured in plate layers (finest LEGO unit), not bricks — a standard brick is 3 plates tall. `DMG-004`'s four examples are rewritten so a brick-built shield (Resistance 3) sits between a 2-plate wall (Resistance 2) and a 4-plate stack (Resistance 4), instead of the old inconsistent mix of units that put a brick wall *below* a thinner plate stack.
- **A-04 (reaction fire)**: `CORE-009`/Design Code Principle 9 no longer promise "if it can see you, it can shoot you" as an out-of-turn reaction — reworded to target-symmetry ("if it can see you, you can be its target during its own activation"). StudCraft has no reaction fire; `CBT-014` already correctly lists it as a possible future extension.
- **A-05 (melee counterattack)**: `MEL-004`/`CBT-010`'s "both combatants declare their attacks" no longer implies an automatic free counter-attack for the defender. A melee attack is one unit's own action; simultaneous resolution only applies when two attacks are *already* legitimately declared to resolve together (not a currently-existing case in the base ruleset).
- **A-06 (shields)**: shields are an interposed/targetable component only (`DMG-007`), like an Armor Plate — no separate defensive bonus. `SCS-022`/`CMP-014` no longer promise "defensive benefits" beyond that.
- **A-07 (cover)**: `CORE-010` no longer defines "partial"/"heavy" cover levels with no mechanical effect. Cover is now exactly "hidden = not a legal target" (`DMG-012`), fully delegated, no dead levels left over.

One finding (**A-03**, the Impact Strength ceiling making high-Resistance components invulnerable) turned out not to need a decision at all: `WPN-002`'s 1×1–4×4 muzzle-size list was always meant as illustrative examples, not a hard ceiling — a large enough Weapon Front Footprint supports arbitrarily large muzzles/striking ends, so Impact Strength has no maximum either. Fixed by clarifying the existing text rather than adding a new mechanic; see `design.md`.

## What Changes

**Direct contradictions (A-08, A-09, A-10):**
- `CBT-013` rewritten: Armour is not a separate statistic, it's the colloquial name for a component's Resistance — no phantom mechanic. Spelling unified to "Armour" across `docs/16-damage-system.md` and `docs/15-geometry-layers.md` (both previously used the US spelling "Armor" while every other document used "Armour"). Added a missing glossary entry.
- `MOVE-004` dropped its incorrect "12 studs = three Unit Base lengths" justification (the 4-stud front edge, not the 3-stud depth of travel, is what "three lengths" actually measures) — kept the 12-stud value, dropped the wrong derivation.
- `WPN-016` synced to the post-`Impact Strength` ruleset: it still described weapon effect as depending on now-phantom "Armour"/"Cover" mechanics predating `WPN-021`.

**Omissions (B-01 through B-12):**
- Added the missing AP costs the audit found nowhere in the ruleset: Move (1 AP, `MOVE-004`/`VEH-004`), Attack (1 AP per weapon system, `CBT-001`), vehicle/turret rotation (1 AP, `VEH-008`–`011`, matching infantry's existing `MOVE-008`).
- `CORE-006`'s "Stand up" action now cross-references `DMG-019` (Repairs) as the same mechanism — they were almost certainly the same rule stated twice under different names. `DMG-019` now states its own cost (1 AP) and that it can be self-performed or performed by an adjacent unit.
- `TRN-005`/`TRN-006` (Embarking/Disembarking): clarified the AP comes from the embarking/disembarking unit's own pool, and that embarking/disembarking constitutes that unit's own activation — resolving whether an embarked passenger gets a separate activation (it doesn't; it already used its AP to embark, or spends its own activation's AP to disembark and then act). Also fixed the AP asymmetry the audit found (embark was a flat 1 AP regardless of size while disembark scaled per UB) — embark now scales per UB too, matching disembark.
- `FLOW-002`: added the missing rule for uneven army sizes — once one player has no unactivated units left, the other continues activating consecutively.
- `CORE-001`: stated the previously-implicit Unit Base orientation convention (`W × D` UB — first number is 4-stud widths, second is 3-stud depths) so "Jeep: 2 × 3 UB" has one unambiguous meaning.
- `07-movement.md` and `02-core-rules.md`: added honest scope acknowledgments for the two large gaps the audit found (no vehicle-vs-terrain rules; no structure-damage/collapse rules) rather than inventing full systems for either — each points to the general Physical Priority / Component Damage System principle in the meantime.
- `TRN-010`: clarified that penetration can reach closed-transport passengers through the hull, using the same Internal Components mechanism (`DMG-007`) already established for Armor-Plate-protects-Pilot.

**Duplications (C-01 through C-05):**
- `SCS-003`/`VEH-001` (vehicle footprint tables): merged into one table in `VEH-001` (Bike, Buggy, Jeep, Tank, Heavy Transport, Super Heavy — reconciling the "Bike"/"Motorbike" naming mismatch and each table's exclusive entries); `SCS-003` now cross-references it.
- `CMP-004`/`005`/`006` (tracks/hover/walkers): now cross-reference `VEH-009`/`011`/`010` for pivot behavior instead of restating it.
- `07-movement.md`'s unnumbered Doors/Ramps/Interactive Terrain sections now cite `CORE-007` for their "1 AP" cost, matching every other document that already does.
- `WPN-010` now cross-references `CORE-015` (Hands) instead of repeating its one/two-handed equipment list.
- C-04 (Attack Dice/threshold "declared three times"): confirmed already resolved by the existing pattern — `CBT-004`/`DMG-010`/`DMG-011` each cite `WPN-006`/`CBT-005` as the source rather than independently asserting the fact; no further change needed.

**Minor (D-01 through D-07):**
- Line of Sight viewpoint unified to "the attacker's point of view" (`CORE-008`'s wording) everywhere — `CBT-002` said "the attacking weapon's" and `WPN-012` said "the muzzle's," both now reconciled to the same, model-wide viewpoint.
- `DMG-017` (Penetration) clarified that "successfully affects a component" means passing the Geometry Check, independent of the Damage Roll's outcome — penetration is a consequence of geometry, not chance.
- `DMG-018`: added a one-line note confirming infantry always qualifying for the free-rotation exception (a person's torso turns; a vehicle hull doesn't) is intentional, not an oversight.
- `MEL-014` (Weapon Reach) reworded: reach isn't a value consulted separately from the Physical Contact check, it's why that check comes out the way it does for a given weapon's construction.
- `motorized` (CMP-002) unified to `powered` (matching `VEH-013`), with an explicit note that it covers wheels, tracks, walkers, and hover alike.
- `docs/14-glossary.md`: added its missing `**Version:**` header and closing `Every Brick Matters` quote (the only document missing both).
- `CORE-012` (Wounded) now says explicitly that Wounded carries no gameplay penalty — a Wounded unit moves, attacks, rotates, and climbs exactly as if Operational; the seated pose is purely cosmetic.

**Not changed:** D-08 (stray `delete-me-*.md` files in the repo root) — these aren't tracked by git and aren't part of the ruleset; left for the user to remove.

## Capabilities

### Modified Capabilities
- `component-damage`: `Requirement: Geometry Defines Resistance` updated from ambiguous "bricks or plates" (with a scenario asserting "1 brick → Resistance 1") to plate layers only, with a standard brick explicitly counting as 3 plate layers — matching A-02's fix in `docs/16-damage-system.md` DMG-003/DMG-004. This is the one place the audit's finding was already encoded in a formalized requirement, not just doc prose.

## Impact

- Documents touched: `02-core-rules.md`, `03-game-flow.md`, `04-construction-standard.md`, `05-construction-components.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`, `11-combat.md`, `12-melee.md`, `14-glossary.md`, `16-damage-system.md`, `15-geometry-layers.md`, `README.md`, `CODE_OF_DESIGN.md`, `system/documentation-standards.md`. No rule ID added, removed, or renumbered.
- **Real mechanical changes** (not pure consistency fixes): Dead is now always a removal (previously ambiguous); Resistance is now measured in plate layers with three of `DMG-004`'s four example values recalculated; Move/Attack/vehicle-rotation now cost 1 AP each (previously undefined — this is new, not a change to an existing value); embarking now costs 1 AP per Unit Base instead of a flat 1 AP; shields and cover no longer imply a mechanical bonus beyond being a targetable/interposed component; melee no longer implies an automatic free counter-attack for the defender.
- No change to muzzle/striking-end sizing, Attack Dice counts, Impact Strength values, or the resolution sequence itself.
