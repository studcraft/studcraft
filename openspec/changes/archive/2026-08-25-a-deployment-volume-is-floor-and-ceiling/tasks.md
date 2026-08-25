# Tasks — A Deployment Volume's floor is counted, not packed

## How to apply this change

Every anchor below was checked with exact-substring matching against the
pre-change files and occurs **exactly once in the file its task names**.
Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than
guessing which occurrence was meant. Never edit a document to make a
verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is
not part of the text** — do not write the backticks into the document.

### This file was revised after its audit

Eleven findings, two of them blockers, **all folded into the tasks below rather
than added as a repair section** — nothing had been applied yet. What the audit
found, beyond the two broken verification commands:

- **`DEP-003` was declared untouched, against #81's own record.** #81 wrote that
  settling this question is "a mechanical change to `DEP-002` **and
  `DEP-003`**". `DEP-003` still closes "This area is unavailable for any other
  model" — the last exclusion-of-space sentence in the chapter, in the rule this
  change nominates as the one that was always right. Task 1.4.
- **`DEP-002` was losing its only link to `DEP-001`.** The rule that states the
  arithmetic never said where the floor comes from. Task 1.2 now cites it.
- **The worked example named a vehicle the footprint table does not.** `VEH-001`
  calls it a **Bike**; "motorcycle" appears only in `09-transport.md`. Task 1.3
  uses the ruleset's own row and cites it.
- **"No vehicle of any kind can be fielded in a Patrol game" was overstated.**
  `VEH-028` allows two Unit Bases side by side (`2 × 1 UB`), which is one deep
  and fits a `5 × 1` floor under either reading. #81's own qualifier — "no
  vehicle **deeper than one Unit Base**" — is restored in `proposal.md` and
  `design.md`.

### The three things this change must not do

**No rule ID is retired or renumbered.** `DEP-001` through `DEP-009` all keep
their numbers, and nothing is deleted.

**The ceiling is not reopened.** `H` is agreed in whole Unit Bases, compared
against each model's own height, and charged nothing. #81 settled that. If a
replacement block would change what the ceiling does, it is wrong — stop and
report it.

**No footprint or cost changes.** A Bike is `1 × 2 UB` and spends 2; a Tank is
`2 × 5 UB` and spends 10; an infantry model spends 1. This change states how
those are added up, and moves none of them.

- [x] 0.1 The branch is `a-deployment-volume-is-floor-and-ceiling`, named for
  this change directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Two ruleset documents and **one capability delta**: five anchor pairs, plus a
`MODIFIED` requirement against `unit-base` written directly into
`specs/unit-base/spec.md` rather than as an anchor pair.

**That delta is superseded and has moved.** `general-review` (#130) modified the
same requirement afterwards and is the later change, so it carries the
authoritative version (`system/workflow.md`, "When several changes modified the
same requirement"). This change's delta now lives at
`specs-superseded/unit-base/spec.md`, with a header saying why, and this change
carries no live delta.

**Every `specs/unit-base/spec.md` path below is the record of where it was
written and verified, not a path that still resolves.**

| `proposal.md` item | Task | Path |
|---|---|---|
| `DEP-001` — `W × D` yields a count | 1.1 | `docs/06-deployment.md` |
| `DEP-002` — the arithmetic, not "fits inside" | 1.2 | `docs/06-deployment.md` |
| `DEP-002`'s examples — replaced | 1.3 | `docs/06-deployment.md` |
| `DEP-003` — the last exclusion-of-space sentence | 1.4 | `docs/06-deployment.md` |
| Glossary ***Deployment Volume*** entry | 2.1 | `docs/14-glossary.md` |
| `unit-base` — one `MODIFIED` requirement | 3.1 | `specs/unit-base/spec.md` |

**Untouched, deliberately:** `DEP-003`'s cost arithmetic and its double height
bound, which are what the rest is being made to agree with — only its closing
sentence changes. `DEP-004`, `DEP-005`. **`DEP-006`**, whose "one Unit Base for
an infantry model (DEP-004), its own footprint for a vehicle (DEP-003)" says
something local about externally carried models; task 1.2 deliberately does
**not** repeat that list in `DEP-002`, so this change creates no second copy.
`DEP-007`, `DEP-008` and `DEP-009`, which are known findings that **wait for
this answer rather than ship with it** — `design.md`, Decision 5. The Design
Philosophy section, the Design Notes and the document Summary, all three of
which already read as a budget. `docs/01-foundations.md:85`, checked and clean.
`CHANGELOG.md` and every version header.

---

## 1. `docs/06-deployment.md`

- [x] 1.1 In `docs/06-deployment.md`, `DEP-001`, replace this anchor — the rule's second paragraph:

```
A Deployment Volume is measured in **Unit Bases (UB)** — see `02-core-rules.md` (CORE-001) for the Unit Base definition — and is written `W × D × H`: a floor `W × D`, and the height `H` every model in a player's army must fit under.
```

with:

```
A Deployment Volume is measured in **Unit Bases (UB)** — see `02-core-rules.md` (CORE-001) for the Unit Base definition — and is written `W × D × H`. **The floor is `W × D` Unit Bases, counted**: a `5 × 1` floor and a `1 × 5` floor are the same five, and neither is a shape a model has to fit within. `H` is the height every model in a player's army must fit under.
```

  **The notation stays and now says what it yields.** Two numbers tell players the scale of the game they are agreeing to, which one number would not — `5 × 5` reads differently from `25 × 1`. What was missing is that their product is a count (`design.md`, Decision 2). The sentence about `H` is unchanged in substance and moved to its own clause so the floor and the ceiling stop sharing one.


- [x] 1.2 In `docs/06-deployment.md`, `DEP-002`, replace this anchor — the rule's first line:

```
A player's army may occupy any combination of models that fits inside the agreed Deployment Volume — on its floor and under its ceiling. An infantry model's height is its Unit Base, weapons and equipment included (`02-core-rules.md`, CORE-001; `09-transport.md`, TRN-002). A vehicle's is what `08-vehicles.md`, VEH-028 measures: from the surface it rests on to the top of its Gameplay Geometry.
```

with:

```
Each model spends the Unit Bases of its footprint, and a player's army is any combination whose total does not exceed the agreed floor (DEP-001). Every model must also stand under the ceiling: an infantry model's height is its Unit Base, weapons and equipment included (`02-core-rules.md`, CORE-001; `09-transport.md`, TRN-002), and a vehicle's is what `08-vehicles.md`, VEH-028 measures — from the surface it rests on to the top of its Gameplay Geometry.
```

  **"Any combination of models that fits inside" was the packing reading**, and it sat forty lines from `DEP-003`'s "Deployment cost: 10 Unit Bases", which is the budget one. The two are now the same rule.

  **The floor is cited to `DEP-001`** — the rule that states the whole arithmetic has to say where the quantity being spent comes from. And what a model spends is deliberately **not** re-listed here: `DEP-003` and `DEP-004` state it, `DEP-006` already repeats it for externally carried models, and a third copy is the failure class this change is an instance of.


- [x] 1.3 In `docs/06-deployment.md`, `DEP-002`, replace this anchor — the whole example block, from "Examples:" through the line closing it. The "No additional points system exists." line above is **not** part of the anchor and stays:

```
Examples:

A 5 × 5 × 4 UB Deployment Volume could contain:

- 25 infantry.

or

- 1 large tank.

or

- 2 medium vehicles.

or

- 1 transport carrying infantry.

Any legal combination is allowed provided it fits, read that way.
```

with:

```
Example:

A `5 × 5 × 4 UB` Deployment Volume gives a floor of **25 Unit Bases** and a ceiling of 4. Against that floor:

- 25 infantry, at one Unit Base each (DEP-004), spend all 25.
- Two Tanks of `2 × 5 UB` (`08-vehicles.md`, VEH-001) spend 10 each (DEP-003), leaving 5 for infantry.

A smaller game works the same way. A `5 × 1 × 2 UB` volume gives a floor of 5 Unit Bases: a Bike of `1 × 2 UB` (`08-vehicles.md`, VEH-001) spends 2 and leaves 3, and its own maximum height is 2 Unit Bases (`08-vehicles.md`, VEH-028) — exactly the ceiling agreed, so it is legal on both bounds.

Any combination is legal whose footprints total no more than the floor and whose models all stand under the ceiling.
```

  **Every line after the first was wrong under a budget.** Twenty-five Unit Bases do not buy *one* large tank — `VEH-001` lists a Tank at `2 × 5 UB`, so they buy two and five infantry besides. "2 medium vehicles" names no footprint and cannot be checked. And the **or** framing implied each line exhausted the volume, which is the packing reading arriving through the back door.

  **The second volume gets its own lead-in**, because three bullets under one "25 Unit Bases" line would have a reader checking the third against 25. Every figure is cited to the rule that states it, and the vehicles are named as `VEH-001`'s own table names them — **Bike** and **Tank**, not "motorcycle", which appears only in `09-transport.md`.


- [x] 1.4 In `docs/06-deployment.md`, `DEP-003`, replace this anchor — one line:

```
This area is unavailable for any other model.
```

with:

```
Those Unit Bases are spent, and cannot be spent again.
```

  **#81 recorded that settling this question is "a mechanical change to `DEP-002` and `DEP-003`", and this is `DEP-003`'s half.** Everything else in the rule is already a budget — it states a cost as a number — but this sentence is the last exclusion-of-space language in the chapter, sitting in the rule the rest is being made to agree with. "Unavailable" describes a region; "spent" describes a count.


---

## 2. `docs/14-glossary.md`

- [x] 2.1 In `docs/14-glossary.md`, the `## Deployment Volume` entry, replace this anchor — the entry's body:

```
The battlefield space a player's army must fit inside, agreed before the game and measured in Unit Bases: a floor `W × D` and a ceiling `H`. See `06-deployment.md` (DEP-001).
```

with:

```
The limit on a player's army, agreed before the game and measured in Unit Bases: a floor of `W × D` Unit Bases to spend, and a ceiling `H` every model must stand under. See `06-deployment.md` (DEP-001).
```

  `system/proposal-review.md` ("The Summary Is Part of the Rule") — a glossary entry is a restatement and is checked in the same pass as the rule. "The battlefield space a player's army must fit inside" is the packing reading, in the one place a reader goes to look the term up.


---

## 3. The capability delta

- [x] 3.1 `openspec/changes/a-deployment-volume-is-floor-and-ceiling/specs/unit-base/spec.md` is written and holds one `## MODIFIED Requirements` block for **Unit Base Projections**.

  The requirement's middle clause read "the volume itself for transport capacity, interior space, and **the Deployment Volume a model must fit inside**". It now reads "…and **the model height checked against the agreed ceiling**". Nothing else in the sentence changes.

  **All four scenarios are reproduced unchanged.** `scripts/check_delta_coverage.py` fails a `MODIFIED` block that drops a scenario the living spec has, and none of the four is affected: one already says a vehicle's cost "is read from the horizontal projection … and its height is charged nothing", which is the budget reading this change makes the rest agree with.

  **This capability carried both readings, exactly as `docs/` did** — `design.md`, Decision 4.

---

## 4. Verification

Run each command and write down what it actually returned. If a figure differs
from the one stated here, **stop and report it** — do not edit a document to
make it match. Every figure below was produced by running the command.

- [x] 4.1 `grep -rn -F "fits inside" docs/` — before: **two hits**, `DEP-002` and `DEP-005`. After: **one**, `DEP-005`'s "If a Unit Base fits inside the vehicle", which is a physical check on a model and is correct as it stands.

- [x] 4.2 `grep -rn -F "must fit inside" docs/` — before: **two hits**, `09-transport.md:330` (TRN-019) and the glossary entry. After: **one**, `09-transport.md:330`, which asks whether a Unit Base physically fits inside a vehicle and is a different question entirely. **A zero here means task 2.1 went further than it should have.**

- [x] 4.3 `grep -c -F "must fit inside" openspec/changes/a-deployment-volume-is-floor-and-ceiling/specs/unit-base/spec.md` — **0**. The delta is the corrected text; `openspec/specs/unit-base/spec.md` still carries the old wording until the change is archived, and that is expected.

- [x] 4.4 `grep -c -F "10 Unit Bases." docs/06-deployment.md` — **1**, before and after. `DEP-003`'s cost arithmetic is untouched; only its closing sentence changes. **The string is on its own line** — "Deployment cost:" sits two lines above it.

- [x] 4.5 `grep -c -F "This area is unavailable" docs/06-deployment.md` — before: **1**, after: **0**. Task 1.4.

- [x] 4.6 `python3 scripts/check_delta_coverage.py` — must **exit 0**. This is what confirms the `MODIFIED` block drops none of the four scenarios.

- [x] 4.7 `python3 scripts/lint_ruleset.py` — before: `Checked 15 docs, no structural issues found.` After: the same line.

- [x] 4.8 `python3 scripts/check_id_stability.py` — must **exit 0** and report **194** rule IDs, none renumbered or reused, and **no** `retired` count. Nothing is deleted here.

- [x] 4.9 `python3 scripts/rule.py refs DEP-001` — gains `DEP-002`, task 1.2. Before: `FLOW-001`, `FLOW-013`, `DEP-003`, `VEH-001`, `VEH-028`. After: those five plus `DEP-002`.

- [x] 4.10 `python3 scripts/check_task_anchors.py a-deployment-volume-is-floor-and-ceiling` — must **exit 0**.

- [x] 4.11 `python3 scripts/preflight.py` — **all 12 checks PASS.** `openspec validate` now has a delta to read; a failure there is about the delta's shape, not about `docs/`.

- [x] 4.12 `git status --short` — **two modified files**, `docs/06-deployment.md` and `docs/14-glossary.md`, plus the untracked change directory as a single `??` entry. Anything else is a mismatch: report it and stage nothing.
