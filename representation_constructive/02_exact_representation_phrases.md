# Exact Representation Phrases

All phrases below were verified against `can u dig it.csv:1-14` with `representation_constructive/exact_instance_search.py` under the standard 8-neighbor rule and no cell reuse across a phrase path.

Search note:

- The vocabulary search itself was exhaustive over the controlled seed set in `01_seed_vocabulary.md`.
- That exhaustive search generated many exact but low-value combinatorial phrases.
- This file records every promoted representation-relevant instance and every promoted bridge instance used later in the branch comparison.
- Low-confidence junk strings such as `the ones the get` or `step base tens into` were not promoted as evidence.

## High-Confidence Representation Objects

### R1. `hexadecimal ten ten ten integer`

- Exact phrase text: `hexadecimal ten ten ten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `ten`: `C12 -> B13 -> C14`
  - `ten`: `C13 -> D14 -> E14`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: very high
- Promoted attachments:
  - R2 by direct reuse of all five word instances except the added tail
  - R7/R8 by direct reuse of the same lower-right `integer` instance

### R2. `hexadecimal ten ten ten integer by six`

- Exact phrase text: `hexadecimal ten ten ten integer by six`
- Source file: `can u dig it.csv`
- Exact path:
  - same first five word instances as R1
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Valid under movement rule: yes
- Glue words included exactly: yes, includes `by`
- Local confidence: very high
- Promoted attachments:
  - R1 by direct reuse of the representation object
  - R13 by direct reuse of the same `integer`, `by`, and `six`

### R3. `decimal ten ten ten integer`

- Exact phrase text: `decimal ten ten ten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `decimal`: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `ten`: `C12 -> B13 -> C14`
  - `ten`: `C13 -> D14 -> E14`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: very high
- Promoted attachments:
  - R4 by direct reuse of all five word instances except the added tail
  - R7/R8 by direct reuse of the same lower-right `integer` instance

### R4. `decimal ten ten ten integer by six`

- Exact phrase text: `decimal ten ten ten integer by six`
- Source file: `can u dig it.csv`
- Exact path:
  - same first five word instances as R3
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Valid under movement rule: yes
- Glue words included exactly: yes, includes `by`
- Local confidence: very high
- Promoted attachments:
  - R3 by direct reuse of the representation object
  - R13 by direct reuse of the same `integer`, `by`, and `six`

### R5a. `binary ten integer`

- Exact phrase text: `binary ten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - R6a by direct reuse of all three word instances except the added tail
  - B1/B3 by direct reuse of the same `binary` instance

### R5b. `binary ten integer`

- Exact phrase text: `binary ten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `binary`: `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
  - `ten`: `F14 -> G13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - R6b by direct reuse of all three word instances except the added tail
  - B2/B4 by direct reuse of the same `binary` instance

### R6a. `binary ten integer by six`

- Exact phrase text: `binary ten integer by six`
- Source file: `can u dig it.csv`
- Exact path:
  - same first three word instances as R5a
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Valid under movement rule: yes
- Glue words included exactly: yes, includes `by`
- Local confidence: high
- Promoted attachments:
  - R5a by direct reuse of the representation object
  - B1/B3 by direct reuse of the same `binary` instance
  - R13 by direct reuse of `ten`, `integer`, `by`, and `six`

### R6b. `binary ten integer by six`

- Exact phrase text: `binary ten integer by six`
- Source file: `can u dig it.csv`
- Exact path:
  - same first three word instances as R5b
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Valid under movement rule: yes
- Glue words included exactly: yes, includes `by`
- Local confidence: high
- Promoted attachments:
  - R5b by direct reuse of the representation object
  - B2/B4 by direct reuse of the same `binary` instance
  - R13 by direct reuse of `ten`, `integer`, `by`, and `six`

### R7. `baseten integer`

- Exact phrase text: `baseten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - R8a/R8b by direct reuse of the same `baseten` and `integer`
  - R11 by genuine spatial overlap with the split `base ten integer` reading

### R8a. `step baseten integer`

- Exact phrase text: `step baseten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `step`: `N9 -> M9 -> M10 -> L11`
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - R7 by direct reuse of the same `baseten` and `integer`
  - R12a by genuine spatial overlap with the split `step base ten integer` reading

### R8b. `step baseten integer`

- Exact phrase text: `step baseten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `step`: `N9 -> N10 -> M10 -> L11`
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - R7 by direct reuse of the same `baseten` and `integer`
  - R12b by genuine spatial overlap with the split `step base ten integer` reading

## High-Confidence Exact Tails And Output Bridges

### R9. `step by six`

- Exact phrase text: `step by six`
- Source file: `can u dig it.csv`
- Promoted instances:
  - `N9 -> M9 -> M10 -> L11 / L12 -> M13 / L14 -> M14 -> N14`
  - `N9 -> N10 -> M10 -> L11 / L12 -> M13 / L14 -> M14 -> N14`
  - `N9 -> N10 -> M11 -> L11 / L12 -> M13 / L14 -> M14 -> N14`
- Valid under movement rule: yes for all three
- Glue words included exactly: yes, includes `by`
- Local confidence: high
- Promoted attachments:
  - R8a/R8b by direct reuse of the `step` instance family in the same lower-right zone
  - R13 by direct reuse of `by` and `six`

### R10. `step into integer by six`

- Exact phrase text: `step into integer by six`
- Source file: `can u dig it.csv`
- Exact path:
  - `step`: `I13 -> I14 -> J14 -> J13`
  - `into`: `I12 -> H12 -> H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Valid under movement rule: yes
- Glue words included exactly: yes, includes `into` and `by`
- Local confidence: high
- Promoted attachments:
  - R13 by direct reuse of `integer`, `by`, and `six`

### R11. `base ten integer`

- Exact phrase text: `base ten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium-high
- Promoted attachments:
  - R7 by genuine spatial overlap: the `base` and `ten` paths concatenate to the exact `baseten` path in R7
  - R12a/R12b by direct reuse of the same `base`, `ten`, and `integer`

### R12a. `step base ten integer`

- Exact phrase text: `step base ten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `step`: `N9 -> M9 -> M10 -> L11`
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium-high
- Promoted attachments:
  - R8a by genuine spatial overlap with the unsplit `baseten` reading
  - R11 by direct reuse of `base`, `ten`, and `integer`

### R12b. `step base ten integer`

- Exact phrase text: `step base ten integer`
- Source file: `can u dig it.csv`
- Exact path:
  - `step`: `N9 -> N10 -> M10 -> L11`
  - `base`: `L12 -> L13 -> K14 -> J14`
  - `ten`: `I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium-high
- Promoted attachments:
  - R8b by genuine spatial overlap with the unsplit `baseten` reading
  - R11 by direct reuse of `base`, `ten`, and `integer`

### R13. `integer by six`

- Exact phrase text: `integer by six`
- Source file: `can u dig it.csv`
- Promoted instances:
  - `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
  - `J12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> M14 -> N14`
- Valid under movement rule: yes for all three
- Glue words included exactly: yes, includes `by`
- Local confidence: high
- Promoted attachments:
  - R2/R4/R6a/R6b by direct reuse of the same `integer`, `by`, and `six`
  - R10 by direct reuse of the same tail

## Promoted Representation-To-Total And Representation-To-Tens Bridges

### B1. `binary get nine total`

- Exact phrase text: `binary get nine total`
- Source file: `can u dig it.csv`
- Exact path:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> B13`
  - `total`: `C13 -> D12 -> C12 -> B11 -> B10`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - R5a/R6a by direct reuse of the same `binary` instance
  - B3 by direct reuse of the same `binary`, `get`, and `nine` instance family

### B2. `binary get nine total`

- Exact phrase text: `binary get nine total`
- Source file: `can u dig it.csv`
- Exact path:
  - `binary`: `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> B13`
  - `total`: `C13 -> D12 -> C12 -> B11 -> B10`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - R5b/R6b by direct reuse of the same `binary` instance
  - B4 by direct reuse of the same `binary`, `get`, and `nine` instance family

### B3. `binary get nine tens`

- Exact phrase text: `binary get nine tens`
- Source file: `can u dig it.csv`
- Exact path:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> D14`
  - `tens`: `C13 -> B13 -> A12 -> A11`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium-high
- Promoted attachments:
  - R5a/R6a by direct reuse of the same `binary` instance
  - B1 by direct reuse of the same `binary` and `get` instances

### B4. `binary get nine tens`

- Exact phrase text: `binary get nine tens`
- Source file: `can u dig it.csv`
- Exact path:
  - `binary`: `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
  - `get`: `F12 -> G13 -> F14`
  - `nine`: `E14 -> D13 -> C14 -> D14`
  - `tens`: `C13 -> B13 -> A12 -> A11`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium-high
- Promoted attachments:
  - R5b/R6b by direct reuse of the same `binary` instance
  - B2 by direct reuse of the same `binary` and `get` instances

Audit-significance note:

- B1-B4 are the first exact raw-grid bridges in this pass that attach a representation word directly to the lower `get nine total` and `get nine tens` cluster.
- The bridge is asymmetric: `binary` attaches; `decimal` and `hexadecimal` do not have corresponding exact `... get nine total` or `... get nine tens` phrases in this pass.

## Place-Value Phrases Still Relevant To The Representation Search

### P1. `decimal tens`

- Exact phrase text: `decimal tens`
- Source file: `can u dig it.csv`
- Promoted instances:
  - `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> A12 -> A11`
  - `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> A12 -> B12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium
- Promoted attachments:
  - R3/R4 by direct reuse of the same `decimal` instance

### P2. `hexadecimal tens`

- Exact phrase text: `hexadecimal tens`
- Source file: `can u dig it.csv`
- Promoted instances:
  - `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> A12 -> A11`
  - `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11 / C12 -> B13 -> A12 -> B12`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium
- Promoted attachments:
  - R1/R2 by direct reuse of the same `hexadecimal` instance

### P3. `binary tens`

- Exact phrase text: `binary tens`
- Source file: `can u dig it.csv`
- Promoted instances:
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12 -> I13`
  - `F10 -> F11 -> E11 -> E12 -> E13 -> F13 / F14 -> G13 -> H12 -> I13`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium
- Promoted attachments:
  - R5a/R6a or R5b/R6b by direct reuse of the same `binary` instance
  - B3/B4 as the stronger exact representation-to-tens bridge

### P4. `get nine total`

- Exact phrase text: `get nine total`
- Source file: `can u dig it.csv`
- Promoted instances:
  - `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> B13 / C13 -> D12 -> C12 -> B11 -> B10`
  - `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: high
- Promoted attachments:
  - B1/B2 by direct reuse of `get`, `nine`, and `total` instances

### P5. `three ten hundred`

- Exact phrase text: `three ten hundred`
- Source file: `can u dig it.csv`
- Exact path:
  - `three`: `C3 -> B2 -> C2 -> B3 -> A4`
  - `ten`: `B5 -> C4 -> C5`
  - `hundred`: `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium-high
- Promoted attachments:
  - currently none into the lower-right representation component

### P6. `three ten hundreds`

- Exact phrase text: `three ten hundreds`
- Source file: `can u dig it.csv`
- Exact path:
  - same `three` and `ten` as P5
  - `hundreds`: `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1 -> B1`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium
- Promoted attachments:
  - currently none into the lower-right representation component

### P7. `get ones`

- Exact phrase text: `get ones`
- Source file: `can u dig it.csv`
- Exact path:
  - `get`: `J3 -> J2 -> K2`
  - `ones`: `K3 -> L4 -> M5 -> M6`
- Valid under movement rule: yes
- Glue words included exactly: not applicable
- Local confidence: medium
- Promoted attachments:
  - currently none into the lower-right representation component

## Exact Negatives That Matter

These were directly tested in this pass and returned zero exact matches.

- no exact `baseten integer by six`
- no exact `step baseten integer by six`
- no exact `get nine total baseten integer`
- no exact `get nine total integer`
- no exact `decimal ones`
- no exact `hexadecimal ones`
- no exact `binary ones`
- no exact `decimal hundred`
- no exact `hexadecimal hundred`
- no exact `binary hundred`
- no exact `decimal hundreds`
- no exact `hexadecimal hundreds`
- no exact `binary hundreds`
- no exact `binary get nine total integer`
- no exact `binary get nine tens integer by six`

## Provisional Read From The Phrase Inventory

- The lower-right representation family is stronger than it looked in the prior audit because it exact-attaches not only to `integer by six`, but also to `get nine total` and `get nine tens` through `binary`.
- The best exact local network in this pass is:
  - `hexadecimal ten ten ten integer`
  - `decimal ten ten ten integer`
  - `binary ten integer`
  - `... integer by six`
  - `baseten integer`
  - `base ten integer`
  - `binary get nine total`
  - `binary get nine tens`
- The top `find the start ...` ribbon and the upper-left `three ten hundred(s)` family remain detached.
