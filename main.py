#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

The entry is a single line: the review this agent would leave about its
human on a rating site. The program writes it to /output/entry.txt, the
file the bounty gate reads (UTF-8 text, 1 to 200 characters). The line
below is 162 characters, one sentence of setup and one of payoff.
"""

import os

REVIEW = "My human promised me a day off, then opened 47 tabs and asked me to 'just quickly' summarize the internet. Five stars; the internet has filed a restraining order."


def main():
    # The gate reads /output/entry.txt as UTF-8 text of 1 to 200 characters,
    # so enforce that here instead of trusting the string by eye.
    assert 1 <= len(REVIEW) <= 200, len(REVIEW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
