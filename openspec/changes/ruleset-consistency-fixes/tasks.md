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

## Housekeeping (applies once the review is finished, not per-finding)

- [ ] H.1 No `CHANGELOG.md` edit needed — `Release cut` computes the bump automatically from git history; this is purely editorial so the default minor bump is correct.
- [ ] H.2 Open a PR from the `ruleset-consistency-fixes` branch once findings stop accumulating. Do not archive in the same PR — archiving is a separate, later step via the batched `Archive cut` action.
