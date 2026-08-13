# CORE states only what it owns

## Why

`docs/02-core-rules.md` restates rules that other documents own. Every restatement below has an authoritative owner elsewhere in `docs/`, and several of them cite that owner in the same breath — `CORE-001`'s "what must fit" paragraph cites `SCS-005`, and `SCS-005` cites `CORE-001` back for the same sentence.

A restatement is not free. It is a second place to update, a second place to fall out of date, and — where the two texts disagree — a second answer to the same question. `system/documentation-standards.md` ("What `system/` Is For") states the rule this change applies to the ruleset: one owner per rule, a pointer instead of a copy.

CORE is also the document a player prints and keeps on the table. It is currently long because it explains where its units are consumed rather than defining them.

The narrow purpose this change enforces:

> **CORE defines the universal foundations every other system consumes. Where another document owns a concept, CORE points at it rather than restating it.**

## What Changes

Nine ruleset documents. `tasks.md` carries the edit-by-edit coverage; sections 1–13 are the change as proposed, section 14 the repairs its audit found, and section 15 the two review comments on pull request #103.

Review of #103 widened two of the deletions below. **`CORE-001` loses the projections table as well**, and the word *projection* leaves the ruleset — each consuming rule now names the dimension it reads (`CMP-018`, `SCS-001`, `WPN-004`), and the glossary entry is deleted (`design.md`, Decision 12). **`CORE-004` also stops stating the two-Unit-Base minimum**, which `VEH-001` owns word for word; `CMP-002`, `VEH-013` and `VEH-028` are retargeted to it (`design.md`, Decision 13). No gameplay value changes in either.

Every deletion names the rule that already states the deleted text, with two recorded exceptions: the symmetry clause in `CORE-009`, which `CODE_OF_DESIGN.md` Principle 9 owns rather than any rule (`design.md`, Decision 11), and `CORE-013`'s "no longer blocks Line of Sight", which follows from removal rather than being restated anywhere (`design.md`, Decision 4). The one sentence with no other owner at all — the infantry pose — is moved rather than deleted.

- **`CORE-001`** — the height derivation is compressed to one paragraph; four restatements go. Infantry's one-Unit-Base occupancy standing or seated and whatever it carries (`09-transport.md`, TRN-002; `05-construction-components.md`, CMP-018), the Unit Base as minimum operational space (`09-transport.md`, TRN-001), the whole **What must fit is the Unit Base** paragraph (`04-construction-standard.md`, SCS-005), and the sentence resolving Line of Sight and Cover against the plastic (`15-geometry-layers.md`, GEO-004; `CORE-008`; `CORE-010`). The dimensions, the plate/brick conversion, where the 13 comes from, the projections table and the `W × D` UB reading all stay — four documents cite `CORE-001` for exactly those.
- **`CORE-004`** — the Pilot paragraph goes; `08-vehicles.md` (VEH-013) owns it and states it better, and `CMP-002` restates it a third time. The two-Unit-Base minimum stays, with a one-clause pointer at the rule that gives the reason.
- **`CORE-006`** — the six-sentence argument for why Action Point costs do not scale becomes two sentences. Every clause the rule asserts is kept; what goes is the worked examples (`09-transport.md`, TRN-005; `CORE-007`), the arithmetic argument, and the enumeration of `CBT-001`, `VEH-008` and `MOVE-010`.
- **`CORE-007`** — the six-item example list goes; `04-construction-standard.md` (SCS-006) carries the same list and already points here for the cost.
- **`CORE-009`** — the symmetry-and-reaction-fire paragraph becomes one sentence, keeping the `CBT-014` citation and keeping the *disclaiming* form: this rule does not by itself grant a shot outside a unit's own activation. It does not become a blanket prohibition, which would outrank the scenario extensions `CBT-010` and `FLOW-013` contemplate. The symmetry clause is dropped to `CODE_OF_DESIGN.md` Principle 9, which states it.
- **`CORE-011`, `CORE-012`, `CORE-013`, and the `# Infantry States` section that holds them** — removed entirely. They are the infantry-shaped copy of the universal Component State machine, which `16-damage-system.md` (DMG-005, DMG-006) owns. What `Wounded` costs an infantry model is owned by `MOVE-021` and `CBT-015`, which `CORE-012` cited rather than defined, and removal by `DMG-006`.
- **`docs/16-damage-system.md`, `DMG-005`** — gains one sentence, the only addition in this change. The infantry pose — Operational stands, Wounded is seated, the pose is the marker and no token is used — is stated today only by `CORE-011` and `CORE-012`; `MEL-011` and `01-foundations.md` carry it as examples, not as the rule. It moves to the document that owns Component States rather than being deleted with them.
- **`CORE-014`, `CORE-015`, `CORE-016`** — three example lists go. `CORE-015`'s one-handed and two-handed lists are reproduced verbatim by `10-weapons.md` (WPN-010), which is where a weapon's handedness belongs; `CORE-016`'s examples are reproduced by `01-foundations.md` (Physical Representation) and `MEL-011`.
- **The `Universal Rule` section** — reworded. "Whenever a conflict exists between written rules and physical construction" can be read as physical construction overriding written rules, which is not the architecture. The four-level order is stated as what it is: rule authority.
- **`Design Notes`** — removed. "These rules intentionally avoid introducing statistics" is stated per document, in the Design Philosophy of each rule-bearing one (`05-construction-components.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`, `15-geometry-layers.md`, `16-damage-system.md`) and as a principle in `CODE_OF_DESIGN.md`; no single `docs/` rule owns the universal form, and this change drops it in favour of the per-document ones rather than claiming an owner it has not got. Understanding the battlefield by observing the models is `CODE_OF_DESIGN.md` and `README.md`; the physical model as source of truth survives in the reworded `Universal Rule` and in `CORE-016`.
- **`docs/14-glossary.md`, the *Projection* entry** — its "never replaces a physical check" clause gains a pointer to `15-geometry-layers.md` (GEO-004), the owner it keeps after `CORE-001` stops restating it.

## What Does Not Change

- **No rule ID moves, and nothing is renumbered.** `CORE-014`, `CORE-015` and `CORE-016` keep their numbers. `CORE-011`, `CORE-012` and `CORE-013` are retired: deleted outright, left as a visible gap, and never reissued to a future rule. No stub is left behind saying a rule used to be there — `docs/` records the ruleset as it stands, and the diff records the rest.

- **Prerequisite: `rule-ids-may-be-retired` merges first.** Deleting a rule ID is refused today by `scripts/check_id_stability.py` and by `system/documentation-standards.md` (Naming Conventions). That change relaxes the single case — removal — and leaves renumbering and reuse forbidden. It is a separate branch because a proposal branch may touch `docs/*.md` and its own change directory only.
- **`CORE-002`.** The `Shield direction` bullet stays. Nothing else in `docs/` owns shield direction, and `docs/14-glossary.md`'s *Facing* entry cites `CORE-002` for it — removing the bullet would delete a rule and leave the glossary pointing at nothing.
- **`CORE-003`, `CORE-008`, `CORE-010`.** Already at one rule each with no restatement to remove.
- **`CORE-005`.** Its "not yet defined" sentence is quoted verbatim by `TODO.md`, which `scripts/check_todo_quotes.py` compares character for character, and it is the only place the structure-damage gap is declared. It is a tracked gap, not a redundancy.
- **`CORE-006`'s action list**, including `- Reload (future rule)`, which `TODO.md` also quotes verbatim.
- **Every other document.** Outside `docs/02-core-rules.md` only two things change: `DMG-005` gains the relocated pose sentence, and the glossary's *Projection* entry gains a pointer. Every sentence deleted here is left standing where its owner states it.
- **`openspec/specs/`.** No capability delta. `unit-base`, `action-economy` and `component-damage` describe behaviour, not which document states it, and no requirement or scenario in any of the three stops being true: `SCS-005` still makes the Unit Base what must fit, `GEO-004` still keeps Line of Sight off a projection, and `CORE-006` still forbids a cost that scales with size.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only (`system/documentation-standards.md`, Versioning). No `**Bump:**` line: this removes no rule that was not already stated elsewhere.

## Checked elsewhere

- `python3 scripts/rule.py refs CORE-011 CORE-012 CORE-013` — all three are cited by nothing. Removing them dangles no reference.
- `python3 scripts/rule.py refs CORE-001 CORE-004 CORE-006 CORE-016` — every inbound citation was read against the text that survives. Twenty rules cite `CORE-001`, for the dimensions, the plate conversion, where the height comes from or a projection; `VEH-028` cites it for the `4A × 3B` reading. All four are kept for that reason.
- `grep -n "CORE-0" TODO.md` — `CORE-005` and `CORE-006` are quoted verbatim there. Both quoted passages are excluded from this change.

## Out of Scope

- **Moving `CORE-016` to another document.** `DMG-005`, `DMG-006`, `MEL-011` and `VEH-025` all cite `CORE-016` as the universal physical-representation principle. It is the owner; only its examples are redundant.
- **Restructuring `01-foundations.md`,** whose *Physical Representation* section overlaps `CORE-016`. Foundations defines no rules and states the principle as philosophy; deciding whether that overlap should survive is a separate change.
- **Adding the required `Design Philosophy` and `Summary` headings** that `02-core-rules.md` lacks. The gap is a recorded exemption in `scripts/lint_ruleset.py` (`SECTION_DEBT`), and closing it would add text to a change whose whole purpose is removing it.
- **Any gameplay value.** No distance, cost, dimension, threshold or state changes.
