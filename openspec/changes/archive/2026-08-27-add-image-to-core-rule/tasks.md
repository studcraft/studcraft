# Tasks — An image reaches the rule that asked for it

## How to read this file

**Part A is already applied.** The machinery was written on this branch before
this proposal existed — `system/workflow.md` ("When the edits came first") is the
shape that requires, and `design.md` Decision 1 is why it is one branch. Its
boxes are ticked because the work is in the tree, not because a task was
followed. Each entry names the command that verifies the claim, so a reviewer
checks rather than takes it.

**Part A touches no `docs/*.md` file.** That is what makes the order safe here:
nothing in the ruleset changed before this proposal existed. The one `docs/` edit
in this change is task 9.1, and it has not been applied.

**Part B is the ruleset edit**, and it is not typed. `scripts/insert_images.py`
writes it, which is the whole point of Part A — the applier runs a command and
verifies the result. Tasks 8.1 and 8.2 are anchor pairs and are typed.

**Part C is one reading, and it was not the applier's.** `design.md` Decision 2
rests this whole change on an image carrying facts the prose cannot, and nothing
mechanical can check that it does. It is ticked because the maintainer made it;
tasks 8.3 and 8.4 are what came out of it.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is
not part of the text** — do not write the backticks into the document.

### The two fenced blocks under section 9 are not anchors

One is the command's expected output and one is the line it must have written.
`scripts/check_task_anchors.py` cannot tell those from an anchor, so it reports
each as a **note** — "anchor is not in docs/02-core-rules.md". That is expected
before 9.1 runs, and neither block is anything to paste.

### Order matters

Section 8 before section 9. The sentence 8.1 replaces is about a state 9.1 ends.

### If a command disagrees with what a task expects

**Stop and report it.** Never edit a document to make a verification pass — that
is the one failure mode this whole change is built to remove.

---

# Part A — Applied

## 1. `scripts/images_index.py` — the index has one parser

- [x] 1.1 The module exists and owns the parse of `assets/IMAGES.md`: what an
      entry is, which of the two kinds it is, what prefix its filename must
      carry, and what alt text it produces.
      Verify: `python3 -c "import sys; sys.path.insert(0, 'scripts'); import images_index; print(len(images_index.entries()))"` — **20**.

- [x] 1.2 `scripts/lint_ruleset.py` imports it instead of parsing for itself, and
      `check_image_index` reports exactly what it reported before.
      Verify: `grep -c "parse_image_entries" scripts/lint_ruleset.py` — **0**.
      Verify: `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`

## 2. `scripts/insert_images.py` — the placement process

- [x] 2.1 `--check` reports every disagreement between `docs/`, `assets/images/`
      and `assets/IMAGES.md`, writes nothing, and exits non-zero when it finds
      one.

- [x] 2.2 `--write` places, re-places and removes, and refuses on `main`, on
      `develop`, and on a branch that names no unarchived change.

- [x] 2.3 An embed with no entry is reported with the `assets/IMAGES.md` row
      ready to paste, and with the reclassification ritual named when the rule is
      in the rejected list.

- [x] 2.4 A document is written only to place or remove an image
      (`design.md`, Decision 13). The trailing-newline state is preserved, no
      blank run is collapsed except the one an embed sat in, and a rewrite that
      no finding accounts for is itself reported.
      Verify: `.venv/bin/pytest tests/test_insert_images.py -q` — **19 passed**.

## 3. `scripts/build_index.py` — the index carries what the drawing needs

- [x] 3.1 Every document carries an `images` list of entries, in table order;
      every rule that has one carries an `images` list of paths.
      Verify: `python3 scripts/build_index.py`, then
      `python3 -c "import json; d=json.load(open('.studcraft/index.json')); print(d['rules']['CORE-001']['images'], d['documents']['17-infantry.md']['images'][2]['anchor'])"`
      — `['assets/images/core-001-unit-base-volume.png'] Terrain`.

## 4. The gate and its mirror

- [x] 4.1 `.github/workflows/docs-ruleset-linter.yml` runs
      `python3 scripts/insert_images.py --check` as a second step of the existing
      `Docs ruleset linter` job. The job name is unchanged, so branch protection
      still names something that exists.
      Verify: `grep -c "insert_images" .github/workflows/docs-ruleset-linter.yml` — **1**.

- [x] 4.2 `scripts/preflight.py` mirrors it, and its docstring numbers thirteen
      checks with the branch-and-diff gates at 10-13.
      Verify: `python3 scripts/preflight.py` — the run names `Images match their index`.

## 5. `assets/images/core-001-unit-base-volume.png`

- [x] 5.1 The drawn file carries the name the index has named since
      `Add assets/IMAGES.md and TODO.md` (#45). It arrived as
      `core-001-unit-base.png`; `assets/IMAGES.md` was not changed to match it
      (`design.md`, Decision 11).
      Verify: `ls assets/images` — `.gitkeep` and `core-001-unit-base-volume.png`.

## 6. `.claude/rules/assets.md`

- [x] 6.1 Points at `assets/IMAGES.md` for the placement rule rather than
      restating it, and says that `--write` edits `docs/` and therefore runs on a
      proposal branch. `system/documentation-standards.md`: a file under
      `.claude/rules/` routes to an owner, it does not summarise one.

## 7. Tests

- [x] 7.1 `tests/test_insert_images.py` is new, nineteen cases.
      `tests/test_images_index.py` is new and takes the three parser cases that
      were in `tests/test_lint_ruleset.py`. `tests/test_lint_ruleset.py` gains
      eight cases for `check_image_index`, which had none.
      `tests/test_build_index.py` covers the `images` key.
      Verify: `.venv/bin/pytest -q` — **349 passed**.

---

# Part B — To apply

## 8. `assets/IMAGES.md` — two sentences that stopped being true

- [x] 8.1 In `assets/IMAGES.md`, replace this anchor — the sentence closing the
      naming convention:

```
None of the files listed below exist yet. `assets/images/.gitkeep` holds the directory until they are added.
```

with:

```
Files are added as they are drawn, and `scripts/insert_images.py` places each one under the section that specifies it. The rule it keeps is exact in both directions: **an image is embedded in `docs/` exactly when the file exists in `assets/images/` and this file lists it for that section.** An embed placed by hand, with no entry here, is therefore removed — the entry is where the argument for the image is written, and the *Why text alone is not enough* column is that argument. `--check` reports each departure and prints the row to add; `--write` repairs them, and because it edits `docs/` it runs on a proposal branch. `assets/images/.gitkeep` holds the directory.
```

- [x] 8.2 In `assets/IMAGES.md`, replace this anchor — the sentence closing the
      list of rewritten entries, which counts two and has counted five since
      `three image entries describe rules that moved on` (#141) added three:

```
**Both were stale before the change that noticed them**
```

with:

```
**All five were stale before the change that noticed them**
```

- [x] 8.3 In `assets/IMAGES.md`, replace this anchor — the whole `CORE-001` row,
      one line, under `## docs/02-core-rules.md`:

```
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | Three panels. First, the Unit Base as a volume, dimensioned 4 studs wide × 3 studs deep × 13 plate layers tall, with a model inside it and the base it stands on drawn within the volume rather than below it. Second, the same volume seen from above, dimensioned `4 × 3` studs. Last, a `2 × 3 UB` footprint measuring 8 × 9 studs, with the multiplication marked on both axes. | Two geometric facts here are carried by prose alone: that the unit encloses space rather than covering it, and that the base a model stands on is inside the volume rather than the floor under it — the rule says the height is measured from that base's underside, which a reader has to picture to apply. |
```

with:

```
| CORE-001 | `assets/images/core-001-unit-base-volume.png` | One Unit Base built as a stack of plates: 4 studs across the front face, 3 studs deep, 13 plate layers tall, with the layers alternating in colour so a reader can count them. Beside it, on the surface it stands on, the two measures as loose pieces — one 4 studs long for the width, one 3 studs long for the depth. | The height is given in plate layers, and thirteen of them is a quantity nobody converts to a brick in the hand at a glance — the same conversion this file accepts an image for at `Terrain (INF-006 – INF-008)`. Alternating layers make the count readable off the build, and the loose pieces put each horizontal figure beside a real element rather than beside the other number. The rule also calls a Unit Base a volume, which a reader arriving from a game of flat bases reads as a footprint. |
```

- [x] 8.4 In `assets/IMAGES.md`, replace this anchor — the heading that opens the
      list of entries rewritten because their rule moved on, so that the entry
      narrowed by 8.3 is recorded above it rather than filed under a reason that
      is not its own:

```
### Rewritten because the rule changed under them
```

with:

```
### Rewritten because the drawing settled the scope

**`CORE-001`** specified three panels and the image drawn for it is one: the volume, its three dimensions, and the two measures laid beside it. The panels asking for a model inside the volume and for a `2 × 3 UB` footprint are gone, and the entry no longer argues from them — the maintainer's judgement is that a stack of counted plates already shows that a Unit Base encloses space, and that a model inside adds nothing a reader needs.

**Two facts are now carried by prose alone**, knowingly. That the base a model stands on is inside the volume rather than the floor beneath it, which `CORE-001` states and no image shows; and the footprint arithmetic, `2 × 3 UB` measuring `8 × 9` studs. The rejections at `TRN-003`, `TRN-020`, `DEP-003` and `DEP-004` are unaffected: each leans on the dimensioned volume or on the horizontal `4 × 3` figure, and the image carries both.

### Rewritten because the rule changed under them
```

## 9. `docs/02-core-rules.md` — CORE-001 gains its image

- [x] 9.1 Run `python3 scripts/insert_images.py --write` from the repository
      root, on this branch. **Do not type the embed by hand**, and do not edit
      `docs/02-core-rules.md` in any other way.

      Expected output, all four lines, in this order — the disagreement is
      printed before it is repaired:

```
docs/02-core-rules.md:56: assets/images/core-001-unit-base-volume.png is drawn and listed, but CORE-001 does not embed it
  python3 scripts/insert_images.py --write

Wrote 1 document(s): 02-core-rules.md
Checked 20 image entr(ies), 1 drawn. docs/, assets/images/ and assets/IMAGES.md agree.
```

      **If it refuses**, the branch is wrong — the change directory and the
      branch must share the name `add-image-to-core-rule`. Report it; do not
      work around it.

      **If it writes more than one document**, stop and report it. Only one image
      is drawn, so only one document can change. This was a real defect in the
      first version of the script (`design.md`, Decision 13), and the check
      stays because the stop condition is what caught it.

- [x] 9.2 `git diff --stat docs/` — **one file, `docs/02-core-rules.md`, two
      lines added, none removed.** More than one file is a mismatch: report it
      and stage nothing.

- [x] 9.3 `grep -n "assets/images" docs/02-core-rules.md` — one hit, and it is:

```
![CORE-001 — unit base volume](../assets/images/core-001-unit-base-volume.png)
```

      It sits after `CORE-001`'s last sentence and before the `---` that closes
      the rule. If it is under `# CORE-002`, stop and report it.

## 10. Verification

- [x] 10.1 `python3 scripts/insert_images.py --check` — must **exit 0** and
      report `20 image entr(ies), 1 drawn`. This is the run CI makes.

- [x] 10.2 `python3 scripts/insert_images.py --write` a second time — must exit 0
      and print no `Wrote` line at all. A second write that changes something is
      a defect, not a no-op.

- [x] 10.3 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural
      issues found.` Unchanged before and after: an embed is not a citation and
      not a heading.

- [x] 10.4 `python3 scripts/check_id_stability.py` — must **exit 0** and report
      **180** rule IDs. No rule is added, retired or renumbered by this change.

- [x] 10.5 `python3 scripts/rule.py show CORE-001` — the body now ends with the
      embed line. Nothing else about the rule changed.

- [x] 10.6 `.venv/bin/pytest -q` — **349 passed**.

- [x] 10.7 `python3 scripts/preflight.py` — **all 13 checks PASS.**

- [x] 10.8 `git status --short` — modified: `.claude/rules/assets.md`,
      `.github/workflows/docs-ruleset-linter.yml`, `assets/IMAGES.md`,
      `docs/02-core-rules.md`, `scripts/build_index.py`,
      `scripts/lint_ruleset.py`, `scripts/preflight.py`,
      `tests/test_build_index.py`, `tests/test_lint_ruleset.py`. Untracked:
      `assets/images/core-001-unit-base-volume.png`, `scripts/images_index.py`,
      `scripts/insert_images.py`, `tests/test_images_index.py`,
      `tests/test_insert_images.py`, and this change directory. **`CHANGELOG.md`
      and every `**Version:**` header are untouched, deliberately** — both belong
      to the Release cut. Anything else is a mismatch: report it and stage
      nothing.

---

# Part C — The reading no command makes

## 11. The image against the entry that specified it

- [x] 11.1 **`assets/images/core-001-unit-base-volume.png` read against the
      `CORE-001` entry.** Decided by the maintainer, which is the only place this
      decision could be made: `insert_images.py` checks that the file exists,
      never what is in it.

      `proposal-auditor` reported the drawn file against the entry as it stood
      and found one panel where three were asked for, with no model inside the
      volume and no `2 × 3 UB` footprint. **The finding was right about the
      image and wrong about the remedy**, and one part of it was wrong outright:
      it reported no dimensions anywhere, when the two loose pieces beside the
      stack *are* the dimensions and the alternating layers *are* the height.
      Measuring by counting elements rather than by drawn annotation is this
      repository's idiom, not an omission — `system/design-process.md` reaches
      for the model before the notation.

      The maintainer's judgement: the image is representative of a volume, and a
      model inside would not make it clearer. So the entry narrows to what the
      image shows, by task 8.3, and 8.4 records what that costs — the
      base-inside-the-volume fact and the footprint arithmetic are prose-only
      from here.

      **The direction matters and is the one `assets/IMAGES.md:136` warns
      about.** Narrowing an entry to fit a drawing is legitimate exactly when the
      narrowed entry still stands on its own argument, which 8.3's *Why* column
      is written to do. It would not have been legitimate to leave the entry
      asking for three panels and place a one-panel image under it: that is the
      `WPN-003` failure, *"An image drawn from the entry would have contradicted
      the rule, which is worse than a stale argument."*

---

# Coverage

| What changes | Task | File |
|---|---|---|
| The index sentence about undrawn files | 8.1 | `assets/IMAGES.md` |
| The count closing the rewritten-entries list | 8.2 | `assets/IMAGES.md` |
| CORE-001's entry, narrowed to the image drawn | 8.3 | `assets/IMAGES.md` |
| What that narrowing costs, recorded | 8.4 | `assets/IMAGES.md` |
| CORE-001's image | 9.1 | `docs/02-core-rules.md` |
| The placement process | 2.1 | `scripts/insert_images.py` |
| The one parser | 1.1 | `scripts/images_index.py` |
| What the drawing process reads | 3.1 | `scripts/build_index.py` |
| The gate and its mirror | 4.1 | `.github/workflows/docs-ruleset-linter.yml` |
| The image against its own entry | 11.1 | `assets/IMAGES.md` |
