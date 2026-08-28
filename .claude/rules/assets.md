---
paths:
  - "assets/**"
---

# Images

`assets/IMAGES.md` owns the example-image specification and the filename
convention, and it is the only place either is written down. Do not restate
them in `docs/` or `system/`.

`scripts/lint_ruleset.py` checks every filename listed in that file against the
convention, that it names a document which exists, and that the rule it
illustrates exists in that document. Run it after touching either.

`scripts/insert_images.py` places the drawn images and reports every departure
from the rule `assets/IMAGES.md` states about when an embed exists. Read that
file before placing one by hand. `--write` edits `docs/` and therefore runs on a
proposal branch; `--check` writes nothing and is what CI runs.

`scripts/check_image_change.py` asks the other question — not whether the tree
agrees with itself but whether this branch only placed its image. It fires on
any branch touching `assets/images/`, and the edit it refuses first is one to
`assets/IMAGES.md`: an entry narrowed to fit a drawing the maintainer already
accepted leaves every other check green. `scripts/preflight.py` runs it, and so
does the `Docs ruleset linter` job on every pull request — which is why that
job's checkout is not shallow: this check needs the base to diff against.

**The procedure it guards is the `add-image` skill** —
`.claude/skills/add-image/SKILL.md`. Invoke it before starting, not after: it
holds the order, and every defect this flow has shipped came from assembling
that order rather than following it.

The parsing of `assets/IMAGES.md` is `scripts/images_index.py`'s, shared by
those two and by `scripts/build_index.py`, which publishes each entry in
`.studcraft/index.json` for whoever draws the images.
