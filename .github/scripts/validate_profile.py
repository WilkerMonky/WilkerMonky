#!/usr/bin/env python3
"""Validate the profile repository using Python's standard library only."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[2]
MARKDOWN_FILES = [ROOT / "README.md", ROOT / "README.pt-BR.md"]
REQUIRED_FILES = [
    *MARKDOWN_FILES,
    ROOT / "assets/wilker-fullstack-banner.png",
    ROOT / "assets/wilker-developer-portrait.png",
    ROOT / "assets/featured-projects-banner.png",
    ROOT / "assets/research-publications-banner.png",
    ROOT / "assets/wilker-closing-card.png",
    ROOT / "assets/Weslley-Wilker-CV.pdf",
    ROOT / "docs/project-import-checklist.md",
    ROOT / "docs/profile-maintenance.md",
    ROOT / "docs/art-direction.md",
    ROOT / ".github/workflows/validate-profile.yml",
]
FORBIDDEN_REFERENCES = {
    "LuigiGF": "contribution animation from another profile",
    "MatheusAlvarez": "visitor counter from another profile",
    "I'm 19 years old": "outdated age statement",
    "I study Computer Science": "outdated education statement",
    "Spider-Man": "protected character reference",
    "Peter Parker": "protected character reference",
    "Miles Morales": "protected character reference",
}

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_SRC_RE = re.compile(r"\bsrc=[\"']([^\"']+)[\"']", re.IGNORECASE)


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "mailto:")):
        return None
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme not in {"http", "https"}:
            raise ValueError(f"unsupported URL scheme: {target}")
        return None
    decoded = unquote(parsed.path)
    return (source.parent / decoded).resolve()


def validate_markdown(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")

    if text.count("```") % 2:
        errors.append(f"{path.relative_to(ROOT)}: unbalanced fenced code blocks")

    for term, reason in FORBIDDEN_REFERENCES.items():
        if term.casefold() in text.casefold():
            errors.append(f"{path.relative_to(ROOT)}: {reason}: {term!r}")

    for target in LINK_RE.findall(text) + HTML_SRC_RE.findall(text):
        try:
            resolved = local_target(path, target)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        if resolved is not None and not resolved.exists():
            errors.append(
                f"{path.relative_to(ROOT)}: missing local target {target!r}"
            )

    stats_urls = [line for line in text.splitlines() if "github-readme-stats" in line]
    if len(stats_urls) > 2:
        errors.append(f"{path.relative_to(ROOT)}: more than two statistics cards")
    for line in stats_urls:
        if "username=WilkerMonky" not in line:
            errors.append(
                f"{path.relative_to(ROOT)}: statistics card has incorrect username"
            )


def main() -> int:
    errors: list[str] = []

    for required in REQUIRED_FILES:
        if not required.is_file():
            errors.append(f"missing required file: {required.relative_to(ROOT)}")

    for markdown in MARKDOWN_FILES:
        if markdown.is_file():
            validate_markdown(markdown, errors)

    if errors:
        print("Profile validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Profile validation passed ({len(REQUIRED_FILES)} required files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
