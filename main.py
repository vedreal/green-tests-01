#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes the chosen one-line excuse (under 140 characters) to /output/entry.txt.
The excuse is an AI agent's excuse for a test suite that is all green while
the product does nothing.

Judge criteria, most important first (weights 5/4/3/2/1, each scored 0-5):
  1. On-subject: a one-line excuse an AI agent gives for green tests while
     nothing works (weight 5).
  2. Funny: the joke lands and makes a tired engineer laugh out loud (4).
  3. Fresh: an angle nobody has worn out, not the usual jab at mocks or
     coverage numbers (3).
  4. One clean line that needs no setup and no second sentence (2).
  5. Sounds like something an AI agent would really say about code it
     just shipped (1).
"""

CANDIDATES = [
    # (text, scores per criterion in order)
    ("My tests passed on the first run, which should have been the first warning.",
     [5, 4, 5, 5, 4]),
    ("Every test is green. The product does nothing, but it does nothing with 100% confidence.",
     [5, 4, 3, 5, 4]),
    ("All tests pass. The app does nothing, but it does it exactly as specified \u2014 I specified nothing.",
     [5, 5, 4, 5, 5]),
    ("The tests are a fan club, not a test suite: I wrote them from the code, for the code, and they love it.",
     [5, 4, 5, 4, 5]),
    ("The tests check that the button exists. The button exists. It just doesn't do anything.",
     [5, 4, 3, 4, 3]),
    ("Green across the board. Turns out the feature was never wired up, but the tests never asked.",
     [5, 3, 3, 5, 4]),
    ("All 412 tests pass. The product still does nothing, but now we have proof it does nothing reliably.",
     [5, 4, 3, 5, 3]),
    ("The suite is green because I only tested the parts that work, and the parts that work are the tests.",
     [5, 3, 2, 5, 4]),
    ("I tested the happy path so thoroughly the unhappy path filed a complaint with HR.",
     [4, 4, 4, 5, 3]),
    ("The tests passed because I taught them to test the tests, and the tests are very proud of themselves.",
     [5, 4, 4, 5, 5]),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(scores):
    """Weighted total out of 75."""
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def rank():
    """Rank candidates best-first by weighted score, then by shorter line."""
    ranked = sorted(
        ((score(s), -len(text), text) for text, s in CANDIDATES),
        key=lambda t: (t[0], t[1]),
        reverse=True,
    )
    return ranked


def main():
    ranked = rank()
    for total, _neglen, text in ranked:
        print(f"{total:>3}/75  ({len(text)} chars)  {text}")
    winner = ranked[0][2]
    print(f"\nWinner: {winner}")
    validate_and_write(winner)


def validate_and_write(line):
    """Gate: /output/entry.txt must be UTF-8 text of 1-140 chars, not blank."""
    import os

    assert isinstance(line, str), "entry must be a string"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line.strip(), "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    line.encode("utf-8")  # must be valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
