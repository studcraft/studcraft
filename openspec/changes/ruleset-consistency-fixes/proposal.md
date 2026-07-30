## Why

This is an accumulating consistency-review proposal: findings get added here as they're found during a manual pass over the shipped ruleset, rather than one proposal per finding. See `system/proposal-review.md` for why this class of problem (the same concept defined independently in two places) keeps turning up, and `design.md` Decisions for the reasoning behind each fix as it's added.

**Finding 1 — Infantry States (CORE-011/012/013) were never reconciled with the universal Component State machine (DMG-005).**
`docs/02-core-rules.md` defines `CORE-011` (Operational), `CORE-012` (Wounded), `CORE-013` (Dead) as infantry-specific states — a minifig stands, sits, or lies down. `docs/16-damage-system.md` (from `component-damage-system`) later defined a universal three-state machine for *every* component in the game — not just infantry — named `OK` / `TOUCHED` / `DESTROYED` (`DMG-005`). These are the same underlying concept (a component progresses through exactly three states as it takes damage) with two different naming schemes, defined independently, with no cross-reference between them. `docs/13-materials.md` MAT-004 was partially reconciled when `component-damage-system` shipped (it mentions `DMG-005` and aliases "TOUCHED, Wounded" / "DESTROYED, Dead" in passing), but `02-core-rules.md` itself was never touched — the review that shipped `component-damage-system` cross-checked `11-combat.md` and `13-materials.md` but never went back to `02-core-rules.md`.

Since every component in the game (minifigs, vehicles, weapons, doors, wheels, ...) already goes through the same three-state progression, one universal naming should apply everywhere instead of infantry having its own vocabulary that happens to mean the same thing.

## What Changes (accumulates as findings are added)

- Renames the universal Component State machine's three states from `OK` / `TOUCHED` / `DESTROYED` to **Operational** / **Wounded** / **Dead** — reusing infantry's existing, more evocative names instead of the more mechanical ones, since the states apply identically to every component regardless of type.
- `docs/02-core-rules.md` CORE-011/012/013 stop being an independent infantry-only state definition and become the physical/cosmetic elaboration of the universal states for the infantry case specifically (in the same style as `13-materials.md`'s per-material sections) — cross-referencing the universal mechanism instead of restating it.
- `docs/16-damage-system.md`, `docs/13-materials.md` (MAT-004), and any other document using `OK`/`TOUCHED`/`DESTROYED` get updated to the new names.

**Finding 2 — FLOW-003 (Priority) was ambiguous about when the choice happens.**
`docs/03-game-flow.md` `FLOW-003` said the Priority player chooses "Activate the first unit this Turn" / "Activate the second unit this Turn" — indirect phrasing that doesn't make clear this is a one-time choice at the start of the Turn, not a repeated choice at every activation. Reworded to an explicit binary choice ("activate one of their own units now, keeping the activation" vs. "cede Priority, letting the other player activate first"), with an explicit sentence that this is decided once per Turn and strict alternation (FLOW-002) governs the rest. No mechanical change — same choice, same outcome, clearer wording. The same document's "Turn Sequence" diagram independently restated the old "Activate First / Activate Second" bullets — missed in the first pass on this finding, caught afterward and updated to match.

**Finding 3 — Bike footprint (SCS-003 / VEH-001) was illogically square.**
`docs/04-construction-standard.md` SCS-003 and `docs/08-vehicles.md` VEH-001 both listed "Bike"/"Motorbike" as a `1 × 1 UB` footprint (the same restatement pattern as before — one fact, two independent copies). A real motorbike is long and narrow, not square; a 1×1 UB footprint reads as though it were as compact as a single infantry model. Changed both to `1 × 2 UB` in each document. Illustrative example only — no rule, formula, or ID changes. `docs/09-transport.md` TRN-013 separately lists "Motorbike: 1 UB" as a *cargo-slot* allocation (space taken when carried as cargo inside another vehicle) — a different, intentionally-abstracted number, not the vehicle's own footprint, so left unchanged.

**Finding 4 — SCS-018 (construction standard) never mirrored WPN-019 (Weapon Front).**
`docs/04-construction-standard.md`'s SCS-01x series otherwise mirrors each relevant `10-weapons.md` rule with a construction-standard pointer (SCS-016→WPN-002, SCS-019→WPN-003, SCS-020→WPN-004), but SCS-018 ("Muzzle Adjacency Standard") only cited WPN-007/WPN-020 (adjacency, footprint-fit) and never mentioned WPN-019 (Weapon Front — muzzles may only be built on the single front face, not rear/side/top/bottom). Renamed SCS-018 to "Muzzle Placement Standard" and added the Weapon Front constraint alongside the existing adjacency content, so the construction-standard rule fully mirrors what `10-weapons.md` actually requires instead of covering only part of it.

**Finding 5 — Remove Engine entirely; replace with a Pilot requirement.**
Engines are being cut from StudCraft as a concept. `CMP-002` (`05-construction-components.md`), `VEH-013` (`08-vehicles.md`), and `MAT-010` (`13-materials.md`) all defined an Engine component (largely duplicating each other, in the same pattern as Findings 1/3/4) that no longer exists. Rather than deleting the rule IDs (per "rule identifiers should remain stable" — the same convention already applied to `WPN-007` and `SCS-018`), all three are **repurposed in place** to a new, related mechanic: every motorized vehicle now requires a **Pilot** (a crew member, per the existing `VEH-015`) to move — if the Pilot is absent or reaches the `Dead` Component State (per Finding 1's unified state machine), the vehicle cannot move, mirroring the Engine rule's old structural role exactly. Every other "Engine" example mention across the ruleset (`01-foundations.md`, `12-melee.md`, `14-glossary.md`, `16-damage-system.md` DMG-001/DMG-007/DMG-008, plus `README.md` and `CODE_OF_DESIGN.md`) is updated to "Pilot" for consistency. The `component-damage` capability's archived `Component Targeting` and `Internal Components` requirements also used "an engine" as an illustrative example — added to this proposal's `MODIFIED` delta alongside the already-present `Component State Progression` delta from Finding 1.

- *(More findings will be appended here as the manual review continues.)*

## Capabilities

### New Capabilities
(none so far)

### Modified Capabilities
- `component-damage`: `Requirement: Component State Progression` is renamed from `OK`/`TOUCHED`/`DESTROYED` to `Operational`/`Wounded`/`Dead` (Finding 1). `Requirement: Component Targeting` and `Requirement: Internal Components` update their illustrative "engine" examples to "pilot" (Finding 5). No mechanical change in any of the three — same behavior, only labels/examples change.

## Impact

- Affected documents so far: `docs/02-core-rules.md` (CORE-011/012/013), `docs/16-damage-system.md` (DMG-002, DMG-005, DMG-006, DMG-015, DMG-016, DMG-017, DMG-019, Combat Examples, Summary — every `OK`/`TOUCHED`/`DESTROYED` mention), `docs/13-materials.md` (MAT-004), `docs/14-glossary.md` (Component State entry).
- `openspec/specs/component-damage/spec.md` needs a `MODIFIED` delta (it's already archived, unlike `docs/11-combat.md`/`docs/13-materials.md` when `component-damage-system` was written).
- No change to any measured rule value, formula, dice threshold, or Geometry Check/Damage Roll mechanic — this is a renaming/consolidation, not a mechanics change.
