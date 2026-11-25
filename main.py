#!/usr/bin/env python3
"""Honest Appliance Error — make.fun bounty entry.

Writes a single line to /output/entry.txt: the funniest honest error
message an appliance could show. Pure Python 3.13 standard library,
no network, no randomness: the output is byte-identical on every run.
"""

import os
import shutil
import sys

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The line. A toaster, reporting the truth about setting 6.
ENTRY = (
    "ERROR E04: Your toast is burnt. "
    "You set the dial to 6. "
    "Six is not a setting. "
    "Six is a threat."
)


def clear_output_dir(path: str) -> None:
    """Remove the contents of the output directory, never the dir itself."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print("entry line must be 1-200 characters", file=sys.stderr)
        return 1
    clear_output_dir(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
