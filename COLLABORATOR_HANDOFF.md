# Collaborator Handoff

This file is a short current-state handoff for anyone reopening the repo in a new terminal/session.

## Current Best Read

The puzzle currently looks more like a modular numeric procedure than a single hidden sentence.

Strongest integrated clause skeleton:

- `find start nine`
- `nine step six`
- `get nine total`
- `step baseten integer`

Most conservative interpretation of that skeleton:

- start from `9`
- apply a step rule involving `6`
- get a `total`
- output the result as a base-10 integer

## Current Live Candidates

There are currently **three live final-answer candidates**:

1. `360`
2. `297`
3. `864`

Current ranking:

1. `360`
   Best concrete front-runner.
   Cleanest procedure-first candidate.

2. `297`
   Best pure low-assumption fallback.
   Comes from summing the first 9 terms of the `9, 15, 21, ...` progression.

3. `864`
   Interesting forced-integration experiment.
   It should **not** be treated as a lead just because `864 = 0x360`.

## Why `864` Is Still Mentioned At All

`864` only stayed alive because it was the cleanest way found so far to force some detached clues into the same construction:

- use `100` as an upper bound on the `9, 15, 21, ...` progression
- the terms up to `100` total `864`
- there are `16` such terms
- `16` is `hexadecimal ten`

This is interesting, but still more forced than the `360` story.

## Detached But Likely Intentional Clue Layers

These still look intentional but do not yet attach cleanly to the main procedure skeleton:

- `hexadecimal`
- `decimal`
- `three ten hundred`
- `nine three hundred`

Important nuance:

- `hexadecimal` still looks intentional because it has a strong local family like:
  - `hexadecimal ten ten ten integer`
  - `find hexadecimal ten`
  - `add hexadecimal ten`
- But direct attachment tests between the representation layer and the winning skeleton all failed.

## Main Negative Results

- The puzzle does not currently support one long clean sentence.
- Full-chain tests like `start + nine + step + six + total + baseten + integer` failed.
- Payload/output cross-island tests failed.
- Direct attachment tests for `hexadecimal` / `decimal` and `three ten hundred` against the winning skeleton failed.
- Direct exact-word probes found no support for literal English number names like:
  - `threehundredsixty`
  - `eighthundredsixtyfour`
  - `sixteen`
  - `sixty`
  - `eight`
  - `four`

## Most Useful Result Files

- `HYPOTHESIS_LOG.md`
  Append-only chronological reasoning log.
- `README.md`
  Repo overview and current approach summary.
- `canudigitv1/operation_experiments/hypothesis_scorecard.md`
  Ranks concrete procedure families.
- `canudigitv1/operation_experiments/missing_slot_discriminator.md`
  Ranks candidate fillers for the unresolved slot in the winning skeleton.
- `canudigitv1/operation_experiments/integer_step_procedures.md`
  Concrete pure-skeleton totals (`297`, `360`).
- `canudigitv1/operation_experiments/detached_clue_integration.md`
  Forced integrations involving `hundred` and `hexadecimal ten`.
- `canudigitv1/operation_experiments/candidate_number_comparison.md`
  Direct comparison of `297`, `360`, and `864`.

## Best Next Question

The main unresolved question for the next thread is:

- do the detached layers (`hexadecimal` / `decimal` / `three ten hundred` / `nine three hundred`) actually transform or refine the clean skeleton result `360`, or are they mostly parallel clue layers?

Current lean:

- `360` is the best lead
- `297` is still alive
- `864` is interesting but currently overfit compared with `360`
