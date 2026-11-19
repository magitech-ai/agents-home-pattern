#!/usr/bin/env python3
"""Validate field-note evidence headers and README index coverage.

Read-only. Exits 1 with actionable messages when a note lacks one of the four
evidence headers or is not linked from README.md. No protocol conformance is
claimed: this checks this repository's own evidence discipline.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "docs" / "field-notes"
REQUIRED = ("Recorded", "Evidence type", "Status", "Limitations")


def main() -> int:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    failures: list[str] = []
    for note in sorted(NOTES.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        for header in REQUIRED:
            if not re.search(rf"\*\*{re.escape(header)}:\*\*", text):
                failures.append(f"{note.name}: missing **{header}:**")
        link = f"docs/field-notes/{note.name}"
        if link not in readme:
            failures.append(f"{note.name}: not linked from README.md")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"Validated {len(list(NOTES.glob('*.md')))} field notes and README links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
