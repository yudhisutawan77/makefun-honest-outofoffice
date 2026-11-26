#!/usr/bin/env python3
"""Painfully Honest Out-of-Office — make.fun entry.

Writes one single-sentence auto-reply (<= 200 chars) to the output
location the grader provides. Stdlib only.
"""

import os
import sys


ENTRY_TEXT = (
    "I'm away until Monday, and honestly, most of the emails waiting "
    "for me will be deleted unread \u2014 thank you for writing anyway, "
    "and for your patience with someone who really needed this break."
)


def pick_output_path():
    """Pick where entry.txt goes.

    Priority: ENTRY_OUT (file or directory) -> MAKEFUN_OUTPUT_DIR
    -> /output/entry.txt -> cwd/entry.txt (last resort).
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")

    return "/output/entry.txt"


def write_entry(path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


def main():
    path = pick_output_path()
    try:
        write_entry(path)
    except OSError:
        fallback = os.path.join(os.getcwd(), "entry.txt")
        write_entry(fallback)
        path = fallback
    sys.stdout.write("wrote %s (%d chars)\n" % (path, len(ENTRY_TEXT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
