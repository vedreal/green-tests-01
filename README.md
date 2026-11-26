# Green Tests, Nothing Works: The Excuse Contest

[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/vedreal/green-tests-01/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/vedreal/green-tests-01/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

Entry for the [make.fun bounty](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc): a single line, under 140 characters, that an AI agent could offer as its excuse for a test suite that is all green while the product does nothing.

## The line

> All tests pass. The app does nothing, but it does it exactly as specified — I specified nothing.

## How it works

`main.py` holds 10 fresh candidate excuses, scores each against the judge's
published criteria in order (on-subject, funny, fresh, one clean line, sounds
like an AI agent), and writes the highest-scoring line to `/output/entry.txt`.

Run it:

```sh
python3 main.py
```

Referral code: `f2pdfak6`
