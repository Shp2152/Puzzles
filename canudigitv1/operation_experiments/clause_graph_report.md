# Clause Graph Report

Candidate clause graph and overlap report built from the current default run plus the targeted operation-word experiments.

## How Strength Is Measured

Clause strength here is not just raw frequency in the sentence scorer.

A clause is treated as stronger when several of these are true:

- it survives as a `TOP CONTENT CORE`, not only as a fluent-looking full phrase
- it survives a targeted `--must-have-all` experiment
- it survives a more specific experiment with more required words
- it appears in more than one output file or experiment
- it keeps a high best-score while staying content-heavy

In the tables below:

- `req` means the largest number of required words in a successful supporting experiment
- `op_sup` means how many successful operation experiments support the clause
- `all_sup` means total supporting output files, including the default run

## Candidate Clauses

| Core | Kind | Region | req | op_sup | all_sup | Best score | Representative phrase | BBox |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| `step integer six` | instruction | lower-right | 3 | 3 | 3 | 55 | `step into integer by six` | `I10:N14` |
| `step baseten integer` | representation | lower-right | 3 | 2 | 3 | 57 | `step baseten to integer` | `H9:N14` |
| `nine step six` | instruction | lower-right | 3 | 2 | 2 | 48 | `nine step or six` | `H11:N14` |
| `get nine total` | instruction | lower-left | 3 | 2 | 2 | 47 | `get nine total` | `B10:G14` |
| `add start nine` | instruction | upper-right | 3 | 2 | 2 | 47 | `add the start nine` | `G1:N4` |
| `find start nine` | instruction | upper-right | 3 | 2 | 2 | 46 | `find the start nine` | `E1:N4` |
| `three ten hundred` | payload | upper-left | 3 | 1 | 2 | 57 | `three ten in hundred` | `A1:D6` |
| `is integer six` | hybrid | lower-right | 3 | 1 | 1 | 53 | `is into integer by six` | `I10:N14` |
| `is integer baseten` | representation | lower-right | 2 | 1 | 1 | 53 | `is integer baseten` | `H10:M14` |
| `ten step six` | payload | lower-right | 2 | 1 | 1 | 47 | `ten step or six` | `F12:N14` |
| `baseten integer` | representation | lower-right | 2 | 1 | 1 | 42 | `baseten to integer` | `H10:M14` |
| `get step six` | instruction | lower-right | 2 | 1 | 1 | 42 | `get step or six` | `L9:N14` |
| `integer baseten` | representation | lower-right | 2 | 1 | 1 | 40 | `integer baseten` | `H10:M14` |
| `step six` | instruction | lower-right | 2 | 1 | 1 | 32 | `step or six` | `L9:N14` |
| `start nine` | instruction | upper-right | 2 | 1 | 1 | 32 | `start nine` | `K1:N4` |
| `decimal ten ten ten integer` | representation | central/mixed | 0 | 0 | 1 | 75 | `decimal as ten ten ten integer` | `B7:M14` |
| `hexadecimal ten ten ten integer` | representation | right-spanning | 0 | 0 | 1 | 74 | `hexadecimal as ten ten ten integer` | `B3:M14` |

## Clause Details

### `step integer six`

- kind: instruction
- representative phrase: `step into integer by six`
- representative region: lower-right
- representative bbox: `I10:N14`
- strength signals: req=3, op_sup=3, all_sup=3, best_score=55
- supporting outputs: `op_step_integer_six, op_into_integer_six, op_step_six`

### `step baseten integer`

- kind: representation
- representative phrase: `step baseten to integer`
- representative region: lower-right
- representative bbox: `H9:N14`
- strength signals: req=3, op_sup=2, all_sup=3, best_score=57
- supporting outputs: `op_step_baseten_integer, op_baseten_integer, default`

### `nine step six`

- kind: instruction
- representative phrase: `nine step or six`
- representative region: lower-right
- representative bbox: `H11:N14`
- strength signals: req=3, op_sup=2, all_sup=2, best_score=48
- supporting outputs: `op_nine_step_six, op_step_six`

### `get nine total`

- kind: instruction
- representative phrase: `get nine total`
- representative region: lower-left
- representative bbox: `B10:G14`
- strength signals: req=3, op_sup=2, all_sup=2, best_score=47
- supporting outputs: `op_get_nine_total, op_get_total`

### `add start nine`

- kind: instruction
- representative phrase: `add the start nine`
- representative region: upper-right
- representative bbox: `G1:N4`
- strength signals: req=3, op_sup=2, all_sup=2, best_score=47
- supporting outputs: `op_add_start_nine, op_start_nine`

### `find start nine`

- kind: instruction
- representative phrase: `find the start nine`
- representative region: upper-right
- representative bbox: `E1:N4`
- strength signals: req=3, op_sup=2, all_sup=2, best_score=46
- supporting outputs: `op_find_start_nine, op_start_nine`

### `three ten hundred`

- kind: payload
- representative phrase: `three ten in hundred`
- representative region: upper-left
- representative bbox: `A1:D6`
- strength signals: req=3, op_sup=1, all_sup=2, best_score=57
- supporting outputs: `op_three_ten_hundred, default`

### `is integer six`

- kind: hybrid
- representative phrase: `is into integer by six`
- representative region: lower-right
- representative bbox: `I10:N14`
- strength signals: req=3, op_sup=1, all_sup=1, best_score=53
- supporting outputs: `op_into_integer_six`

### `is integer baseten`

- kind: representation
- representative phrase: `is integer baseten`
- representative region: lower-right
- representative bbox: `H10:M14`
- strength signals: req=2, op_sup=1, all_sup=1, best_score=53
- supporting outputs: `op_baseten_integer`

### `ten step six`

- kind: payload
- representative phrase: `ten step or six`
- representative region: lower-right
- representative bbox: `F12:N14`
- strength signals: req=2, op_sup=1, all_sup=1, best_score=47
- supporting outputs: `op_step_six`

### `baseten integer`

- kind: representation
- representative phrase: `baseten to integer`
- representative region: lower-right
- representative bbox: `H10:M14`
- strength signals: req=2, op_sup=1, all_sup=1, best_score=42
- supporting outputs: `op_baseten_integer`

### `get step six`

- kind: instruction
- representative phrase: `get step or six`
- representative region: lower-right
- representative bbox: `L9:N14`
- strength signals: req=2, op_sup=1, all_sup=1, best_score=42
- supporting outputs: `op_step_six`

### `integer baseten`

- kind: representation
- representative phrase: `integer baseten`
- representative region: lower-right
- representative bbox: `H10:M14`
- strength signals: req=2, op_sup=1, all_sup=1, best_score=40
- supporting outputs: `op_baseten_integer`

### `step six`

- kind: instruction
- representative phrase: `step or six`
- representative region: lower-right
- representative bbox: `L9:N14`
- strength signals: req=2, op_sup=1, all_sup=1, best_score=32
- supporting outputs: `op_step_six`

### `start nine`

- kind: instruction
- representative phrase: `start nine`
- representative region: upper-right
- representative bbox: `K1:N4`
- strength signals: req=2, op_sup=1, all_sup=1, best_score=32
- supporting outputs: `op_start_nine`

### `decimal ten ten ten integer`

- kind: representation
- representative phrase: `decimal as ten ten ten integer`
- representative region: central/mixed
- representative bbox: `B7:M14`
- strength signals: req=0, op_sup=0, all_sup=1, best_score=75
- supporting outputs: `default`

### `hexadecimal ten ten ten integer`

- kind: representation
- representative phrase: `hexadecimal as ten ten ten integer`
- representative region: right-spanning
- representative bbox: `B3:M14`
- strength signals: req=0, op_sup=0, all_sup=1, best_score=74
- supporting outputs: `default`

## Lexical Bridges

These edges connect clauses that share at least one content word. This is the main candidate clause graph.

| Left | Right | Shared words | Spatial overlap | Min distance |
| --- | --- | --- | ---: | ---: |
| `add start nine` | `find start nine` | `nine, start` | 10 | 0 |
| `add start nine` | `start nine` | `nine, start` | 9 | 0 |
| `baseten integer` | `integer baseten` | `baseten, integer` | 14 | 0 |
| `baseten integer` | `is integer baseten` | `baseten, integer` | 13 | 0 |
| `baseten integer` | `step baseten integer` | `baseten, integer` | 14 | 0 |
| `decimal ten ten ten integer` | `hexadecimal ten ten ten integer` | `integer, ten` | 23 | 0 |
| `find start nine` | `start nine` | `nine, start` | 9 | 0 |
| `get step six` | `nine step six` | `six, step` | 3 | 0 |
| `get step six` | `step integer six` | `six, step` | 4 | 0 |
| `get step six` | `step six` | `six, step` | 7 | 0 |
| `get step six` | `ten step six` | `six, step` | 3 | 0 |
| `integer baseten` | `is integer baseten` | `baseten, integer` | 13 | 0 |
| `integer baseten` | `step baseten integer` | `baseten, integer` | 14 | 0 |
| `is integer baseten` | `is integer six` | `integer, is` | 8 | 0 |
| `is integer baseten` | `step baseten integer` | `baseten, integer` | 13 | 0 |
| `is integer six` | `step integer six` | `integer, six` | 11 | 0 |
| `nine step six` | `step integer six` | `six, step` | 8 | 0 |
| `nine step six` | `step six` | `six, step` | 3 | 0 |
| `nine step six` | `ten step six` | `six, step` | 8 | 0 |
| `step baseten integer` | `step integer six` | `integer, step` | 9 | 0 |
| `step integer six` | `step six` | `six, step` | 3 | 0 |
| `step integer six` | `ten step six` | `six, step` | 7 | 0 |
| `step six` | `ten step six` | `six, step` | 3 | 0 |
| `baseten integer` | `decimal ten ten ten integer` | `integer` | 7 | 0 |
| `baseten integer` | `hexadecimal ten ten ten integer` | `integer` | 7 | 0 |
| `baseten integer` | `is integer six` | `integer` | 7 | 0 |
| `baseten integer` | `step integer six` | `integer` | 9 | 0 |
| `decimal ten ten ten integer` | `integer baseten` | `integer` | 7 | 0 |
| `decimal ten ten ten integer` | `is integer baseten` | `integer` | 8 | 0 |
| `decimal ten ten ten integer` | `is integer six` | `integer` | 6 | 0 |
| `decimal ten ten ten integer` | `step baseten integer` | `integer` | 7 | 0 |
| `decimal ten ten ten integer` | `step integer six` | `integer` | 6 | 0 |
| `decimal ten ten ten integer` | `ten step six` | `ten` | 3 | 0 |
| `get step six` | `is integer six` | `six` | 4 | 0 |
| `get step six` | `step baseten integer` | `step` | 5 | 0 |
| `hexadecimal ten ten ten integer` | `integer baseten` | `integer` | 7 | 0 |
| `hexadecimal ten ten ten integer` | `is integer baseten` | `integer` | 8 | 0 |
| `hexadecimal ten ten ten integer` | `is integer six` | `integer` | 6 | 0 |
| `hexadecimal ten ten ten integer` | `step baseten integer` | `integer` | 7 | 0 |
| `hexadecimal ten ten ten integer` | `step integer six` | `integer` | 6 | 0 |
| `hexadecimal ten ten ten integer` | `ten step six` | `ten` | 3 | 0 |
| `integer baseten` | `is integer six` | `integer` | 7 | 0 |
| `integer baseten` | `step integer six` | `integer` | 9 | 0 |
| `is integer baseten` | `step integer six` | `integer` | 9 | 0 |
| `is integer six` | `nine step six` | `six` | 5 | 0 |
| `is integer six` | `step baseten integer` | `integer` | 7 | 0 |
| `is integer six` | `step six` | `six` | 3 | 0 |
| `is integer six` | `ten step six` | `six` | 4 | 0 |
| `nine step six` | `step baseten integer` | `step` | 5 | 0 |
| `step baseten integer` | `step six` | `step` | 3 | 0 |
| `step baseten integer` | `ten step six` | `step` | 3 | 0 |
| `get nine total` | `nine step six` | `nine` | 0 | 1 |
| `decimal ten ten ten integer` | `three ten hundred` | `ten` | 0 | 3 |
| `hexadecimal ten ten ten integer` | `three ten hundred` | `ten` | 0 | 3 |
| `get nine total` | `get step six` | `get` | 0 | 5 |
| `ten step six` | `three ten hundred` | `ten` | 0 | 6 |
| `add start nine` | `nine step six` | `nine` | 0 | 7 |
| `find start nine` | `nine step six` | `nine` | 0 | 7 |
| `nine step six` | `start nine` | `nine` | 0 | 7 |
| `add start nine` | `get nine total` | `nine` | 0 | 8 |
| `find start nine` | `get nine total` | `nine` | 0 | 8 |
| `get nine total` | `start nine` | `nine` | 0 | 8 |

## Spatial Overlap Report

These edges connect clauses whose representative content paths overlap or sit within distance 2, even if they do not share words.

| Left | Right | Shared words | Spatial overlap | Min distance |
| --- | --- | --- | ---: | ---: |
| `decimal ten ten ten integer` | `hexadecimal ten ten ten integer` | `integer, ten` | 23 | 0 |
| `baseten integer` | `integer baseten` | `baseten, integer` | 14 | 0 |
| `baseten integer` | `step baseten integer` | `baseten, integer` | 14 | 0 |
| `integer baseten` | `step baseten integer` | `baseten, integer` | 14 | 0 |
| `baseten integer` | `is integer baseten` | `baseten, integer` | 13 | 0 |
| `integer baseten` | `is integer baseten` | `baseten, integer` | 13 | 0 |
| `is integer baseten` | `step baseten integer` | `baseten, integer` | 13 | 0 |
| `is integer six` | `step integer six` | `integer, six` | 11 | 0 |
| `add start nine` | `find start nine` | `nine, start` | 10 | 0 |
| `add start nine` | `start nine` | `nine, start` | 9 | 0 |
| `baseten integer` | `step integer six` | `integer` | 9 | 0 |
| `find start nine` | `start nine` | `nine, start` | 9 | 0 |
| `integer baseten` | `step integer six` | `integer` | 9 | 0 |
| `is integer baseten` | `step integer six` | `integer` | 9 | 0 |
| `step baseten integer` | `step integer six` | `integer, step` | 9 | 0 |
| `decimal ten ten ten integer` | `get nine total` | `-` | 8 | 0 |
| `decimal ten ten ten integer` | `is integer baseten` | `integer` | 8 | 0 |
| `get nine total` | `hexadecimal ten ten ten integer` | `-` | 8 | 0 |
| `hexadecimal ten ten ten integer` | `is integer baseten` | `integer` | 8 | 0 |
| `is integer baseten` | `is integer six` | `integer, is` | 8 | 0 |
| `nine step six` | `step integer six` | `six, step` | 8 | 0 |
| `nine step six` | `ten step six` | `six, step` | 8 | 0 |
| `baseten integer` | `decimal ten ten ten integer` | `integer` | 7 | 0 |
| `baseten integer` | `hexadecimal ten ten ten integer` | `integer` | 7 | 0 |
| `baseten integer` | `is integer six` | `integer` | 7 | 0 |
| `decimal ten ten ten integer` | `integer baseten` | `integer` | 7 | 0 |
| `decimal ten ten ten integer` | `step baseten integer` | `integer` | 7 | 0 |
| `get step six` | `step six` | `six, step` | 7 | 0 |
| `hexadecimal ten ten ten integer` | `integer baseten` | `integer` | 7 | 0 |
| `hexadecimal ten ten ten integer` | `step baseten integer` | `integer` | 7 | 0 |
| `integer baseten` | `is integer six` | `integer` | 7 | 0 |
| `is integer baseten` | `nine step six` | `-` | 7 | 0 |
| `is integer six` | `step baseten integer` | `integer` | 7 | 0 |
| `step integer six` | `ten step six` | `six, step` | 7 | 0 |
| `decimal ten ten ten integer` | `is integer six` | `integer` | 6 | 0 |
| `decimal ten ten ten integer` | `step integer six` | `integer` | 6 | 0 |
| `hexadecimal ten ten ten integer` | `is integer six` | `integer` | 6 | 0 |
| `hexadecimal ten ten ten integer` | `step integer six` | `integer` | 6 | 0 |
| `baseten integer` | `nine step six` | `-` | 5 | 0 |
| `get step six` | `step baseten integer` | `step` | 5 | 0 |
| `integer baseten` | `nine step six` | `-` | 5 | 0 |
| `is integer six` | `nine step six` | `six` | 5 | 0 |
| `nine step six` | `step baseten integer` | `step` | 5 | 0 |
| `get step six` | `is integer six` | `six` | 4 | 0 |
| `get step six` | `step integer six` | `six, step` | 4 | 0 |
| `is integer baseten` | `ten step six` | `-` | 4 | 0 |
| `is integer six` | `ten step six` | `six` | 4 | 0 |
| `baseten integer` | `ten step six` | `-` | 3 | 0 |
| `decimal ten ten ten integer` | `nine step six` | `-` | 3 | 0 |
| `decimal ten ten ten integer` | `ten step six` | `ten` | 3 | 0 |
| `get step six` | `nine step six` | `six, step` | 3 | 0 |
| `get step six` | `ten step six` | `six, step` | 3 | 0 |
| `hexadecimal ten ten ten integer` | `nine step six` | `-` | 3 | 0 |
| `hexadecimal ten ten ten integer` | `ten step six` | `ten` | 3 | 0 |
| `integer baseten` | `ten step six` | `-` | 3 | 0 |
| `is integer six` | `step six` | `six` | 3 | 0 |
| `nine step six` | `step six` | `six, step` | 3 | 0 |
| `step baseten integer` | `step six` | `step` | 3 | 0 |
| `step baseten integer` | `ten step six` | `step` | 3 | 0 |
| `step integer six` | `step six` | `six, step` | 3 | 0 |
| `step six` | `ten step six` | `six, step` | 3 | 0 |
| `get nine total` | `ten step six` | `-` | 2 | 0 |
| `baseten integer` | `get step six` | `-` | 1 | 0 |
| `decimal ten ten ten integer` | `get step six` | `-` | 1 | 0 |
| `get step six` | `hexadecimal ten ten ten integer` | `-` | 1 | 0 |
| `get step six` | `integer baseten` | `-` | 1 | 0 |
| `get step six` | `is integer baseten` | `-` | 1 | 0 |
| `add start nine` | `hexadecimal ten ten ten integer` | `-` | 0 | 1 |
| `baseten integer` | `get nine total` | `-` | 0 | 1 |
| `baseten integer` | `step six` | `-` | 0 | 1 |
| `decimal ten ten ten integer` | `step six` | `-` | 0 | 1 |
| `find start nine` | `three ten hundred` | `-` | 0 | 1 |
| `get nine total` | `integer baseten` | `-` | 0 | 1 |
| `get nine total` | `is integer baseten` | `-` | 0 | 1 |
| `get nine total` | `nine step six` | `nine` | 0 | 1 |
| `get nine total` | `step baseten integer` | `-` | 0 | 1 |
| `hexadecimal ten ten ten integer` | `step six` | `-` | 0 | 1 |
| `integer baseten` | `step six` | `-` | 0 | 1 |
| `is integer baseten` | `step six` | `-` | 0 | 1 |
| `find start nine` | `hexadecimal ten ten ten integer` | `-` | 0 | 2 |
| `get nine total` | `is integer six` | `-` | 0 | 2 |
| `get nine total` | `step integer six` | `-` | 0 | 2 |
| `hexadecimal ten ten ten integer` | `start nine` | `-` | 0 | 2 |

## Word Hubs

Words that appear in multiple candidate clauses are the most plausible semantic pivots.

| Word | Clause count | Clauses |
| --- | ---: | --- |
| `integer` | 8 | `baseten integer`, `decimal ten ten ten integer`, `hexadecimal ten ten ten integer`, `integer baseten`, `is integer baseten`, `is integer six`, `step baseten integer`, `step integer six` |
| `step` | 6 | `get step six`, `nine step six`, `step baseten integer`, `step integer six`, `step six`, `ten step six` |
| `six` | 6 | `get step six`, `is integer six`, `nine step six`, `step integer six`, `step six`, `ten step six` |
| `nine` | 5 | `add start nine`, `find start nine`, `get nine total`, `nine step six`, `start nine` |
| `baseten` | 4 | `baseten integer`, `integer baseten`, `is integer baseten`, `step baseten integer` |
| `ten` | 4 | `decimal ten ten ten integer`, `hexadecimal ten ten ten integer`, `ten step six`, `three ten hundred` |
| `start` | 3 | `add start nine`, `find start nine`, `start nine` |
| `get` | 2 | `get nine total`, `get step six` |
| `is` | 2 | `is integer baseten`, `is integer six` |

## Failed Composition Tests

These experiments required multiple words at once and produced no phrase. They are negative evidence against a single-sentence reading.

| Failed required words | Nearby successful clauses |
| --- | --- |
| `start, nine, step, six, total, baseten, integer` | `step integer six`, `step baseten integer`, `nine step six`, `ten step six` |
| `three, ten, hundred, baseten, integer` | `three ten hundred`, `step baseten integer`, `is integer baseten`, `integer baseten` |
| `start, nine, step, six, total` | `nine step six`, `ten step six`, `step six`, `step integer six` |
| `get, total, baseten, integer` | `step baseten integer`, `is integer baseten`, `integer baseten`, `get nine total` |
| `start, nine, baseten, integer` | `step baseten integer`, `start nine`, `is integer baseten`, `integer baseten` |
| `step, baseten, integer, six` | `step integer six`, `step baseten integer`, `ten step six`, `step six` |
| `open, integer` | - |
| `point, integer` | - |

## Current Read

What jumps out from the current graph:

- `nine` is the strongest lexical bridge between the upper-right instruction family and the lower-right action/total family.
- `step` and `integer` are the strongest lower-right pivots.
- `baseten integer` and `step baseten integer` look like output-format clauses rather than payload clauses.
- `three ten hundred` remains a payload candidate, but it is still not graph-connected to the output clauses by a successful joint phrase.
- The failed composition tests strongly suggest that the puzzle is exposing several short clauses that must be composed conceptually, not one long readable sentence.

Graphviz file: `clause_graph.dot`
