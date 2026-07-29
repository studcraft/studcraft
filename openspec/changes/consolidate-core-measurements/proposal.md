## Why

`docs/*.md` independently restates two foundational facts instead of citing the one place that already defines them: "one Unit Base measures 4×3 studs" appears as a fresh assertion in 7 documents (`01-foundations.md`, `04-construction-standard.md` SCS-001, `06-deployment.md`, `07-movement.md`, `08-vehicles.md` VEH-001, `09-transport.md` TRN-001 — plus the canonical `02-core-rules.md` CORE-001), and "every unit receives exactly 3 Action Points per activation" appears independently in `01-foundations.md` and, within a single document, four times in `03-game-flow.md` (FLOW-004, FLOW-005, FLOW-011, FLOW-012) — on top of the canonical `02-core-rules.md` CORE-006. This is exactly the kind of duplication `system/proposal-review.md` and `system/documentation-standards.md` warn about: every one of these copies is an independent maintenance point, and copies of adjacent facts (reading-order lists, repository-structure trees) have already been caught stale multiple times this session. `05-construction-components.md` already shows the right pattern (CMP-009/CMP-010 cross-reference CORE-007 instead of restating "costs 1 Action Point") — this proposal extends that pattern to Unit Base and Action Points.

## What Changes

- Formalizes `unit-base` and `action-economy` as OpenSpec capabilities for the first time, capturing `02-core-rules.md` CORE-001 and CORE-006 exactly as currently worded. No rule value changes.
- Trims every other document that independently restates "Unit Base = 4×3 studs" (`01-foundations.md`, `04-construction-standard.md`, `06-deployment.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`) to a one-line cross-reference to CORE-001, keeping only each document's own doc-specific elaboration (e.g. `08-vehicles.md`'s vehicle-footprint examples stay; only the "4×3 studs" restatement is trimmed).
- Trims `03-game-flow.md`'s near-duplicate FLOW-004/FLOW-005 pair and the "3 AP" restatements in FLOW-011/FLOW-012 down to cross-references to CORE-006, and does the same for `01-foundations.md`'s "Action Points (AP)" section. FLOW-005's rule ID is kept (per "rule identifiers should remain stable") but repurposed to hold only its one piece of content not already covered elsewhere: that the same 3 AP applies to every unit type with no exceptions.
- Replaces `01-foundations.md`'s stale "Learning StudCraft" reading-order list (missing `docs/15` and `docs/16`, same staleness bug already caught twice this session in other files) with a pointer to `README.md`'s Rulebook section, removing a fourth independent copy of reading-order information.
- No measured rule value, formula, or player-facing behavior changes anywhere. This is a pure editorial consolidation.

## Capabilities

### New Capabilities
- `unit-base`: The Unit Base (UB) as StudCraft's universal measurement (4×3 studs) — currently only defined as prose in CORE-001, never formalized as an OpenSpec capability.
- `action-economy`: The universal Action Point system (exactly 3 AP per activation, no exceptions by unit type) — currently only defined as prose in CORE-006, never formalized as an OpenSpec capability.

### Modified Capabilities
(none — `02-core-rules.md` itself is not being reworded, only formalized; every other affected document is a direct trim, not a capability modification)

## Impact

- Affected documents: `01-foundations.md`, `03-game-flow.md`, `04-construction-standard.md`, `06-deployment.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md` (all trimmed to cross-reference `02-core-rules.md` CORE-001/CORE-006 instead of restating the underlying fact).
- `02-core-rules.md` itself is unchanged — it's already the canonical source.
- No changes to `docs/10-weapons.md` through `docs/16-damage-system.md` — spot-checked, none of them restate Unit Base or Action Point values as a fresh rule (they either don't mention these systems, or already reference them correctly, e.g. `10-weapons.md`'s Jeep example just uses UB as a unit of measure, not a redefinition).
- No `openspec/specs/` capability's requirements change — `unit-base`/`action-economy` are newly formalized, not modified from a prior state.
