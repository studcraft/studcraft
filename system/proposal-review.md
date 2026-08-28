# Proposal Review

Every proposal here gets an explicit review pass before it is applied, and
again on the applied text before archiving. This is what that pass looks for.

---

# The Scope and the Checklist Are Computed, Not Decided

```bash
python3 scripts/review_scope.py <change-name>
```

It prints what the review reads — the rules the change names, the rules that
cite them, the Summary of every document touched, the glossary entry of every
term touched, **the spec deltas it ships, and the retired IDs worth a
repository-wide grep** — and the numbered checklist to answer. **Two reviews of
one change read the same text and answer the same questions**, which is what
deciding both per invocation used to prevent.

The last two are there because nothing else prompts them. A delta is written
against `docs/` at proposal time and read again only at archive time, weeks
later; and a retired ID is invisible to both `scripts/lint_ruleset.py`, which
reads `docs/` and `assets/IMAGES.md`, and `scripts/rule.py`, which reads an
index built from `docs/`.

**Every item gets a verdict**: `CLEAN`, `FINDING`, or `N/A` with the reason. An
item nobody answered is indistinguishable from an item nobody checked, and
"what I checked and found clean" written as prose is where a skipped class
hides.

The sections below say why each class recurs; the script holds the list to
walk. **Adding a class here means adding a line to `CHECKLIST` in the script**,
or the review stops covering it.

**A review ends when a pass returns no finding above an observation.** A second
pass returning new blockers means the first was incomplete or the scope moved
after it ran — `system/delegating-to-agents.md` forbids the second, so report
which it was.

---

# Review Against the Shipped Ruleset, Not Just Internally

A proposal can be perfectly self-consistent and still contradict a rule that
already shipped. Every real contradiction found here came from not
cross-checking siblings: a new muzzle-adjacency rule against the rule already
governing muzzle placement, a new dice-distribution rule against the one
already splitting Attack Dice, "Visual Geometry is always ignored" against the
two Core Rules that read the physical model.

**Before applying, read every document the subject matter touches, not just the
ones the proposal cites.** Weapons means combat and melee too; damage means
combat, melee and vehicles. The contradiction is almost never in the document
the proposal is about. Grep repo-wide, not scoped to the obvious neighbours — a
vehicle rule restated the universal Weapon System rules for years and only a
repo-wide grep caught it.

---

# Common Failure Classes

Look for these specifically. They recur.

- **Dangling cross-references** — a doc cites a section name that exists
  nowhere in the change's own artifacts.
- **A retired rule ID still cited from outside `docs/`** — grep the whole
  repository before deleting a rule. `scripts/lint_ruleset.py` reads only
  `docs/` and `assets/IMAGES.md`, and `README.md`, `CODE_OF_DESIGN.md`,
  `TODO.md`, `scripts/` and `system/` all cite rule IDs. Archived changes
  under `openspec/changes/archive/` are history and are left as they are.
- **A changed rule's own ID never grepped, only the ones it retired** —
  `action-points-have-one-owner` emptied one rule and wrote into another, and
  `TODO.md` quoted both; `check_todo_quotes.py` is a required check, so the
  stale quote is a red gate, not a reading defect.
- **A duplicate in a document that defines no rules** — `01-foundations.md`
  held a fourth copy of the list that change was deduplicating and was never
  opened, because the sweep looked for rules; it and `14-glossary.md` define
  none and restate plenty.
- **Absolute claims falsified by a later fix** — once you make one exception
  explicit, re-scan for every place the old absolute claim still stands
  unqualified.
- **The same rule asserted twice in two documents** — a combat rule and a
  materials rule both said "prefer physical representation" until the materials
  document was removed. A proposal touching either is the moment to
  consolidate, not to add a third near-duplicate.
- **A task referencing a spec section that was never written** — grep the spec
  files for a section name before trusting a task that cites it.
- **Requirement order not matching the described sequence** — if the design
  says A then B then C, the spec's Requirements appear in that order.
- **A new rule-bearing document with no namespace, or a reused one** — run
  `scripts/lint_ruleset.py` after writing it.

After fixing, re-read the whole change. A fix can expose another defect.

---

# The Principles That Catch Defects Here

`CODE_OF_DESIGN.md` holds fifteen, and every rule is measured against all of
them. These six account for most findings in this repository:

- **Principle 1 — The Model Is The Rules.** Does the rule take a label at its
  word where it should be checking the plastic?
- **Principle 7 — One Universal Measurement.** Is the value in Unit Bases, or
  has the rule wandered into raw studs, millimetres or an invented unit?
- **Principle 11 — Simplicity Before Complexity.** A subsystem where a
  criterion on an existing category would do?
- **Principle 12 — Consistency.** Solved differently from the way the same
  problem was solved elsewhere?
- **Principle 13 — Build Freedom.** A fixed number the model should be
  deriving?
- **Principle 15 — Future Compatibility.** A damage or resolution path parallel
  to the Impact system rather than inside it?

The **Design Checklist** closing `CODE_OF_DESIGN.md` applies too: any "no" is
worth raising even where no single principle is squarely violated.

---

# What an Audit Reports, and What It Does Not

Findings first, ordered by severity. Each names **where** — file, rule ID, line
or task number; **what** the defect is, in one sentence; **why** it is a defect
— the principle, standard or failure class it violates; and **what it would
take to fix**, in one sentence. A finding that cannot name what it violates is
a preference: drop it, or label it an observation.

Then state what was checked and found clean. An audit that reports only
problems leaves the reviewer unable to tell thoroughness from luck. Finding
nothing is a result — say what was looked at, and never manufacture a finding
to justify the run.

## Size the Fix Before You Rank the Finding

**Find the repair before writing the severity down.** A defect fixed by one
heading level is not a blocker, whatever the symptom looked like from the other
end. Sizing costs one search, and it is the difference between "the ruleset has
no concept of a unit" and "one chapter lists a rule that is not one" — the same
gap, reported twice, with opposite consequences for whoever reads the report.

It also decides what a gap *is*. This ruleset is executed by a person holding a
build, not compiled: it may leave to common language what a specification would
have to close. The section below ranks by whether a reader can proceed; sizing
is how you find out.

## Silence Is Not Contradiction, and They Are Not the Same Severity

**Two rules that disagree, and one question no rule answers, are different
findings.** Say which one you have.

A contradiction quotes both sides. If a finding claims the ruleset states two
incompatible things, the report carries the two passages and they must
*actually* be incompatible as written — not once a reasonable assumption is
added to one of them.

Where a passage only supports the finding under a particular reading, **say
what the reading assumes and what text would settle it.** A rule that is silent
on who acts does not take a side by being silent, and reporting it as though it
did makes an argument look like a conflict.

This is written down because an audit reported that "the two readings are both
anchored in the shipped text" when one of them rested on an assumption no rule
stated — that only a transport may open its own ramp. The gap it found was real
and the evidence for one half was not, which cost the maintainer a verification
the report should have made unnecessary.

Silence usually matters less, and not always: a question asked on every attack
is worse than a contradiction between two rules nobody reaches. Rank by how
often a reader meets it and whether they can proceed without an answer, and say
which of the two you are ranking.

Out of scope for every audit here:

- **Balance.** This ruleset has no points system by design; deployment size in
  Unit Bases does that work.
- **Rewriting.** The reviewer decides. Suggest a direction in one sentence
  where it is obvious; never draft replacement rule text unless asked.
- **Style.** Report formatting only where it changes meaning or breaks a stated
  standard.
- **Versions.** `docs/*.md` defaults to a minor bump computed by
  `scripts/release_cut.py`, and a required check already blocks a PR that
  touches a `**Version:**` header.

---

# Review the Applied Text, Not Only the Diff

**Every review pass here that found something real found it by reading the
result.** The pattern held every time: the execution was faithful and the
proposal was wrong.

Verification greps confirm instructions were followed. They cannot see that a
correctly-inserted paragraph now reads as part of the wrong example, that two
paragraphs now say the same thing, or that a rule now contradicts one three
documents away. All of these were found only by reading the file end to end: a
rule's closing paragraph displaced three times by later examples; a new
movement table reintroducing another rule's footprints as a parenthetical.

After applying, read every rule the change touched in full, plus the rules it
cites and the document's Summary. Budget for it: it is where the findings are.

---

# The Summary Is Part of the Rule

A document's `# Summary` restates the rules above it and nothing enforces that
it stays true. It has gone stale after almost every substantive change — one
Summary omitted every AP cost and listed "five principles" that had become six;
another still charged a flat Action Point for an action whose rule had become a
cost per Unit Base.

**Any change touching a rule checks that document's Summary and its glossary
entry in the same pass.** Both are restatements, and restatements drift.

---

# Record What You Decided Not to Do

Reviews here have repeatedly re-proposed ideas already considered and rejected,
because nobody wrote down the reason — one re-proposed a reordering that had
been applied and reverted days earlier.

A rejection and its reasoning belong in `design.md`, and if the question will
recur for a reader of the ruleset, in the rule itself: keep the superseded thing
visible and say why, rather than leaving a clean surface that invites the same
suggestion again.

---

# Verify the Number, Not Just the Direction

**If a proposal or rule states a count, recompute it mechanically before
merging.** One proposal claimed nineteen defects while listing twenty-two, with
category headers summing to a third number. The same goes for worked examples:
a rule saying "a weapon reaching 90 studs" uses a figure its own table shows.

---

# Multipliers Set Early Get Falsified by Numbers Added Later

A vehicle movement multiplier and a weapon range multiplier were both reasonable
when written and both wrong once the infantry, weapon-capacity and Unit Base
rules existed to check them against: an infantry weapon reaching 8 studs against
a 12-stud move, a motorbike slower than a walking soldier, half-stud distances
on a stud grid.

**When a change adds a number, check it against every number it can be compared
with** — especially movement against range, and any multiplier against the
granularity of what it multiplies.

---

# Do Not Cap What the Model Already Bounds

The instinct to add a maximum is usually wrong here. Nothing is unconditionally
invulnerable; a component is only safe from whatever cannot be mounted on the
attacker's current platform.

Look for the chain that already exists. For weapon Range it is complete, and
every link is read from the model or agreed by the players:

```
Range ≤ a multiple of Weapon Length
      ≤ a multiple of Platform Length
      ≤ what fits the agreed Deployment Volume
      ≤ the battlefield agreed before the forces were built
```

What is worth adding instead is a paragraph in `docs/` stating the chain with
its current multipliers, so a reader who computes an alarming figure finds the
answer where they already are.

---

# Delta vs. Direct Edit

A `MODIFIED` or `REMOVED` delta can only target a capability that already
exists under `openspec/specs/`. Several ruleset documents (`11-combat.md`,
`03-game-flow.md`, ...) predate the OpenSpec workflow and were
never formalised, so there is nothing to delta against.

- **Do not invent a delta against a capability that does not exist.**
- Track the change as an ordinary doc-edit task in `tasks.md`, and explain the
  reasoning in `design.md`.
- If the proposal introduces a genuinely new capability that overlaps such a
  document, only the new capability gets `openspec/specs/` entries. The old
  document does not become tracked because a proposal touched it.

---

# Capability Boundaries Don't Have to Match Document Boundaries

One change can introduce several capabilities and still ship as a single
`docs/*.md`. `weapon-construction-system` shipped two capabilities as
`10-weapons.md`; `component-damage-system` shipped two as `16-damage-system.md`,
because Resistance is meaningless without the Geometry Check that reads it.

**Default to one document per proposal** unless the capabilities are
independent enough that a reader would want one without the other. Splitting
"because there are two capabilities" forces a reader to jump between files to
follow one mechanic.
