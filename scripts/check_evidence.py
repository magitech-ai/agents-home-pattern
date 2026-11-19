#!/usr/bin/env python3
"""Validate evidence notes, local links and the conformance claim set.

Read-only. No protocol conformance is claimed: this checks this repository's
own evidence discipline. Exit 1 with actionable messages on any failure.

Checks:
  - every field note has Recorded, Evidence type, Label, Status and Limitations
  - the Label uses the controlled vocabulary from README.md
  - every field note is linked from README.md
  - notes recorded from REPRODUCE_FROM onward include a Reproduce block
  - local Markdown links resolve (cross-repo `../` links are skipped so CI
    stays hermetic when only this repo is checked out)
  - CONFORMANCE.md claim rows have a valid label and a proof that resolves
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "docs" / "field-notes"
CONFORMANCE = ROOT / "CONFORMANCE.md"
REQUIRED = ("Recorded", "Evidence type", "Label", "Status", "Limitations")
LABELS = {
    "Pilot observation",
    "Documented behavior",
    "Hypothesis",
    "Open question",
}
# Notes recorded on or after this date must show how to reproduce the claim.
REPRODUCE_FROM = "2026-11-20"


def check_notes(failures: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    notes = sorted(NOTES.glob("*.md"))
    for note in notes:
        text = note.read_text(encoding="utf-8")
        for header in REQUIRED:
            if not re.search(rf"\*\*{re.escape(header)}:\*\*", text):
                failures.append(f"{note.name}: missing **{header}:**")

        label = re.search(r"\*\*Label:\*\*\s*(.+)", text)
        if label and label.group(1).strip() not in LABELS:
            failures.append(
                f"{note.name}: label {label.group(1).strip()!r} is not in "
                f"the README vocabulary"
            )

        index_link = f"docs/field-notes/{note.name}"
        if index_link not in readme:
            failures.append(f"{note.name}: not linked from README.md")

        recorded = re.search(
            r"\*\*Recorded:\*\*\s*(\d{4}-\d{2}-\d{2})", text
        )
        if recorded and recorded.group(1) >= REPRODUCE_FROM:
            has_reproduce = re.search(r"\*\*Reproduce:\*\*", text) or re.search(
                r"^## Reproduce\b", text, re.MULTILINE
            )
            if not has_reproduce:
                failures.append(
                    f"{note.name}: recorded {recorded.group(1)} needs a "
                    "**Reproduce:** block"
                )
    if "CONFORMANCE.md" not in readme:
        failures.append("README.md: CONFORMANCE.md is not linked")


def check_links(failures: list[str]) -> None:
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http:", "https:", "mailto:", "#", "../")):
                continue
            if not (md.parent / target).exists():
                failures.append(f"{md.relative_to(ROOT)}: broken link {target!r}")


def check_claims(failures: list[str]) -> None:
    text = CONFORMANCE.read_text(encoding="utf-8")
    rows = [
        line for line in text.splitlines() if re.match(r"^\|\s*C\d+\s*\|", line)
    ]
    if len(rows) < 3:
        failures.append("CONFORMANCE.md: expected at least 3 claim rows")
    for row in rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if len(cells) != 4:
            failures.append(f"CONFORMANCE.md: malformed row {cells[0]!r}")
            continue
        claim_id, _claim, evidence, proof = cells
        if evidence not in LABELS:
            failures.append(f"{claim_id}: evidence {evidence!r} is not in the vocabulary")
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", proof):
            if not (ROOT / link).exists():
                failures.append(f"{claim_id}: proof link {link!r} does not resolve")
        for path in re.findall(r"check:\s*`?([^`,\s]+)", proof):
            if path.startswith("../"):
                continue
            if not (ROOT / path).exists():
                failures.append(f"{claim_id}: checker {path!r} does not exist")


def main() -> int:
    failures: list[str] = []
    check_notes(failures)
    check_links(failures)
    check_claims(failures)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    notes = len(list(NOTES.glob("*.md")))
    claims = len(
        [
            line
            for line in CONFORMANCE.read_text(encoding="utf-8").splitlines()
            if re.match(r"^\|\s*C\d+\s*\|", line)
        ]
    )
    print(f"Validated {notes} field notes, local links and {claims} conformance claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
