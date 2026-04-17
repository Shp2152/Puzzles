# Detached Clue Integration

This report forces detached clues into a few natural arithmetic-progression interpretations of the current skeleton.

Fixed skeleton used here:

- start = 9
- step = 6
- seek some total / count / terminal value
- output as base-10 integer

Detached clues being forced in:

- `three ten hundred` as counts or bounds
- `hexadecimal` / `decimal` as representation-derived counts or values

## Ranked Integrations

| Rank | Construction | Family | Decimal | Hex | Score | Interpretation |
| ---: | --- | --- | ---: | --- | ---: | --- |
| 1 | Total up to 100 | payload | 864 | `360` | 17 | Treat `hundred` as upper bound. |
| 2 | Hex ten terms total | representation | 864 | `360` | 16 | Treat `hexadecimal ten` as decimal 16 terms. |
| 3 | Hex ten count to 100 | representation | 16 | `10` | 12 | Observe that the count to 100 is 16, i.e. hexadecimal ten. |
| 4 | 10 terms total | payload | 360 | `168` | 10 | Treat `ten` as term-count. |
| 5 | Count up to 100 | payload | 16 | `10` | 6 | Treat `hundred` as upper bound and count instead of total. |
| 6 | 3 terms total | payload | 45 | `2D` | 3 | Treat `three` as term-count. |
| 7 | 100 terms total | payload | 30600 | `7788` | 0 | Treat `hundred` as term-count. |
| 8 | Last term up to 100 | payload | 99 | `63` | 0 | Treat `hundred` as upper bound and keep the terminal term. |

## Direct Representation Values

- `hexadecimal ten ten ten` -> `2730` (hex `AAA`): Interpret `ten ten ten` as `A A A` under the `hexadecimal` label.
- `decimal ten ten ten` -> `101010` (hex `18A92`): Interpret `ten ten ten` literally as decimal `10 10 10`.

## Details

### 1. Total up to 100

- decimal value: `864`
- hex value: `360`
- formula: sum terms <= 100 in the 9 + 6k sequence
- clue use: Treat `hundred` as upper bound.
- heuristic score: 17

### 2. Hex ten terms total

- decimal value: `864`
- hex value: `360`
- formula: sum of first 16 terms of 9, 15, 21, ...
- clue use: Treat `hexadecimal ten` as decimal 16 terms.
- heuristic score: 16

### 3. Hex ten count to 100

- decimal value: `16`
- hex value: `10`
- formula: count terms <= 100 in the 9 + 6k sequence
- clue use: Observe that the count to 100 is 16, i.e. hexadecimal ten.
- heuristic score: 12

### 4. 10 terms total

- decimal value: `360`
- hex value: `168`
- formula: sum of first 10 terms of 9, 15, 21, ...
- clue use: Treat `ten` as term-count.
- heuristic score: 10

### 5. Count up to 100

- decimal value: `16`
- hex value: `10`
- formula: count terms <= 100 in the 9 + 6k sequence
- clue use: Treat `hundred` as upper bound and count instead of total.
- heuristic score: 6

### 6. 3 terms total

- decimal value: `45`
- hex value: `2D`
- formula: sum of first 3 terms of 9, 15, 21, ...
- clue use: Treat `three` as term-count.
- heuristic score: 3

### 7. 100 terms total

- decimal value: `30600`
- hex value: `7788`
- formula: sum of first 100 terms of 9, 15, 21, ...
- clue use: Treat `hundred` as term-count.
- heuristic score: 0

### 8. Last term up to 100

- decimal value: `99`
- hex value: `63`
- formula: last term <= 100 in the 9 + 6k sequence
- clue use: Treat `hundred` as upper bound and keep the terminal term.
- heuristic score: 0

## Current Read

The most notable constructions from this forced-integration pass are:

- `10 terms total = 360`
- `total up to 100 = 864 = 0x360`
- `count up to 100 = 16 = hexadecimal ten`
- `hex ten terms total = 864`

These are not proved solutions. They are the first somewhat usable constructions that let the detached layers interact with the step-6 skeleton in a nontrivial way.
