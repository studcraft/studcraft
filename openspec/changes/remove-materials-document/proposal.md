## Why

`docs/13-materials.md` predates `component-damage-system`. Before that change shipped, materials.md was the only place damage was resolved at all (fixed hit-count assumptions per material). `component-damage-system` then introduced the real mechanism — Resistance, the Geometry Check, the Damage Roll, the universal Component State machine (`16-damage-system.md`) — and `16-damage-system.md`'s own DMG-008 explicitly said it "does not discard" materials.md, framing it as a complementary layer that still owns per-material cosmetic/physical-response flavor text (glass breaks, doors jam, wheels get marked, etc.).

The user has decided that layer no longer earns its own document: material handling now lives entirely in `16-damage-system.md`, and the per-material flavor text (MAT-003 Glass, MAT-005 Doors, MAT-006 Windows, MAT-007 Wheels, MAT-008 Tracks, MAT-009 Weapon Systems, MAT-012–MAT-015 Stone/Metal/Wood/Organic, MAT-001/MAT-002/MAT-011/MAT-016/MAT-017/MAT-020) is deliberately dropped, not merged — a conscious content reduction, not an oversight.

Two rules inside `13-materials.md` were not flavor text, though: **MAT-018** (Target Components — only visible components may be selected) and **MAT-019** (Independent Resolution — a single attack's impacts may be split across different components of the same target) are real mechanics that `16-damage-system.md`'s own DMG-012, DMG-013, and DMG-018 already cite by reference instead of restating. Deleting `13-materials.md` without addressing these two would leave those rules with no home and DMG-012/013/018 with dangling citations to a file that no longer exists. These two are folded into `16-damage-system.md` (DMG-012 strengthened, DMG-013 expanded) before the file is deleted — confirmed with the user as the one exception to "delete without merging."

`16-damage-system.md`'s DMG-008 ("Relationship to Materials") existed solely to reconcile the two documents — with materials.md gone, DMG-008 is repurposed in place (per this repo's "rule identifiers remain stable" convention, already used for `WPN-007`, `SCS-018`, `CMP-002`/`VEH-013`/`MAT-010` in `ruleset-consistency-fixes`) to state the design decision directly: no material modifies Resistance, the Geometry Check, or the Damage Roll — every component follows the exact same mechanical rules regardless of what it represents.

## What Changes

- Delete `docs/13-materials.md` entirely.
- `docs/16-damage-system.md`:
  - DMG-012 (Select Target Component): strengthened to state the visibility requirement directly ("hidden components cannot be selected") instead of citing `13-materials.md` MAT-018.
  - DMG-013 (Composite Vehicle Targeting): expanded to explicitly state that a single attack's impacts may be split across different components of the same target, absorbing MAT-019's example, instead of citing `13-materials.md` MAT-019.
  - DMG-018 (Weapon Distribution): citation updated from MAT-019 to DMG-013.
  - DMG-005, DMG-006: drop the `13-materials.md` (MAT-017) citations, keep the `11-combat.md` (CBT-009) / `02-core-rules.md` (CORE-016) ones.
  - DMG-008: repurposed in place from "Relationship to Materials" to "No Material-Specific Mechanics" — states directly that every component follows the same Resistance/Geometry Check/Damage Roll regardless of material, and that physical/cosmetic flavor is left to the player, not defined by a dedicated document.
  - Summary: updated to no longer reference Materials/DMG-008's old framing.
- `docs/11-combat.md`: CBT-008 (Defender Resolution), CBT-009 (Physical State Changes), CBT-012 (Cover), CBT-013 (Armour) — remove `13-materials.md`/MAT- citations; CBT-012 now points directly to `02-core-rules.md` CORE-010, CBT-013 drops the MAT-011 mention (already fully absorbed by DMG-008/DMG-014/DMG-015).
- `docs/04-construction-standard.md` SCS-023 (Transparency): "Material rules determine whether they stop projectiles" replaced with a direct reference to Resistance/the Geometry Check.
- `docs/05-construction-components.md` CMP-011 (Windows): "Follow the Material Rules for transparent elements" replaced with a direct `16-damage-system.md` reference.
- `docs/09-transport.md` TRN-012 (Transparent Elements): "follows the Material Rules" replaced with a direct Line of Sight (`CORE-008`) reference.
- `docs/10-weapons.md` WPN-012 (Line of Fire): "transparent elements follow the Material Rules" replaced with a reference to `04-construction-standard.md` SCS-023 (Transparency).
- `docs/08-vehicles.md` VEH-017 (Components): "See: materials.md" replaced with a `16-damage-system.md` reference.
- `docs/12-melee.md`: Purpose section, MEL-010, and MEL-012's document list updated to drop the Material Rules reference in favor of the Component Damage System.
- `README.md` and `system/documentation-standards.md`: remove `13-materials.md` from the directory tree and rulebook reading order (renumbering subsequent entries), plus README's Current Status implemented-systems list and Core Concepts "materials" mention.
- `system/proposal-review.md`: remove the now-nonexistent `docs/13-materials.md` from its illustrative example list.
- `scripts/generate_site_docs.py`: remove `13-materials.md` from the `TITLES` dict, which the script's own sync check would otherwise flag as stale.

## Capabilities

### Modified Capabilities
- `damage-resolution`: `Requirement: Select Target Component` drops its `13-materials.md` MAT-018 citation (no behavior change — the requirement's own SHALL/scenario text was already self-contained). `Requirement: Composite Vehicle Targeting` gains an explicit statement (and scenario) that a single attack's impacts may be split across different components of the same target, absorbing MAT-019's content.

## Impact

- One document removed (`docs/13-materials.md`), reducing `docs/` from 16 files to 15.
- All per-material cosmetic/physical-response flavor text (glass, doors, windows, wheels, tracks, weapon systems, stone, metal, wood, organic, cover-as-flavor, armour-as-mapping) is deliberately dropped, not preserved elsewhere — a conscious scope reduction.
- No change to any measured rule value, dice threshold, or resolution sequence — the mechanism (Resistance, Geometry Check, Damage Roll, Component State) was already fully owned by `16-damage-system.md` before this change.
- No cross-reference in any remaining `docs/*.md` file points to `13-materials.md` after this change.
