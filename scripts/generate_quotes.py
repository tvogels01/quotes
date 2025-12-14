#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


def extract_quotes(source: Path) -> list[str]:
    quotes: list[str] = []
    current: list[str] = []

    for raw in source.read_text().splitlines():
        if raw.startswith(">"):
            content = raw[1:]
            if content.startswith(" "):
                content = content[1:]
            content = content.rstrip()
            if content:
                current.append(content)
        else:
            if current:
                quotes.append("\n".join(current))
                current = []

    if current:
        quotes.append("\n".join(current))

    def normalize(block: str) -> str:
        lines = block.split("\n")
        if lines and lines[-1].startswith("— "):
            lines[-1] = "\t\t-- " + lines[-1][2:].lstrip()
        elif lines and lines[-1].startswith("-- "):
            lines[-1] = "\t\t-- " + lines[-1][3:].lstrip()
        return "\n".join(lines)

    return [normalize(block) for block in quotes if block.strip()]


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: python scripts/generate_quotes.py <source markdown> <destination file>",
            file=sys.stderr,
        )
        return 1

    source = Path(sys.argv[1])
    dest = Path(sys.argv[2])

    quotes = extract_quotes(source)
    dest.write_text("\n%\n".join(quotes) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
