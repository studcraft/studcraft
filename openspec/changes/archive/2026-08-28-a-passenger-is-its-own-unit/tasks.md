# Tasks — A passenger is its own unit

## How to read this file

Every edit below is an anchor pair: an exact substring that occurs once, and the
text that replaces it. `scripts/apply_tasks.py` performs them; nothing here is
transcribed by hand.

**The Action Point allotment is never printed.** `CORE-006` owns how many a unit
has (`action-points-have-one-owner`), and every block below cites it rather than
copying the number. A replacement block that names a figure is wrong.

**If a command disagrees with what a task expects, stop and report it.** Never
edit a document to make a verification pass.

---

## 1. `docs/02-core-rules.md` — CORE-005 leaves `# Unit Types`

- [x] 1.1 In `docs/02-core-rules.md`, replace this anchor:

```
## CORE-005 — Structures
```

with:

```
# CORE-005 — Structures
```

      One character. The rule keeps its ID, its document, its position in the
      file and every word of its body. `# Unit Types` is left holding `CORE-003`
      and `CORE-004`, which is two rules and satisfies the chapter rule in
      `system/documentation-standards.md`.

## 2. `docs/14-glossary.md` — a `Unit` entry

- [x] 2.1 In `docs/14-glossary.md`, replace this anchor — the file's closing
      lines:

```
---

> **Every Brick Matters.**
```

with:

```
---

## Unit

What activates and receives Action Points: infantry or a vehicle. A structure is not a unit. A model a vehicle carries is a unit of its own. See `02-core-rules.md`, CORE-003, CORE-004, CORE-005, CORE-006, and `09-transport.md`, TRN-021.

---

> **Every Brick Matters.**
```

      `docs/14-glossary.md` is in append order, so the entry goes last, and the
      body is one unwrapped line like every other entry in the file.

      **Both citations use the comma form, and that is load-bearing.**
      `lint_ruleset.CROSS_REF_RE` pairs a filename with the next `(ABC-000)`
      inside eighty characters, and a parenthesis holding several IDs matches
      nothing — so a parenthesised multi-ID citation followed by another
      filename hands its own IDs' place to that filename's. In that form this
      entry made the linter report `02-core-rules.md (TRN-021), which does not
      exist`. The comma form leaves no parentheses for that scan to reach, and
      `COMMA_REF_RE` captures every ID of both citations. `design.md`,
      Decision 3.

## 3. `docs/09-transport.md` — TRN-021

- [x] 3.1 In `docs/09-transport.md`, replace this anchor:

```
The number of levels a vehicle can contain is limited by its construction and deployment height agreement.

---

# Summary
```

with:

```
The number of levels a vehicle can contain is limited by its construction and deployment height agreement.

---

# TRN-021 — An Embarked Model Is Its Own Unit

A model a vehicle carries, or is about to carry, remains its own unit. It activates in its own right and receives its own Action Points (`02-core-rules.md`, CORE-006).

Those are the Action Points it spends to embark (`TRN-005`), to disembark (`TRN-006`), and to open or close the access point it uses (`TRN-008`).

While embarked it counts as part of its transport for Deployment Volume (`06-deployment.md`, DEP-006). Carried on the outside it is not embarked, and occupies its own (`08-vehicles.md`, VEH-030).

---

# Summary
```

      `TRN-020` is the highest number in the document, so `TRN-021` appends and
      the IDs stay strictly increasing. The title is not `Embarked Units`:
      `06-deployment.md` already has a rule of that name.

- [x] 3.2 In `docs/09-transport.md`, replace this anchor — the last two numbered
      principles of the Summary:

```
8. Closed transports protect passengers according to their construction.
9. Interior construction determines available capacity and access.
```

with:

```
8. Closed transports protect passengers according to their construction.
9. Interior construction determines available capacity and access.
10. A model a transport carries is its own unit and spends its own Action Points.
```

      Principles 5 and 6 state what embarking and disembarking cost. This states
      whose points pay, which is what the change settles, in the place a reader
      skims the costs.

## 4. `system/proposal-review.md` — sizing a finding

- [x] 4.1 In `system/proposal-review.md`, replace this anchor:

```
## Silence Is Not Contradiction, and They Are Not the Same Severity
```

with:

```
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
```

## 5. Verification

- [x] 5.1 `python3 scripts/lint_ruleset.py` — must **exit 0**. It checks rule IDs
      strictly increasing within a document, the chapter rule, and cross-document
      citation existence in both forms.

- [x] 5.2 `python3 scripts/check_id_stability.py` — must **exit 0**. No ID moves
      document and no retired number returns; `TRN-021` appends above `TRN-020`.

- [x] 5.3 `python3 scripts/rule.py doc 02-core-rules.md` — `# Unit Types` now
      lists **two** rules, `CORE-003` and `CORE-004`. `CORE-005` appears as a
      top-level rule, not indented under the chapter.

- [x] 5.4 `python3 scripts/rule.py show TRN-021` — its `cites` line reads
      `CORE-006, TRN-005, TRN-006, TRN-008, DEP-006, VEH-030`, in that order:
      the index takes every ID in the body in document order.

- [x] 5.5 `python3 scripts/rule.py glossary` — must report **0** entries citing no
      rule.

- [x] 5.6 `grep -c "Action Points per activation" docs/14-glossary.md` — must
      print **0**. `CORE-006` owns the allotment and no other document prints it.

- [x] 5.7 `git diff --stat` — exactly four files: three under `docs/` and
      `system/proposal-review.md`. **`CHANGELOG.md` and every `**Version:**`
      header are untouched, deliberately** — both belong to the Release cut.

- [x] 5.8 `python3 scripts/preflight.py` — all checks PASS.

---

## Coverage

| What changes | Task | File |
|---|---|---|
| `CORE-005` leaves the chapter | 1.1 | `docs/02-core-rules.md` |
| The `Unit` entry | 2.1 | `docs/14-glossary.md` |
| `TRN-021` | 3.1 | `docs/09-transport.md` |
| The Summary states whose points pay | 3.2 | `docs/09-transport.md` |
| Sizing a finding | 4.1 | `system/proposal-review.md` |
