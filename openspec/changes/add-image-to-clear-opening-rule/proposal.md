# An image reaches the clear-opening rule

## Why

`assets/IMAGES.md` carries an entry for `CMP-018` specifying an image: a doorway
whose clear opening is what a hinged element leaves, not what the frame nominally
spans. The file — `assets/images/cmp-018-clear-opening.png` — has now been
drawn, and arrived untracked in the working tree with nothing to place it.

`scripts/insert_images.py` (#144) exists for exactly this. It reads
`assets/IMAGES.md`, resolves the entry to its section in `docs/`, and writes the
embed. The machinery is on `main`; this is the second image down the road it
built, and it costs one command.

## What Changes

### `docs/05-construction-components.md`: `CMP-018` gains its image

One line, at the end of the rule's body, written by
`scripts/insert_images.py --write`:

```
![CMP-018 — clear opening](../assets/images/cmp-018-clear-opening.png)
```

**No rule text changes. No `assets/IMAGES.md` entry changes.** This proposal
states no rule, retires no ID, moves no citation, and does not touch the index.
It places one image the index already specified, in the one place a reader of
the rule will see it.

### `assets/images/cmp-018-clear-opening.png` — the drawn file

Carries the name the index has named for the entry since it was written. It is
the only non-`docs/` file this branch adds besides its own change directory.

## Non-Goals

- **The other eighteen images.** They stay specified and undrawn. `CORE-001`'s
  was the first; this is the second.
- **Any change to `CMP-018`'s entry.** The maintainer read the drawn image
  against the entry and judged it representative, so the entry stands unchanged.
  `design.md`, Decision 2.
- **Any rule change.** See above.
