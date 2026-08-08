# Tasks — Infantry occupies a Unit Base rather than being mounted on one

## 0. Setup

- [x] 0.1 Work on branch `infantry-occupies-a-unit-base` (`openspec/config.yaml` requires one branch per proposal, and `system/repository-strategy.md` requires the branch to be named for the change).

### How to read the replacement blocks

Every anchor and every replacement is given inside a fenced block. The fence is not
part of the text. Inline backticks, em dashes (`—`) and `×` are part of the text —
write them exactly.

Every replacement is a single paragraph replacing a single paragraph. No task adds a
paragraph, removes one, or touches a blank line.

### Anchors

Every anchor was checked with `grep -rcF` against the pre-change `docs/` and occurs
exactly **once**, in exactly one file. If an anchor returns anything other than 1,
**stop and report it** rather than guessing which occurrence was meant.

Never change, remove or renumber a heading. No heading is edited by any task below.

### Citation form

Citations **added** below use the comma form — `` `04-construction-standard.md`, SCS-002 ``.
Task 2.1 keeps the parenthesised form it already had; that one is retained text, not
an addition.

This is not cosmetic. `scripts/lint_ruleset.py` pairs a filename with **any**
parenthesised rule ID that follows it within 80 characters, and resolves the ID
against that file. The pattern is one-directional — an ID *before* a filename is
never paired — so the hazard is a backticked filename followed closely by a
parenthesised ID. `` `07-movement.md` … (SCS-002) `` in one paragraph makes
the linter look for `SCS-002` in `07-movement.md` and fail the build. A parenthesised
ID whose prefix belongs to the *host* document is rescued by #76's owner fallback,
which is why task 1.1's trailing `(CORE-002)` is safe inside `02-core-rules.md` — but
that is luck, not a rule. Do not convert any added citation to the parenthesised
form, and do not introduce a parenthesised foreign-prefix ID near a filename.

### Scope and coverage

Three ruleset documents change, ten anchors. Every item in `proposal.md`'s
What Changes maps to a task here, and no task adds material `proposal.md` does not
describe.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-001` stops calling the volume the standard base | 1.1 | `docs/02-core-rules.md` |
| `CORE-003` stops restating the mounting requirement | 1.2 | `docs/02-core-rules.md` |
| `SCS-001` defers without quoting figures | 2.1, 2.2 | `docs/04-construction-standard.md` |
| `SCS-002` says what is required, stops naming the edge | 2.3, 2.4 | `docs/04-construction-standard.md` |
| `MOVE-002` cites instead of restating | 3.1, 3.2, 3.3 | `docs/07-movement.md` |
| `MOVE-004` stops asking a player to lay a volume down | 3.4 | `docs/07-movement.md` |

`CORE-003` keeps only "Infantry occupy one Unit Base", unedited. The base is mentioned
in `CORE-001` (task 1.1) and used by `CORE-002`, whose bare "the base" takes `CORE-001`
as its antecedent once task 1.2 removes `CORE-003`'s — which is why task 1.1's clause
is load-bearing beyond `CORE-001` itself (`design.md`, Decision 2).

`CHANGELOG.md`, every `**Version:**` header and `openspec/specs/` are untouched
(`system/documentation-standards.md`, Versioning; `system/workflow.md`, Archiving).
No spec delta is written — `design.md`, "Why no spec delta".

---

## 1. `docs/02-core-rules.md` — `CORE-001` and `CORE-003`

- [x] 1.1 In `CORE-001`, replace this anchor:

```
This is the standard base for infantry. The 4-stud edge is the front (CORE-002).
```

with:

```
Read horizontally, this is the size of the physical base an infantry model is built on — required by `04-construction-standard.md`, SCS-002. The 4-stud edge is the front (CORE-002).
```

The qualifier is load-bearing: the base measures 4 × 3 studs, not 4 × 3 × 12. Without
"read horizontally" this sentence asserts that a volume is a plate, which is the
conflation this change exists to remove.

- [x] 1.2 In `CORE-003`, replace this anchor:

```
Infantry are represented by LEGO minifigures mounted on a standard Unit Base.
```

with:

```
Infantry are represented by LEGO minifigures.
```

**`CORE-003`'s second sentence — "Infantry occupy one Unit Base." — is not edited.**
Occupancy is what `CORE-003` owns, and the base is mentioned in `CORE-001` already
(`design.md`, Decision 2). Do not add a pointer to `SCS-002` here.

---

## 2. `docs/04-construction-standard.md` — `SCS-001` and `SCS-002`

- [x] 2.1 In `SCS-001`, replace this anchor:

```
The fundamental building unit of StudCraft is the Unit Base — see `02-core-rules.md` (CORE-001) for its definition (4 × 3 studs).
```

with:

```
The fundamental building unit of StudCraft is the Unit Base — see `02-core-rules.md` (CORE-001) for its definition, where its height comes from, and which projection each rule reads.
```

- [x] 2.2 In `SCS-001`, replace this anchor:

```
This corresponds to the footprint of a LEGO minifigure.
```

with:

```
Its horizontal projection corresponds to the footprint of a LEGO minifigure.
```

- [x] 2.3 In `SCS-002`, replace this anchor:

```
Every infantry model must be mounted on one Unit Base (`02-core-rules.md`, CORE-001 — 4 × 3 studs).
```

with:

```
Every infantry model must be built on one physical base measuring 4 × 3 studs — one Unit Base read horizontally (`02-core-rules.md`, CORE-001).
```

- [x] 2.4 In `SCS-002`, replace this anchor:

```
The 4-stud edge defines the front of the unit.
```

with:

```
Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).
```

---

## 3. `docs/07-movement.md` — `MOVE-002` and `MOVE-004`

- [x] 3.1 In `MOVE-002`, replace this anchor:

```
All infantry are mounted on a standard Unit Base (UB) — see `02-core-rules.md` (CORE-001) for the definition (4 × 3 studs).
```

with:

```
Every infantry model is built on the base required by `04-construction-standard.md`, SCS-002.
```

No size is stated here. `SCS-002` gives it, and repeating it would be the third copy.

- [x] 3.2 In `MOVE-002`, replace this anchor:

```
The 4-stud edge is always considered the front.
```

with:

```
Which edge of that base is its front is settled by the universal Facing rule (`02-core-rules.md`, CORE-002).
```

- [x] 3.3 In `MOVE-002`, replace this anchor:

```
This orientation defines movement and line of advance.
```

with:

```
The base's orientation defines movement and line of advance.
```

This sentence is `MOVE-002`'s own and its content does not change. Only the pronoun
does: task 3.2 stops naming the front edge, so "This orientation" would point at an
orientation this rule no longer states.

- [x] 3.4 In `MOVE-004`, replace this anchor:

```
The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (MOVE-005). Both numbers come from the base itself, so a player can measure either by laying spare Unit Bases end to end.
```

with:

```
The step size is the Unit Base's depth (`02-core-rules.md`, CORE-001): moving forward crosses the 3-stud axis, so forward movement counts whole base-depths, exactly as side movement counts whole base-widths of 4 (MOVE-005). Both numbers come from the base itself, so a player can measure either by laying spare infantry bases end to end.
```

One word changes, `Unit` to `infantry`. #73 left this sentence alone because
`CORE-001` still identified the 4 × 3 plate with the standard base; task 1.1 removes
that identification, and a volume cannot be laid end to end. The physical thing a
player lays down is `SCS-002`'s infantry base.

---

## 4. Verify

Run each of these from the repository root. Every expected number below was measured
against the pre-change text; where a "before" value is given, it was observed, not
reasoned.

- [x] 4.1 `python3 scripts/lint_ruleset.py` → `Checked 15 docs, no structural issues found.` This is the check the Citation form note protects; a failure naming a rule ID against the wrong document means a citation was written in the parenthesised form.
- [x] 4.2 `grep -rcE '^#{1,2} [A-Z]{3,4}-[0-9]{3} ' docs/ | awk -F: '{s+=$2} END {print s}'` → **225**, the same as before. No rule is added, removed or renumbered.
- [x] 4.3 `grep -rnF 'mounted on a standard Unit Base' docs/` → no hits (**2** before: `CORE-003`, `MOVE-002`).
- [x] 4.4 `grep -rnF 'must be mounted on one Unit Base' docs/` → no hits (**1** before: `SCS-002`).
- [x] 4.5 `grep -rnF 'This is the standard base for infantry.' docs/` → no hits (**1** before: `CORE-001`).
- [x] 4.6 `grep -rnF 'laying spare Unit Bases end to end' docs/` → no hits (**1** before: `MOVE-004`).
- [x] 4.7 `grep -rnF 'This orientation defines' docs/` → no hits (**1** before: `MOVE-002`).
- [x] 4.8 `grep -rn 'definition (4 × 3 studs)' docs/` → exactly **2** hits, **4** before: `docs/06-deployment.md` (`DEP-001`) and `docs/08-vehicles.md` (`VEH-001`). Both are deliberately kept — `design.md`, Decision 3. `docs/04-construction-standard.md` and `docs/07-movement.md` must not appear.
- [x] 4.9 `grep -rin 'horizontal projection' docs/` → exactly **3** hits, **2** before: `docs/02-core-rules.md` (`CORE-001`'s projection table), `docs/10-weapons.md` (`WPN-004`, pre-existing and untouched) and `docs/04-construction-standard.md` (`SCS-001`, task 2.2). `06-deployment.md` and `08-vehicles.md` must **not** appear: naming the reading in either would restate `CORE-001`'s table in two more documents (`design.md`, Decision 3). `07-movement.md` must not appear for a different reason — `MOVE-002` states no size at all, so it has no reading to name.
- [x] 4.10 `grep -rnF '4-stud edge' docs/` → exactly **3** hits, **5** before: `docs/02-core-rules.md` twice (`CORE-001`'s front-edge sentence, kept by task 1.1, and its vertical-projection sentence) and `docs/05-construction-components.md` once (`CMP-018`, pre-existing and out of scope). `SCS-002` and `MOVE-002` must not appear.
- [x] 4.11 `grep -ro '4 × 3' docs/ | wc -l` → **10**, **12** before. The two removed are `SCS-001`'s and `MOVE-002`'s pointer parentheticals. No other figure moves.
- [x] 4.12 `git status --short` and `git diff --stat` → exactly the three documents under **Scope** modified, plus `openspec/changes/infantry-occupies-a-unit-base/` as the only untracked path. `CHANGELOG.md`, every `**Version:**` header and `openspec/specs/` must be absent. Run against the working tree, because the applier makes no commit; after the commit, `git diff --stat main...HEAD` must show the same six files.
- [x] 4.13 Confirm no numeric value changed anywhere in `docs/`: every Action Point cost, every movement distance, every footprint example and every plate-layer figure is as it was. `MOVE-004`'s 12, 3, 6, 9 and 4 are untouched by task 3.4, which changes one word.

---

## 5. Verify only — make no edit

- [x] 5.1 `CORE-001`'s floor-plate sentence — "Height is measured from the top face of the plate an infantry model stands on" — is untouched. #73 put it there deliberately and it is out of scope (`proposal.md`).
- [x] 5.2 `CORE-002`, `CORE-004` and `SCS-004` are untouched. `SCS-004` is cited by no task: it defers to `CORE-002` and names no edge (`design.md`, Decision 2).
- [x] 5.3 `SCS-003` is untouched, its "size ceiling (none)" clause included (`proposal.md`, Out of Scope).
- [x] 5.4 `MOVE-003`, `MOVE-005` and `MOVE-006` are untouched, and no step size is stated by the new `MOVE-002` text. Only `MOVE-004`'s one word changes, in task 3.4.
- [x] 5.5 `DEP-001` and `VEH-001` are untouched, pointers included (`design.md`, Decision 3).
- [x] 5.6 `CMP-018`, `DEP-004`, `TRN-002` and `TRN-014` are untouched. Each reads occupancy, which `CORE-003` still states.
- [x] 5.7 `docs/14-glossary.md` and `docs/01-foundations.md` are untouched.
- [x] 5.8 No `openspec/specs/` file and no spec delta is written (`design.md`, "Why no spec delta").
- [x] 5.9 `SCS-002`'s requirement is not removed, weakened or made optional. The external review that asked for that is answered in `design.md`, "Rejected".
