## Why

StudCraft's weapons already derive Range, Attack Dice, and Impact Strength from geometry (`weapon-construction-system`), and Materials (`docs/13-materials.md`) already sketch how components respond to Impacts, but the connection between the two was never fully specified: nothing says how a component's own geometry determines whether an Impact can hurt it, and several Material rules (glass breaks on the first hit, infantry on the second) hard-code a hit count per material instead of deriving it from construction. `docs/11-combat.md` also predates Impact Strength entirely and still says weapons never possess "Strength." This proposal closes that gap: every component gets a construction-derived Resistance, and a single dice-based resolution sequence (Attack Roll → Geometry Check → Damage Roll) replaces the ad hoc per-material hit counts.

## What Changes

- Every object on the battlefield is a collection of independent **Components** (Minifig, Shield, Door, Cannon, Wheel, Engine, ...), each with its own state — never a single unit-level health pool.
- Introduces **Component Resistance**: a component's resistance is the smallest structural cross-section an Impact must cross, read directly from its construction (bricks/plates, not a stat).
- Introduces the universal three-state **Component State** machine (`OK → TOUCHED → DESTROYED`) — every component, regardless of type, uses exactly these three states.
- Introduces the combat resolution sequence: **Attack Roll** (existing 4+/D6 threshold, per CBT-005) generates a valid Impact → **Geometry Check** (Impact Strength vs. Component Resistance; below resistance, the Impact ends immediately) → **Damage Roll** (a second D6; on 1-3 the component advances one state) → **Penetration** (remaining strength continues to the next component behind it).
- Introduces **Weapon Distribution**: multi-muzzle weapons on a free-rotating mount (turntable, ball joint, swivel) may split their impacts across different target units; fixed mounts still cannot (per existing CBT-007).
- Introduces **Repairs**: consumes Action Points, restores exactly one state (`TOUCHED → OK`); `DESTROYED` is not repairable.
- **BREAKING**: Replaces the fixed, material-specific hit-count assumptions in `13-materials.md` (MAT-003's "first Impact breaks glass", MAT-004's "first/second unresolved Impact" for infantry) with the geometry-derived Resistance + Geometry Check + Damage Roll mechanism. The *outcome* for a typical minifig is unchanged (still two hits), but the *mechanism* is now construction-driven rather than a fixed per-material rule.
- **BREAKING**: `docs/11-combat.md` CBT-011 ("Weapons never possess: Damage, Strength, Armour Penetration") needs updating — weapons do now possess Impact Strength (already shipped as WPN-021), which this change's Geometry Check depends on directly.
- `docs/11-combat.md` CBT-007 ("Individual attack dice from the same weapon system cannot be split between multiple targets") gets one exception added for free-rotating mounts (see Weapon Distribution above); fixed mounts are unaffected.

## Capabilities

### New Capabilities
- `component-damage`: The structural model — components, geometry-derived Resistance, the universal Component State machine, Composite Objects, and internal/layered protection.
- `damage-resolution`: The dice-based combat sequence that resolves an Impact against a component — Attack Roll, Geometry Check, Damage Roll, Penetration, Weapon Distribution, and Repairs.

### Modified Capabilities
(none — `docs/11-combat.md` and `docs/13-materials.md` predate OpenSpec and were never captured as formal capabilities in `openspec/specs/`; their wording changes are tracked as direct doc edits in Impact below, not as spec deltas)

## Impact

- Affected documents: likely a new `docs/*.md` file (or two, matching the two capabilities — see design.md) defining Component Damage and Damage Resolution; `docs/11-combat.md` (CBT-007 gains an exception, CBT-011 needs updating to allow Impact Strength); `docs/13-materials.md` (MAT-003, MAT-004 reworded to derive their hit count from Resistance instead of asserting it per material; MAT-011's "future armour rules" promise is fulfilled by the Geometry Check and Damage Roll; MAT-016 Cover is explicitly untouched); `docs/14-glossary.md` (new terms: Component, Resistance, Impact Strength cross-reference, Component State).
- No changes to `docs/10-weapons.md` — Range, Attack Dice, and Impact Strength (WPN-005/006/021) are consumed as-is, not modified.
- Affects future rule-writing: any future OpenSpec proposal introducing a new destructible object type must define it in terms of Components and Resistance, not a new bespoke health mechanic.
