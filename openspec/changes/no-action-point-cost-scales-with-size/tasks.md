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
`DMG-019`, `12-melee.md` (already flat); `TRN-019`, `DEP-005`; `CHANGELOG.md`, every
`**Version:**` header and `openspec/specs/`. `TRN-005`'s requirements list and `VEH-016`
were on this list and were taken off it — sections 5 and 6 edit both, for the reason
`proposal.md` now records under *What Changes*.

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

- [x] 5.15 **Rename the change to match its own title.** The directory and branch were
  called `an-action-costs-one-action-point`, and `design.md` Decision 3 is titled *Not
  "every action costs exactly 1 AP"* — the name asserts the claim the change refutes, and
  after archiving it is permanent. Rename the directory:

```
git mv openspec/changes/an-action-costs-one-action-point openspec/changes/no-action-point-cost-scales-with-size
```

  The directory is untracked, so if `git mv` refuses, use `mv` with the same two paths.
  Then replace every occurrence of the old slug inside the change's own three artifacts —
  `proposal.md`, `design.md` and `tasks.md` — with `no-action-point-cost-scales-with-size`,
  including task 0.1's branch name and every path in sections 3, 4 and 5. Do not rename
  the git branch: that is not yours to do in this task, and it is done separately.

  Verify with `grep -rc "an-action-costs-one-action-point" openspec/changes/` — **0**
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

---

## 6. Repairs after the third audit

The repairs in section 5 were audited in turn and returned twelve findings. Two of them
are false record that archiving would make permanent, two are rule text that needed a
decision, and the rest are sentences in this change's own documents that section 5 left
describing the text it had just replaced.

- [x] 6.1 In `CORE-006`, replace this anchor — the paragraph as section 5 left it:

```
**No Action Point cost scales with size.** Not with the size of the unit paying it — its footprint, its height, or the Unit Bases it occupies: an infantry model and a motorcycle pay the same to embark (`09-transport.md`, TRN-005). Not with the size of an element it operates: a hatch and a cargo ramp cost the same to open (CORE-007). The allotment above is fixed, so a price that grew with the model would put a large enough model beyond acting at all — forbidden by arithmetic rather than by a rule, which is not how this ruleset forbids anything. A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`07-movement.md`, MOVE-009, MOVE-010). And where more than one Action Point is spent, the reason is stated in the rule that spends it and is never size — `11-combat.md`, CBT-001 charges per weapon system attacking, and `08-vehicles.md`, VEH-008 per 90° turn.
```

with:

```
**No Action Point cost scales with size.** Not with the size of the unit paying it — its footprint, its height, or the Unit Bases it occupies: an infantry model and a motorcycle pay the same to embark (`09-transport.md`, TRN-005). Not with the size of an interactive element it operates (CORE-007): a hatch and a cargo ramp cost the same to open. The allotment above is fixed, so a price that grew with the model would put a large enough model beyond acting at all — forbidden by arithmetic rather than by a rule, which is not how this ruleset forbids anything. A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`07-movement.md`, MOVE-009, MOVE-010). And where more than one Action Point is spent, the reason is stated in the rule that spends it and is never size — `11-combat.md`, CBT-001 charges per weapon system attacking, `08-vehicles.md`, VEH-008 per 90° turn, and MOVE-010 charges the climb itself: the second Action Point buys crossing the obstacle, not the obstacle's height.
```

- [x] 6.2 In `TRN-005`'s Requirements list, replace this anchor — the bullet as section 5
  left it, which states no quantity and reads circularly:

```
- Free Unit Bases must exist inside the transport for everything the unit occupies (TRN-001) — free as a volume, so the compartment's clearance must admit them (TRN-019).
```

with:

```
- The transport must have as many free Unit Bases as the unit occupies (TRN-001) — free as a volume, so the compartment's clearance must admit them (TRN-019). For an infantry model that is one; for a motorcycle, two.
```

- [x] 6.3 In `TRN-005`, replace this anchor — the closing line, whose plural pronoun has
  no referent in the one-Unit-Base case:

```
The model is then physically placed inside them.
```

with:

```
The model is then physically placed in the Unit Bases it occupies.
```

- [x] 6.4 In `docs/08-vehicles.md`, `VEH-016`, replace this anchor — a second,
  independent statement of the admission test that still assumes one Unit Base per
  passenger:

```
If a passenger's Unit Base physically fits, it may embark (`02-core-rules.md`, CORE-001).
```

with:

```
A passenger may embark where the transport has as many free Unit Bases as the passenger occupies (`09-transport.md`, TRN-005).
```

- [x] 6.5 In `proposal.md`, replace this anchor — the claim in *Why* that the repair in
  section 5 established is false:

```
`TRN-006` says the same for disembarking. Everywhere else the price is already flat, and
flat in both directions — it varies neither with the model paying it nor with the thing
it acts on:
```

with:

```
`TRN-006` says the same for disembarking. Everywhere else the price is already flat: it
varies neither with the model paying it nor with the size of an interactive element that
model operates.
```

- [x] 6.6 In `proposal.md`, replace this anchor — the first bullet of *What Changes*:

```
- **`CORE-006`** gains the rule in its own voice: no Action Point cost scales with size
  — neither the size of the unit paying it nor the size of what it acts on. It also says
  what to make of a rule that charges two: the reason is stated in that rule, and it is
  never size.
```

with:

```
- **`CORE-006`** gains the rule in its own voice: no Action Point cost scales with size —
  neither the size of the unit paying it nor the size of an interactive element it
  operates. It also says what a measurement may still do (select which rule applies, as
  `MOVE-009` and `MOVE-010` do) and what to make of a rule that spends two Action Points:
  the reason is stated in that rule, and it is never size.
```

- [x] 6.7 In `proposal.md`, replace this anchor — the `TRN-005` bullet, which claims the
  requirements list is untouched:

```
- **`TRN-005`** — embarking costs **1 Action Point**, whatever the unit occupies. Its
  motorcycle example goes with the multiplier; the requirements below it (adjacency, an
  open access point, a free Unit Base inside) are untouched.
```

with:

```
- **`TRN-005`** — embarking costs **1 Action Point**, whatever the unit occupies. Its
  motorcycle example goes with the multiplier. Its requirements list is edited too, and
  has to be: the per-Unit-Base price was the only text in the rule acknowledging that a
  unit may occupy more than one Unit Base, so removing it would have left a singular
  requirement denying what this change's own spec scenario asserts. The rule now asks for
  as many free Unit Bases as the unit occupies. Adjacency and the open access point are
  untouched.
- **`VEH-016`** stated that same admission test a second time, independently, and still
  in the singular. It now cites `TRN-005` instead of restating it.
```

- [x] 6.8 In `proposal.md`, replace this anchor — the *What Does Not Change* entry that
  the change does in fact change:

```
- **Who may embark, and where.** `TRN-005`'s requirements, `TRN-019`'s clearance and
  `DEP-005` are untouched. This change moves a price, not a permission.
```

with:

```
- **Who may embark, and where.** `TRN-019`'s clearance and `DEP-005` are untouched, and
  no model that could embark before this change is refused after it. `TRN-005`'s
  requirements list and `VEH-016` are reworded — see *What Changes* — but only to state
  the quantity the old per-Unit-Base price implied. This change moves a price, not a
  permission.
```

- [x] 6.9 In `design.md`, replace this anchor — Decision 1's closing sentence, which
  names an example the applied text does not use:

```
`CORE-006` does **not** restate `TRN-005`'s figure: it says an infantry model and a
walker "pay the same to embark" and cites the rule that owns the number.
```

with:

```
`CORE-006` does **not** restate `TRN-005`'s figure: it says an infantry model and a
motorcycle "pay the same to embark" and cites the rule that owns the number.
```

- [x] 6.10 In `design.md`, replace this anchor — Decision 3's closing paragraph, which
  describes a sentence section 5 rewrote:

```
`CORE-006`'s new paragraph therefore closes with what a reader should make of a rule that
charges two: the reason is stated in that rule, and it is never size. `CBT-001`,
`VEH-008` and `MOVE-010` are named there so the rules are read together rather than
against each other.
```

with:

```
`CORE-006`'s new paragraph therefore closes with what a reader should make of a rule that
spends two Action Points: the reason is stated in that rule, and it is never size. All
three are named there — `CBT-001` per weapon system, `VEH-008` per 90° turn, and
`MOVE-010`, which is the ruleset's only rule where one action costs two. `MOVE-010` earns
its own clause, because it is the case that could be read as size pricing an action and
is not: the second Action Point buys crossing the obstacle, and the obstacle's height
decides only which of `MOVE-009`, `MOVE-010` and `MOVE-011` applies.
```

- [x] 6.11 In `design.md`, replace this anchor — the sweep's list of documents, which
  names a file that has never existed:

```
`11-combat.md`, `12-melee.md`, `16-damage-system.md` and `17-components.md`. The rules
```

with:

```
`05-construction-components.md`, `11-combat.md`, `12-melee.md` and `16-damage-system.md`. The rules
```

- [x] 6.12 In `design.md`'s Decision 2 table, replace this anchor:

```
| `SCS-007`, `SCS-008`, `TRN-008` | doors, ramps, access points, 1 AP, citing `CORE-007` | No |
```

with:

```
| `SCS-007`, `SCS-008`, `TRN-008`, `CMP-009`, `CMP-010` | doors, ramps, access points, 1 AP, citing `CORE-007` | No |
```

- [x] 6.13 In `design.md`, replace this anchor — the open-question bullet, whose
  justification does not hold, since `TRN-013` classes the motorbike as cargo too:

```
- **Whether a multi-Unit-Base vehicle embarks or is loaded.** `TRN-001` lists a Light
  Walker and a Heavy Walker among the objects a transport carries and `TRN-005` prices a
  unit embarking, while `TRN-013`'s table classes a motorbike and a walker as *cargo*,
  which no rule prices in Action Points at all. This change does not settle it: it fixes
  what embarking costs for whatever embarks, and `CORE-006`'s example is the motorcycle
  `TRN-005` already uses rather than a walker, so the core document asserts nothing about
  the open question.
```

with:

```
- **Whether a multi-Unit-Base vehicle embarks or is loaded.** `TRN-001` lists a Light
  Walker and a Heavy Walker among the objects a transport carries and `TRN-005` prices a
  unit embarking, while `TRN-013`'s table classes both a motorbike and a walker as
  *cargo*, which no rule prices in Action Points at all. Those two entries are the whole
  of the ambiguity, and `CORE-006`'s motorcycle is one of them: this change therefore
  takes the reading `TRN-005` already had — a motorcycle embarks and pays for the action
  — and states it in `02-core-rules.md` as well. It does not settle the general question,
  and a later change must either confirm that reading for every multi-Unit-Base object or
  overturn it. What it does settle is that whatever embarks pays the same.
- **A price keyed to the size of a *target*.** The rule bars scaling by the size of the
  unit paying and of an interactive element it operates. A future rule charging more to
  attack something large is barred by neither clause. That is narrower than the sentence
  in *Why*, and deliberately: the wider claim is the one `MOVE-009` falsifies.
```

- [x] 6.14 In `tasks.md`, replace this anchor — the "Untouched, deliberately" list, which
  names two things section 5 and section 6 change:

```
`DMG-019`, `12-melee.md` (already flat); `TRN-005`'s requirements list; `TRN-019`,
`DEP-005`; `CHANGELOG.md`, every `**Version:**` header and `openspec/specs/`.
```

with:

```
`DMG-019`, `12-melee.md` (already flat); `TRN-019`, `DEP-005`; `CHANGELOG.md`, every
`**Version:**` header and `openspec/specs/`. `TRN-005`'s requirements list and `VEH-016`
were on this list and were taken off it — sections 5 and 6 edit both, for the reason
`proposal.md` now records under *What Changes*.
```

- [x] 6.15 In `tasks.md`, repair task 5.15, which the slug substitution it ordered then
  applied to itself. Three replacements inside that task, and nowhere else in the file:

  Replace `The directory and branch are\n  called \`no-action-point-cost-scales-with-size\`` with `The directory and branch were\n  called \`an-action-costs-one-action-point\``.

  Replace the fenced command `git mv openspec/changes/no-action-point-cost-scales-with-size openspec/changes/no-action-point-cost-scales-with-size` with `git mv openspec/changes/an-action-costs-one-action-point openspec/changes/no-action-point-cost-scales-with-size`.

  Replace ``Verify with `grep -rc "no-action-point-cost-scales-with-size" openspec/changes/` — **0**`` with ``Verify with `grep -rc "an-action-costs-one-action-point" openspec/changes/` — **0**``.

  Leave every other occurrence of the new slug in the file exactly as it is: those are
  live paths and they are correct.

### Verification after section 6

- [x] 6.16 `grep -c "17-components" openspec/changes/no-action-point-cost-scales-with-size/design.md` — before: **1**, after: **0**. The same command on `tasks.md` returns **1** both times: task 5.9's block quotes the text it replaced, and that quotation is the record.

- [x] 6.17 `grep -c "an element it operates" docs/02-core-rules.md` — before: **1**, after: **0**; `grep -c "interactive element it operates" docs/02-core-rules.md` — before: **0**, after: **1**.

- [x] 6.18 `grep -c "MOVE-010 charges the climb itself" docs/02-core-rules.md` — before: **0**, after: **1**.

- [x] 6.19 `grep -c "as many free Unit Bases as the" docs/` across `09-transport.md` and `08-vehicles.md` — after: **1** in each.

- [x] 6.20 `grep -c "physically placed inside them" docs/09-transport.md` — before: **1**, after: **0**.

- [x] 6.21 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`

- [x] 6.22 `openspec validate no-action-point-cost-scales-with-size` — valid.

- [x] 6.23 `python3 scripts/check_delta_coverage.py` — must **exit 0**; report the line it printed.

- [x] 6.24 `grep -c "^- \[ \]" openspec/changes/no-action-point-cost-scales-with-size/tasks.md` — after ticking every box in this section: **0**.

- [x] 6.25 In `docs/08-vehicles.md`, `VEH-016`, replace this anchor — the line after the
  one task 6.4 rewrote, whose "it" referred to the Unit Base that sentence used to name:

```
If it does not fit, it cannot.
```

with:

```
If it does not have them, the passenger cannot embark.
```

- [x] 6.26 `grep -c "If it does not fit, it cannot." docs/08-vehicles.md` — before: **1**,
  after: **0**. `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues
  found.`
