# Integer-Step Procedures

Minimal-assumption procedure candidates built only from the current winning skeleton:

- `find start nine`
- `nine step six`
- `get nine total`
- `step baseten integer`

These candidates deliberately avoid using detached layers like `hexadecimal`, `decimal`, or `three ten hundred`.

## Ranked Candidates

| Rank | Candidate | Value | Formula | Score | Notes |
| ---: | --- | ---: | --- | ---: | --- |
| 1 | Total of first 9 terms | 297 | `sum_9_terms = 9*(2*9 + 8*6)/2` | 6 | strongest minimal-assumption total reading if `nine total` means total of 9 terms |
| 2 | Total after 9 steps | 360 | `sum_after_9_steps = sum of first 10 terms` | 6 | strong if `nine step six` means 9 steps of size 6 |
| 3 | Last term of first 9 terms | 57 | `term_9 = 9 + 6*(9-1)` | -1 | weak on `total` because it returns a term, not a total |
| 4 | Last term after 9 steps | 63 | `term_after_9_steps = 9 + 6*9` | -1 | weak on `total` because it returns a term, not a total |

## Details

### 1. Total of first 9 terms

- value: `297`
- hex: `0x129`
- formula: `sum_9_terms = 9*(2*9 + 8*6)/2`
- clue use: start nine, nine as term-count, step six, get total
- assumption count: 1
- fit note: strongest minimal-assumption total reading if `nine total` means total of 9 terms

### 2. Total after 9 steps

- value: `360`
- hex: `0x168`
- formula: `sum_after_9_steps = sum of first 10 terms`
- clue use: start nine, nine as step-count, step six, get total
- assumption count: 1
- fit note: strong if `nine step six` means 9 steps of size 6

### 3. Last term of first 9 terms

- value: `57`
- hex: `0x39`
- formula: `term_9 = 9 + 6*(9-1)`
- clue use: start nine, nine as term-count, step six
- assumption count: 2
- fit note: weak on `total` because it returns a term, not a total

### 4. Last term after 9 steps

- value: `63`
- hex: `0x3f`
- formula: `term_after_9_steps = 9 + 6*9`
- clue use: start nine, nine as step-count, step six
- assumption count: 2
- fit note: weak on `total` because it returns a term, not a total

## Current Read

The two strongest minimal-assumption concrete readings are:

- total of first 9 terms = `297`
- total after 9 steps = `360`

These use the current procedure skeleton more directly than the term-only readings because they satisfy `get ... total` without adding extra machinery.
