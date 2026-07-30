## Context

This change accumulates findings from a manual consistency review of the shipped ruleset, done one at a time rather than as a single upfront audit. Each finding gets a Decision entry here explaining the resolution chosen and the alternatives considered, in the same style as `weapon-construction-system`/`gameplay-visual-geometry`/`component-damage-system`'s design docs.

## Goals / Non-Goals

**Goals:**
- Fix each accumulated finding without changing any measured rule value, formula, or mechanic — these are naming/consolidation fixes, not gameplay changes, unless a finding explicitly says otherwise.
- Keep every fix traceable to the specific duplication/inconsistency it resolves.

**Non-Goals:**
- A complete, one-time audit of the entire ruleset. This proposal grows incrementally as issues are found in conversation, not from a single exhaustive pass.

## Decisions

### Finding 1: Unify Infantry States (CORE-011/012/013) with the universal Component State machine (DMG-005)

**Rename the universal states to Operational / Wounded / Dead, rather than keeping OK / TOUCHED / DESTROYED and just aliasing infantry to it.**
Alternative considered: keep `DMG-005`'s `OK`/`TOUCHED`/`DESTROYED` as the canonical universal names, and have `CORE-011`/`012`/`013` simply cross-reference them without renaming anything (i.e. "Operational = OK, per DMG-005"). Rejected — `OK`/`TOUCHED`/`DESTROYED` reads naturally for a generic component (a wheel, a door) but awkwardly for the case that's actually most central to the game (a minifig), and `Operational`/`Wounded`/`Dead` already existed, was already player-facing terminology, and reads naturally for both organic and mechanical components alike ("the engine is Dead" reads fine; "the engine is DESTROYED" also reads fine, but "the minifig is TOUCHED" reads worse than "the minifig is Wounded"). Reusing the name that already existed and already read well, rather than the one that was newer but more mechanical, minimizes how much vocabulary players need to learn.

**`CORE-011`/`012`/`013` become infantry's physical/cosmetic elaboration of the universal states, not an independent definition.**
Mirrors exactly how `13-materials.md`'s per-material sections (MAT-003 Glass, MAT-012 Stone, etc.) describe physical response to a universal mechanism instead of redefining it — and how `MAT-004` was already partially reconciled this way when `component-damage-system` shipped. `CORE-011`/`012`/`013` keep their rule IDs and their infantry-specific physical detail (stands upright / seated / laid down or replaced by a casualty marker) but stop asserting the state machine itself, which now lives solely in `DMG-005`.

**This requires a `MODIFIED` delta on `component-damage`, unlike the direct edits used for `combat.md`/`materials.md` in `component-damage-system`.**
`component-damage` was archived as a real OpenSpec capability once `component-damage-system` merged — this is the first proposal in this repo to modify an already-archived capability's requirement rather than write a fresh `ADDED` requirement or edit an un-formalized document directly. See `system/proposal-review.md` (Delta vs. Direct Edit) for when each applies.

### Finding 2: Clarify FLOW-003 (Priority) as a one-time, explicit binary choice

**Reword to an explicit "continue vs. cede" choice, and state outright that it's decided once per Turn.**
Alternative considered: leave the mechanic as-is and only add the clarifying sentence about it being one-time, without changing the bullet wording. Rejected — the original bullets ("Activate the first unit this Turn" / "Activate the second unit this Turn") describe the *consequence* of the choice, not the choice itself, which is what made it possible to misread as a repeated per-activation decision rather than a single up-front one. Rewording the bullets to name the actual choice (continue with your own activation vs. cede Priority to the opponent) and then stating explicitly that FLOW-002's strict alternation takes over afterward removes the ambiguity from both ends at once. No mechanical change: same choice, same outcome.

### Finding 3: Fix the illogical square Bike footprint

**Change `1 × 1 UB` to `1 × 2 UB` in both places it's listed, rather than picking a different value per document.**
`SCS-003` and `VEH-001` independently list the same footprint table for the same set of example vehicles — same duplication pattern as Findings 1/2, just for an example value rather than a rule. `1 × 2` was chosen over other elongated options (e.g. `1 × 3`) as the minimal fix that makes the footprint non-square without exaggerating it relative to Buggy's `2 × 2`.

### Finding 4: SCS-018 never mirrored WPN-019 (Weapon Front)

**Expand SCS-018 in place rather than adding a new SCS- rule ID.**
Alternative considered: leave SCS-018 scoped to adjacency only and append a new rule (e.g. `SCS-025`) for the Weapon Front constraint. Rejected — SCS-018 is already "the muzzle-placement slot" in the construction standard's structure; splitting the concept across two IDs when `10-weapons.md`'s own WPN-020 (Muzzle Placement) already treats footprint-fit, front-face, and adjacency as one cohesive concept would recreate exactly the kind of fragmentation this proposal is trying to remove. Renamed SCS-018 from "Muzzle Adjacency Standard" to "Muzzle Placement Standard" to reflect its broadened scope.

### Finding 5: Remove Engine, replace with a Pilot requirement

**Repurpose CMP-002/VEH-013/MAT-010 in place, don't delete the IDs.**
Alternative considered: delete the Engine rules outright and leave a documented gap in the numbering (`scripts/lint_ruleset.py` only checks for duplicate/decreasing IDs, not gaps, so this would have been mechanically valid). Rejected — same reasoning as `WPN-007`/`SCS-018` earlier in this same proposal: a repurposed ID carrying a related new mechanic is more informative to a future reader than a silent gap, and no official release has happened yet, but "rule identifiers should remain stable" isn't scoped to releases — it's a standing repo convention this proposal has already relied on twice.

**Pilot is the mechanic that replaces Engine's structural role: a mandatory component whose loss immobilizes the vehicle.**
This wasn't just "delete Engine" — the user specifically asked for a replacement mechanic. Pilot reuses the already-existing `VEH-015` (Crew) concept instead of introducing a new one, and its Component State (`Dead`, per Finding 1) is what gates movement, tying this finding directly into Finding 1's unified state machine rather than inventing a separate on/off flag.

### Finding 6: MOVE-016 (Falling Damage) never specified what counts as damage

**Reuse the Damage Roll threshold (DMG-015) rather than inventing a new one for falls.**
Alternative considered: define a bespoke threshold specifically for falling (e.g. a different die range, or a fixed number of studs per damage step). Rejected — `MOVE-016` already produces exactly one kept D6 result per fall, which is precisely the shape a Damage Roll expects; introducing a second, different damage-threshold convention for one specific case would undermine the "one universal resolution mechanism" goal this whole proposal is built around (see Finding 1).

## Risks / Trade-offs

- [Risk] Renaming `OK`/`TOUCHED`/`DESTROYED` to `Operational`/`Wounded`/`Dead` touches every place `component-damage-system` introduced those names (`docs/16-damage-system.md` alone uses them roughly a dozen times across rules, examples, and the summary) — a wide diff for a renaming-only change. → Mitigation: accepted, same reasoning as `consolidate-core-measurements`'s wide diff — the fix has to touch everywhere the problem does; `scripts/lint_ruleset.py` plus a full reread confirms nothing else breaks.

## Open Questions

*(Add here as they come up during the review.)*
