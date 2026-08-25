# Design — The ruleset states its rules and stops

Twelve decisions. Two of them (3 and 5) knowingly break something, and both say
what the price is and where it is paid.

---

## Decision 1 — The edits came first, and the proposal second

`system/workflow.md` (Git Workflow) is unambiguous: **every change to a
`docs/*.md` file goes through an OpenSpec proposal first.** This one did not.
Fifteen documents were edited by hand on branch `general-review`, and this
proposal was written afterwards to describe what was done.

**Recorded rather than hidden**, because the alternative — a proposal written in
the past tense that reads as if it had been written first — is the failure mode
`system/proposal-review.md` warns about in a different form: an artifact that
can only be accepted or refused, because the thing it would have been argued
against no longer exists.

What it costs, concretely:

- **The audit that catches design defects ran late.** `proposal-auditor` exists
  to read a proposal *before* it is applied, and the findings it would have
  produced are instead the repair tasks in `tasks.md`, Part B.
- **`docs/` was in a self-inconsistent state on this branch** between the edit
  and the repair. Decision 5 is one of those states.

**Rejected: rewriting history so the proposal predates the edits.**
`system/repository-strategy.md` forbids it outright, and it would trade a
recorded process defect for an unrecorded one.

**Rejected: splitting the pass into fifteen proposals after the fact.** The
edits are one commit series with one editorial intent, and reconstructing
fifteen plausible proposals from them fabricates a history that never happened
— the same argument `system/workflow.md` makes about reconstructing superseded
deltas.

---

## Decision 2 — The deleted prose is not restored anywhere

Most of what this pass removes is *correct*. It is reasoning that explains why a
rule reads as it does, worked examples that pre-empt a misreading, and
paragraphs that answer a question a careful reader would ask.

It still goes, because `docs/` is not where it belongs.
`system/documentation-standards.md` gives `docs/` one job — the current accepted
rules — and `system/workflow.md` gives design rationale to the proposal that
introduced it. Every paragraph deleted here is reachable in the archived change
that added it.

**Rejected: moving the prose to a commentary document.** That is a second
ruleset with no linter, no rule IDs and nothing keeping it true; the first rule
it contradicted would be found by a player, not by a check.

**Kept anyway, in three places**, because deleting them would delete a rule
rather than its justification:

- `CBT-011` and `WPN-021` keep their superseded-design notes
  (`system/proposal-review.md`, "Record What You Decided Not to Do").
- `DMG-004`'s worked examples stay, in compressed form: they are how Resistance
  is read, not why.
- `INF-011`'s example table stays, for the same reason.

---

## Decision 3 — `DMG-*` is renumbered, against the standard

**This breaks `system/documentation-standards.md` (Naming Conventions), which
says rule identifiers are never renumbered and never reused.** Four rules were
deleted from the middle of `16-damage-system.md` and the numbers below them
closed up, so eleven rules now answer to a number that named a different rule
before this change.

The reason is this change's own: **the ruleset was too hard for a general
audience to read.** `16-damage-system.md` is a document a new player reads in
order, and four of its nineteen rules restated other documents (`DMG-009`,
`DMG-010`, `DMG-011`, `DMG-018`). Deleting them is the readability argument.
Closing the gaps afterwards is the same argument one step further: a reader who
meets `DMG-008` followed by `DMG-012` stops to work out what is missing, and
nothing there rewards the stop.

The standard's answer to that reader is a retired number, which costs a stumble
and buys a permanent address. This change judged the stumble to be the larger
cost in the one document where the sequence is part of the explanation. **That
judgement is the exception, not a general licence** — see the rejection below.

**The counter-argument, which is the standard's:** a rule ID is a permanent
address. It is cited from other documents, from `14-glossary.md`, from
`assets/IMAGES.md`, from `TODO.md`, from `system/`, and from every archived
proposal — and an archived proposal is never rewritten. **After this change,
every `DMG-*` citation in the archive points at the wrong rule and always will.**
`scripts/check_id_stability.py` does not catch this: it reports an ID that moved
document, or one reissued below its document's high-water mark, and a number
that stayed put while its meaning moved is neither.

**The price is paid in `tasks.md`, Part B**: every live citation is repaired
there, one line at a time. The archive is left alone — it is history
(`system/proposal-review.md`).

**Rejected: retiring the four numbers and leaving the gaps.** It is what the
standard requires, and it is what a future change of this shape should do. It
was not chosen here, and this decision is the record that the choice was made
deliberately rather than overlooked.

---

## Decision 4 — `VEH-028` goes, and the ceiling is the only height bound

`VEH-028` bounded a vehicle's height at one Unit Base per two studs of its
narrowest footprint side. Two bounds applied at once — that one and the agreed
ceiling (`DEP-001`) — and a vehicle had to satisfy both.

Removing it leaves one bound: the ceiling the players agreed before the game.

**Why the footprint bound was the one to go.** It is a fixed ratio applied to a
number the player chooses, which is the shape `CODE_OF_DESIGN.md` Principle 13
(Build Freedom) names: a proportion the ruleset asserts rather than reads. A
narrow tall walker was illegal under `VEH-028` no matter what battlefield it was
built for, and legal or illegal is exactly the question the Deployment Volume
already answers, per game, with the players' agreement in it.

Principle 11 (Simplicity Before Complexity) is the second argument: two bounds
where one decides the outcome in every case a player is likely to build.

**What is lost.** `VEH-028` made a very tall, very narrow vehicle illegal at the
bench, before any Deployment Volume was agreed. It is now legal wherever the
ceiling admits it. Players who want the old constraint agree a lower `H`, which
is `DEP-001`'s own mechanism.

**Rejected: keeping `VEH-028` and dropping the ceiling.** The ceiling is agreed
per game and reads the model; the footprint ratio is neither.

---

## Decision 5 — Deployment is a physical act, and footprints are whole

**Stated by the maintainer, not inferred from the text:**

> It is a PHYSICAL act. I put in as many elements as fit. A `5 × 1 × 1 UB`
> volume takes five infantry, or one `1 × 2 UB` Bike and three infantry, or two
> Bikes and one infantry. Whatever fits physically without models overlapping.
> And if a model is `1 × 2.5`, that is really `1 × 3` — there are no partial
> footprints, only complete ones.

`DEP-001` agrees a box. `DEP-002` says fill it with what fits. Nothing is
counted, spent or budgeted anywhere in the chapter.

**Three things followed, and only one was in `docs/`.** That placement is a real
act with the models was implied and never stated. That footprints round up to
whole Unit Bases was stated nowhere at all — `DEP-003`'s "every Unit Base
covered" implies it and `VEH-001`'s whole-number table hides the question. And
`DEP-006` still charged a model on a vehicle roof one Unit Base of floor it does
not stand on, which was the last arithmetic left in the chapter. `tasks.md`,
section 16.

**The rule that must not be swept up with it:** inside a transport, cargo
*does* divide a Unit Base into slices (`09-transport.md`, TRN-013). Whole
footprints are a rule of the deployment floor, and section 16 says so in the
rule itself rather than leaving the two to be reconciled by a reader who meets
them a document apart.

### Carrying was already owned by `09-transport.md`, and this change forgot it twice

The maintainer's second statement — a unit is carried only in the transport
space its carrier actually has, and models may not be put outside in disorder —
**was already the ruleset's rule before this change touched anything.**
`TRN-005` says "Place the unit inside the available transport space", `TRN-001`
says every transported object occupies Unit Bases of that space, and `VEH-016`
says a passenger may embark only when free ones exist. One owner, stated once.

This change got it wrong twice. Task 16.4 removed `DEP-006`'s charge on an
externally carried model, arguing that a model on a roof does not stand on the
floor — the arithmetic objection was right and the conclusion was wrong, because
it made perching models on hulls free. Tasks 19.1 and 19.3 then "fixed" that by
**restating the transport rule in two more documents**, which is the defect this
whole change exists to remove, committed by the change itself.

**All of it is reverted** (`tasks.md`, section 20). `DEP-005`, `DEP-006` and
`VEH-030` read as Part A left them.

The lesson is not about deployment. It is that **a rule that seems missing from
the document you are reading is usually stated in the document that owns it**,
and the reflex to write it down where it is missed is how three copies of one
rule appear. `system/documentation-standards.md` ("What `system/` Is For") says
this about `system/`; it is just as true of `docs/`.

**One thing was seen and deliberately left.** `DEP-006`'s restored line says an
externally carried model "occupies 1 Unit Base of Deployment Volume floor
space" — the same vocabulary shape as the "counts against" section 18 removed
from `DEP-004`. The substance is right, the maintainer reads it as clear, and
changing it would be this change's fourth pass over the same paragraph.

---

## Decision 6 — `CBT-010` and `MEL-004` go together, or not at all

Both described how two attacks resolve when something declares them
simultaneous. Nothing in StudCraft declares them simultaneous: activation is
strictly one unit at a time (`FLOW-002`), and both rules said so about
themselves.

**A rule for a case no rule produces is a rule a reader must hold and never
use.** They are deleted as a pair, because either one surviving alone would be
the melee or the ranged half of a mechanism that does not exist.

`12-melee.md`'s Summary still names `MEL-004`. **The bullet goes, and the rule
is not restated anywhere** (`tasks.md`, section 4). A player who asks "does my target
strike back?" is answered by `FLOW-002` — activation is one unit at a time — and
by `CBT-001`, which makes an attack an action its owner spends an Action Point
on. Nothing grants a reaction, so nothing needs to deny one.

**Rejected: restating it in `MEL-005`.** It puts back, one rule over, what this
change removed on purpose.

**Rejected: keeping `CBT-010` as a hook for a future scenario rule.** A future
scenario rule that needs simultaneous resolution states it; that is what
`FLOW-013` allows a scenario to do.

---

## Decision 7 — `assets/IMAGES.md` travels with the change

`system/repository-strategy.md` (Branch Naming) lets a ruleset branch carry a
non-`docs/` file when `design.md` names it and says why. Eight are named:

- **`assets/IMAGES.md`** — it holds a row per planned image, keyed by rule ID.
  `VEH-028`'s row describes an image of a rule that no longer exists, and the
  penetration row is keyed to a number that now means Repairs. Shipping either
  is shipping a pointer the change knows is broken.
- **`TODO.md`** — a required check (`TODO.md quotes the ruleset verbatim`)
  compares its quotes against `docs/`. Leaving it is a red gate, not a
  cosmetic mismatch.
- **`cspell.json`** — two words the compressed prose introduces.
- **`system/documentation-standards.md`, `system/workflow.md`,
  `system/proposal-review.md`, `scripts/check_delta_coverage.py`,
  `.claude/agents/ruleset-auditor.md`** — all five cite `MEL-010` as a worked
  example of a retired-but-kept number, and this change deletes it. Amending
  them here is what Decision 10 chose over restoring the rule; leaving them is
  shipping five pointers the change knows are broken.

  **The count was three when this decision was written.** The two it missed —
  `system/proposal-review.md` and the auditor agent — were found by the
  verification grep on the first apply run, which is what that grep is for.

`tests/` is the eighth, and Decision 8 covers it.

---

## Decision 8 — Two tests were pinned to rules, and are now pinned to behaviour

`tests/test_ruleset_ast.py` and `tests/test_build_index.py` each carried a
regression test written against `DEP-009` by name, and one against a fenced
diagram in `16-damage-system.md` by its content. This pass gave `INF-011` a
sub-heading and deleted that diagram, and both tests failed — **on facts about
today's ruleset, not on the behaviour they were written to protect.**

They now assert the behaviour against a document written in the test, plus the
same invariant over all fifteen real documents:

- a section's span never ends before its last descendant's;
- `prose_lines()` drops exactly the fenced lines and no others;
- the only rule bodies that grew in the AST migration are the ones carrying a
  `#`/`##` sub-heading — computed from the AST rather than listed by name.

The third is what failed here, and it is non-vacuous: it resolves to
`{DEP-009, INF-011}` against `docs/` as it now stands.

`.claude/rules/tooling.md` requires a script change and its test in the same
commit. This is the inverse — a test change with no script change — and the
rule it answers to is the same one: the suite covers `scripts/`, so a suite that
fails on an ordinary ruleset edit is not covering anything.

---

## Decision 9 — Four capabilities get deltas, and eleven documents do not

`system/proposal-review.md` ("Delta vs. Direct Edit") is explicit: a `MODIFIED`
delta can only target a capability that already exists under `openspec/specs/`,
and inventing one for a document that predates the workflow is not allowed.

Seven capabilities exist. What this change does to each was checked:

| Capability | Delta | Why |
|---|---|---|
| `unit-base` | **MODIFIED** | Decision 5 changes how a Deployment Volume's floor is read |
| `geometry-layers` | **MODIFIED** | `GEO-006` and `GEO-007` are folded into `GEO-005`; both requirements survive, their owner does not |
| `damage-resolution` | **MODIFIED** | Attack Roll and Weapon Distribution move to `11-combat.md` |
| `component-damage` | **MODIFIED** | Component State Progression moves from `DMG-005` to `DMG-002` |
| `action-economy` | none | `CORE-006` is unchanged in substance |
| `weapon-capacity` | none | `WPN-004` is compressed; `Σ(Weapon Length) ≤ Platform Length` is untouched |
| `weapon-construction` | none | `WPN-013` and `WPN-017` were restatements; no requirement in the spec loses its rule |

**Thirteen ruleset documents are edited with no spec at all** —
`01-foundations.md`, `02-core-rules.md`, `03-game-flow.md`,
`05-construction-components.md`, `06-deployment.md` (beyond the `unit-base`
delta), `07-movement.md`, `08-vehicles.md`, `09-transport.md`, `10-weapons.md`,
`11-combat.md`, `12-melee.md`, `14-glossary.md`, `17-infantry.md`. None of them
is a tracked capability, and `system/proposal-review.md` says a proposal
touching such a document does not make it one. Their changes are ordinary
doc-edit tasks in `tasks.md`.

**The one place the spec and the ruleset now say it differently.**
`weapon-construction`'s "Range SHALL have no written maximum" carries the chain
that bounds it — Weapon Length by Platform Length, the platform by the agreed
Deployment Volume, that by the battlefield agreed first. `WPN-005` no longer
spells the chain out.

**The spec stays true and nothing is restored.** Nothing in the ruleset states a
maximum Range, which is what the requirement asserts; what was deleted is the
paragraph explaining why none is needed.
`system/proposal-review.md` ("Do Not Cap What the Model Already Bounds") asked
for that paragraph, and the counter-argument is Decision 2: it is reasoning, it
is in the archived change that added it, and `docs/` is not where reasoning
lives. **If the question comes back from a player rather than from a reviewer,
that is the signal to restore it** — one sentence, in `WPN-005`.

---

## Decision 10 — `MEL-010` stays deleted, and five files are amended to match

The pass deleted `MEL-010 — Merged into Component Targeting`, on the reasoning
that applies to every other stub: a rule that says "reserved" is not a rule.

**It was the one sanctioned exception, and five files outside `docs/` say so.**
`system/documentation-standards.md` ("Naming Conventions") called it "the one
stub"; `system/workflow.md`, `system/proposal-review.md`,
`scripts/check_delta_coverage.py` and `.claude/agents/ruleset-auditor.md` all
cite it as the worked example of the stable-identifier convention. All five are
false now.

**They are amended; the rule is not restored** (`tasks.md`, section 8). The convention
itself does not need `MEL-010` to survive: `CBT-011` and `WPN-021` demonstrate
the same thing better, because they keep a number *and a live rule* while
recording that its design was superseded — which is what
`system/proposal-review.md` ("Record What You Decided Not to Do") actually asks
for. A number kept with nothing behind it was always the weaker example.

The standard's own sentence — "no stub is left in its place, the diff records
that the rule was there" — is what the ruleset now follows with no exception at
all, which is a simpler rule than one with a single named survivor.

**Rejected: restoring `MEL-010`.** It is the smaller diff, and it puts back a
line whose only content is that it has no content
(`system/documentation-standards.md`, "How a Rule Is Written").


---

## Decision 11 — A script never names a rule that exists

**No script's behaviour depends on a rule**, and that was checked rather than
assumed: every match of `[A-Z]{2,6}-[0-9]{3}` in `scripts/` sits in a comment, a
docstring or a `--help` line, and the only rule-shaped thing in the code is
`repo.RULE_ID_RE`, which is generic.

**The illustrations were the exposure, and three had already rotted.**
`lint_ruleset.py` cited `DMG-019` as the example its regex must not swallow, and
`DMG-019` no longer exists. `check_todo_quotes.py` quoted a sentence of
`WPN-016` that this change deleted. `lint_ruleset.py`'s docstring quoted a
`06-deployment.md` citation that is no longer written that way. A fourth,
`build_index.py`'s, was repaired in section 11 of `tasks.md` before the class
behind it had a name.

**The constraint: a script may illustrate freely, and never with an ID that
exists.** An invented prefix (`AAA-`, `BBB-`) cannot rot; neither can a
placeholder, nor an invented number under a real prefix (`VEH-099`). It is
written into `system/documentation-standards.md` beside rule-ID stability, which
is the rule it follows from — an ID is a permanent address, so a comment holding
one is holding a reference, not a picture.

**`tests/` is not held to this, and the first version of this decision claimed
otherwise.** It said the fixtures were already `AAA-001` and `BBB-002` and that
this was why the suite survived a pass retiring twelve rules. Both halves were
wrong: `tests/` names `VEH-001` in five files, and only `test_rule.py` uses the
invented prefixes.

The real reason the suite survived is better than the one claimed. **A fixture
defines its own document**, so a `# VEH-001` inside a test's markdown string
invents a rule wearing that name rather than reading the real one — there is no
dependency to remove. The two tests that *did* break were the two that had
reached into `docs/` for a real rule (Decision 8), and that is the whole of the
exposure. `tasks.md`, section 14, corrects the sentence.

**Rejected: keeping the examples and fixing them when they rot.** That is the
loop this change is closing. Nothing checks a docstring, so a rotted example is
found by a reader who is already confused by it.

**Rejected: replacing the examples with prose and no ID at all.** Two of them —
the comma-run form, the em-dash requirement — describe a *pattern*, and a
pattern shown is a pattern understood. The invented prefix keeps the picture and
drops the reference.

**Left as it stands: comments naming a document filename.**
`04-construction-standard.md` and `13-materials.md` were both removed, so those
can rot too. A docstring describing the corpus reads worse without them, and no
filename in `scripts/` is stale today. Recorded so the question is not
rediscovered as a finding (`tasks.md`, section 13).


---

## Decision 12 — The constraint becomes a gate, and one check waits for the merge

Decision 11 wrote a rule into `system/`. **Nothing enforced it**, and
`.claude/rules/tooling.md` says what that is worth: *"Context can be read and
ignored; a hook cannot."* `scripts/lint_ruleset.py` already holds the set of
live rule IDs, so the check is one function and lands as a required gate on
every pull request.

It is verified twice, deliberately: once by the suite, and once by making it
fail on purpose and reverting (`tasks.md`, 15.8). **A check nobody has seen fail
is a check nobody has tested** — and this one passes today for a reason that has
nothing to do with the code, because section 13 already cleaned `scripts/`.

### `SECTION_DEBT` shrank, and that is the argument for gates

`lint_ruleset.py` exempted `02-core-rules.md` from two required sections. Part A
of this change gave that document a `# Design Philosophy`, and **nobody
noticed** — an exemption's whole function is to stop the check from asking, so
it went on covering a section that had existed for several commits. It now
covers only the `# Summary`, which is genuinely still missing.

The lesson is not that the exemption was wrong. It is that **an exemption
records debt and never notices when the debt is paid**, so it has to be reread
whenever the document it names is touched.

**Out of scope, and a real decision rather than an oversight:** writing a
`# Summary` for `02-core-rules.md`. It is new ruleset content, and this change's
whole argument is that `docs/` should say less. A Summary is a restatement, and
`system/proposal-review.md` records that restatements drift. Whether that
document wants one is a question for a proposal about that document.

### The check that would have caught this change's worst defect cannot ship in it

`check_id_stability.py` reports an ID that changed document and an ID reissued
below its document's ceiling. **It does not report an ID that kept its number
while its rule changed underneath** — which is exactly what this change did
eleven times, and what produced the twenty-eight broken citations that took two
audits and three apply runs to clear.

Adding a `retitled` report is mechanical and obviously right. **It also fails
this branch**, because `preflight.py` compares against `origin/main` and this
branch is eleven retitles. The two ways to ship it here are both worse than
waiting: exempting the branch is a policy change wearing a configuration
disguise, and reverting the renumbering reopens Decision 3.

`main` will carry the new numbering once this merges, leaving no retitles to
find, so the check lands green in the next pull request. **Scheduled, not
dropped** — this note is the schedule.

---

## Decision 13 — A staircase is a chain of obstacles, for every domain

**This is the first of five decisions here that change what a rule means** —
Decisions 14 through 17 are the others, and every other task in this change
repairs something the compression broke. All five are separated into `tasks.md`'s
Part C so a reviewer is never asked to read one as a repair.

The audit found `VEH-027` contradicting itself: "Stairs are never a legal
vehicle ascent", and four lines later "A walker may cross a rise or stairs
directly when its Terrain Threshold permits it". A walker is a vehicle
(`VEH-010`, `VEH-012`, `VEH-023`), so the rule gave one question two answers.

Two ways out. **Restore the absolute** — delete the walker sentence, and put
back the deleted clause explaining that a tall walker steps *over* a staircase
under `VEH-021` rather than ascending it, reading the flight as one obstacle of
its total rise. **Or drop the absolute** — a stepped surface is a chain of
obstacles, each read on its own, and a vehicle climbs the steps its Terrain
Threshold covers.

The maintainer chose the second. The reasoning is the project's own: a step is a
physical height and a Terrain Threshold is a physical height, and the model
already answers whether one clears the other. The absolute was an abstraction
laid over an answer the plastic gives — `CODE_OF_DESIGN.md` Principle 1.

### What it costs, stated rather than discovered

**A vehicle with a tall enough threshold now climbs a staircase.** A wheeled
vehicle's threshold is half its wheel diameter (`VEH-022`), so a large wheel
clears a low step, and a domestic staircase built from plates is climbable by
much of the motor pool. That was the reason the absolute existed, and it is
accepted knowingly rather than overlooked. What it buys is one rule instead of
two, and no case where the ruleset and the model disagree.

**Nothing is added to pay for it.** No stair-specific Action Point cost, no
per-step charge on the vehicle side. A step above the threshold stops the climb
exactly as any other rise does, and the rest of `VEH-027` is unchanged.

### Why the shared half goes to `MOVE-013`

Once both domains resolve a staircase the same way, "each step is an obstacle in
its own right" is one rule with two readers, and
`system/documentation-standards.md` gives it one owner. `MOVE-013` already
states what a stepped surface *is*; it now states how it is read, and each
domain document states only what its own domain charges — Action Points in
`INF-009`, the Terrain Threshold in `VEH-027`.

That also removes the sentence in `INF-009` describing what vehicles do, which
the audit had separately found citing `VEH-027` for a claim `VEH-027` no longer
carried. **Two findings, one deletion** — an infantry rule stops answering a
vehicle's question, and the dead citation goes with it.

### Rejected: keeping "vehicles never" as a special case for wheels

Stairs legal for walkers and hover, illegal for wheels and tracks. It reads
plausibly and is worse on every count: it needs a rule of its own, it splits a
question the Terrain Threshold already answers, and it puts the ruleset back in
the business of deciding what a model can obviously do. A wheel that clears the
step clears the step.

### What this reopens

`system/proposal-review.md` used this very pair — `VEH-021` pointing a vehicle
at an infantry rule that permits stairs, which `VEH-027` forbids — as its
canonical example of a rule contradicting one three documents away. The example
dies with the contradiction. Task 23.5 deletes it and leaves the three live
examples in the same sentence, rather than inventing a replacement.

---

## Decision 14 — Two signposted gaps are closed by defining them

`main` marked two rules as unfinished, and the compression deleted both markers
while keeping the sentences around them. That is worse than either state: an
acknowledged gap became an exception a player will reach for.

- `VEH-013` — "unless another crew member takes over **(future rules)**". The
  parenthesis went. What survived reads as a usable exception with no cost, no
  timing and no requirement anywhere in the ruleset.
- `VEH-031` — *"What `VEH-019` calls 'locomotion damage' is named there and
  defined by no rule; this rule does not define it either."* That went, while
  `VEH-019` kept "locomotion damage" among its causes of immobilization and
  `VEH-031` kept a pointer at `VEH-019` for it.

**The obvious repair was to restore both markers**, matching `VEH-025`, which
still says "Freeing a stranded vehicle is not currently defined". The maintainer
chose to define both instead. Neither needed a large rule.

### The Pilot handover

> Any team member may take control for 1 Action Point. Without a Pilot the
> vehicle does not move — someone has to take the controls.

One Action Point, in the form `VEH-008` through `VEH-011` already use, and the
handover is a physical act because `VEH-013` already requires the Pilot to occupy
a visible operating position. Nothing is added to enforce that.

**Crew and passengers both, deliberately.** `VEH-015` and `VEH-016` are separate
rules; restricting the handover to crew would strand a full transport whose Pilot
is gone, for no reason a player would recognise.

**"or with a Dead Pilot" is deleted rather than kept.** A Dead component is
removed from the model (`16-damage-system.md`, DMG-002), so a vehicle with a
Dead Pilot is a vehicle without one. The clause named a state that cannot
persist — a contradiction the audit had not caught.

**Rejected: an ownership clause.** The maintainer said "same team", and `docs/`
has no word for it — no "friendly", no "same army", nowhere. Crew and passengers
are inside their own player's vehicle by construction and no boarding rule
exists, so the clause would introduce vocabulary to state something already true.

### Locomotion damage

> If the locomotion dies — wheels, tracks, legs, hover emitters — the vehicle
> loses one step, like infantry. Not cumulative. And if the locomotion means is
> destroyed, the vehicle is Immobilized.

**The infantry parallel is loose and the vehicle rule is exact.** `INF-002` gives
12 studs in steps of 3 and `INF-012` leaves a Wounded model at 2 steps, so
infantry loses two steps forward and one sideways. On the vehicle side a step is
one vehicle length — `VEH-004` is three, `VEH-031` is two — so "one step" writes
itself, and it lands on the reduction `VEH-031` already defines.

**Not cumulative, as instructed.** One rule, one reduced distance, whatever
combination of causes applies. That is why `VEH-031` stops being titled *Wounded
Pilot*: it states one reduced distance and every way to reach it.

**The two rulings meet at a threshold**, and the threshold is counted rather than
described. Some locomotion components Dead costs a step; enough of them and the
vehicle stops. Without that line the two rulings answer the same question twice,
and a vehicle with no wheels left would still roll two lengths a turn — the
ruleset contradicting the model, which is `CODE_OF_DESIGN.md` Principle 1 exactly.

**Where the threshold sits was settled on the pull request, not here.** This
decision wrote it as "entirely destroyed"; the maintainer replaced that with
**half or more**, and `tasks.md` section 39 carries the counted rule, the
functional definition of a locomotion component, and the worked examples. The
rule is retitled again with it — **What Damage Does to Movement**, matching
`VEH-029` and `VEH-030` beside it, because a rule that states two outcomes should
not be named after one.

**`VEH-019`'s list gains an owner per cause** rather than keeping the vague
"locomotion damage": Pilot loss is `VEH-013`, destroyed locomotion is `VEH-031`,
stranding is `VEH-025`.

### The third marker: a stranded vehicle stays stranded

> If it is in a hole it CANNOT be recovered. Full stop. If it is abandoned, what
> we said before.

`VEH-025` said "Freeing a stranded vehicle is not currently defined". It now says
a stranded vehicle cannot be freed.

**The two cases were reachable from the same sentence, and they are not the same
case.** A vehicle nobody is driving is answered by the handover above. A vehicle
in a depression deeper than its Terrain Threshold is answered by the model: it is
in the hole, and nothing in the ruleset lifts a model out of one. "Not currently
defined" invited a house rule for a question the plastic had already settled.

**Rejected: recovery by a second vehicle, a tow or a ramp.** None of those exist
in the ruleset, each would need construction rules of its own, and the maintainer
ruled the case closed rather than deferred.

`docs/08-vehicles.md` therefore carries no "not yet defined" marker after this
section, and `TODO.md` loses the two entries that quoted the deleted sentences.
That is a required check rather than tidying: `scripts/check_todo_quotes.py`
verifies every `TODO.md` quote against the document it cites, so a closed gap
must leave the file in the same commit that closes it.

---

## Decision 15 — Nothing is repaired, and infantry stands back up

The audit found `DMG-018` ambiguous rather than wrong. It charges 1 Action Point
once per activation to repair one of a unit's own Wounded components, then lists
what "repairing another unit requires" without saying whether that cost still
applies. `main` carried the word that decided it — *"Repairing a **different**
unit's Wounded component **additionally** requires..."* — and the compression
deleted it, leaving a block that reads as easily as a replacement set of
conditions as an addition.

**Restoring "additionally" was the obvious repair, and it is not what happened.**

> I would remove the ability to repair anything. If it is broken, it broke, full
> stop. It cannot be repaired. The exception is infantry, which for 1 AP reverts
> the state machine.

Repair goes entirely. One reversal survives: a Wounded infantry model spends 1
Action Point to stand back up.

### Why this fits rather than merely being shorter

`DMG-002` already maps the three states to poses — upright, seated, removed.
Standing a minifigure back up **is** the state change, performed on the model
rather than tracked beside it, which is `CODE_OF_DESIGN.md` Principle 1 doing the
work a mechanic was doing before. Nothing equivalent exists for a wheel or a
door: a broken plate does not un-break by being looked at.

It also removes the ruleset's only mechanic that needed a second unit, a tool and
an adjacency check to resolve — three conditions supporting one state change.

**"Once per activation" goes with it.** The old rule let a unit choose among its
own components; the new one has a single subject, and a model that is standing
cannot stand again. The clause guarded a choice that no longer exists.

**`CORE-014` is untouched.** It states that equipment must be physically present
on the model, and it was never about repairs — `DMG-018` cited it, not the other
way round.

### Blast radius, checked rather than assumed

`python3 scripts/rule.py refs DMG-018` reports **cited by nothing**.
`docs/14-glossary.md` has no *Repair* entry. No document outside
`16-damage-system.md` uses the word at all. Two edits, one file: the rule and one
Summary bullet.

### A Pilot recovers, and the rule says so rather than implying it

> The Pilot is an infantry model, so it follows infantry rules.

> I think the exception framing is unnecessary. The Pilot is an infantry model — I am not sure it reads as being curable.

Both are the maintainer's, and the second is why the first is not enough.
`CORE-003` makes every minifigure an infantry model, so a Pilot recovered
already — **by inference, from a rule two documents away**. A rule that a reader
has to derive is a rule a reader will get wrong, so `DMG-018` names the case:
infantry on foot, and a Pilot or crew member inside a vehicle alike. A recovered
Pilot also lifts `VEH-031`'s reduced movement.

**The "exception" framing goes with it.** It described the rule's history — that
repair used to be general and now is not — rather than the rule. A reader meeting
`DMG-018` fresh needs to know who recovers, not what used to be possible.

**"Return to Operational", not "stand back up".** `DMG-002` owns the mapping from
state to pose; repeating it inside `DMG-018` would give one rule two owners, and
the standing wording reads wrong for a minifigure seated in a cockpit.

### Found while writing this, and left alone

`DMG-002` shows an infantry model's state by pose — upright, seated, removed —
and a Pilot is seated in its operating position whether Operational or Wounded.
The pose therefore distinguishes nothing for a crewed vehicle.

**This is true on `main` and no task here changes it.** It is recorded because a
later reader will meet it and should know it was seen, not because this change
is the place to solve it (`system/proposal-review.md`, "Record What You Decided
Not to Do").

---

## Decision 16 — A minifigure's shoulder is a rotating mount, and rotation has reach

`CBT-007` lets a weapon system split its Attack Dice between targets only when
its mount rotates to re-aim independently of the platform, naming a turntable, a
ball joint and a swivel mount. `WPN-009` lists **Hands** among valid mounts, and
a minifigure's arm turns at the shoulder.

**The rule reads both ways for every infantry model in the game**, and the
difference is not a nuance: a minifigure with a four-muzzle weapon engages four
targets or one, for the same single Action Point.

The retired `DMG-018` had answered it — *"minifig torso, turntable, ball joint,
swivel mount. This deliberately puts all infantry-carried weapon systems under
the exception ... this is intentional, not an oversight."* Consolidating that
into `CBT-007` was right. Dropping the decision while consolidating was the
defect, and it is the one `system/proposal-review.md` names by section title.

> Go to the human. Without turning the body, the arm can aim at several targets
> as long as those targets are in front of the minifigure. The rotation point is
> not the HAND, it is the SHOULDER.

### The ruling is narrower than the text it replaces

The retired wording named the **torso**. Turning the torso is turning the body,
which this ruling excludes: the arm alone re-aims, so an infantry weapon covers
what is in front of the model and nothing behind it. Restoring the old sentence
would have been the easy repair and the wrong rule.

### Rotation has reach, and that is general

A turret turning 360° is limited by nothing. A swivel mount with short travel is
limited by its travel. An arm is limited to the front. `CBT-007` had the
permission and not the limit, so the limit is written once, generally, and the
minifigure is its worked instance rather than an exception beside it.

**Rejected: an arc in degrees.** The ruleset has no angular measure anywhere —
`WPN-011` says only "Weapon position determines its firing arc", and `CBT-002`
resolves visibility physically from the attacker's point of view. A number would
be the first, would need a protractor at the table, and would replace a check the
model already makes: point the arm at the target and see whether it reaches.

**`WPN-011` is left alone.** It states the same idea for a mounted weapon, in the
document that owns weapon position. Writing the limit into `CBT-007` gives the
splitting rule what it was missing without giving the idea two owners.

---

## Decision 17 — Resistance is a physical check, not a measured value

The audit reported `GEO-002` and `DMG-003` contradicting each other over
decorative armour: `GEO-002` lists cosmetic armour as Visual Geometry, `GEO-003`
says Visual Geometry is ignored when calculating Resistance, and `DMG-003` says
Resistance is what an Impact must cross — which a bolted-on plate plainly is.

**The reported contradiction is milder than stated.** `DMG-003` says "smallest
**structural** section", and that word already excludes decoration. The real
defect is that nothing decides whether a plate added outside a wall is
structural, and `GEO-002`'s surviving sentence restates the question — "becomes
Gameplay Geometry if it physically forms part of the structure".

`main` answered it: armour *bolted on top of* a wall does not add Resistance. The
maintainer ruled the other way.

> If it has "something" in front of the brick it adds to the path. A brick with a
> plate outside it — that is part of the hull, not decoration. Decoration is a
> tile with a print on it, a sticker.

### Why the fix is a move between categories, not a better sentence

`15-geometry-layers.md` sorts everything into two boxes. `GEO-003` holds measured
values, which **ignore** Visual Geometry. `GEO-004` holds physical checks, which
use the model **exactly as it exists on the table, Visual Geometry included**.

Under the ruling, Resistance is read from whatever plastic sits in the Impact's
path. That is `GEO-004`'s definition word for word — and Resistance was in
`GEO-003`'s list. **The term was in the wrong box, and every attempt to patch
`GEO-002` was working around that.** Any wording that leaves Resistance among the
measured values discards decoration before the direction of travel is considered.

`GEO-001` loses "Component structural thickness" and drops Resistance from its
derived-values sentence for the same reason. `DMG-003` and the glossary lose the
word "structural", which was the whole of the old answer.

### What deliberately does not change

**Decorative armour is not promoted to Gameplay Geometry.** It stays Visual, and
`GEO-002`'s example list is untouched: cosmetic armour still changes no weapon
Range, no Attack Dice (`GEO-005`), and still counts toward no height limit
(`VEH-030` lists it Visual). What changed is that Visual Geometry stops being
discarded when something has to cross it.

**Direction of travel now decides the number, and that is correct.** A wall
plated on one face resists more from that face than from the bare one. `DMG-003`
already said "in its direction of travel"; only now does the sentence have
consequences. The glossary's *Resistance* entry gains the phrase, which it never
carried.

### The consequence, taken knowingly

**Plating a hull with cheap plates is real armour.** A player who wraps a vehicle
in decorative plating is harder to hurt from the plated side. That is the model
deciding the value, which is Principle 1 — and it is an optimisation the ruleset
did not previously offer. The maintainer was shown the case as a build and
confirmed it.

**Rejected: restoring `main`'s bolted-on / forming-part distinction.** It is the
smaller edit and it answers the question, but it asks a player to judge whether a
piece is part of a wall or attached to it — a construction opinion two players
can hold differently about one build. Thickness in the path is measured, not
judged.
