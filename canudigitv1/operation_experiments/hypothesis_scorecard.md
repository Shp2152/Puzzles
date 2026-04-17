# Hypothesis Scorecard

This report compares a small number of concrete endgame procedure families.
The goal is to rank stories by minimal assumptions first, while still rewarding strong clause support and bridge support.

## Scoring Model

For each hypothesis:

- `support_points` rewards strong chosen clauses
- `bridge_points` rewards lexical or spatial continuity between consecutive roles
- `gap_penalty` penalizes consecutive roles that have no direct lexical or spatial support
- `assumption_penalty` is `4 * unresolved_slots`
- `ignored_penalty` penalizes strong clue families that the hypothesis leaves unexplained
- `missing_role_penalty` penalizes any role the hypothesis could not fill from current clause evidence

This is not a proof engine. It is a way to avoid re-reading the same graph and instead compare concrete procedure stories under one fixed rubric.

## Ranked Hypotheses

| Rank | Hypothesis | Total | Support | Bridges | Gap penalty | Assumption penalty | Ignored penalty | Missing-role penalty |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | H1 Procedure Skeleton | 61 | 61 | 6 | 0 | 4 | 2 | 0 |
| 2 | H2 Integer-Step Procedure | 54 | 65 | 3 | 2 | 8 | 4 | 0 |
| 3 | H6 Payload-Slotted Procedure | 54 | 59 | 6 | 2 | 8 | 1 | 0 |
| 4 | H3 Nine-Total Procedure | 52 | 61 | 3 | 0 | 8 | 4 | 0 |
| 5 | H5 Payload-Driven | 33 | 58 | 0 | 2 | 16 | 7 | 0 |
| 6 | H4 Representation-Normalization | 18 | 34 | 3 | 0 | 12 | 7 | 0 |

## Details

### 1. H1 Procedure Skeleton

- summary: Start at 9, apply a step-of-6 style rule, obtain a total, then report as a base-10 integer.
- total score: 61
- score breakdown: support=61, bridges=6, gaps=-0, assumptions=-4, ignored=-2, missing_roles=-0
- chosen clauses:
  start: `find start nine` (region=upper-right, req=3, op_sup=2, all_sup=2)
  action: `nine step six` (region=lower-right, req=3, op_sup=2, all_sup=2)
  total: `get nine total` (region=lower-left, req=3, op_sup=2, all_sup=2)
  output: `step baseten integer` (region=lower-right, req=3, op_sup=2, all_sup=3)
- bridges:
  start -> action: +2 (shared=nine, overlap=0, distance=7)
  action -> total: +3 (shared=nine, overlap=0, distance=1)
  total -> output: +1 (shared=-, overlap=0, distance=1)
- unresolved slots:
  What exact object/process is being stepped and totaled?
- ignored clue families: payload, representation

### 2. H2 Integer-Step Procedure

- summary: Step through integers by 6 and report the result as a base-10 integer.
- total score: 54
- score breakdown: support=65, bridges=3, gaps=-2, assumptions=-8, ignored=-4, missing_roles=-0
- chosen clauses:
  start: `find start nine` (region=upper-right, req=3, op_sup=2, all_sup=2)
  action: `step integer six` (region=lower-right, req=3, op_sup=3, all_sup=3)
  output: `step baseten integer` (region=lower-right, req=3, op_sup=2, all_sup=3)
- bridges:
  start -> action: no direct lexical/spatial support
  action -> output: +3 (shared=integer, step, overlap=9, distance=0)
- unresolved slots:
  What quantity is totaled or targeted?
  Why does `get nine total` exist if total is not part of the procedure?
- ignored clue families: total, payload, representation

### 3. H6 Payload-Slotted Procedure

- summary: Use the start/step/total/output skeleton and assume `three ten hundred` fills the missing payload slot.
- total score: 54
- score breakdown: support=59, bridges=6, gaps=-2, assumptions=-8, ignored=-1, missing_roles=-0
- chosen clauses:
  start: `find start nine` (region=upper-right, req=3, op_sup=2, all_sup=2)
  action: `nine step six` (region=lower-right, req=3, op_sup=2, all_sup=2)
  total: `get nine total` (region=lower-left, req=3, op_sup=2, all_sup=2)
  output: `step baseten integer` (region=lower-right, req=3, op_sup=2, all_sup=3)
  payload: `three ten hundred` (region=upper-left, req=3, op_sup=1, all_sup=2)
- bridges:
  start -> action: +2 (shared=nine, overlap=0, distance=7)
  action -> total: +3 (shared=nine, overlap=0, distance=1)
  total -> output: +1 (shared=-, overlap=0, distance=1)
  output -> payload: no direct lexical/spatial support
- unresolved slots:
  How should `three ten hundred` be interpreted numerically?
  Why should the payload clause attach to the otherwise lower-right procedure?
- ignored clue families: representation

### 4. H3 Nine-Total Procedure

- summary: Start from 9, get a total involving 9, and report as a base-10 integer.
- total score: 52
- score breakdown: support=61, bridges=3, gaps=-0, assumptions=-8, ignored=-4, missing_roles=-0
- chosen clauses:
  start: `find start nine` (region=upper-right, req=3, op_sup=2, all_sup=2)
  total: `get nine total` (region=lower-left, req=3, op_sup=2, all_sup=2)
  output: `step baseten integer` (region=lower-right, req=3, op_sup=2, all_sup=3)
- bridges:
  start -> total: +2 (shared=nine, overlap=0, distance=8)
  total -> output: +1 (shared=-, overlap=0, distance=1)
- unresolved slots:
  What role does the step/6 family play?
  What operation turns the start value into the total?
- ignored clue families: action, payload, representation

### 5. H5 Payload-Driven

- summary: Treat `three ten hundred` as the payload and combine it with the base-10 output clue.
- total score: 33
- score breakdown: support=58, bridges=0, gaps=-2, assumptions=-16, ignored=-7, missing_roles=-0
- chosen clauses:
  payload: `three ten hundred` (region=upper-left, req=3, op_sup=1, all_sup=2)
  output: `step baseten integer` (region=lower-right, req=3, op_sup=2, all_sup=3)
- bridges:
  payload -> output: no direct lexical/spatial support
- unresolved slots:
  How should `three ten hundred` be interpreted numerically?
  Why are the start/nine clauses present?
  Why are the step/6 clauses present?
  Why is `get nine total` present?
- ignored clue families: start, action, total, representation

### 6. H4 Representation-Normalization

- summary: Interpret a representation-heavy numeric phrase and normalize it to a base-10 integer.
- total score: 18
- score breakdown: support=34, bridges=3, gaps=-0, assumptions=-12, ignored=-7, missing_roles=-0
- chosen clauses:
  representation: `decimal ten ten ten integer` (region=central/mixed, req=0, op_sup=0, all_sup=1)
  output: `step baseten integer` (region=lower-right, req=3, op_sup=2, all_sup=3)
- bridges:
  representation -> output: +3 (shared=integer, overlap=7, distance=0)
- unresolved slots:
  Why are the start/nine clauses present?
  Why are the step/6 clauses present?
  Why is `get nine total` present?
- ignored clue families: start, action, total, payload

## Current Read

What this ranking is meant to clarify:

- If one procedure family clearly leads, the graph is becoming discriminative rather than descriptive.
- If several families remain tied even after explicit penalties, the current modular story is still underconstrained.
- `three ten hundred` should only be promoted if a payload-using hypothesis ranks well without exploding the assumption count.
