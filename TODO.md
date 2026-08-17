# TODO

This file lists gaps the StudCraft ruleset acknowledges in its own text — places where a document explicitly says something is not yet defined, deferred to a future rule, or left to a future supplement. Nothing here is invented; every entry cites the rule or section that declares the gap and quotes it.

This file is updated as gaps close (a future rule fills them) or as new gaps are declared in the documents. An entry appearing here is a record that the ruleset itself flagged the gap — it is not a commitment that the gap will be closed, and nothing here is prioritised or ordered.

Every quote below is checked against the document it cites by `scripts/check_todo_quotes.py`, which `scripts/preflight.py` runs. Completeness is not checked — whether a passage declares a gap at all needs the sentence read, which is `ruleset-auditor`'s job.

Work someone has decided to *do* belongs in the issue tracker, not here; see issue #57 for why the two are separate files and what `ROADMAP.md` would add to them.

---

## Structures

### Structure-wide damage and Deployment Volume occupation

`CORE-005` (`docs/02-core-rules.md`):

> A structure's doors, windows and other functional parts follow `05-construction-components.md`, like any other model's; its walls, slopes, stairs and platforms are terrain, and how a unit crosses or stands on them is `07-movement.md` (MOVE-009 through MOVE-014). Structure-specific damage (collapse, breaching walls) and Deployment Volume occupation for scenario-placed structures are not yet defined — a structure's individual components (doors, windows, walls) already resolve Impacts through the standard Component Damage System (`16-damage-system.md`) like any other component; only structure-wide consequences (e.g. a building collapsing) remain future work.

The same gap is restated in the Design Philosophy section of `docs/06-deployment.md`:

> Every vehicle and infantry model occupies space; a scenario-placed structure's Deployment Volume occupation is not yet defined (`02-core-rules.md`, CORE-005).

What would have to be decided: whether a structure can suffer a whole-structure state (e.g. collapse) beyond its individual components reaching Dead, and how much Deployment Volume a structure placed by a scenario (rather than brought by a player as part of their army) should be counted as consuming.

---

## Vehicles

### Lateral movement for hover vehicles

`VEH-011` (`docs/08-vehicles.md`):

> Future rules may introduce lateral movement for advanced hover systems.

What would have to be decided: whether hover vehicles should gain a side-movement action distinct from the 90° turns they currently have, and at what AP cost.

### A crew member taking over from a dead Pilot

`VEH-013` (`docs/08-vehicles.md`):

> If the vehicle has no Pilot — none embarked, or the Pilot is Dead — the vehicle cannot move, unless another crew member takes over (future rules).

What would have to be decided: which crew positions are eligible to take over, whether taking over costs AP, and whether it requires a dedicated action or happens automatically.

### What "locomotion damage" means

`VEH-031` (`docs/08-vehicles.md`):

> A Wounded wheel, track or hover assembly therefore reduces nothing on its own, and Terrain Thresholds (VEH-021 through VEH-024) are read from the locomotion's geometry whether it is Operational or Wounded. What VEH-019 calls "locomotion damage" is named there and defined by no rule; this rule does not define it either.

What would have to be decided: which components count as a vehicle's locomotion, what state they must reach before the vehicle is Immobilized (`VEH-019`), and whether losing some of them short of all of them does anything at all.

### Freeing a stranded vehicle

`VEH-025` (`docs/08-vehicles.md`):

> Freeing a stranded vehicle is not yet defined, in the same way VEH-013 leaves crew replacement to future rules.

What would have to be decided: whether a stranded vehicle can be freed at all (by its own crew, by another vehicle, or only by scenario rules), and what it would cost.

### Reverse movement restrictions

`VEH-006` (`docs/08-vehicles.md`):

> Reverse movement uses the same movement distance unless restricted by future scenarios.

What would have to be decided: whether any scenario or vehicle type should reduce reverse movement below the standard distance, and under what conditions.

---

## Movement

### Sprinting and other special movement

`MOVE-004` (`docs/07-movement.md`):

> Future scenarios may allow sprinting or other special movement.

What would have to be decided: what a sprint action would cost in AP, how far it would extend the 12-stud limit, and whether it applies to infantry only or to vehicles as well.

---

## Weapons and Equipment

### Reload

`CORE-006` (`docs/02-core-rules.md`) lists, among the actions Action Points can be spent on:

> - Reload (future rule)

What would have to be decided: whether any weapon in the current construction rules needs reloading at all (none currently runs out of ammunition), and if so, what triggers it and what it costs.

### Limiting weapons fired per activation

`WPN-014` (`docs/10-weapons.md`):

> A unit carrying multiple weapons may use them according to its available Action Points.
>
> Future scenarios may limit the number of weapons fired during a single activation.

What would have to be decided: whether such a limit should be a scenario-specific rule or a universal one, and what the limit would be.

### Future weapon types

`WPN-017` (`docs/10-weapons.md`):

> Future supplements may introduce:
>
> - Flamethrowers
> - Explosive Weapons
> - Beam Weapons
> - Energy Weapons
> - Indirect Fire
> - Smoke Launchers
>
> These must continue to follow the StudCraft Weapon Construction Standard.

What would have to be decided: how each of these weapon types generates Impacts within the existing muzzle/Impact Strength system (`10-weapons.md`), since none of them currently has construction rules of its own.

---

## Combat

### Suppression, blast, fire, smoke, explosions, overwatch, reaction fire

`CBT-014` (`docs/11-combat.md`):

> Future versions may include:
>
> - Suppression
> - Blast Weapons
> - Fire
> - Smoke
> - Explosions
> - Overwatch
> - Reaction Fire
>
> These additions must preserve the Impact-based combat system.

What would have to be decided: mechanics for each of these effects that stay within the Impact/Component Damage System rather than introducing a parallel damage mechanic (per `CODE_OF_DESIGN.md` Principle 15, Future Compatibility).

### Simultaneous resolution for mutual engagement

`CBT-010` (`docs/11-combat.md`):

> StudCraft's default activation (`03-game-flow.md`, FLOW-002) is strictly one unit at a time — two attacks only resolve together when something else already declares them so (e.g. a future scenario rule for mutual engagement).

What would have to be decided: whether and how a scenario rule could grant two units mutually declared attacks in the first place; CBT-010 only defines how such attacks would resolve once declared, not what would declare them.

---

## Damage and Construction

### Rebuilding Dead components

`DMG-019` (`docs/16-damage-system.md`):

> Dead components cannot be repaired — they have already been removed from the model. Future construction rules will define rebuilding.

What would have to be decided: whether a removed (Dead) component can ever be restored during a game, and if so, what it would cost and require.

### Cosmetic guidance for specific constructions

`DMG-008` (`docs/16-damage-system.md`):

> Physical/cosmetic representation of a component reaching Dead (how a broken window should look versus a destroyed wheel) is left entirely to the player and the table, per `02-core-rules.md` (CORE-016) — this document does not prescribe it. Future supplements may add cosmetic guidance for specific constructions without changing any mechanic defined here.

What would have to be decided: whether specific, non-binding cosmetic suggestions (e.g. how to represent a destroyed window versus a destroyed wheel) would be useful enough to document, given that DMG-008 is explicit that no mechanic would change either way.
