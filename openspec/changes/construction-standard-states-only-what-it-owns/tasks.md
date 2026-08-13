# Tasks — Construction Standard states only what it owns

## How to apply this change

Every anchor below is pre-change text, checked with exact-substring matching and occurring **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which occurrence was meant. Never edit a document to make a verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the text** — do not write the backticks into the document.

A `#` heading or a `---` horizontal rule inside a fence is real markdown that must land in the file as markdown, not as quoted text. Tasks 1.1, 2.1, 6.1 and 7.1 all contain real `# ` headings and real `---` rules.

**This change is mostly deletion, but not entirely.** Twelve of the sixteen replacement blocks are shorter than their anchor, and four of those consist of a single line that already appears at the end of the anchor. **That repeated line is a landmark, not an edit** — it stays in the file exactly once, where it already is. Copy each block exactly.

**Four blocks are longer than their anchor: tasks 8.1, 9.1, 10.1 and 14.1.** Each adds one sentence, and none of them is a mistake. Task 15.2 has no replacement block at all — see below.

**Thirteen rule IDs are deleted and nothing is renumbered.** `SCS-001`, `SCS-003`, `SCS-004`, `SCS-005`, `SCS-014`, `SCS-015`, `SCS-018`, `SCS-019`, `SCS-020`, `SCS-021`, `SCS-022`, `SCS-023` and `SCS-024` are removed outright. Do not renumber the rules that remain, do not close the gaps, and do not leave a stub saying a rule used to be there.

**Sections 8, 9, 10 and 14 are not deletions, and skipping one deletes a rule.** Each moves a sentence out of a rule this change retires and into the document that owns it — `SCS-004`'s into `CORE-002` (section 8), `SCS-023`'s into `CORE-008` (section 9), `SCS-005`'s gap clause into `TRN-019` (section 10), `SCS-022`'s into `CMP-014` (section 14). Section 2 without sections 8 and 10, or section 7 without sections 9 and 14, is a deletion rather than a move.

**Task 15.2 is the one task with no fenced anchor.** It names its first and last line instead, and says why in the task itself. Every other task in this file follows the fence convention above.

**Section 15 edits `TODO.md`, whose blockquotes are compared character for character** against the documents they quote by `scripts/check_todo_quotes.py`, which `scripts/preflight.py` runs. Two entries quote text this change edits. Applying sections 7 and 12 without section 15 turns the pull request red (`design.md`, Decision 11).

- [x] 0.1 The branch is `construction-standard-states-only-what-it-owns`, named for this change directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Nine ruleset documents, `TODO.md` and one `system/` document, no spec delta: **twenty-eight edits and twenty-four non-edit tasks** (0.1, 16.1 – 16.11, 17.4 – 17.7, 18.8 – 18.12 and 19.2 – 19.4). Sections 1–16 are the change as proposed — seventeen edits, listed below. **Section 17 adds three repairs from the audit of the applied text**, **section 18 the seven from the review of pull request #104**, which brings in `docs/06-deployment.md` and `docs/08-vehicles.md`, and **section 19 the one edit outside the ruleset**, which has its own note on why it is here. Sections 17 and 18 carry anchors that are post-change text where an earlier section touched the same line; each says so.

| `proposal.md` item | Task | Path |
|---|---|---|
| `SCS-001` retired | 1.1 | `docs/04-construction-standard.md` |
| `SCS-003`, `SCS-004`, `SCS-005` retired | 2.1 | `docs/04-construction-standard.md` |
| `SCS-007` trimmed | 3.1 | `docs/04-construction-standard.md` |
| `SCS-008` trimmed | 4.1 | `docs/04-construction-standard.md` |
| `SCS-009` trimmed | 5.1 | `docs/04-construction-standard.md` |
| `SCS-014`, `SCS-015` retired | 6.1 | `docs/04-construction-standard.md` |
| `SCS-018` – `SCS-024` retired | 7.1 | `docs/04-construction-standard.md` |
| `SCS-004`'s legality sentence lands in `CORE-002` | 8.1 | `docs/02-core-rules.md` |
| `SCS-023`'s visibility clause lands in `CORE-008` | 9.1 | `docs/02-core-rules.md` |
| `TRN-019` absorbs the gap clause, drops the `SCS-005` citation | 10.1 | `docs/09-transport.md` |
| `WPN-005` retargeted from `SCS-003` to `VEH-001` | 11.1 | `docs/10-weapons.md` |
| `WPN-012` retargeted off `SCS-023` | 11.2 | `docs/10-weapons.md` |
| `DMG-008` retargeted off `SCS-024` | 12.1 | `docs/16-damage-system.md` |
| Glossary ***Facing*** entry retargeted off `SCS-004` | 13.1 | `docs/14-glossary.md` |
| `SCS-022`'s orientation sentence lands in `CMP-014` | 14.1 | `docs/05-construction-components.md` |
| `TODO.md` — the `DMG-008` quote | 15.1 | `TODO.md` |
| `TODO.md` — the *Energy shields* entry | 15.2 | `TODO.md` |

**Untouched, deliberately:** `SCS-002`, `SCS-006`, `SCS-013`, `SCS-016` and `SCS-017`, and the `# Purpose`, `# Design Philosophy`, `# Construction Principles` and `# Summary` sections of `docs/04-construction-standard.md`. **`SCS-010`, `SCS-011`, `SCS-012`, `CMP-009` and `CMP-010` were on this list and are now edited by section 18**, at the request of the review of #104 — the three terrain rules lose their `07-movement.md` sentence (`design.md`, Decision 13) and the two component rules stop restating the `1 AP` cost (`design.md`, Decision 8). `CMP-018`, which the same review calls overlong, stays out. `WPN-009`, which keeps the mounting rule `SCS-015` restated (`design.md`, Decision 4). Every archived change under `openspec/changes/archive/`. `openspec/specs/` — this change ships no delta (`design.md`, Decision 9). `CHANGELOG.md` and every `**Version:**` header.

---

## 1. `docs/04-construction-standard.md` — `SCS-001`

- [x] 1.1 Replace this anchor — the whole `SCS-001` rule, its trailing `---`, and the heading of the rule below it:

```
# SCS-001 — Unit Base (UB)

The fundamental measuring unit of StudCraft is the Unit Base — see `02-core-rules.md` (CORE-001) for its definition.

Its `4 × 3` stud footprint corresponds to the base of a LEGO minifigure.

Every measurement in the game is derived from this unit.

---

# SCS-002 — Infantry Base
```

with:

```
# SCS-002 — Infantry Base
```

  `SCS-002`'s heading is the landmark that ends the anchor; it stays in the file. `CORE-001` defines the Unit Base, its footprint and its use as the measuring unit for every measurement in the game.

---

## 2. `docs/04-construction-standard.md` — `SCS-003`, `SCS-004`, `SCS-005`

- [x] 2.1 Replace this anchor — three whole rules with their `---` rules, and the heading of the rule below them:

```
# SCS-003 — Vehicle Footprint

Vehicles are measured using Unit Bases — see `08-vehicles.md` (VEH-001) for the canonical footprint examples and the maximum size (none — the agreed Deployment Volume naturally limits model size).

---

# SCS-004 — Facing

Every model must have an obvious front, per the universal Facing rule (`02-core-rules.md`, CORE-002).

Models with ambiguous fronts are not legal.

---

# SCS-005 — Physical Volume

Only physical space exists.

If something physically fits:

It fits.

If it does not fit:

It cannot be used.

This applies to:

- passengers
- cargo
- vehicles
- buildings
- terrain

What must fit is measured in Unit Bases (`02-core-rules.md`, CORE-001): a minifigure needs one whole Unit Base, a vehicle its own volume in Unit Bases. A model that would slip into a gap smaller than its Unit Base does not fit there.

---

# SCS-006 — Interactive Elements
```

with:

```
# SCS-006 — Interactive Elements
```

  `SCS-006`'s heading is the landmark; it stays in the file. **Task 8.1 must be applied with this one** — it is where `SCS-004`'s legality sentence goes. `SCS-005`'s gap clause goes to `TRN-019` in task 10.1.

---

## 3. `docs/04-construction-standard.md` — `SCS-007`

- [x] 3.1 In `SCS-007`, replace this anchor. The bullet at the top is a landmark and is **not** an edit:

```
- may close physically

Opening and closing cost 1 AP each, per `02-core-rules.md` (CORE-007).

A decorative door cannot be used.
```

with:

```
- may close physically
```

  `CORE-007` owns the cost, which `SCS-006` already points at four lines above. `SCS-006` also states "Decoration alone has no gameplay effect."

---

## 4. `docs/04-construction-standard.md` — `SCS-008`

- [x] 4.1 In `SCS-008`, replace this anchor. The first line is a landmark and is **not** an edit:

```
A ramp must physically rotate or lower.

Lowering and raising cost 1 AP each, per `02-core-rules.md` (CORE-007).

Once deployed, it becomes valid terrain.
```

with:

```
A ramp must physically rotate or lower.
```

  `CORE-007` owns the cost. `07-movement.md` (MOVE-019) owns the terrain sentence: "A lowered ramp immediately becomes usable terrain and is a legal access point."

---

## 5. `docs/04-construction-standard.md` — `SCS-009`

- [x] 5.1 In `SCS-009`, replace this anchor. The first line is a landmark and is **not** an edit:

```
Transparent LEGO elements represent windows.

Windows allow visibility.

If a model can be seen through a window:

It may be targeted.

If the window is destroyed, remove the transparent element.

The opening remains.
```

with:

```
Transparent LEGO elements represent windows.
```

  The surviving line is the one `05-construction-components.md` (CMP-011) and `09-transport.md` (TRN-012) both cite `SCS-009` for. Visibility and firing positions are `CMP-011`; visibility as a physical check is `CORE-008`; removing a destroyed component is `16-damage-system.md` (DMG-006).

---

## 6. `docs/04-construction-standard.md` — `SCS-014`, `SCS-015`

- [x] 6.1 Replace this anchor — two whole rules with their `---` rules, and the heading of the rule below them:

```
# SCS-014 — Cargo Compartments

Transport capacity is determined exclusively by the interior volume.

Players may not declare extra capacity.

The model defines capacity.

---

# SCS-015 — Weapon Mounts

Weapons must be physically attached to the model.

Valid mounting points are defined in `10-weapons.md` (WPN-009).

Floating weapons are illegal.

---

# SCS-016 — Functional Weapons
```

with:

```
# SCS-016 — Functional Weapons
```

  `SCS-016`'s heading is the landmark; it stays in the file. `TRN-003` owns transport capacity, `06-deployment.md` (DEP-005) owns "Transport capacity is not purchased … The LEGO model is the source of truth", and `WPN-009` owns both of `SCS-015`'s sentences.

---

## 7. `docs/04-construction-standard.md` — `SCS-018` through `SCS-024`

- [x] 7.1 Replace this anchor — seven whole rules with their `---` rules, and the section heading below them. It is long; copy it whole:

```
# SCS-018 — Muzzle Placement Standard

Muzzles must be built on the Weapon Front — the single face from which the weapon may fire; not the rear, side, top, or bottom (`10-weapons.md`, WPN-019).

Muzzle adjacency rules (muzzles may be placed directly adjacent; only overlap is forbidden) are defined in `10-weapons.md` (WPN-007, WPN-020).

---

# SCS-019 — Weapon Length

Weapon length measurement is defined in `10-weapons.md` (WPN-003).

---

# SCS-020 — Weapon Size Limit

Weapon Capacity (the total mounted weapon length a platform may carry) is defined in `10-weapons.md` (WPN-004).

---

# SCS-021 — Equipment

Only visible equipment exists.

General equipment visibility requirements are defined in `02-core-rules.md` (CORE-014).

---

# SCS-022 — Shields

Shields must be physically carried and remain visible to function.

A shield facing the attacker may be selected as the component that protects whatever is positioned behind it (`16-damage-system.md`, DMG-007) — the same as any other interposed component. A shield facing away does not block anything. Shield orientation matters for this reason, not for any separate defensive bonus.

---

# SCS-023 — Transparency

Transparent LEGO pieces represent transparent materials.

Examples:

Glass

Energy shields (future)

Cockpit canopies

Visibility passes through transparent pieces.

Resistance and the Geometry Check (`16-damage-system.md`, DMG-003, DMG-014) determine whether they stop an Impact — the same as any other component.

---

# SCS-024 — Damage Representation

Whenever possible, damage is represented by changing the model.

Examples:

Broken window

Removed weapon

Destroyed door

Opened hatch

Destroyed wheel

Physical representation always takes priority over markers.

---

# Construction Principles
```

with:

```
# Construction Principles
```

  **This is one edit, not seven.** `# Construction Principles` is the landmark that ends the anchor; it stays in the file. The owners: `WPN-019` (`SCS-018`), `WPN-003` (`SCS-019`), `WPN-004` (`SCS-020`), `CORE-014` (`SCS-021`), `CMP-014` with `DMG-007` (`SCS-022`), `DMG-008` (`SCS-023`'s mechanical clause), `CORE-016` (`SCS-024`). **Tasks 9.1, 14.1 and 15.2 must be applied with this one** — 9.1 is where `SCS-023`'s visibility clause goes, 14.1 where `SCS-022`'s orientation sentence goes, and 15.2 removes the `TODO.md` entry that quotes `SCS-023`.

---

## 8. `docs/02-core-rules.md` — `CORE-002`

- [x] 8.1 In `CORE-002`, replace this anchor — the heading and the sentence below it:

```
## CORE-002 — Facing

Every unit has a facing.
```

with:

```
## CORE-002 — Facing

Every unit has a facing.

Every model must have an obvious front.
```

  This is an addition, not a deletion: `CORE-002` said every unit *has* a facing and never that the model must show it. The sentence is the one thing `SCS-004` stated that `CORE-002` did not, and task 2.1 removes it from `04-construction-standard.md`. It lands above `For infantry:`, which is where `CORE-002` starts settling *which* edge is the front. The `Facing determines:` list further down is not touched.

---

## 9. `docs/02-core-rules.md` — `CORE-008`

- [x] 9.1 In `CORE-008`, replace this anchor — the rule's last sentence:

```
This includes Visual Geometry (decoration, greebling, and similar) — see `15-geometry-layers.md` (GEO-004).
```

with:

```
This includes Visual Geometry (decoration, greebling, and similar) — see `15-geometry-layers.md` (GEO-004).

A transparent element does not block sight.
```

  An addition, and it goes **after** the Visual Geometry sentence rather than before it. "This includes Visual Geometry" refers back to the visibility test at the top of `CORE-008`; a sentence inserted between the two steals that antecedent and can be read as "Visual Geometry does not block sight", which is the reverse of `GEO-004`. The new sentence is the one clause of `SCS-023` no other rule states — `16-damage-system.md` (DMG-008) owns the rest, that a transparent component resolves an Impact exactly like any other, so the plastic stops the shot without stopping the sight line.

---

## 10. `docs/09-transport.md` — `TRN-019`

- [x] 10.1 In `TRN-019`, replace this anchor — the rule's first sentence:

```
What must fit inside a vehicle is the Unit Base itself rather than the loose model (`02-core-rules.md`, CORE-001; `04-construction-standard.md`, SCS-005).
```

with:

```
What must fit inside a vehicle is the Unit Base itself rather than the loose model, and a model that would slip into a gap smaller than its Unit Base does not fit there (`02-core-rules.md`, CORE-001).
```

  The added clause is the one thing `SCS-005` carried that `TRN-019` did not. The rest of the sentence, and the rest of `TRN-019`, is unchanged.

---

## 11. `docs/10-weapons.md` — `WPN-005`, `WPN-012`

- [x] 11.1 In `WPN-005`, replace this anchor:

```
Weapon Length is bounded by Platform Length (WPN-004), platform size by the agreed Deployment Volume (`04-construction-standard.md`, SCS-003; `06-deployment.md`, DEP-003), and the Deployment Volume by the battlefield the players agree on before it (`03-game-flow.md`, FLOW-001).
```

with:

```
Weapon Length is bounded by Platform Length (WPN-004), platform size by the agreed Deployment Volume (`08-vehicles.md`, VEH-001; `06-deployment.md`, DEP-003), and the Deployment Volume by the battlefield the players agree on before it (`03-game-flow.md`, FLOW-001).
```

  One citation changes: `SCS-003` becomes `VEH-001`, which states "No maximum vehicle size exists … the agreed Deployment Volume bounds it again". Nothing else in the sentence moves.

- [x] 11.2 In `WPN-012`, replace this anchor:

```
buildings, terrain and vehicles block it, and transparent elements follow the Transparency rule (`04-construction-standard.md`, SCS-023).
```

with:

```
buildings, terrain and vehicles block it, and transparent elements do not.
```

  `WPN-012` already cites `CORE-008` earlier in the same sentence, which is where task 9.1 puts the clause. No second citation is added.

---

## 12. `docs/16-damage-system.md` — `DMG-008`

- [x] 12.1 In `DMG-008`, replace this anchor:

```
per `02-core-rules.md` (CORE-016) and `04-construction-standard.md` (SCS-024) — this document does not prescribe it.
```

with:

```
per `02-core-rules.md` (CORE-016) — this document does not prescribe it.
```

  One of two citations for the same sentence is removed. `CORE-016` is the owner (`design.md`, Decision 7).

---

## 13. `docs/14-glossary.md` — ***Facing***

- [x] 13.1 In the ***Facing*** entry, replace this anchor:

```
Determines forward and rear movement, the left and right sides, front and rear firing arcs, and shield direction. See `02-core-rules.md`, CORE-002 and `04-construction-standard.md`, SCS-004.
```

with:

```
Determines forward and rear movement, the left and right sides, front and rear firing arcs, and shield direction. See `02-core-rules.md`, CORE-002.
```

  After task 8.1, `CORE-002` states both halves the entry used two citations for.

---

## 14. `docs/05-construction-components.md` — `CMP-014`

- [x] 14.1 In `CMP-014`, replace this anchor — the rule's last paragraph:

```
A shield provides no bonus beyond being a component in the way — its own Resistance (DMG-003) determines what it takes to get through it.
```

with:

```
A shield provides no bonus beyond being a component in the way — its own Resistance (DMG-003) determines what it takes to get through it.

A shield protects only what it stands between: one facing the attacker interposes, one facing away does not. This is the `Shield direction` that `02-core-rules.md` (CORE-002) determines.
```

  An addition. It is the one sentence `SCS-022` stated that no surviving rule states, and `CORE-002`'s `Facing determines:` list ends with `Shield direction` — a term nothing would explain once task 7.1 removes `SCS-022` (`design.md`, Decision 12). The `Requirements:` list above the anchor already covers carried, attached, visible and one-handed, and is not touched.

---

## 15. `TODO.md`

`TODO.md` records the gaps the ruleset declares in its own text, each quoting the rule that declares it. `scripts/check_todo_quotes.py` compares every quote character for character against the document it cites, and `scripts/preflight.py` runs it. Two entries quote text this change edits.

**The path is `TODO.md` at the repository root — not under `docs/`.**

- [x] 15.1 In `./TODO.md`, under the ***Cosmetic guidance for specific constructions*** heading, replace this anchor — the citation line and the blockquote below it. The `> ` prefix is real markdown, `TODO.md`'s own format, and must land in the file:

```
`DMG-008` (`docs/16-damage-system.md`):

> Physical/cosmetic representation of a component reaching Dead (how a broken window should look versus a destroyed wheel) is left entirely to the player and the table, per `02-core-rules.md` (CORE-016) and `04-construction-standard.md` (SCS-024) — this document does not prescribe it. Future supplements may add cosmetic guidance for specific constructions without changing any mechanic defined here.
```

with:

```
`DMG-008` (`docs/16-damage-system.md`):

> Physical/cosmetic representation of a component reaching Dead (how a broken window should look versus a destroyed wheel) is left entirely to the player and the table, per `02-core-rules.md` (CORE-016) — this document does not prescribe it. Future supplements may add cosmetic guidance for specific constructions without changing any mechanic defined here.
```

  The citation line is a landmark and is unchanged; only the blockquote loses its `SCS-024` citation.

  The quote must match `DMG-008` as task 12.1 leaves it. The gap itself does not close — `DMG-008` still declines to prescribe cosmetic representation — so the entry stays.

- [x] 15.2 In `./TODO.md`, delete one whole entry. **This is the only task in this file with no fenced anchor**, and the reason is mechanical: the entry contains a seven-line `> ` blockquote, and `scripts/check_task_anchors.py` reads any run of three or more `> ` lines in a `tasks.md` as replacement text written in the abandoned blockquote convention. Reproducing the entry here would fail that check on a proposal that is doing nothing wrong. The boundaries below are exact lines, each unique in the file.

  **Delete from** the line:

  `### Energy shields as a transparent-material example`

  **down to and including** the line beginning:

  `What would have to be decided: what construction and gameplay rules, if any, would distinguish an "energy shield"`

  together with the blank line that follows it — everything between those two lines goes, blockquote included.

  **Leave in place:** the `---` and the `## Combat` heading below the entry, and the ***Future weapon types*** entry above it, which quotes `WPN-017` and is unaffected. After the edit, the paragraph ending "since none of them currently has construction rules of its own." is followed by a blank line, then `---`, then `## Combat`.

  This entry is removed rather than re-sourced: its declaring text is `SCS-023`'s speculative example list, which task 7.1 deletes, and after that no document in the ruleset mentions an energy shield. `TODO.md`'s own preamble scopes the file to gaps the ruleset declares in its own text (`design.md`, Decision 11).

---

## 16. Verification

Run these after every edit above. Each is a bare command; none of them edits anything. Where a count is given, it is the count observed on the pre-change tree, so a mismatch means the edit did not land.

- [x] 16.1 `python3 scripts/preflight.py` passes. This runs `scripts/check_todo_quotes.py`, which fails if section 15 was skipped.

- [x] 16.2 `grep -n "^# SCS-" docs/04-construction-standard.md` lists exactly eleven headings, in this order: `SCS-002`, `SCS-006`, `SCS-007`, `SCS-008`, `SCS-009`, `SCS-010`, `SCS-011`, `SCS-012`, `SCS-013`, `SCS-016`, `SCS-017`. Any other count, or any heading renumbered to close a gap, is a defect.

- [x] 16.3 `grep -rn "SCS-0" docs/` returns **eighteen lines: the eleven surviving rule headings in `docs/04-construction-standard.md`, and seven citations from other documents.** Before this change the same command returned thirty-six — twenty-four lines in `docs/04-construction-standard.md` and twelve citations. The seven citations, each naming a rule this change keeps:

  | File | Cites |
  |---|---|
  | `docs/02-core-rules.md` (`CORE-001`) | `SCS-002` |
  | `docs/05-construction-components.md` (`CMP-011`) | `SCS-009` |
  | `docs/07-movement.md` (`MOVE-002`) | `SCS-002` |
  | `docs/08-vehicles.md` (`VEH-027`) | `SCS-011` and `SCS-008`, on one line |
  | `docs/09-transport.md` (`TRN-012`) | `SCS-009` |
  | `docs/14-glossary.md` (*Weapon Body*) | `SCS-017` |
  | `docs/14-glossary.md` (*Interactive Element*) | `SCS-006` |

  Read the output rather than counting it. What matters is that **no line names a retired ID** — `SCS-001`, `SCS-003`, `SCS-004`, `SCS-005`, `SCS-014`, `SCS-015`, or `SCS-018` through `SCS-024`. One that does is an edit that did not land; stop and report it.

- [x] 16.4 `python3 scripts/rule.py refs SCS-002 SCS-008 SCS-009 SCS-011 SCS-006 SCS-017` — six surviving rules. Four print a citer list; **`SCS-006` and `SCS-017` print "is cited by nothing", and that is correct** — their only citer is `docs/14-glossary.md`, which `rule.py` does not read (it walks the rule graph). Task 16.3 is what covers the glossary. Every citer printed must name a rule that still exists.

- [x] 16.5 `python3 scripts/check_id_stability.py` reports no renumbered and no reused ID. Thirteen retirements are expected and are not reported.

- [x] 16.6 `python3 scripts/lint_ruleset.py` passes — rule IDs ascend within the document, gaps and all, and the required sections are still present.

- [x] 16.7 `grep -rn "SCS-0" system/ README.md CODE_OF_DESIGN.md CONTRIBUTING.md AGENTS.md TODO.md` returns exactly one hit: `system/proposal-review.md`, citing `SCS-003`. **Do not fix it here** — it is recorded in `proposal.md` (Out of Scope) for its own branch (`design.md`, Decision 11). A hit in `TODO.md` means task 15.1 or task 15.2 was skipped — `TODO.md:124` is 15.2's, `TODO.md:182` is 15.1's. Any other hit is a reference this change missed; stop and report it.

The four checks below each confirm one addition landed. Deletions are visible in the diff; an addition that was skipped looks exactly like a change applied correctly, which is what these catch.

- [x] 16.8 `grep -c -F "Every model must have an obvious front." docs/02-core-rules.md` returns `1`. It returned `0` before task 8.1.

- [x] 16.9 `grep -c -F "A transparent element does not block sight." docs/02-core-rules.md` returns `1`. It returned `0` before task 9.1.

- [x] 16.10 `grep -c -F "a model that would slip into a gap smaller than its Unit Base does not fit there" docs/09-transport.md` returns `1`. It returned `0` before task 10.1.

- [x] 16.11 `grep -c -F "one facing the attacker interposes, one facing away does not" docs/05-construction-components.md` returns `1`. It returned `0` before task 14.1. **Superseded by task 17.1**, which rewrites that sentence; after section 17 this command returns `0` and 17.4 replaces it.

---

## 17. Repairs from the audit of the applied text

Sections 1–16 are the change as proposed. These three edits come from the audit of the result, and **their anchors are post-change text** — each names a sentence sections 8–14 put there. Apply them after section 16, not before.

- [x] 17.1 In `docs/05-construction-components.md`, `CMP-014`, replace this anchor — the sentence task 14.1 added:

```
A shield protects only what it stands between: one facing the attacker interposes, one facing away does not. This is the `Shield direction` that `02-core-rules.md` (CORE-002) determines.
```

with:

```
A shield protects only what it physically stands between: one interposed between the attacker and a component protects it, one facing away blocks nothing. Orientation matters for that reason, not for any separate defensive bonus.
```

  The second sentence of 14.1's version claimed `CORE-002` determines which way a shield protects. It does not, and the two tests disagree on a real model: a shield on a minifigure's left arm stands between a westward attacker and the torso while the unit's Facing, set by the 4-stud edge of its base, is north. The retired `SCS-022` never made that claim — it said orientation matters "for this reason, not for any separate defensive bonus", which is what this restores. Whether `CORE-002`'s `Shield direction` bullet is itself right is recorded in `proposal.md` (Out of Scope).

- [x] 17.2 In `docs/02-core-rules.md`, `CORE-008`, replace this anchor — the sentence task 9.1 added:

```
A transparent element does not block sight.
```

with:

```
A transparent element does not block sight. It stops an Impact only by its own Resistance, like any other component (`16-damage-system.md`, DMG-008).
```

  Without the second sentence, `WPN-012`'s "buildings, terrain and vehicles block it, and transparent elements do not" can be read as a shot ignoring glass. `DMG-008` owns the mechanical half and was cited by neither rule after task 11.2.

- [x] 17.3 In `docs/09-transport.md`, `TRN-019`, replace this anchor — the sentence task 10.1 left:

```
What must fit inside a vehicle is the Unit Base itself rather than the loose model, and a model that would slip into a gap smaller than its Unit Base does not fit there (`02-core-rules.md`, CORE-001).
```

with:

```
What must fit inside a vehicle is the Unit Base itself — see `02-core-rules.md` (CORE-001) for its dimensions — rather than the loose model, and a model that would slip into a gap smaller than its Unit Base does not fit there.
```

  A trailing `(CORE-001)` reads as sourcing the whole claim, and `CORE-001` no longer states anything about fitting — `TRN-019` owns that now. The citation moves to the clause it actually supports. `VEH-015` and `DEP-005` have the same shape and are recorded in `proposal.md` (Out of Scope); this repairs only the rule this change edited.

- [x] 17.4 `grep -c -F "one interposed between the attacker and a component protects it" docs/05-construction-components.md` returns `1`, and `grep -c -F "This is the \`Shield direction\`" docs/05-construction-components.md` returns `0`.

- [x] 17.5 `grep -c -F "It stops an Impact only by its own Resistance" docs/02-core-rules.md` returns `1`.

- [x] 17.6 `grep -c -F "see \`02-core-rules.md\` (CORE-001) for its dimensions" docs/09-transport.md` returns `1`.

- [x] 17.7 `python3 scripts/preflight.py` passes again, all 12 checks.

---

## 18. Review of pull request #104

Seven edits from the maintainer's review. Two of them close items this change had recorded as Out of Scope, at the reviewer's explicit request; `proposal.md` no longer lists them there. **Anchors here are post-change text where section 17 touched the file, and pre-change text everywhere else.** Two new documents join the change: `docs/06-deployment.md` and `docs/08-vehicles.md`.

### `docs/04-construction-standard.md` — the terrain rules lose their delegation sentence

Each of `SCS-010`, `SCS-011` and `SCS-012` ends by naming the document that owns its gameplay consequence. The reviewer's point: the rule states a construction requirement, `07-movement.md` owns what that construction does, and saying so inside the rule explains an ownership the rule already demonstrates. **Add no replacement sentence.**

- [x] 18.1 In `docs/04-construction-standard.md`, `SCS-010`, replace this anchor:

```
Walls must be physically built from LEGO elements.

How walls affect movement during a game is defined in `07-movement.md`.
```

with:

```
Walls must be physically built from LEGO elements.
```

- [x] 18.2 In `docs/04-construction-standard.md`, `SCS-011`, replace this anchor:

```
Slopes must be physically built from LEGO slope elements.

How slopes affect movement during a game is defined in `07-movement.md`.
```

with:

```
Slopes must be physically built from LEGO slope elements.
```

- [x] 18.3 In `docs/04-construction-standard.md`, `SCS-012`, replace this anchor:

```
Stairs must be physically built from LEGO plates or bricks.

How stairs affect movement during a game is defined in `07-movement.md`.
```

with:

```
Stairs must be physically built from LEGO plates or bricks.
```

  Each rule keeps its single sentence and its `---`. `VEH-027` cites `SCS-011` and `SCS-008` for their physical requirements, not for the deleted sentences, so nothing dangles.

### `docs/05-construction-components.md` — `CMP-009` and `CMP-010` stop restating the cost

`CORE-007` owns the generic interaction cost. `MOVE-018` and `MOVE-019` point at it without repeating the number; these two repeat it. The physical requirement stays in both rules — only the restated value goes.

- [x] 18.4 In `docs/05-construction-components.md`, `CMP-009`, replace this anchor. The bullet at the top is a landmark and is **not** an edit:

```
- Line of Sight

Opening or closing a door costs **1 Action Point** (see `02-core-rules.md`, CORE-007).
```

with:

```
- Line of Sight
```

- [x] 18.5 In `docs/05-construction-components.md`, `CMP-010`, replace this anchor. The first line is a landmark and is **not** an edit:

```
Ramps may serve as vehicle access points.

Lowering or raising a ramp costs **1 Action Point** (see `02-core-rules.md`, CORE-007).
```

with:

```
Ramps may serve as vehicle access points.
```

  No gameplay value changes: the cost is still `1 Action Point`, stated once, by `CORE-007`. Both rules keep "Must physically open and close" / "Must physically move".

### The stale `CORE-001` citations

`CORE-001` defines the Unit Base and no longer states anything about what must fit; `TRN-019` owns that. Both rules below cite `CORE-001` for the fit claim. **Do not restore any text to `CORE-001`** — the consumer citation moves.

- [x] 18.6 In `docs/08-vehicles.md`, `VEH-015`, replace this anchor:

```
Crew must physically fit inside the vehicle. A crew member occupies a Unit Base like any other passenger (`09-transport.md`, TRN-014), so what must fit is that Unit Base (`02-core-rules.md`, CORE-001).
```

with:

```
Crew must physically fit inside the vehicle. A crew member occupies a Unit Base like any other passenger (`09-transport.md`, TRN-014), so what must fit is that Unit Base (`09-transport.md`, TRN-019).
```

- [x] 18.7 In `docs/06-deployment.md`, `DEP-005`, replace this anchor:

```
If a Unit Base fits inside the vehicle, a minifigure may be transported in it (`02-core-rules.md`, CORE-001; `09-transport.md`, TRN-019).
```

with:

```
If a Unit Base fits inside the vehicle, a minifigure may be transported in it (`09-transport.md`, TRN-019).
```

  `DEP-005` already cited `TRN-019` alongside `CORE-001`; only the stale half goes.

### Verification

- [x] 18.8 `grep -c "07-movement.md" docs/04-construction-standard.md` returns `0`. It returned `3` before tasks 18.1 – 18.3.

- [x] 18.9 `grep -c "1 Action Point" docs/05-construction-components.md` returns `0`. It returned `2` before tasks 18.4 and 18.5.

- [x] 18.10 `grep -n "CORE-001" docs/06-deployment.md docs/08-vehicles.md` — no line claims `CORE-001` states what must fit. `VEH-001`, `VEH-021`, `VEH-028` and `DEP-001` cite it for the Unit Base as a measure, which is what it defines; those are untouched.

- [x] 18.11 `grep -n "^# SCS-" docs/04-construction-standard.md` still lists exactly the same eleven headings as task 16.2. No rule was removed or renumbered by this section.

- [x] 18.12 `python3 scripts/preflight.py` passes, all 12 checks.

---

## 19. `system/proposal-review.md` — the last citation of a retired rule

This is the one edit outside `docs/`, `TODO.md` and this change directory, and it is deliberate. `system/repository-strategy.md` (Branch Naming) describes a `<change-name>` branch as carrying `docs/*.md` plus its own change, so this needs saying rather than assuming: **no gate refuses it.** `Branch name follows the convention` only requires that a branch touching `docs/` is named for its single change; `Docs require OpenSpec proposal` only that the proposal exists and is complete; `Docs must not edit CHANGELOG.md directly` and `OpenSpec archive must be separate from apply` are about other paths entirely. The `PreToolUse` hook gates `CHANGELOG.md`, `docs/*.md` and `**Version:**` headers, and `system/` is none of them.

It was recorded Out of Scope while pull request #104 was being written, on the reasoning that nothing checks `system/` against `docs/`. That is still true, and it is the argument for fixing it here rather than later: a stale citation nothing checks is one nobody will notice, and the pull request that retires the rule is the last moment the connection is obvious.

- [x] 19.1 In `system/proposal-review.md`, under "Do Not Cap What the Model Already Bounds", replace this anchor — three lines inside a fenced block. **The fenced block itself stays; only these three lines are the anchor**, and their leading spaces are part of the text:

```
Range ≤ 6 × Weapon Length ≤ 6 × Platform Length (WPN-004)
      ≤ what fits the Deployment Volume (SCS-003, DEP-003)
      ≤ the battlefield agreed first (FLOW-001, step 2)
```

with:

```
Range ≤ 6 × Weapon Length ≤ 6 × Platform Length (WPN-004)
      ≤ what fits the Deployment Volume (VEH-001, DEP-003)
      ≤ the battlefield agreed first (FLOW-001, step 2)
```

  One identifier changes. `SCS-003` was retired by task 2.1, and `WPN-005` — the rule this chain paraphrases — was retargeted to `VEH-001` by task 11.1, which states "No maximum vehicle size exists … the agreed Deployment Volume bounds it again". The first and third lines are landmarks and are unchanged.

- [x] 19.2 `grep -rn "SCS-0" system/ README.md CODE_OF_DESIGN.md CONTRIBUTING.md AGENTS.md TODO.md` returns **nothing**. Task 16.7 expected one hit; this section removes it, and 16.7 is superseded.

- [x] 19.3 `grep -c -F "(VEH-001, DEP-003)" system/proposal-review.md` returns `1`.

- [x] 19.4 `python3 scripts/preflight.py` passes, all 12 checks.
