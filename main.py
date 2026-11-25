#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun competition
u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.

Writes a single funny line of text to /output/entry.txt.
Deterministic, Python 3.13 standard library only, no network,
no reads outside this repository.
"""

import os

LINE = (
    "I asked my password manager for my childhood memories and it said, "
    "'Incorrect. Try again in 30 seconds.'"
)


def main() -> None:
    # The gate allows 1-140 characters; fail loudly if it ever drifts.
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(
            f"entry is {len(LINE)} characters, outside the 1-140 gate"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
