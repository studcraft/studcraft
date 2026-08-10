# Tasks — No Action Point cost scales with size

## How to apply this change

Every anchor below was checked with exact-substring matching against the pre-change file
and occurs **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing
which occurrence was meant. Never edit a document to make a verification command pass —
report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part
of the text** — do not write the backticks into the document.

Task 3.1's block is markdown that must land as markdown: `## ADDED Requirements`,
`### Requirement:` and `#### Scenario:` are headings in the file it creates, not quoted
text, and the `- **WHEN**` / `- **THEN**` lines are list items.

No heading is edited by any task, no rule is added, removed or renumbered, and no rule ID
changes.

- [x] 0.1 The branch is `no-action-point-cost-scales-with-size`, named for this change
  directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Two ruleset documents and one spec delta: **six edits and nine non-edit tasks** (0.1 and
4.1 – 4.8), before the repairs recorded in section 5.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-006` states the rule | 1.1 | `docs/02-core-rules.md` |
| `TRN-005` — embarking costs 1 AP | 2.1 | `docs/09-transport.md` |
| `TRN-006` — disembarking costs 1 AP | 2.2 | `docs/09-transport.md` |
| `TRN-002`'s citation of `TRN-005` | 2.3 | `docs/09-transport.md` |
| The transport Summary, points 5 and 6 | 2.4 | `docs/09-transport.md` |
| The `action-economy` spec delta | 3.1 | this change's `specs/` |

**Untouched, deliberately:** `FLOW-005` and `FLOW-006` (the allotment, and "each action's
AP cost is defined in its corresponding rule document" — still true); `MOVE-008`,
`MOVE-009` – `MOVE-011` and `VEH-008` – `VEH-011` (rotation and climbing, neither of
which scales with size); `CORE-007`, `SCS-007`, `SCS-008`, `TRN-008`, `CBT-001`,
`DMG-019`, `12-melee.md` (already flat); `TRN-005`'s requirements list; `TRN-019`,
`DEP-005`; `CHANGELOG.md`, every `**Version:**` header and `openspec/specs/`.

---

## 1. `docs/02-core-rules.md` — `CORE-006`

- [x] 1.1 Replace this anchor — the closing paragraph of `CORE-006`:

```
Every unit receives exactly **3 Action Points** per activation, regardless of its type or construction. No unit gains additional AP through its profile.
```

with:

```
Every unit receives exactly **3 Action Points** per activation, regardless of its type or construction. No unit gains additional AP through its profile.

**No Action Point cost scales with size.** Not with the size of the unit paying it: an infantry model and a walker pay the same to embark (`09-transport.md`, TRN-005). Not with the size of what the action acts on: opening a hatch and opening a cargo ramp cost the same (CORE-007), and climbing an obstacle of 4 plate layers costs what climbing one of 6 costs (`07-movement.md`, MOVE-010). The allotment above is fixed, so a price that grew with the model would put a large enough model beyond acting at all — forbidden by arithmetic rather than by a rule, which is not how this ruleset forbids anything. Where a rule charges more than one Action Point, the reason is stated in that rule and is never size: `11-combat.md` (CBT-001) charges per weapon system attacking, `08-vehicles.md` (VEH-008) per 90° turn, and MOVE-010 charges a climb on top of the move that crosses the obstacle.
```

---

## 2. `docs/09-transport.md` — `TRN-005`, `TRN-006`, `TRN-002` and the Summary

- [x] 2.1 In `TRN-005`, replace this anchor:

```
Embarking costs **1 Action Point per Unit Base** the embarking unit occupies — an infantry model (1 UB) costs 1 AP; a motorcycle (2 UB) costs 2 AP, matching Disembarking (TRN-006).
```

with:

```
Embarking costs **1 Action Point**, whatever the unit occupies — an infantry model of one Unit Base and a motorcycle of two pay the same, matching Disembarking (TRN-006). No Action Point cost scales with size (`02-core-rules.md`, CORE-006).
```

- [x] 2.2 In `TRN-006`, replace this anchor — the cost statement and the example below
  it:

```
Disembarking costs:

**1 Action Point per Unit Base**

An infantry model (1 UB) therefore costs:

**1 AP**
```

with:

```
Disembarking costs:

**1 Action Point**

The cost is the same whatever the unit occupies, matching Embarking (TRN-005). No Action Point cost scales with size (`02-core-rules.md`, CORE-006).
```

- [x] 2.3 In `TRN-002`, replace this anchor — one sentence:

```
The space was paid for on embarking (TRN-005).
```

with:

```
The space is claimed on embarking (TRN-005).
```

- [x] 2.4 In the Summary, replace this anchor — points 5 and 6 together:

```
5. Embarking costs 1 AP per occupied Unit Base.
6. Disembarking costs 1 AP per occupied Unit Base.
```

with:

```
5. Embarking costs 1 AP, whatever the unit occupies.
6. Disembarking costs 1 AP, whatever the unit occupies.
```

---

## 3. The spec delta

- [x] 3.1 Create
  `openspec/changes/no-action-point-cost-scales-with-size/specs/action-economy/spec.md` with
  exactly this content:

```
## ADDED Requirements

### Requirement: Action Cost Does Not Scale With Size
An action's Action Point cost SHALL NOT scale with the size of the unit performing it, nor with the number of Unit Bases that unit occupies, nor with the size of the element or obstacle the action acts on. Embarking and disembarking SHALL each cost exactly 1 Action Point. Where a rule charges more than one Action Point, the reason SHALL be stated in that rule and SHALL NOT be size.

#### Scenario: Infantry embarks for one Action Point
- **WHEN** an infantry model occupying one Unit Base embarks
- **THEN** it spends 1 Action Point

#### Scenario: A larger unit embarks for the same cost
- **WHEN** a unit occupying four Unit Bases embarks
- **THEN** it spends 1 Action Point

#### Scenario: Disembarking costs the same as embarking
- **WHEN** an embarked unit disembarks
- **THEN** it spends 1 Action Point, whatever it occupies

#### Scenario: A larger element costs no more to operate
- **WHEN** a small hatch and a large gate are each opened
- **THEN** each costs the same number of Action Points
```

`*Universal Action Points*` in the living spec is **not** touched: this is an `ADDED`
block, and that requirement keeps both of its scenarios.

---

## 4. Verification

Run each command and write down what it actually returned. If a figure differs from the
one stated here, **stop and report it** — do not edit a document to make it match.

- [x] 4.1 `grep -c "per Unit Base" docs/09-transport.md` — before: **2** (TRN-005's
  sentence and TRN-006's bold line; the Summary's two use "per occupied Unit Base" and
  are counted by 4.3), after: **0**.

- [x] 4.2 `grep -c "Action Point" docs/02-core-rules.md` — before: **5**, after: **6**.
  `grep -c` counts lines, and the paragraph added by 1.1 is a single line carrying the
  phrase several times.

- [x] 4.3 `grep -rn "1 AP per occupied Unit Base" docs/` — before: **2 lines**, both in
  `docs/09-transport.md`; after: **0 lines**.

- [x] 4.4 `grep -c "was paid for on embarking" docs/09-transport.md` — before: **1**,
  after: **0**.

- [x] 4.5 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues
  found.`

- [x] 4.6 `python3 scripts/check_delta_coverage.py` — must **exit 0**. Do not check its
  count: this change adds an `ADDED` block, which the script does not count, and the
  number it prints depends on whether the archive batch for
  `a-unit-base-is-thirteen-plate-layers` has merged yet. Report the line it printed.

- [x] 4.7 `openspec validate no-action-point-cost-scales-with-size` — valid. If the `openspec`
  CLI is not on PATH, say so rather than guessing.

- [x] 4.8 `git status --short` — two modified documents, `docs/02-core-rules.md` and
  `docs/09-transport.md`, plus the untracked change directory
  `openspec/changes/no-action-point-cost-scales-with-size/` reported as a single `??` entry.
  Anything else in the list is a mismatch: report it and stage nothing.

---

## 5. Repairs after the audit of the applied text

The applied text was audited and returned twelve findings. Seven are repaired here; the
rest are wording of the proposal documents themselves and are corrected in
`proposal.md` and `design.md` rather than in `docs/`.

**The finding that matters.** `CORE-006`'s new paragraph said no cost scales with "the
size of what the action acts on" and cited `MOVE-010` for it, comparing an obstacle of 4
plate layers against one of 6 — true, and the wrong comparison. Against `MOVE-009` it is
false: the same infantry crosses a 3-plate-layer obstacle for 1 AP and a 4-plate-layer
one for 2 (`MOVE-010`, "a move over such an obstacle costs 2 AP in total"). The height of
the terrain does move the price.

The repair is to say what the rule actually forbids. An **element that is operated** — a
door, a ramp, a hatch, an access point — costs the same whatever its size; that is the
owner's case and `CORE-007` already charges it flat. Terrain is not operated: an
obstacle's height decides **which rule applies**, not what a given action costs. Both
statements are true of the whole ruleset, and neither needs an exception.

- [x] 5.1 In `CORE-006`, replace the paragraph added by task 1.1 — this anchor:

```
**No Action Point cost scales with size.** Not with the size of the unit paying it: an infantry model and a walker pay the same to embark (`09-transport.md`, TRN-005). Not with the size of what the action acts on: opening a hatch and opening a cargo ramp cost the same (CORE-007), and climbing an obstacle of 4 plate layers costs what climbing one of 6 costs (`07-movement.md`, MOVE-010). The allotment above is fixed, so a price that grew with the model would put a large enough model beyond acting at all — forbidden by arithmetic rather than by a rule, which is not how this ruleset forbids anything. Where a rule charges more than one Action Point, the reason is stated in that rule and is never size: `11-combat.md` (CBT-001) charges per weapon system attacking, `08-vehicles.md` (VEH-008) per 90° turn, and MOVE-010 charges a climb on top of the move that crosses the obstacle.
```

with:

```
**No Action Point cost scales with size.** Not with the size of the unit paying it — its footprint, its height, or the Unit Bases it occupies: an infantry model and a motorcycle pay the same to embark (`09-transport.md`, TRN-005). Not with the size of an element it operates: a hatch and a cargo ramp cost the same to open (CORE-007). The allotment above is fixed, so a price that grew with the model would put a large enough model beyond acting at all — forbidden by arithmetic rather than by a rule, which is not how this ruleset forbids anything. A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`07-movement.md`, MOVE-009, MOVE-010). And where more than one Action Point is spent, the reason is stated in the rule that spends it and is never size — `11-combat.md`, CBT-001 charges per weapon system attacking, and `08-vehicles.md`, VEH-008 per 90° turn.
```

- [x] 5.2 In `TRN-005`, replace this anchor — the sentence applied by task 2.1, which
  copies `CORE-006`'s headline instead of citing it:

```
Embarking costs **1 Action Point**, whatever the unit occupies — an infantry model of one Unit Base and a motorcycle of two pay the same, matching Disembarking (TRN-006). No Action Point cost scales with size (`02-core-rules.md`, CORE-006).
```

with:

```
Embarking costs **1 Action Point**, whatever the unit occupies (`02-core-rules.md`, CORE-006) — an infantry model of one Unit Base and a motorcycle of two pay the same, matching Disembarking (TRN-006).
```

- [x] 5.3 In `TRN-006`, replace this anchor — the sentence applied by task 2.2, for the
  same reason:

```
The cost is the same whatever the unit occupies, matching Embarking (TRN-005). No Action Point cost scales with size (`02-core-rules.md`, CORE-006).
```

with:

```
The cost is the same whatever the unit occupies (`02-core-rules.md`, CORE-006), matching Embarking (TRN-005).
```

- [x] 5.4 In `TRN-005`'s Requirements list, replace this anchor:

```
- A free Unit Base must exist inside the transport — free as a volume, so the compartment's clearance must admit it (TRN-019).
```

with:

```
- Free Unit Bases must exist inside the transport for everything the unit occupies (TRN-001) — free as a volume, so the compartment's clearance must admit them (TRN-019).
```

  The per-Unit-Base price removed by task 2.1 was the only text in `TRN-005`
  acknowledging that a unit may occupy more than one Unit Base. Removing it left a
  singular requirement as the rule's sole statement, which would have denied what this
  change's own spec scenario asserts.

- [x] 5.5 In `TRN-005`, replace this anchor — the closing line, for the same reason:

```
The model is then physically placed inside one available Unit Base.
```

with:

```
The model is then physically placed inside them.
```

- [x] 5.6 In `openspec/changes/no-action-point-cost-scales-with-size/specs/action-economy/spec.md`,
  replace this anchor — the requirement sentence:

```
An action's Action Point cost SHALL NOT scale with the size of the unit performing it, nor with the number of Unit Bases that unit occupies, nor with the size of the element or obstacle the action acts on. Embarking and disembarking SHALL each cost exactly 1 Action Point. Where a rule charges more than one Action Point, the reason SHALL be stated in that rule and SHALL NOT be size.
```

with:

```
An action's Action Point cost SHALL NOT scale with the size of the unit performing it — its footprint, its height, or the number of Unit Bases it occupies — nor with the size of an element that action operates. Where more than one Action Point is spent, the reason SHALL be stated in the rule that spends it and SHALL NOT be size. A measurement MAY decide which rule applies to an action; it SHALL NOT decide what that action costs.
```

  The deleted sentence copied `TRN-005`'s figure into a capability that does not own it,
  which is the duplication `design.md` Decision 1 refuses for `CORE-006`. The scenarios
  below it still carry the figure, which is where an example belongs.

- [x] 5.7 In `design.md`, replace this anchor — the `MOVE-010` row of Decision 2's table:

```
| `MOVE-010` | 1 additional AP to climb | No — same at 4 plate layers as at 6 |
```

with:

```
| `MOVE-009`, `MOVE-010` | crossing an obstacle: free below 4 plate layers, 1 additional AP from 4 to 6 | Within a rule, no — 4 and 6 cost the same. Between them, the obstacle's height selects the rule, and that is the distinction `CORE-006` draws |
```

- [x] 5.8 In `design.md`, replace this anchor — the paragraph after that table:

```
`MOVE-010` is the case that looked dangerous and is not. It charges for **crossing** an
obstacle, and the price is flat across the whole climbable band: 4, 5 and 6 plate layers
all cost the same additional Action Point, and a model twice the size pays the same.
Above the band nothing is charged at all — `MOVE-011` forbids the climb outright and
requires an access point. So the anti-scaling rule holds with no exception, and the
movement rules can be left exactly as the owner asked.
```

with:

```
`MOVE-010` is the case that decided the wording. Read against `MOVE-011` above it, it
looks safe: the band is 4 to 6 plate layers, the price is flat across it, and above 6 no
climb is permitted at any price. Read against `MOVE-009` below it, it is not: the same
infantry crosses 3 plate layers for 1 AP and 4 for 2. An earlier draft of `CORE-006`
claimed no cost varies with "the size of what the action acts on" and cited the
within-band comparison for it, which is the true half of a false claim.

So the rule states the two things that are true of the whole ruleset. An **element that
is operated** — door, ramp, hatch, access point — costs the same whatever its size;
`CORE-007` already charges it that way and it is the owner's own case. Terrain is not
operated: its height selects which movement rule applies, and each of those rules is flat
within itself. Neither statement needs an exception, and the movement rules are left
exactly as the owner asked.
```

- [x] 5.9 In `design.md`, replace this anchor — the sweep's opening claim:

```
A repo-wide `grep` for every AP charge in `docs/` finds nine rules, and all nine are
already flat in both directions once `TRN-005` and `TRN-006` are fixed:
```

with:

```
A repo-wide `grep` for AP charges in `docs/` finds them in `02-core-rules.md`,
`04-construction-standard.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`,
`11-combat.md`, `12-melee.md`, `16-damage-system.md` and `17-components.md`. The rules
that set a price are these, and every one of them is flat once `TRN-005` and `TRN-006`
are fixed. `VEH-004` is the clearest statement of the principle already in the ruleset:
every vehicle covers three of its own lengths per action, "whatever its size".
```

- [x] 5.10 In `design.md`, replace this anchor — the rotation row, which reads four rules
  as one:

```
| `VEH-008` – `VEH-011` | 1 AP per 90° turn, "matching MOVE-008's infantry rotation cost" | No |
```

with:

```
| `VEH-008`, `VEH-011` | 1 AP per 90° turn, "matching MOVE-008's infantry rotation cost" | No |
| `VEH-009`, `VEH-010` | 1 AP to rotate 90°, 180° or 270° | No — a tracked hull turns further for the same Action Point than a wheeled one, which is locomotion, not size |
```

- [x] 5.11 In `proposal.md`, replace this anchor — the climbing bullet under *What Does
  Not Change*:

```
- **Climbing.** `MOVE-010` keeps its additional Action Point. It is charged for crossing
  an obstacle, not for how big the obstacle is: 4 plate layers and 6 cost the same, and a
  larger model pays no more. The movement rules are out of scope by the owner's
  instruction, and nothing here disturbs them.
```

with:

```
- **Climbing.** `MOVE-010` keeps its additional Action Point, and `MOVE-009` keeps its
  free crossing below 4 plate layers. An obstacle's height selects which of the two
  applies; within each, the price is flat and a larger model pays no more. `CORE-006`
  says exactly that, and says it about terrain rather than about elements a unit
  operates. The movement rules are out of scope by the owner's instruction, and nothing
  here disturbs them.
```

- [x] 5.12 In `proposal.md`, replace this anchor — the `MOVE-010` bullet in *Why*:

```
- `MOVE-010` — 1 additional AP to climb an obstacle of 4 to 6 plate layers: the same
  price at 4 as at 6, and the same for any model that can climb it.
```

with:

```
- `MOVE-010` — 1 additional AP to climb an obstacle of 4 to 6 plate layers: the same
  price at 4 as at 6, and the same for any model that can climb it. Below 4 the crossing
  is free (`MOVE-009`), so the obstacle's height selects the rule rather than pricing the
  action.
```

- [x] 5.13 In `tasks.md`, replace this anchor — the scope sentence, whose second count
  was wrong:

```
Two ruleset documents and one spec delta: **six edits and eight verify-only tasks.**
```

with:

```
Two ruleset documents and one spec delta: **six edits and nine non-edit tasks** (0.1 and
4.1 – 4.8), before the repairs recorded in section 5.
```

- [x] 5.14 In `design.md`, append this to the list under *What this change deliberately
  leaves open*, as a new bullet at the end of that list:

```
- **Whether a multi-Unit-Base vehicle embarks or is loaded.** `TRN-001` lists a Light
  Walker and a Heavy Walker among the objects a transport carries and `TRN-005` prices a
  unit embarking, while `TRN-013`'s table classes a motorbike and a walker as *cargo*,
  which no rule prices in Action Points at all. This change does not settle it: it fixes
  what embarking costs for whatever embarks, and `CORE-006`'s example is the motorcycle
  `TRN-005` already uses rather than a walker, so the core document asserts nothing about
  the open question.
```

- [x] 5.15 **Rename the change to match its own title.** The directory and branch are
  called `no-action-point-cost-scales-with-size`, and `design.md` Decision 3 is titled *Not
  "every action costs exactly 1 AP"* — the name asserts the claim the change refutes, and
  after archiving it is permanent. Rename the directory:

```
git mv openspec/changes/no-action-point-cost-scales-with-size openspec/changes/no-action-point-cost-scales-with-size
```

  The directory is untracked, so if `git mv` refuses, use `mv` with the same two paths.
  Then replace every occurrence of the old slug inside the change's own three artifacts —
  `proposal.md`, `design.md` and `tasks.md` — with `no-action-point-cost-scales-with-size`,
  including task 0.1's branch name and every path in sections 3, 4 and 5. Do not rename
  the git branch: that is not yours to do in this task, and it is done separately.

  Verify with `grep -rc "no-action-point-cost-scales-with-size" openspec/changes/` — **0**
  matches afterwards, in any file.

### Verification after section 5

- [x] 5.16 `grep -c "No Action Point cost scales with size" docs/02-core-rules.md` and
  the same on `docs/09-transport.md` — before: **1** and **2**, after: **1** and **0**.

- [x] 5.17 `grep -c "one available Unit Base" docs/09-transport.md` — before: **1**,
  after: **0**.

- [x] 5.18 `grep -c "exactly 1 Action Point" openspec/changes/no-action-point-cost-scales-with-size/specs/action-economy/spec.md` — before: **1**, after: **0**.

- [x] 5.19 `grep -c "MOVE-009" docs/02-core-rules.md` — before: **0**, after: **1**. The
  paragraph now names the rule that falsified the earlier wording.

- [x] 5.20 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues
  found.`

- [x] 5.21 `openspec validate no-action-point-cost-scales-with-size` — valid.

- [x] 5.22 `python3 scripts/check_delta_coverage.py` — must **exit 0**; report the line
  it printed and do not check its count, for the reason given in 4.6.

- [x] 5.23 `grep -c "^- \[ \]" openspec/changes/no-action-point-cost-scales-with-size/tasks.md`
  — after ticking every box in this section: **0**.
