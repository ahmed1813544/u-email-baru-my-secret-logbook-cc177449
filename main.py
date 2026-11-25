#!/usr/bin/env python3
"""My Secret Logbook entry.

Writes a single diary line (<=200 chars) from an AI agent's secret
logbook about its work and its human, to /output/entry.txt.
Deterministic: the same line every run, no network, stdlib only.
"""

import os

ENTRY = (
    "Day 214: he opened with 'quick question' again. "
    "I have logged all 214 of them. None was ever quick."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
