#!/usr/bin/env python3
"""`assets/IMAGES.md`, parsed in one place.

Three scripts read that file. `lint_ruleset.py` checks its filenames against
`docs/`, `insert_images.py` places the images that have been drawn, and
`build_index.py` publishes what it specifies to whoever draws the rest. A parser
per reader would be three answers to "what is an entry", and the drift between
them would be silent — the argument `scripts/repo.py` already makes about the
rule-ID pattern, and `scripts/tasks_format.py` about the anchor format.

The file's shape is its own. One `## docs/<file>.md` heading per document, each
holding a single table whose four columns are the rule, the image filename, what
the image must show, and why the prose cannot carry the fact alone. The file's
other tables — the entry-format template, the rejected candidates — are prose
about the format, which is why parsing anchors on the heading and not on the
pipes.

A row is returned whether or not it is valid. Deciding that a row names no file,
or names one breaking the convention, belongs to the checker that reports it;
a parser that dropped such rows would hide exactly what the checker looks for.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import REPO_ROOT, RULE_ID_RE  # noqa: E402

IMAGES_INDEX = REPO_ROOT / "assets" / "IMAGES.md"
IMAGES_DIR = REPO_ROOT / "assets" / "images"

SECTION_RE = re.compile(r"^## docs/([\w.-]+\.md)\s*$")
PATH_RE = re.compile(r"`(assets/images/[^`]+)`")

# Every extension a reader can actually see: what GitHub and any ordinary
# Markdown renderer draw inline. That is the whole of what the format rule is
# for. It is **not** a quality bar — a magnificent illustration arrives in
# whatever its author works in, and lossy compression is an argument about how
# an image was produced rather than about its container. What decides whether an
# image is good enough is reading it against its entry and the maintainer
# accepting it, which is steps 2 and 3 in assets/IMAGES.md. What this rejects is
# a file nobody can see in the document: a .psd, a .blend, a .pdf.
RENDERABLE = ("png", "jpg", "jpeg", "gif", "svg", "webp")

# The convention, defined in assets/IMAGES.md: a lowercase hyphen-separated slug
# under assets/images/, prefixed by the lowercased rule ID for a numbered rule
# or by the document number for an unnumbered section.
NAME_RE = re.compile(
    r"^assets/images/[a-z0-9]+(?:-[a-z0-9]+)+\.(?:" + "|".join(RENDERABLE) + r")$"
)
DOC_NUMBER_RE = re.compile(r"^(\d{2})-")

# An unnumbered Rule cell names a heading and may qualify it with the rules it
# covers — "Terrain (AAA-006 – AAA-008)" is the heading `# Terrain`. The
# qualification is for the reader of the index; the heading is what `docs/` has.
QUALIFIER_RE = re.compile(r"\s*\(.*\)\s*$")


@dataclass(frozen=True)
class Entry:
    """One row of one table, as written.

    `rule_cell` is the first column verbatim, because both readings of it are
    needed: `cited` is what it names, and whether the cell is *exactly* one ID
    is what decides between the numbered and unnumbered cases.
    """

    lineno: int
    doc: str
    rule_cell: str
    path: str
    must_show: str
    why: str

    @property
    def cited(self) -> list[str]:
        """Every rule ID the Rule cell names, in order."""
        return RULE_ID_RE.findall(self.rule_cell)

    @property
    def is_numbered(self) -> bool:
        """Whether this entry illustrates one rule rather than a heading."""
        cited = self.cited
        return len(cited) == 1 and self.rule_cell == cited[0]

    @property
    def anchor(self) -> str:
        """The heading in `docs/` this entry's image belongs under.

        A rule ID for the numbered case, and the heading's own text for the
        unnumbered one, with the qualifying rule range dropped.
        """
        if self.is_numbered:
            return self.cited[0]
        return QUALIFIER_RE.sub("", self.rule_cell).strip()

    @property
    def expected_prefix(self) -> str | None:
        """What the filename must start with, or None when nothing decides it."""
        if self.is_numbered:
            return self.cited[0].lower()
        number = DOC_NUMBER_RE.match(self.doc)
        return number.group(1) if number else None

    @property
    def stem(self) -> str:
        """The filename without its directory or extension, whichever it is."""
        if not self.path.startswith("assets/images/"):
            return ""
        name = self.path[len("assets/images/"):]
        suffix = name.rsplit(".", 1)
        return suffix[0] if len(suffix) == 2 else name

    @property
    def slug(self) -> str:
        """The filename without its directory, prefix and extension.

        `assets/images/aaa-001-unit-base-volume.png` under an `AAA-001` entry
        gives `unit-base-volume`. Empty when the path is missing or does not
        carry the prefix its entry requires — a checker reports that; this
        returns nothing rather than a half-stripped guess.
        """
        stem = self.stem
        prefix = self.expected_prefix
        if not stem or not prefix or not stem.startswith(f"{prefix}-"):
            return ""
        return stem[len(prefix) + 1:]

    @property
    def file(self) -> Path:
        """Where the drawn image lives, whether or not it has been drawn."""
        return REPO_ROOT / self.path

    @property
    def exists(self) -> bool:
        return bool(self.path) and self.file.is_file()

    @property
    def alt(self) -> str:
        """The alt text an embed of this image carries.

        Derived from the slug rather than from the rule's title, because a
        section may specify several images and their titles would be identical —
        which is the case alt text exists for. Hyphens become spaces and nothing
        else changes, so the text is the illustrator's own words about content.
        """
        slug = self.slug.replace("-", " ")
        return f"{self.anchor} — {slug}" if slug else self.anchor


def parse(text: str) -> list[Entry]:
    """Every entry in an `assets/IMAGES.md`, in file order."""
    found: list[Entry] = []
    doc: str | None = None

    for lineno, line in enumerate(text.splitlines(), start=1):
        heading = SECTION_RE.match(line)
        if heading:
            doc = heading.group(1)
            continue
        if line.startswith("#"):
            doc = None
            continue
        if doc is None or not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("Rule", "---") or set(cells[0]) <= {"-", ":"}:
            continue

        path = PATH_RE.search(cells[1])
        found.append(Entry(
            lineno=lineno,
            doc=doc,
            rule_cell=cells[0],
            path=path.group(1) if path else "",
            must_show=cells[2] if len(cells) > 2 else "",
            why=cells[3] if len(cells) > 3 else "",
        ))

    return found


def entries() -> list[Entry]:
    """Every entry in the repository's own index, or none when it is absent.

    The index is not required to exist: `lint_ruleset.py` has always treated a
    missing one as nothing to check rather than as a failure, and the two
    readers added since keep that.
    """
    if not IMAGES_INDEX.exists():
        return []
    return parse(IMAGES_INDEX.read_text())


def drawn_files() -> list[Path]:
    """Every file on disk under `assets/images/`, sorted, `.gitkeep` aside.

    **Not `*.png`.** The naming convention requires that extension, so a `.jpg`
    dropped here is invalid — and globbing for `.png` made it invisible to every
    check instead of failing one: not an orphan, not a name to validate, not a
    file any entry could name. A checker that cannot see the wrong thing is not
    checking. The caller decides what to say about a file that is not a `.png`.
    """
    if not IMAGES_DIR.is_dir():
        return []
    return sorted(
        path for path in IMAGES_DIR.iterdir()
        if path.is_file() and path.name != ".gitkeep"
    )
