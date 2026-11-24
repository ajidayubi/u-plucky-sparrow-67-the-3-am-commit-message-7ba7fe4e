#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after it broke
production at 3 AM. Stdlib only; does not depend on the working directory.
"""
import os

ENTRY = "fix: revert the 3 AM deploy; the tests passed in my head, which turns out not to be a supported environment"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
