## Why

`delete-me-audit-resut.md` is a second-pass audit run against `full-audit-repairs` (#28, commit `314e671`) — it verified all 35 original findings (30 held up cleanly) and found 24 new issues: 5 regressions introduced by that PR's own fixes (propagation misses — a summary, a glossary entry, or a mirror rule that wasn't updated alongside the canonical rule it restates), 7 new substantive findings, and 12 minor ones. This change applies fixes for all 24.

One finding (**R-01**) was a real design flaw, not a propagation miss, and required a user decision before touching anything: `full-audit-repairs`'s A-02 fix (Resistance measured in plate layers) correctly resolved the original bricks/plates ambiguity, but recalibrating *only* the Resistance side of the Strength-vs-Resistance comparison — without checking it against the Impact Strength side — left infantry structurally unable to damage almost anything. A minifig's real molded torso is roughly 1 brick (3 plate layers) thick, and infantry-carried ranged weapons are capped at Impact Strength 2 by an unrelated, already-existing geometry chain (`CORE-001` → `WPN-004` → `WPN-018` → `WPN-019`/`WPN-020` → `WPN-021`, Platform Length 4 → max muzzle 2×2). If a real minifig measured Resistance 3 under the new unit, no infantry weapon — nor an unarmed attack (Impact Strength 1) — could ever pass the Geometry Check against any minifig, friendly or enemy.

## What Changes

**R-01 (design decision, confirmed with the user)**: a minifig is a fixed piece — a single molded part, not something the player builds choice-by-choice the way a shield, wall, or hull is. `DMG-003`/`DMG-004` now say explicitly that Resistance's plate-layer measurement applies only to *constructed* components; a minifig uses a fixed baseline of Resistance 1 instead of a literal measurement of its real molded thickness. This preserves every existing worked example (pistol vs. minifig, unarmed vs. minifig) without touching the Impact Strength scale, the infantry weapon-size ceiling, or `WPN-018`'s proportion rule — none of which needed to change.

**R-02 through R-05 (regressions, direct propagation-miss fixes):**
- `CBT-012` (Cover) still said cover "affects how the target resolves incoming impacts" — directly contradicting the binary "hidden = untargetable, no effect after that" rule `A-07` shipped in `CORE-010`/`WPN-016`. Fixed to match.
- `docs/15-geometry-layers.md` GEO-004 still described cover as gradual ("the physical amount... hidden") and said decoration can "grant extra cover" — both stale relative to the binary rule. Fixed.
- `docs/09-transport.md`'s own Summary still listed "Embarking costs 1 AP" after `B-06`'s fix made it scale per Unit Base like Disembarking. Fixed.
- `TRN-005` said embarking "is a complete activation... exactly like any other action" — self-contradictory (a complete activation vs. "like any other action," when no other action consumes a whole activation). Fixed to match `TRN-006`'s framing: AP from the same 3-AP pool, spendable on other actions the same activation.

**N-01 through N-07 (new substantive findings):**
- `Resistance` was missing from `GEO-001`/`GEO-003`'s Gameplay Geometry taxonomy — meaning, read literally, Visual Geometry (explicitly including "decorative armour") wasn't excluded from affecting it. Added Resistance to both lists, and added the missing carve-out to `GEO-002`: a plate only counts as Visual Geometry if it isn't part of the structural cross-section an Impact must cross.
- `DMG-019` (Repairs) let any unit repair any Wounded component, self or others, unlimited times, with no equipment requirement — contradicting `CORE-014`'s "equipment must be visibly present" principle and trivializing the Wounded state. Now: self-repair is limited to once per activation; repairing *another* unit requires visible repair equipment and adjacency.
- `CBT-007` (Multiple Targets) never said how Line of Sight/Range verification or AP cost work when a weapon system's dice are split across several targets. Added: each target verified individually before rolling, cost stays the single per-weapon-system AP from `CBT-001` regardless of split.
- `MEL-003` (One Weapon, One Impact) read as if dual-wielding produced one 2-dice attack; it's actually two 1-die attacks (two weapon systems, `WPN-008`), costing 2 AP. Clarified in the rule and its example table; `MEL-008` (Unarmed Combat) got the same AP-cost clarification.
- `MOVE-016` (Falling Damage) applied a Damage Roll with no Geometry Check and no declared exception. Added the explicit exception (falling has no Impact Strength, so there's nothing to Geometry-Check; Resistance plays no part) and scoped the rule to infantry, since vehicle falling is already an acknowledged gap.
- `FLOW-003` still said Priority's alternation is "strict" after `B-07` added the uneven-forces exception to `FLOW-002`. Fixed to match.
- `CBT-010`'s example ("two infantry models with mutually declared attacks") illustrates a case no current rule can produce, in the same rule that explains why it can't happen yet. Marked explicitly as hypothetical.

**M-01 through M-12 (minor, direct fixes):** last stray "armor" spelling; `DMG-004` Example 2's header/body mismatch; glossary "Weapon Reach" and "Closed Transport" entries reworded to match their corrected rules; `VEH-011` no longer double-charges movement already covered by `VEH-004`; `DEP-004` reworded so it can't be misread as contradicting `DEP-006`; residual "no maximum vehicle size" duplication trimmed from `SCS-003`; a note on round-piece availability added to `WPN-002` (3×3/5×5 round LEGO elements aren't standard manufactured sizes); `MOVE-004` given a correct geometric note (12 is a multiple of both the UB's 3-stud and 4-stud axes) after the earlier fix removed an incorrect one without replacing it; the intentional "Every Brick Matters" vs. "The Model Is The Rules" closing-quote split documented in `system/documentation-standards.md`; `README.md` Part III retitled "Deployment & Movement"; `DEP-001`'s Design Philosophy cross-references `CORE-005`'s acknowledged structure-damage gap instead of silently overstating scope.

## Capabilities

### Modified Capabilities
- `component-damage`: `Requirement: Geometry Defines Resistance` further modified (on top of `full-audit-repairs`'s pending delta) to add the fixed-piece exception — a minifig uses Resistance 1 by definition, not by measuring plate layers.

## Impact

- Documents touched: `02-core-rules.md` (none this round — R-01 lives entirely in `16-damage-system.md`), `03-game-flow.md`, `04-construction-standard.md`, `06-deployment.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`, `11-combat.md`, `12-melee.md`, `14-glossary.md`, `15-geometry-layers.md`, `16-damage-system.md`, `README.md`, `system/documentation-standards.md`. No rule ID added, removed, or renumbered.
- **Real mechanical change**: minifig Resistance is fixed at 1 by definition (not derived from measurement) — this is what makes infantry combat function at all under the plate-layer Resistance system; repairing now costs a real constraint (equipment for others, once-per-activation for self) where before it was unlimited; dual-wielding now explicitly costs 2 AP for 2 dice, not 1 AP.
- No change to any other measured value, dice threshold, or resolution sequence.
