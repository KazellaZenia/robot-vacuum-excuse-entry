#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — round 1.

Writes one line (<=140 chars) to /output/entry.txt:
a robot vacuum's excuse for missing a spot, in the vacuum's own voice.
Pure stdlib; writes only to MAKEFUN_OUTPUT_DIR.
"""
import os

LINE = "I did not miss the spot. My map now lists it as a pet, and I do not eat pets."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
