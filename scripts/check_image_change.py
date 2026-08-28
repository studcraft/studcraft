#!/usr/bin/env python3
"""A branch that places a drawn image changes that image, and nothing else.

`assets/IMAGES.md` ("When an image appears, or disappears") states the shape a
placement has: the drawn file, one embed line per image in the one document that
specifies it, and the change directory. Three paths, no fourth.

The shape was written down because it was got wrong. Placing
`cmp-018-clear-opening.png` wandered three times in one session — the file was
almost committed inside the change directory instead of `assets/images/`, the
entry was almost rewritten after the maintainer had already accepted the image,
and the audit was paid for twice. None of that is visible to
`insert_images.py`, which asks whether `docs/`, `assets/images/` and the index
agree and would answer yes to every one of them.

So this asks the other question. Not *is the tree consistent* but *is this
branch only doing the one thing*:

  - **`assets/IMAGES.md` is not edited.** This is the important half. The
    *What it must show* column is the instruction given to whoever drew the
    image, and once the maintainer has accepted the drawing (step 4) the entry
    is the record of what was asked for. Narrowing it to fit the drawing
    afterwards erases the record and is a separate editorial change, on its own
    branch, if the maintainer wants it at all.
  - **Nothing outside `assets/images/`, `docs/*.md` and `openspec/changes/`
    is touched.** A placement that also edits `system/`, `scripts/` or
    `.claude/` is two changes sharing a branch.
  - **Every line added to or removed from `docs/` is an embed or a blank.** The
    embed is written by `scripts/insert_images.py --write`; a rule reworded on
    the way through is a ruleset change wearing an image change's name.

It reports only on a branch that touches `assets/images/`, since that is what a
placement or a removal always does and what nothing else does. A branch editing
only the index, adding an entry for an image nobody has drawn yet, is a
different change and is left alone.

Removal is the same shape read backwards — the file leaves `assets/images/`, the
embed leaves `docs/` — so both directions are checked with one rule about which
lines may move.

Usage:

    python3 scripts/check_image_change.py             against origin/main
    python3 scripts/check_image_change.py <revision>  against anything else

Exit code 0 when the branch is not a placement or is only a placement, 1
otherwise. A revision passed explicitly and not resolvable is an error rather
than a skip: CI names the pull request's base, and a base that is not there
would otherwise report every placement clean without comparing it to anything.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from insert_images import EMBED_RE  # noqa: E402
from repo import git  # noqa: E402

BASES = ("origin/main", "main")

IMAGES_DIR = "assets/images/"
IMAGES_INDEX = "assets/IMAGES.md"

# The three places a placement is allowed to write. `openspec/changes/` is the
# change directory itself; which one, and that the branch is named for it, is
# `scripts/preflight.py`'s question rather than this script's.
ALLOWED_PREFIXES = (IMAGES_DIR, "docs/", "openspec/changes/")

DOC_RE = re.compile(r"^docs/[\w.-]+\.md$")


def base_revision(argv: list[str]) -> str | None:
    """The revision to compare against, or None when none can be resolved.

    The merge base with `origin/main` is what the pull request would diff
    against. `main` stands in where the remote ref is not present locally,
    which is the case in a freshly initialised repository.
    """
    if argv:
        code, resolved = git("rev-parse", "--verify", argv[0])
        return resolved if code == 0 else None

    for ref in BASES:
        code, resolved = git("merge-base", ref, "HEAD")
        if code == 0:
            return resolved
    return None


def changed_paths(base: str) -> list[str]:
    """Every path this branch changes, committed or not.

    `git diff <base>` compares the base against the working tree, so staged and
    unstaged edits are both included. Untracked files are added separately: a
    drawn image arrives untracked, and it is the whole subject here.
    """
    paths: set[str] = set()

    code, out = git("diff", "--name-only", base)
    if code == 0 and out:
        paths.update(out.splitlines())

    code, out = git("ls-files", "--others", "--exclude-standard")
    if code == 0 and out:
        paths.update(out.splitlines())

    return sorted(paths)


def image_files(paths: list[str]) -> list[str]:
    """The drawn images this branch adds or removes. `.gitkeep` is not one."""
    return [
        path for path in paths
        if path.startswith(IMAGES_DIR) and not path.endswith("/.gitkeep")
    ]


def moved_doc_lines(base: str) -> list[tuple[str, str]]:
    """Every line `docs/` gains or loses, as (sign, text) pairs.

    `--unified=0` so the context lines a reader would have to filter out are
    never printed. The `+++`/`---` file headers are dropped by length: a header
    is three signs, a moved line is one.
    """
    code, diff = git("diff", "--unified=0", base, "--", "docs/")
    if code != 0 or not diff:
        return []

    moved: list[tuple[str, str]] = []
    for line in diff.splitlines():
        if line.startswith(("+++", "---")):
            continue
        if line.startswith(("+", "-")):
            moved.append((line[0], line[1:]))
    return moved


def survey(base: str, paths: list[str]) -> list[str]:
    """Everything this branch does that a placement does not do."""
    errors: list[str] = []

    if IMAGES_INDEX in paths:
        errors.append(
            f"{IMAGES_INDEX} is edited on a branch that places a drawn image. The "
            f"entry is the record of what the illustrator was asked for, and the "
            f"maintainer accepted the drawing against it — assets/IMAGES.md "
            f"('When an image appears, or disappears', steps 4 and 5). Changing "
            f"the entry is a separate change on its own branch. Revert it here."
        )

    outside = sorted(
        path for path in paths
        if not path.startswith(ALLOWED_PREFIXES) and path != IMAGES_INDEX
    )
    if outside:
        errors.append(
            "a placement writes to assets/images/, docs/ and its own change "
            "directory only. Also changed: " + ", ".join(outside)
        )

    stray = sorted(
        path for path in paths
        if path.startswith("docs/") and not DOC_RE.match(path)
    )
    if stray:
        errors.append("docs/ holds the ruleset only. Also changed: " + ", ".join(stray))

    for sign, text in moved_doc_lines(base):
        if not text.strip() or EMBED_RE.match(text):
            continue
        direction = "added to" if sign == "+" else "removed from"
        errors.append(
            f"a line was {direction} docs/ that is not an image embed: {text.strip()!r}. "
            f"The embed is written by scripts/insert_images.py --write and is the "
            f"whole of what a placement changes in the ruleset."
        )

    return errors


def main(argv: list[str]) -> int:
    base = base_revision(argv)
    if base is None:
        # A base that was *asked for* and is not there is a wrong answer, not a
        # missing one: in CI it would pass this check without running it, which
        # is the one outcome worse than not having the check. Auto-detection
        # failing is different — a fresh clone with no remote legitimately has
        # nothing to compare against.
        if argv:
            print(
                f"::error::Cannot resolve {argv[0]}, which was named explicitly. "
                f"Refusing to report a placement as clean without comparing it "
                f"against anything.",
                file=sys.stderr,
            )
            return 1
        print(
            f"Cannot resolve {' or '.join(BASES)}; nothing to compare against. Skipping."
        )
        return 0

    paths = changed_paths(base)
    images = image_files(paths)

    if not images:
        print("No image is added or removed on this branch; not a placement.")
        return 0

    errors = survey(base, paths)

    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"\n{len(errors)} thing(s) this placement does besides place its image.")
        return 1

    embeds = sum(1 for sign, text in moved_doc_lines(base) if EMBED_RE.match(text))
    documents = sorted({path for path in paths if DOC_RE.match(path)})
    where = ", ".join(path[len("docs/"):] for path in documents) or "no document"
    print(
        f"Image placement: {len(images)} image file(s), {embeds} embed line(s) in "
        f"{where}. assets/IMAGES.md and everything else untouched."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
