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
