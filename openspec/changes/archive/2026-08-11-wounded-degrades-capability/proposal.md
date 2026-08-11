# Wounded degrades capability

## Why

`DMG-005` gives every component in StudCraft three states and then defines the middle one as a no-op:

> **Wounded** — the component has suffered structural damage. It continues to function normally. A second successful damaging impact will kill it.

`CORE-012` says the same thing in the strongest words the ruleset owns:

> A Wounded unit has no penalty of any kind — it moves, attacks, rotates, and climbs exactly as if Operational

So the three-state machine is two states and a flag. A seated minifigure is not a soldier in worse shape; it is a soldier who is one Impact from removal, and the sitting itself carries no consequence. That is the defect, and it is visible from two directions:

- **Principle 6 asks the model to show its condition, and here the model shows a condition that does nothing.** "A wounded soldier sits down" is the principle's own first example. A player looking at a seated model learns only what the next Impact will do — never what this one can still do.
- **The state has no cost while it lasts, so `DMG-019` prices insurance rather than repair.** Spending 1 Action Point to restore a Wounded component buys nothing at all in the present; it buys only the removal of a future risk. Every other Action Point in the game buys an action.

Nothing here is a complaint about the damage model. Resistance, the Geometry Check, the Damage Roll and the removal of Dead components all work, and this change touches none of them. What is missing is that being Wounded costs the thing that was wounded something, in the capability it provides — and that a Wounded cannon is degraded without the Jeep carrying it being degraded, which is what component targeting (`DMG-001`) is for.

## What Changes

- **`DMG-005`** — the Wounded paragraph. Wounded stops meaning "continues to function normally" and starts meaning "still functions, with the capability it provides degraded". The rule names the three degradations, cites the document that owns each, and closes the list: nothing else about a Wounded component changes.

- **New `MOVE-021` — Wounded Movement.** A Wounded infantry model moves **at most two steps** in whichever direction it travels — 6 studs forward or backward (steps of 3, MOVE-004/MOVE-006), 8 studs sideways (steps of 4, MOVE-005). Both are distances those rules already allow. The Action Point cost, the one-direction-per-action rule, rotation, climbing and falling are all untouched.

- **New `VEH-031` — Wounded Pilot.** A vehicle whose Pilot is Wounded moves **twice its own length** instead of three times (VEH-004). One whole length less, so every resulting distance stays a whole number of studs at every vehicle size. The Pilot is the only component read, because `VEH-013` already makes the Pilot the one component a vehicle needs in order to move at all.

- **New `CBT-015` — Wounded Weapon System.** For each Attack Die a Wounded weapon generates, **two dice are rolled and only the lower is read**, resolved against CBT-005's unchanged 4-5-6 threshold. The second die is never an Impact: the *number* of Attack Dice is still the number of functional muzzles (`WPN-006`) or independently wielded melee weapons (`MEL-003`). A hit goes from one chance in two to one in four. The rule also settles the one attack whose weapon system is the attacker — an unarmed attack (`MEL-008`), where the Wounded component and the weapon are the same minifigure.

- **`DMG-011`** — the Attack Roll rule inside the damage document says "the attacker rolls one die for every generated impact", which `CBT-015` makes untrue for a Wounded weapon. It gains a sentence deferring to `CBT-015` and stating that the number of impacts rolled for does not change.

- **`DMG-008`** — its first paragraph says the Component State machine applies "identically to every component". Still true of the machine and no longer true of what a state costs, so the sentence gains a clause saying the cost comes from the capability the component provides and never from the material it represents. `DMG-008`'s subject — no material-specific mechanics — is unaffected.

- **`CORE-012`** — rewritten. The seated pose stops being "purely a visual marker" and becomes the marker for a real limit. It points at `MOVE-021` rather than repeating its numbers.

- **`MOVE-010`** — "the 12-stud limit (MOVE-004) still applies to the move as a whole" is a number that is wrong for a Wounded model. Requalified.

- **The paragraph above `CORE-011`**, which says `CORE-011`/`012`/`013` describe "the infantry-specific physical representation of each state". They now describe a cost as well.

- **Pointers, not copies**, at the six rules a reader reaches first and would otherwise leave without knowing a degraded case exists: `MOVE-004`, `MOVE-005`, `VEH-004`, `WPN-006`, `MEL-003` and `MEL-008`. Each is one clause naming the rule that owns the degradation.

- **Four Summaries** — `07-movement.md` (a seventh principle, and the word "six" with it), `08-vehicles.md`, `11-combat.md`, `16-damage-system.md`.

- **`docs/14-glossary.md`** — a new ***Wounded*** entry at the end of the file, in the glossary's append order. The term now carries mechanical consequences a reader cannot infer from the *Component State* entry, which is unchanged and still true.

- **`TODO.md`** — `VEH-031` states in its own text that it does not define what `VEH-019` calls "locomotion damage". That is a gap the ruleset declares about itself, which is exactly what `TODO.md` records.

- **Two spec deltas.** `component-damage`'s *Component State Progression*, whose scenario *Wounded component still functions* keeps its name and gains a corrected body; and `damage-resolution`'s *Attack Roll*, which currently requires exactly one D6 per Impact. Scenario names are identifiers (`system/workflow.md`), so both requirements carry every living scenario through unrenamed.

## What Does Not Change

- **Nothing on the defending side of an Impact.** The Damage Roll is one D6 for a Wounded component exactly as for an Operational one. `DMG-005`'s "a second successful damaging impact will kill it", `DMG-008`'s "exactly two failed Damage Rolls", `DMG-016`'s shotgun and `MOVE-016`'s falling dice all remain literally true, and every one of `16-damage-system.md`'s five combat examples resolves to the number it already prints. A defensive die for a Wounded component was considered and rejected; `design.md`, Decision 2 records why, so the same suggestion is not re-proposed.

- **Every physical and resource property.** Resistance (`DMG-003`), Impact Strength (`WPN-021`), Unit Base occupancy, footprint, vehicle height, transport capacity, Line of Sight and Cover, and every Action Point cost in the ruleset. A wounded object has not become smaller, thinner or cheaper to operate.

- **The number of Attack Dice, and the number of Impacts.** `CBT-004`, `WPN-006`, `MEL-003` and `DMG-010` keep their counts exactly. `CBT-015` changes how a die is read, never how many Attack Dice or Impacts exist — which is why `weapon-construction`'s *Attack Dice From Muzzle Count* requirement needs no delta.

- **`DMG-019` Repairs.** Already restores `Wounded → Operational` for 1 Action Point, and now buys back a capability instead of only insurance. No edit.

- **`DMG-001`, and the absence of any unit-level state.** Combat targets components, and this change adds no state above them. A Jeep whose cannon is Wounded is a Jeep with a degraded cannon — the Jeep is not Wounded, has no Wounded, and moves at three times its length until its Pilot is the component that suffers.

- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only. No `**Bump:**` line: minor is the default and this is one — no legal army becomes illegal, no measurement moves, and no existing distance or die count is renamed.

## Out of Scope

- **What `VEH-019` calls "locomotion damage".** The phrase is named there and defined by no rule, and it predates this change. A Wounded wheel, track or hover assembly therefore degrades nothing here. Defining it is a change about vehicles, not about the Wounded state; this change records the gap in `TODO.md` instead of closing it.
- **Terrain thresholds, climbing and falling while Wounded.** `VEH-021`–`VEH-024` and `MOVE-010`/`MOVE-016` read geometry, and a Wounded component's geometry has not changed. `MOVE-010`'s edit corrects a distance figure, not the climb.
- **Additional damage states, recovery beyond `DMG-019`, and rebuilding Dead components.** `DMG-019` already closes the recovery case; the rest stays where `DMG-019` leaves it.
- **Cosmetic representation of a Wounded component that is not a minifigure.** `DMG-008` leaves it to the player and the table, and continues to.
