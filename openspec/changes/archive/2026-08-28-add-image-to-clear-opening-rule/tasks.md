# Tasks — An image reaches the clear-opening rule

## How to read this file

**The embed is not typed.** `scripts/insert_images.py --write` writes it; the
applier runs the command and verifies the result. There are no anchor pairs and
no `docs/` edit to transcribe.

**Part C is one reading, and it was the maintainer's.** `assets/IMAGES.md` rests
the image on a fact the prose cannot carry alone, and nothing mechanical checks
that it does. Task 3.1 records that reading.

### The two fenced blocks under section 1 are not anchors

One is the command's expected output (task 1.1); one is the line the command
must have written (task 1.4). `scripts/check_task_anchors.py` cannot tell either
from an anchor, so it reports each as a **note** — "anchor is not in
docs/05-construction-components.md". That is expected before task 1.1 runs, and
**neither block is anything to paste** into `docs/`.

### If a command disagrees with what a task expects

**Stop and report it.** Never edit a document to make a verification pass — that
is the one failure mode this machinery was built to remove.

---

## 1. `docs/05-construction-components.md` — CMP-018 gains its image

- [x] 1.1 Run `python3 scripts/insert_images.py --write` from the repository
      root, on this branch. **Do not type the embed by hand**, and do not edit
      `docs/05-construction-components.md` in any other way.

      Expected output, in this order — the disagreement is printed before it is
      repaired:

```
docs/05-construction-components.md:91: assets/images/cmp-018-clear-opening.png is drawn and listed, but CMP-018 does not embed it
  python3 scripts/insert_images.py --write

Wrote 1 document(s): 05-construction-components.md
Checked 20 image entr(ies), 2 drawn. docs/, assets/images/ and assets/IMAGES.md agree.
```

      **If it refuses**, the branch is wrong — the branch and the change
      directory must both be `add-image-to-clear-opening-rule`. Report it; do
      not work around it.

      **If it writes more than one document**, stop and report it. Only
      `cmp-018-clear-opening.png` is newly drawn, so only one document can
      change.

- [x] 1.2 `ls -la assets/images/` — `cmp-018-clear-opening.png` is present, a
      `.png`, about 123 KB, far under the 3 MB cap of `assets/IMAGES.md`. Its
      path and `docs/05-construction-components.md` are the two paths handed to
      `git-operator`; the PNG is committed in the same commit as the embed, or
      `docs/` points at a file not in the repository.

- [x] 1.3 `git diff --stat docs/` — **one file,
      `docs/05-construction-components.md`, two lines added, none removed.** More
      than one file is a mismatch: report it and stage nothing.

- [x] 1.4 `grep -n "assets/images" docs/05-construction-components.md` — one
      hit (its `NNN:` line-number prefix aside), and it is:

```
![CMP-018 — clear opening](../assets/images/cmp-018-clear-opening.png)
```

      It sits after `CMP-018`'s last line — `> **If it fits, it passes.**` — and
      before the `---` that closes the rule. If it is under `# CMP-019`, stop
      and report it.

## 2. Verification

- [x] 2.1 `python3 scripts/insert_images.py --check` — must **exit 0** and
      report `20 image entr(ies), 2 drawn`. This is the run CI makes.

- [x] 2.2 `python3 scripts/insert_images.py --write` a second time — must exit 0
      and print no `Wrote` line at all. A second write that changes something is
      a defect, not a no-op.

- [x] 2.3 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural
      issues found.` Unchanged before and after: an embed is not a citation and
      not a heading.

- [x] 2.4 `python3 scripts/check_id_stability.py` — must **exit 0** and report
      `Compared 180 rule ID(s) against origin/main: none renumbered or reused.`
      No rule is added, retired or renumbered by this change.

- [x] 2.5 `python3 scripts/rule.py show CMP-018` — the body now ends with the
      embed line. Nothing else about the rule changed.

- [x] 2.6 `.venv/bin/pytest -q` — **358 passed**, the same as `main`. This
      change touches no script and no test.

- [x] 2.7 `python3 scripts/preflight.py` — all checks PASS.

- [x] 2.8 `git status --short` — modified: `docs/05-construction-components.md`.
      Untracked: `assets/images/cmp-018-clear-opening.png` and this change
      directory (both to be staged by `git-operator`, by name). **`CHANGELOG.md`
      and every `**Version:**` header are untouched, deliberately** — both
      belong to the Release cut. Anything else is a mismatch: report it and
      stage nothing.

---

## 3. The reading no command makes

- [x] 3.1 **`assets/images/cmp-018-clear-opening.png` read against the `CMP-018`
      entry.** Decided by the maintainer, which is the only place this decision
      could be made: `insert_images.py` checks that the file exists, never what
      is in it.

      `CMP-018`'s *What it must show* column instructs the illustrator to
      dimension the frame's nominal aperture, to draw the clear-opening
      measurement around the hinged element and label it, and to dimension it
      against the model. The drawn image carries none of those as a drawn
      annotation. It shows a doorway with a hinged door part-way across it,
      twice, a minifig on its base at each, and pass versus no-pass marked by
      the signage above.

      **The maintainer's decision: the image is representative, and the entry is
      not changed.** A minifig on its `4 × 3` base (`INF-001`) at the height it
      stands is one Unit Base (`CORE-001`); that Unit Base passes the clear
      opening the hinged element leaves, or it does not, which is `CMP-018`'s
      check read off the model rather than a dimension line. Measuring by the
      state of the build is this repository's idiom (the archived
      `add-image-to-core-rule` `design.md`, Decision 14).

      **This proposal does not claim the entry's text now describes the drawn
      image.** It does not; the *What it must show* column was an instruction to
      whoever drew the image (`assets/IMAGES.md:18`), the image is drawn and
      accepted, and rewriting the entry to match is a separate editorial act the
      maintainer chose not to take here. `design.md`, Decision 2.

---

## Coverage

| What changes | Task | File |
|---|---|---|
| CMP-018's image | 1.1 | `docs/05-construction-components.md` |
| The drawn file is present and committed | 1.2 | `assets/images/cmp-018-clear-opening.png` |
| The image against its own entry | 3.1 | (no file — the maintainer's reading) |
