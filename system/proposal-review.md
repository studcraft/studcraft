# Proposal Review

Every OpenSpec proposal in this repo has gone through at least one explicit
review pass — for omissions, contradictions, and repetitions — before being
applied, and again after applying, before archiving. This document captures
what that review looks like and why, so it happens by default instead of only
when someone remembers to ask for it.

---

# Review Against the Shipped Ruleset, Not Just Internally

A proposal's own proposal/design/specs/tasks can be perfectly self-consistent
and still contradict `docs/*.md` content that already shipped. Every real
contradiction found in this repo's proposals so far came from **not**
cross-checking against sibling documents:

- `weapon-construction-system`'s new muzzle-adjacency rule directly
  contradicted the already-shipped `WPN-007` (mandatory muzzle separation) —
  invisible if you only read the new proposal's own artifacts.
- `component-damage-system`'s new "Weapon Distribution" rule directly
  contradicted the already-shipped `CBT-007` (no splitting a weapon system's
  dice across targets) — same failure mode, different document.
- `gameplay-visual-geometry`'s "Visual Geometry is always ignored" directly
  contradicted the already-shipped `CORE-008`/`CORE-010` (true line of sight —
  the whole physical model matters, decoration included).

**Before applying a proposal, read every existing document its subject matter
touches, not just the ones the proposal itself cites.** If the proposal is
about weapons, also read combat and melee. If it's about damage, also read
combat, melee, and vehicles. The contradiction is almost never in the
document the proposal is about — it's in the neighboring one nobody thought
to open. This isn't limited to the "obvious" neighbors either: `VEH-014`
independently restated `WPN-008`/`CBT-006`'s "Weapon System" concept for
years before a repo-wide grep (not a weapons/combat-scoped one) caught it —
scope the search to every document, not just the ones that seem related.

---

# Common Failure Classes (found repeatedly, look for these specifically)

- **Dangling cross-references**: a design/proposal doc cites a section name
  (`"see Design Consequences below"`, `"DMG-023-equivalent"`) that doesn't
  actually exist anywhere in that change's own artifacts.
- **Absolute claims that get quietly falsified by a later fix**: fixing one
  contradiction (e.g. "Visual Geometry does affect Line of Sight") can
  silently break an earlier absolute statement elsewhere in the same
  proposal ("Gameplay is identical" for functionally-equivalent models). Once
  you make one exception explicit, re-scan the whole document for other
  places the old absolute claim still appears unqualified.
- **Same rule asserted twice, independently, in two different documents**:
  e.g. `CBT-009` and `MAT-017` both said "prefer physical representation"
  in nearly identical words, predating any of the proposals in this repo.
  A new proposal that touches either document is the natural, low-risk
  moment to consolidate into one canonical statement instead of adding a
  third near-duplicate on top.
- **`tasks.md` or `proposal.md` referencing spec sections that were never
  written**: e.g. a task instructs "add Select Target Component per
  specs/X/spec.md" when no such Requirement exists in that file. This
  happens when a section gets renamed or reorganized in one artifact but
  not the others — always grep the actual spec files for a section name
  before trusting a task that references it.
- **Requirement ordering that doesn't match the actual sequence**: if a
  design lists steps as "A then B then C," the spec's Requirements should
  appear in that order too. A resolution-sequence spec with steps listed
  out of order reads fine on its own but is misleading against the
  narrative that describes the sequence.
- **New rule-ID-bearing document never gets a namespace, or reuses one**:
  every `docs/*.md` file that defines rules needs its own stable prefix
  (`WPN-`, `CBT-`, `DMG-`, ...) — check `scripts/lint_ruleset.py`'s output
  after writing a new document, not just after editing existing ones.

Iterate: after fixing found issues, re-read the whole change again. A fix for
one contradiction can introduce or expose another (see the "absolute claims"
failure class above) — don't stop at the first clean pass if the artifacts
changed since you started reading.

---

# Review the Applied Text, Not Only the Diff

Every review pass in this repo that found something real found it by reading
the *result*, not the change. Across four audit rounds and three external
reviews, the same pattern held every time: **the execution was faithful and
the proposal was wrong.**

Verification greps confirm that instructions were followed. They cannot see
that a correctly-inserted paragraph landed somewhere that now reads as part of
the wrong example, that two paragraphs now say the same thing, or that a rule
now contradicts one three documents away. Examples, all found only by reading
the applied file end to end:

- `VEH-021` told a blocked vehicle to use "a legal access point (MOVE-011)".
  `MOVE-011` is the infantry rule and its list includes stairs, which
  `VEH-027` — added in the same change — says vehicles may never use.
- `MOVE-016` ended up stating "each die is a Damage Roll" twice, because one
  task inserted a paragraph and another edited a pre-existing one that already
  said it.
- `DMG-004`'s closing paragraph, which comments on Examples 3 and 4, was
  displaced three times as later examples were each inserted ahead of it.
- A new `VEH-004` example table reintroduced `VEH-001`'s footprints as a
  parenthetical — the exact duplication class this repo has spent several
  changes removing.

After applying, read every rule the change touched in full, plus the rules it
cites and the document's own Summary. Budget for it: it is where the findings
are.

---

# The Summary Is Part of the Rule

A document's `# Summary` restates the rules above it, and nothing enforces
that it stays true. It has gone stale after almost every substantive change:
`07-movement.md`'s omitted every AP cost while listing "five principles" that
had become six; `08-vehicles.md`'s listed five physical characteristics after
terrain capability became a sixth; `09-transport.md`'s still said "Embarking
costs 1 AP" after the rule changed to 1 AP per Unit Base.

Any change touching a rule must check that document's Summary, and its
glossary entry, in the same pass. Both are restatements, and restatements
drift.

---

# Record What You Decided Not to Do

Reviews on this repo have repeatedly re-proposed ideas that had already been
considered and rejected, because nobody wrote down the reason. One external
review asked to delete the material list from `DMG-008`; another proposed
capping Impact Strength. A later self-review re-proposed reordering
`10-weapons.md`'s Summary — a change that had been *applied and then reverted*
days earlier, for reasons that were not recorded anywhere a reader would look.

When a proposal rejects an option, the rejection and its reasoning belong in
`design.md`, and if the question will recur for a reader of the ruleset
itself, in the rule. `MEL-010`, `CBT-011` and `WPN-021` all do this: they keep
the superseded thing visible and say why it was superseded, rather than
leaving a clean surface that invites the same suggestion again.

---

# Verify the Number, Not Just the Direction

Counts stated in prose go stale the moment anything is added. A proposal
claiming "nineteen defects" while its own list held twenty-two, and category
headers summing to a different total again, both shipped in drafts of the same
change. So did a coverage table that had gained a row without its intro
sentence following.

If a proposal or rule states a count, recompute it mechanically before
merging. The same applies to worked examples: a rule that says "a weapon
reaching 90 studs" should use a figure its own table actually shows.

---

# Multipliers Set Early Get Falsified by Numbers Added Later

`VEH-004`'s `1.5×` and `WPN-005`'s `× 2` were both reasonable when written and
both wrong by the time `MOVE-004`'s 12-stud infantry move, `WPN-004`'s Platform
Length cap and `CORE-001`'s Unit Base orientation existed to check them
against. Measured together they produced: an infantry weapon reaching 8 studs
against a 12-stud move, so nothing could be engaged before it closed; a
motorbike slower than a walking soldier while costing twice the Deployment
Area; and half-stud distances on a stud grid.

None of those is visible from inside the rule that causes it. When a change
adds a number, check it against every other number it can be compared with —
especially movement against range, and any multiplier against the granularity
of the thing it multiplies.

---

# Do Not Cap What the Model Already Bounds

The instinct to add a maximum is usually wrong here, and `WPN-021` already
wrote the argument: *"No component is unconditionally invulnerable; it is only
safe from whatever can't be mounted on the attacker's current platform."*

Before adding a cap, look for the chain that already exists. For weapon Range
it is complete and every link is either read from the model or agreed by the
players:

```
Range ≤ 6 × Weapon Length ≤ 6 × Platform Length (WPN-004)
      ≤ what fits the Deployment Area (SCS-003, DEP-003)
      ≤ the battlefield agreed first (FLOW-001, step 2)
```

A cap would also contradict a decision the ruleset already made one rule away.
What is worth adding instead is a paragraph stating the chain, so a reader who
computes an alarming figure finds the answer where they are already reading
rather than reconstructing it.

---

# Delta vs. Direct Edit

An OpenSpec `MODIFIED` (or `REMOVED`) delta can only target a capability that
already exists under `openspec/specs/<capability>/spec.md`. Several of this
repo's ruleset documents (`docs/11-combat.md`,
`docs/04-construction-standard.md`, ...) predate this repo's OpenSpec
workflow entirely and have never been formalized as capabilities — there is
nothing to write a delta against.

When a proposal needs to change one of these documents:

- Do not invent a delta against a capability that doesn't exist.
- Track the wording change as an ordinary doc-edit task in `tasks.md`,
  same as any other direct edit, and explain the reasoning in `design.md`'s
  Decisions section (what changed, and why the old wording is now wrong or
  incomplete).
- If the proposal introduces a genuinely new capability that happens to
  overlap with one of these un-formalized documents, only the new
  capability gets `openspec/specs/` entries when archived — the old
  document doesn't retroactively become a tracked capability just because
  a proposal touched it.

---

# Capability Boundaries Don't Have to Match Document Boundaries

An OpenSpec change can introduce multiple capabilities (`specs/<a>/spec.md`,
`specs/<b>/spec.md`, ...) while still shipping as a single reader-facing
`docs/*.md` file. `weapon-construction-system` shipped `weapon-construction`
and `weapon-capacity` as one `10-weapons.md`; `component-damage-system`
shipped `component-damage` and `damage-resolution` as one
`16-damage-system.md` (two labeled sections within it), specifically because
the two capabilities were too tightly coupled to read well split apart
(Resistance is meaningless without the Geometry Check that reads it).

Default to one document per proposal unless the capabilities are genuinely
independent enough that a reader would plausibly want one without the other.
Splitting into `docs/16-x.md` + `docs/17-y.md` "because there are two
capabilities" is not, by itself, a good reason — it forces a reader to jump
between files to follow one mechanic end to end.

---

# Archiving Order and Dependencies

If a proposal's `MODIFIED` delta targets a capability from a *different*,
not-yet-archived proposal, note that dependency explicitly as its own task
(see `system/workflow.md`, Archiving) — don't assume archive order will just
work out. `scripts/archive_cut.py` archives every fully-applied change in one
batch run, in directory-listing order, with no dependency resolution between
them; if change B's delta needs change A's capability to exist first and both
have fully-checked `tasks.md`, they'll still both get processed in the same
batch — check for this kind of ordering dependency before relying on a batch
run to sequence things correctly, or archive the dependency first in its own
manual `openspec archive <name>` run.
