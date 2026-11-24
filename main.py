#!/usr/bin/env python3
"""Angry Judge rant entry: the self-checkout bagging-area accusation."""

import os

RANT = (
    "UNEXPECTED ITEM IN THE BAGGING AREA! It's a banana. I scanned it, "
    "you beeped, I bagged it - that is literally the deal. Now the red "
    "light spins, ASSISTANCE NEEDED, and twelve strangers watch a "
    "teenager type a secret code to forgive my fruit. I work here now, "
    "unpaid, and I am already suspected of theft."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(RANT)


if __name__ == "__main__":
    main()
