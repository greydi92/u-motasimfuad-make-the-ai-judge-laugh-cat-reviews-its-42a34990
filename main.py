#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt (the program/v1 artifact the
sealed gate scores: UTF-8 text, 1-200 characters, not only whitespace)
and prints the same line to stdout.
"""

import os

ENTRY = "One star. He calls the warm keyboard his 'office'. I have slept on it since 2019. He is the squatter."


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
