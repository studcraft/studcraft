# Construction Components state only what they own

## Why

`docs/05-construction-components.md` answers two different questions. One is its own: **what physical part must a model show for a capability to exist, and what makes that part functional.** The other belongs to eight other documents — how far the thing moves, what it costs to open, how much it carries, what happens when it is hit.

Nine of its eighteen rules state something another document already owns, and several say so in their own text: `CMP-007` is a list of four weapon properties `10-weapons.md` derives, `CMP-013` is `TRN-014` in different words, `CMP-011` is a pointer to `SCS-009` followed by three gameplay consequences it does not own. Six more carry a closing sentence that hands their gameplay consequence to `08-vehicles.md` — a delegation the rule already demonstrates by not stating the rule.

`system/documentation-standards.md` ("What `system/` Is For") states the rule this change applies to the ruleset: one owner per rule, a pointer instead of a copy. This is the third document to be cut to it, after `02-core-rules.md` (#103) and `04-construction-standard.md` (#104).

The narrow purpose this change enforces:

> **Construction Components defines the physical component. The system that owns the capability defines what that component does.**

## What Changes

Seven ruleset documents, `assets/IMAGES.md`, `TODO.md` and one script comment. **Fifteen rules are retired, nine are trimmed, four move to another document under new IDs, two are absorbed by a rule that already stated most of them, one sentence moves on its own, and four restatements are corrected.** No rule ID is renumbered or reused, and the one requirement that changes strength is recorded below. `tasks.md` carries the edit-by-edit coverage: sections 1–17 are the change as proposed, section 18 the five repairs its own audit found, and **sections 19–20 the boundary the maintainer set once the duplication was visible** — see *The boundary* below.

`docs/04-construction-standard.md` is where the mirror's other half lived — after #104 it owned the door, ramp and window construction requirements (`SCS-006` – `SCS-009`) that `05-construction-components.md` restated. Retiring the copies made the missing boundary visible, and sections 19–21 of `tasks.md` draw it; see *The boundary* below.

### Retired

Each retirement names the rule that already states the retired text.

- **`CMP-002` — Pilot.** `VEH-013` requires every powered vehicle to have a Pilot in a visible operating position, states that losing it stops the vehicle, and derives the two-Unit-Base minimum from it — the three "Current gameplay" bullets, in the same order. Its one sentence with no other owner — the Pilot is a minifigure, not an empty seat — **moves to `VEH-013`**. Cited by nothing.
- **`CMP-007` — Weapons.** Four properties, each owned: length `WPN-003`, range `WPN-005`, Attack Dice `WPN-006`, firing direction `WPN-019`. "Only physically represented weapons may attack" is `WPN-001` ("Weapons that do not satisfy these conditions are decorative") and `CORE-014`. What remained was a pointer at `10-weapons.md`, and a pointer-only rule is not a rule. Cited by nothing.
- **`CMP-009` — Doors.** `SCS-006` states that decoration alone has no gameplay effect and lists doors; `CMP-018` owns the opening requirement it cited; `TRN-005`, `TRN-006`, `MOVE-018` and `CORE-008` own the four uses it listed. **The construction requirement is settled in `SCS-007`'s favour, and that is a decision rather than a transcription:** `CMP-009` required a door to open *and* close, `SCS-007` requires it to open and permits it to close, and after this change a door that opens but cannot close is legal. The two rules have contradicted each other since both were written — both landed in the same initial commit, so neither is the later copy — and retiring the component one is what resolves it. `SCS-007`'s text survives, and section 19 then moves it into this very document as `CMP-020`, so the outcome is not "the Standard won": it is that the permissive wording won, on its merits. Nothing in the ruleset reads whether a door can close (`MOVE-018` reads whether it is open; `CORE-007` and `TRN-008` charge the same for either operation), and a transport whose door cannot close is already an open transport by `TRN-009`'s physical test, with its passengers targetable and unprotected (`TRN-010`) — the model charges for it without a legality rule (`design.md`, Decision 11). Cited only by `CMP-018`, which is retargeted here.
- **`CMP-010` — Ramps.** `SCS-008` requires a ramp to physically rotate or lower; `MOVE-019` states that a lowered ramp becomes usable terrain and a legal access point; `TRN-007` lists rear ramps among access points. Cited only by `CMP-018`, retargeted here.
- **`CMP-011` — Windows.** Its first sentence is `SCS-009`'s, which it cited. Visibility is `CORE-008`, which closes "A transparent element does not block sight. It stops an Impact only by its own Resistance, like any other component"; firing positions are `TRN-011`; and "resolve Impacts like any other component" is `DMG-008`'s whole subject — every component resolves an Impact identically "regardless of what it represents — glass, metal, wood, infantry, or anything else." Cited only by `CMP-018`, whose windows sentence is deleted with it.
- **`CMP-012` — Cargo Bays.** `TRN-003` defines capacity as the Unit Base volume available inside the compartment, `TRN-019` bounds it by clearance, and `DEP-005` states "Transport capacity is not purchased … If a Unit Base fits inside the vehicle, a minifigure may be transported in it." The glossary's *Cargo Bay* entry already points at `TRN-019`. Cited by nothing.
- **`CMP-013` — Crew Compartments.** `TRN-014` states two of its three bullets almost word for word: crew occupy their own Unit Bases, driver positions are separate from passenger compartments, crew space is not cargo capacity. The third — "Must be physically represented" — is stated by no other rule in those words; `VEH-015` ("Crew must physically fit inside the vehicle"), `TRN-019` (clearance measured in the compartment) and `VEH-013` (a visible operating position) each presuppose the compartment exists and are unusable without it. It is retired rather than moved because a rule that only repeats Principle 1 for one component is what this change removes everywhere else. Cited by nothing.
- **`CMP-015` — Accessories.** `CMP-001` states the rule in this change's own text — decorative elements have no gameplay effect unless another rule gives them one — and `GEO-002` lists antennas, exhausts and decorative panels among its own examples of Visual Geometry. Cited by nothing.
- **`CMP-017` — Component Visibility.** "Functional components should be easy to identify" is an adjudication, not a construction requirement: it asks whether a component is visible *enough*. Every rule that needs visibility states its own objective requirement — `CMP-005` (hover components visually distinguishable), `CMP-006` (legs visibly support), `CMP-014` (visible on the model), `VEH-013` (visible operating position), `WPN-001` (a visible functional muzzle, after section 20) — and the document's own `# Design Philosophy` keeps the aspiration where an aspiration belongs. Cited by nothing. Section 21 deletes `04-construction-standard.md`'s `# Construction Principles`, whose `Visible` condition is the same adjudication surviving in another document.

### Trimmed

- **`CMP-001` — Functional Components.** Keeps its defining sentence word for word — the glossary's ***Functional Component*** entry restates it. Loses the ten-item example list, which is an index of rules stated below it and in `01-foundations.md` ("Components"), `VEH-017` and `DMG-001`. Gains `CMP-015`'s qualifier: decorative elements have no gameplay effect **unless another rule gives them one**. Without it the rule contradicts `WPN-002`'s decorative-looking-but-functional muzzle and `GEO-002`'s structural plate.
- **`CMP-003` — Wheels.** Keeps ground contact, free rotation and the decorative exclusion. Loses "Movement is resolved using the Vehicle Movement Rules" and the axle-height Terrain Threshold sentence (`VEH-022`).
- **`CMP-004` — Tracks.** Keeps physical representation on both sides and the decorative exclusion. Loses the pivot and terrain sentence (`VEH-009`, `VEH-022`).
- **`CMP-005` — Hover System.** Keeps both sentences `VEH-024` cites it for: hover emitters replace wheels or tracks, and hover components must be visually distinguishable. Loses the pivot, movement and Terrain Threshold sentence (`VEH-011`, `VEH-024`) — including the reason clause, which `VEH-024` already states in full and attributes to `CMP-005`.
- **`CMP-006` — Walkers.** Keeps articulated legs that visibly support the vehicle, which `VEH-023` cites it for, and the decorative exclusion. Loses the pivot and knee-height sentence (`VEH-010`, `VEH-023`).
- **`CMP-008` — Turrets.** Keeps the physical requirement — a turret must rotate, and the weapons on it rotate with it — and gains the `WPN-009` pointer that names a turret a valid weapon mount. Loses "Rotation should be visible", which is `CMP-017`'s adjudication in miniature, and "Turrets follow the normal rotation rules", which names no rule: vehicle rotation is `VEH-008` – `VEH-011` and re-aiming a rotating mount is `DMG-018`.
- **`CMP-014` — Shields.** Keeps the physical requirements as one sentence and keeps the orientation paragraph #104 placed here, which the glossary's *Facing* entry now routes to. Loses "may be targeted or may interpose … exactly like any other component" (`DMG-007`, `DMG-012`) and the Resistance sentence (`DMG-003`); "not for any separate defensive bonus" survives inside the orientation paragraph, so the no-bonus rule is not lost.
- **`CMP-016` — Functional Integrity.** Keeps both sentences of the principle. Loses the three examples, each owned elsewhere: Pilot lost (`VEH-013`), weapon removed (`WPN-001`, `CORE-014`), door destroyed (`DMG-006`).
- **`CMP-018` — Access Openings.** Eight rules and one glossary entry cite it, and it keeps everything they rely on: the opening must pass the Unit Bases the model occupies, measured with the component open, at least as wide as the model's front edge and as tall as the model stands; the clear opening rather than the nominal frame; opening rather than approach; functional for one model and decorative for another; checked against the plastic as it stands. The front-edge clause is kept deliberately: `CORE-001` gives the Unit Base its `4 × 3` footprint and `CORE-002` names the 4-stud edge the front, but no rule says which face an opening is checked against, and `MOVE-003` lets a model travel sideways — so without it a 3-stud opening could be argued to pass infantry edgeways. It loses the arithmetic it was redoing — infantry is 1 Unit Base and 4 studs (`TRN-002`, `CORE-003`), one Unit Base is 13 plate layers and a `W × D` footprint is `4W × 3D` studs (`CORE-001`) — and the two paragraphs that restate other documents: the ramp-and-Terrain-Threshold worked example (`VEH-021` – `VEH-024`, `MOVE-019`) and the declared-role paragraph (`TRN-007`, `TRN-011`).

### `# Purpose`

One line of `docs/05-construction-components.md`'s `# Purpose` says "A component only has a game effect if it complies with the construction rules defined in this document." After this change that is false — a door complies with `SCS-007`, a weapon with `WPN-001`, a crew compartment with `TRN-014`. It is replaced by the split this change enforces. `# Design Philosophy` and `# Summary` are checked and stay: both describe components providing gameplay through physical construction, which is what the nine surviving rules do.

### `docs/14-glossary.md`

The ***Functional Component*** entry says "Decorative elements have none" and cites `CMP-001`. It gains the same qualifier `CMP-001` gains, because the entry is a restatement and restatements drift (`system/proposal-review.md`, "The Summary Is Part of the Rule").

### The boundary

Retiring `CMP-009`, `CMP-010` and `CMP-011` exposed why they existed. `04-construction-standard.md` held `SCS-006` – `SCS-009` — interactive elements, doors, ramps, windows — and `05-construction-components.md` mirrored three of them one for one, in the same order. Both documents were answering "what must be physically built", with no stated line between them, so the same rule got written twice. Deleting one copy fixes the symptom; the line is what stops it recurring.

The line, decided by the maintainer and now stated in `04-construction-standard.md`'s `# Purpose`:

> **`04-construction-standard.md` is the battlefield and the base every model stands on. `05-construction-components.md` is every functional part of a model.**

It is testable, and the ruleset already agrees with it: `DMG-001` targets a Door and a Window as components, `CMP-016` removes one and changes what the model can do, and a building is a model too (`CORE-005`), so a door belongs to the same side whether it is on a hull or a wall.

**Six rules move, none is rewritten.** Each is transcribed word for word under a new ID; the old ID is retired and never reissued, and the new ones append at the end of their document because IDs ascend and are never renumbered to read better.

| Was | Is now | Why |
|---|---|---|
| `SCS-006` Interactive Elements | `CMP-019` | a part of a model |
| `SCS-007` Doors | `CMP-020` | a part of a model |
| `SCS-008` Ramps | `CMP-021` | a part of a model |
| `SCS-009` Windows | `CMP-022` | a part of a model |
| `SCS-016` Functional Weapons | absorbed by `WPN-001` | `WPN-001` already requires a muzzle; it gains the word `visible` |
| `SCS-017` Weapon Body | absorbed by `WPN-001` | `WPN-001` already requires a weapon body; it gains `SCS-017`'s definition of one |

**No new weapon rule is created.** `SCS-017` was going to become `WPN-022` until the audit pointed out that `WPN-001` already lists a weapon body among a weapon's three requirements — the same ground `SCS-016` was being absorbed on, applied inconsistently one task later (`design.md`, Decision 13).

Four citations are retargeted with them: `VEH-027` → `CMP-021`, `TRN-012` → `CMP-022`, the glossary's ***Interactive Element*** → `CMP-019`, its ***Weapon Body*** → `WPN-001`.

**The four moved rules are trimmed on arrival**, exactly as the nine already in `05-construction-components.md` were. `CMP-019` arrives without `SCS-006`'s six-item example list and without its unqualified "Decoration alone has no gameplay effect" — `CMP-001` states that rule qualified, twelve lines above, and importing the absolute form would reinstate what this change removed. `CMP-020` and `CMP-021` each gain the `CMP-018` pointer the retired `CMP-009` and `CMP-010` carried; with `CMP-018` now in the same document it is a pointer rather than the copy those rules were.

`04-construction-standard.md` keeps five rules: `SCS-002` (the infantry base) and `SCS-010` – `SCS-013` (walls, slopes, stairs, platforms). The base stays because it is the standard base every model is built on rather than a part that provides a capability, and because `CORE-001` and `MOVE-002` both read it there.

### `assets/IMAGES.md`

Two bullets in its declined-candidates list cite `CMP-002` — "A visible minifigure in an operating position … easily verified by looking at the model" — and both are retargeted to `VEH-013`, which states that sentence after this change. The quoted reasoning does not change; only the rule ID does.

**This is a retired ID cited from outside `docs/`, and nothing would have caught it.** `scripts/lint_ruleset.py` validates only the rule named beside a filename in the image table, and the greps in this proposal's own "Checked elsewhere" reached `system/`, `README.md`, `CODE_OF_DESIGN.md`, `CONTRIBUTING.md`, `AGENTS.md` and `TODO.md` — not `assets/`. The audit of the applied text found it (`design.md`, Decision 12).

## What Does Not Change

- **No rule ID is renumbered or reused.** Fifteen are retired — deleted outright, left as visible gaps, never reissued, no stub. The six rules that change document do so by retiring their old ID and appearing under a new one above their new document's highest number; `scripts/check_id_stability.py` reports neither a move nor a reuse, which is the invariant it exists to hold. `system/documentation-standards.md` (Naming Conventions) permits deletion and forbids renumbering and reuse.
- **No moved rule changes what it requires.** `CMP-022` is `SCS-009` word for word. `CMP-020` and `CMP-021` keep their requirements and gain a pointer. `CMP-019` keeps `SCS-006`'s requirement and loses an example list and a sentence `CMP-001` states better. `WPN-001` gains `SCS-016`'s `visible` and `SCS-017`'s definition of a weapon body, its three-item list written inline.
- **No gameplay value.** No distance, cost, dimension, threshold, capacity or state changes. Every sentence deleted here is left standing where its owner states it, with three recorded exceptions: `CMP-002`'s minifigure sentence **moves** to `VEH-013` rather than being deleted; `CMP-009`'s "must physically open **and** close" is **not** carried over — `SCS-007`'s "must open, may close" survives it as `CMP-020`, which is the one requirement this change leaves weaker than it found it (`design.md`, Decision 11); and `SCS-016`'s "**every** weapon must include at least one visible functional muzzle" lands on `WPN-001`'s ranged-weapon bullets, so section 20 adds the same visibility to the melee striking end rather than let it fall out (`design.md`, Decision 13).
- **`CMP-004`'s modality.** "Both sides should contain tracks" stays *should*. Rewriting it to *must* would be a new construction requirement smuggled in as an edit.
- **Every inbound citation still resolves.** `VEH-023` → `CMP-006`, `VEH-024` → `CMP-005`, and the eight citers of `CMP-018` all name rules this change keeps. The only citations pointing at a retired rule are `CMP-018`'s own `(CMP-009, CMP-010)` and `(CMP-011)`, both removed by the same task that rewrites it.
- **`docs/16-damage-system.md`.** Nothing is added to it, and nothing is removed. Every owner this change points at there — `DMG-001`, `DMG-003`, `DMG-006`, `DMG-007`, `DMG-008`, `DMG-012` — already states its rule in full.
- **`docs/09-transport.md` and `docs/02-core-rules.md`.** One citation each, in `TRN-012` and `CORE-005`; no rule in either document changes what it requires.
- **The five rules `docs/04-construction-standard.md` keeps.** `SCS-002` and `SCS-010` – `SCS-013` are untouched, and the document keeps `# Purpose`, `# Design Philosophy` and `# Summary` — the three sections `scripts/lint_ruleset.py` checks.
- **`openspec/specs/`.** No capability delta. No spec mentions `05-construction-components.md` or any `CMP` ID, and no requirement stops being true: the rules move nowhere, only the document that states them changes.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only (`system/documentation-standards.md`, Versioning). No `**Bump:**` line — this removes no rule that was not already stated elsewhere.

## Checked elsewhere

- `python3 scripts/rule.py refs` on all eighteen `CMP` IDs. Twelve are cited by nothing. `CMP-005` is cited by `VEH-024`, `CMP-006` by `VEH-023`, `CMP-018` by `CMP-009`, `CMP-010`, `MOVE-018`, `MOVE-019`, `VEH-030`, `TRN-007`, `TRN-011` and `GEO-004` — every one of those four rules is kept. `CMP-009`, `CMP-010` and `CMP-011` are cited only by `CMP-018`.
- `grep -rn "CMP-0" docs/`. `rule.py refs` reads the rule graph and does not see `docs/14-glossary.md`, which cites `CMP-001` (*Functional Component*), `CMP-014` (*Facing*) and `CMP-018` (*Access Opening*) — all three kept.
- `grep -rn "CMP-0"` across `system/`, `README.md`, `CODE_OF_DESIGN.md`, `CONTRIBUTING.md`, `AGENTS.md` and `TODO.md`: **no hits at all.** `TODO.md` quotes no text from this document, so `scripts/check_todo_quotes.py` is unaffected by every edit here.
- `README.md` names `05-construction-components.md` twice, in the structure list and the reading order. Neither names a rule and neither changes.
- `grep -rn "05-construction-components" openspec/specs/` and `grep -rn "CMP-"` over the same: nothing.
- The owners were read in full, not grepped: `02-core-rules.md`, `04-construction-standard.md`, `06-deployment.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`, `15-geometry-layers.md`, `16-damage-system.md`, `01-foundations.md` and `14-glossary.md`.

## Out of Scope

- **The source brief's "keep, but simplify" for `CMP-002`, `CMP-007`, `CMP-009`, `CMP-010`, `CMP-011` and `CMP-015`.** Each of those, once the gameplay text is removed, states nothing another document does not — so the simplification bottoms out at retirement rather than at a short rule (`design.md`, Decision 2). This is a deliberate divergence from the brief, taken because keeping the shortened version is precisely the copy `system/documentation-standards.md` forbids.
- **Moving `CMP-014`'s orientation paragraph to `DMG-007`.** Considered and rejected (`design.md`, Decision 4): #104 placed it here one pull request ago and pointed the glossary's *Facing* entry at it, and where a shield physically stands is a property of the model rather than of the damage sequence.
- **Merging `04-construction-standard.md` into `05-construction-components.md`.** Considered once the mirror was visible, and rejected: every moved rule needs a new ID and the old one retires, so merging the terrain rules too would retire five more IDs and renumber `README.md`'s reading order, to remove a boundary that a written criterion already resolves (`design.md`, Decision 13).
- **Renaming `04-construction-standard.md`.** With five rules left it is the battlefield-and-base document, and its number is in `README.md`'s structure list and reading order. A rename is cheap to do and not this change's to decide.
- **`docs/01-foundations.md`'s `# Components` section**, which lists the same components `CMP-001`'s example list did. It defines no rules and states no requirement, so it is not a second owner; `01-foundations.md` was already recorded Out of Scope by #104 for the same reason.
- **`docs/09-transport.md`, `TRN-004` and `TRN-017`.** Both describe interior layout in prose that overlaps the retired `CMP-012`'s subject. Neither restates a rule this change removes, and consolidating Transport's own rules is Transport's change.
- **Renumbering.** Forbidden, and named here because the source brief asked for it conditionally.
