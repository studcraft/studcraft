# TODO

This file lists gaps the StudCraft ruleset acknowledges in its own text — places where a document explicitly says something is not yet defined, deferred to a future rule, or left to a future supplement. Nothing here is invented; every entry cites the rule or section that declares the gap and quotes it.

This file is updated as gaps close (a future rule fills them) or as new gaps are declared in the documents. An entry appearing here is a record that the ruleset itself flagged the gap — it is not a commitment that the gap will be closed, and nothing here is prioritised or ordered.

Every quote below is checked against the document it cites by `scripts/check_todo_quotes.py`, which `scripts/preflight.py` runs. Completeness is not checked — whether a passage declares a gap at all needs the sentence read, which is `ruleset-auditor`'s job.

Work someone has decided to *do* belongs in the issue tracker, not here; see issue #57 for why the two are separate files and what `ROADMAP.md` would add to them.

---

## Structures

### Structure-wide damage

`CORE-005` (`docs/02-core-rules.md`):

> Structure-wide effects such as building collapse or breaching are not currently defined.

What would have to be decided: whether structures can suffer whole-structure effects such as collapse or breaching, and what rules resolve those effects.

---

## Vehicles

### Lateral movement for hover vehicles

`VEH-011` (`docs/08-vehicles.md`):

> Future rules may introduce lateral movement.

What would have to be decided: whether hover vehicles should gain a side-movement action distinct from their current forward, backward and turning movement, and at what AP cost.

### A crew member taking over from a dead Pilot

`VEH-013` (`docs/08-vehicles.md`):

> A vehicle without a Pilot, or with a Dead Pilot, cannot move unless another crew member takes over.

What would have to be decided: which crew positions are eligible to take over, whether taking over costs AP, and whether it requires a dedicated action or happens automatically.

### Freeing a stranded vehicle

`VEH-025` (`docs/08-vehicles.md`):

> Freeing a stranded vehicle is not currently defined.

What would have to be decided: whether a stranded vehicle can be freed at all, by whom, and what action or cost would be required.

### Reverse movement restrictions

`VEH-006` (`docs/08-vehicles.md`):

> Reverse movement uses the same distance as forward movement unless restricted by a scenario.

What would have to be decided: whether any scenario or vehicle type should reduce reverse movement below the standard distance, and under what conditions.

---

## Combat

### Suppression, blast, fire, smoke, explosions, overwatch, reaction fire

`CBT-014` (`docs/11-combat.md`):

> Future combat rules must preserve the Impact-based combat system.

The same rule explicitly lists the following mechanics as not currently part of StudCraft:

* Suppression
* Blast Weapons
* Fire
* Smoke
* Explosions
* Overwatch
* Reaction Fire

What would have to be decided: mechanics for each of these effects that preserve the Impact-based combat system rather than introducing a parallel damage mechanic.

---
