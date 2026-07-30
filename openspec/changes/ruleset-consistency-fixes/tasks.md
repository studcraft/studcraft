## Finding 1: Unify Infantry States with the Universal Component State Machine

- [ ] 1.1 `docs/16-damage-system.md`: rename every `OK`/`TOUCHED`/`DESTROYED` occurrence to `Operational`/`Wounded`/`Dead` — DMG-002, DMG-005 (title stays "Component State Progression"), DMG-006 title/body ("Universal Destruction"), DMG-015 (Damage Roll), DMG-016 (Multiple Impacts example), DMG-017 (Penetration example doesn't use the tokens directly — confirm), DMG-019 (Repairs: `TOUCHED → OK` becomes `Wounded → Operational`), all four Combat Examples, and the Summary.
- [ ] 1.2 `docs/13-materials.md` MAT-004: drop the `OK`/`TOUCHED`/`DESTROYED` primary naming (currently `Standing minifigure (OK)`, `Seated minifigure (TOUCHED, Wounded)`, `Minifigure removed or laid down (DESTROYED, Dead)`) — make `Operational`/`Wounded`/`Dead` the primary names directly, since they're now the universal terms rather than an alias.
- [ ] 1.3 `docs/02-core-rules.md` CORE-011/012/013: keep the rule IDs and all infantry-specific physical detail (stands upright / seated / laid down or replaced by a casualty marker), but reframe each as the infantry-specific elaboration of the universal Component State (`16-damage-system.md`, DMG-005) instead of an independent definition — add the cross-reference, remove any wording that implies infantry has its own separate state system.
- [ ] 1.4 `docs/14-glossary.md` "Component State" entry: update from `OK`/`TOUCHED`/`DESTROYED` to `Operational`/`Wounded`/`Dead`.
- [ ] 1.5 Grep the full `docs/` tree for any other `OK`/`TOUCHED`/`DESTROYED` occurrence missed above before considering this finding done.
- [ ] 1.6 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [ ] 1.7 Confirm no measured rule value, formula, or mechanic changed — purely a renaming/consolidation (per design.md Goals).

## Finding 2: Clarify FLOW-003 (Priority)

- [x] 2.1 `docs/03-game-flow.md` FLOW-003: reword the Priority player's choice from "Activate the first/second unit this Turn" to an explicit "activate one of their own units now" vs. "cede Priority, letting the other player activate first," and add a sentence stating this is a single choice made once per Turn, with FLOW-002's strict alternation governing the rest.
- [x] 2.2 `docs/03-game-flow.md`'s "Turn Sequence" diagram (not a numbered FLOW- rule, the ASCII flow chart near the end of the document) independently restated the old "Activate First / Activate Second" bullets — missed in the original 2.1 pass, caught afterward and updated to match ("Activate own unit now (continue)" / "Cede Priority (opponent activates first)").

## Finding 3: Fix the Illogical Square Bike Footprint

- [x] 3.1 `docs/04-construction-standard.md` SCS-003: change Bike's footprint from `1 × 1 UB` to `1 × 2 UB`.
- [x] 3.2 `docs/08-vehicles.md` VEH-001: change Motorbike's footprint from `1 × 1 UB` to `1 × 2 UB`.
- [x] 3.3 Confirm `docs/09-transport.md` TRN-013's "Motorbike: 1 UB" (a cargo-slot allocation, not the vehicle's own footprint) is a separate, intentionally-abstracted number and does not need to change.

## Finding 4: SCS-018 Never Mirrored WPN-019 (Weapon Front)

- [x] 4.1 `docs/04-construction-standard.md` SCS-018: rename from "Muzzle Adjacency Standard" to "Muzzle Placement Standard"; add the Weapon Front constraint (muzzles only on the single front face, per WPN-019) alongside the existing adjacency content (WPN-007, WPN-020).

## Finding 5: Remove Engine, Replace with a Pilot Requirement

- [x] 5.1 `docs/08-vehicles.md` VEH-013: repurpose from "Engine" to "Pilot" — every powered vehicle requires a Pilot (crew member, VEH-015) to move; no Pilot or a Dead Pilot immobilizes the vehicle.
- [x] 5.2 `docs/08-vehicles.md`: update every other Engine mention (Purpose sentence, Design Philosophy list, VEH-017 Components list, VEH-018 Damage example, VEH-019 Immobilized Vehicles, Summary list) to Pilot/Crew as appropriate.
- [x] 5.3 `docs/05-construction-components.md` CMP-001 and CMP-002: repurpose CMP-002 from "Engine" (2×4 brick requirement) to "Pilot" (visible crew minifigure in an operating position); update CMP-001's example list and CMP-016's example.
- [x] 5.4 `docs/13-materials.md` MAT-010: repurpose from "Engines" to "Pilot" — resolves Impacts via the universal Component State; a Dead Pilot immobilizes the vehicle.
- [x] 5.5 `docs/16-damage-system.md`: update DMG-001's example list, DMG-007's "Armor → Engine" example (and body text), and DMG-008's MAT-010 cross-reference mention, all from Engine to Pilot.
- [x] 5.6 `docs/12-melee.md` MEL-010, `docs/14-glossary.md` Component entry, `docs/01-foundations.md` (two example lists): update Engine mentions to Pilot.
- [x] 5.7 `README.md` and `CODE_OF_DESIGN.md`: update their component-example lists from Engine(s) to Pilot(s) — non-ruleset docs, same branch is sufficient (no dedicated OpenSpec proposal branch needed for these specifically, per `system/workflow.md`).
- [x] 5.8 `specs/component-damage/spec.md` (this change's `MODIFIED` delta): add `Component Targeting` and `Internal Components` alongside the existing `Component State Progression` delta, updating their illustrative "engine" examples to "pilot".
- [x] 5.9 Confirm `CHANGELOG.md`'s historical `[0.1.0]` entry (which lists "Engine" as an added system) and the archived `2026-07-28-component-damage-system` change are left untouched — both are frozen historical records, not living documentation.
- [x] 5.10 Run `python3 scripts/lint_ruleset.py` and grep the full repo for any remaining "engine" mention outside the gitignored `site/docs/` build output, the frozen historical records (5.9), and this proposal's own design-rationale prose.

## Finding 6: Specify What Counts as Damage in MOVE-016 (Falling Damage)

- [x] 6.1 `docs/07-movement.md` MOVE-016: replace "Combat rules determine the effects of the result" with an explicit tie to the Damage Roll (`16-damage-system.md`, DMG-015) — 4/5/6 on the kept die means no damage, 1/2/3 means the faller's Component State advances one step.

## Housekeeping (applies once the review is finished, not per-finding)

- [ ] H.1 No `CHANGELOG.md` edit needed — `Release cut` computes the bump automatically from git history; this is purely editorial so the default minor bump is correct.
- [ ] H.2 Open a PR from the `ruleset-consistency-fixes` branch once findings stop accumulating. Do not archive in the same PR — archiving is a separate, later step via the batched `Archive cut` action.
