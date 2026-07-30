## Why

This is an accumulating consistency-review proposal: findings get added here as they're found during a manual pass over the shipped ruleset, rather than one proposal per finding. See `system/proposal-review.md` for why this class of problem (the same concept defined independently in two places) keeps turning up, and `design.md` Decisions for the reasoning behind each fix as it's added.

**Finding 1 — Infantry States (CORE-011/012/013) were never reconciled with the universal Component State machine (DMG-005).**
`docs/02-core-rules.md` defines `CORE-011` (Operational), `CORE-012` (Wounded), `CORE-013` (Dead) as infantry-specific states — a minifig stands, sits, or lies down. `docs/16-damage-system.md` (from `component-damage-system`) later defined a universal three-state machine for *every* component in the game — not just infantry — named `OK` / `TOUCHED` / `DESTROYED` (`DMG-005`). These are the same underlying concept (a component progresses through exactly three states as it takes damage) with two different naming schemes, defined independently, with no cross-reference between them. `docs/13-materials.md` MAT-004 was partially reconciled when `component-damage-system` shipped (it mentions `DMG-005` and aliases "TOUCHED, Wounded" / "DESTROYED, Dead" in passing), but `02-core-rules.md` itself was never touched — the review that shipped `component-damage-system` cross-checked `11-combat.md` and `13-materials.md` but never went back to `02-core-rules.md`.

Since every component in the game (minifigs, vehicles, weapons, doors, wheels, ...) already goes through the same three-state progression, one universal naming should apply everywhere instead of infantry having its own vocabulary that happens to mean the same thing.

## What Changes (accumulates as findings are added)

- Renames the universal Component State machine's three states from `OK` / `TOUCHED` / `DESTROYED` to **Operational** / **Wounded** / **Dead** — reusing infantry's existing, more evocative names instead of the more mechanical ones, since the states apply identically to every component regardless of type.
- `docs/02-core-rules.md` CORE-011/012/013 stop being an independent infantry-only state definition and become the physical/cosmetic elaboration of the universal states for the infantry case specifically (in the same style as `13-materials.md`'s per-material sections) — cross-referencing the universal mechanism instead of restating it.
- `docs/16-damage-system.md`, `docs/13-materials.md` (MAT-004), and any other document using `OK`/`TOUCHED`/`DESTROYED` get updated to the new names.
- *(More findings will be appended here as the manual review continues.)*

## Capabilities

### New Capabilities
(none so far)

### Modified Capabilities
- `component-damage`: `Requirement: Component State Progression` is renamed from `OK`/`TOUCHED`/`DESTROYED` to `Operational`/`Wounded`/`Dead`. No mechanical change — the same three-state progression, same transition rules — only the labels change.

## Impact

- Affected documents so far: `docs/02-core-rules.md` (CORE-011/012/013), `docs/16-damage-system.md` (DMG-002, DMG-005, DMG-006, DMG-015, DMG-016, DMG-017, DMG-019, Combat Examples, Summary — every `OK`/`TOUCHED`/`DESTROYED` mention), `docs/13-materials.md` (MAT-004), `docs/14-glossary.md` (Component State entry).
- `openspec/specs/component-damage/spec.md` needs a `MODIFIED` delta (it's already archived, unlike `docs/11-combat.md`/`docs/13-materials.md` when `component-damage-system` was written).
- No change to any measured rule value, formula, dice threshold, or Geometry Check/Damage Roll mechanic — this is a renaming/consolidation, not a mechanics change.
