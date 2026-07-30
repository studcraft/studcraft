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
