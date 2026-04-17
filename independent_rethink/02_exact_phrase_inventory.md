# Exact Phrase Inventory

All entries below are from `can u dig it.csv:1-14` and were verified with `independent_rethink/raw_grid_probe.py:61-116`.

## P1. `find the start`

- Exact phrase text: `find the start`
- Source file: `can u dig it.csv`
- Word paths:
  - `find`: cells `4,5,6,7`; coords `E1 -> F1 -> G1 -> H1`
  - `the`: cells `8,9,23`; coords `I1 -> J1 -> J2`
  - `start`: cells `10,24,11,12,13`; coords `K1 -> K2 -> L1 -> M1 -> N1`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: yes, includes `the`
- Local confidence: high

## P2. `find the start nine`

- Exact phrase text: `find the start nine`
- Source file: `can u dig it.csv`
- Word paths:
  - `find`: `E1 -> F1 -> G1 -> H1`
  - `the`: `I1 -> J1 -> J2`
  - `start`: `K1 -> K2 -> L1 -> M1 -> N1`
  - `nine`: cells `26,40,53,52`; coords `M2 -> M3 -> L4 -> K4`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: yes, includes `the`
- Local confidence: medium
- Alternate exact variant: `nine` can also end `M5` via `M2 -> M3 -> L4 -> M5`

## P3. `find the start nine go`

- Exact phrase text: `find the start nine go`
- Source file: `can u dig it.csv`
- Word paths:
  - `find`: `E1 -> F1 -> G1 -> H1`
  - `the`: `I1 -> J1 -> J2`
  - `start`: `K1 -> K2 -> L1 -> M1 -> N1`
  - `nine`: `M2 -> M3 -> L4 -> K4`
  - `go`: cells `37,38`; coords `J3 -> K3`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: yes, includes `the`
- Local confidence: medium-low
- Reason for downgrade: exact but syntactically rough; `go` still lacks an object or destination.

## P4. `step by six`

- Exact phrase text: `step by six`
- Source file: `can u dig it.csv`
- Word paths:
  - `step`: cells `125,139,138,151`; coords `N9 -> N10 -> M10 -> L11`
  - `by`: cells `165,180`; coords `L12 -> M13`
  - `six`: cells `193,194,195`; coords `L14 -> M14 -> N14`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: yes, includes `by`
- Local confidence: high
- Alternate exact variants: two other `step` paths exist ending at the same `L11`.

## P5. `step baseten integer`

- Exact phrase text: `step baseten integer`
- Source file: `can u dig it.csv`
- Word paths:
  - `step`: `N9 -> N10 -> M10 -> L11`
  - `baseten`: cells `165,179,192,191,190,175,161`; coords `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: cells `162,148,135,136,137,152,166`; coords `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: high

## P6. `baseten integer`

- Exact phrase text: `baseten integer`
- Source file: `can u dig it.csv`
- Word paths:
  - `baseten`: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
  - `integer`: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: high

## P7. `step into integer by six`

- Exact phrase text: `step into integer by six`
- Source file: `can u dig it.csv`
- Word paths:
  - `step`: cells `176,190,191,177`; coords `I13 -> I14 -> J14 -> J13`
  - `into`: cells `162,161,147,134`; coords `I12 -> H12 -> H11 -> I10`
  - `integer`: cells `149,148,135,136,137,152,166`; coords `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: cells `165,180`; coords `L12 -> M13`
  - `six`: cells `193,194,195`; coords `L14 -> M14 -> N14`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: yes, includes `into` and `by`
- Local confidence: high

## P8. `into integer by six`

- Exact phrase text: `into integer by six`
- Source file: `can u dig it.csv`
- Word paths:
  - `into`: `I12 -> H12 -> H11 -> I10`
  - `integer`: `J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - `by`: `L12 -> M13`
  - `six`: `L14 -> M14 -> N14`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: yes, includes `into` and `by`
- Local confidence: medium-high

## P9. `get nine total`

- Exact phrase text: `get nine total`
- Source file: `can u dig it.csv`
- Word paths:
  - `get`: cells `159,174,187`; coords `F12 -> G13 -> F14`
  - `nine`: cells `186,171,184,185`; coords `E14 -> D13 -> C14 -> D14`
  - `total`: cells `170,157,156,141,127`; coords `C13 -> D12 -> C12 -> B11 -> B10`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: high
- Alternate exact variant: `nine` also has `E14 -> D13 -> C14 -> B13`.

## P10. `hexadecimal ten ten ten integer`

- Exact phrase text: `hexadecimal ten ten ten integer`
- Source file: `can u dig it.csv`
- Word paths:
  - `hexadecimal`: cells `36,50,64,78,91,104,117,130,129,128,143`; coords `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `ten`: cells `156,169,184`; coords `C12 -> B13 -> C14`
  - `ten`: cells `170,185,186`; coords `C13 -> D14 -> E14`
  - `ten`: cells `187,174,161`; coords `F14 -> G13 -> H12`
  - `integer`: cells `162,148,135,136,137,152,166`; coords `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: very high

## P11. `decimal ten ten ten integer`

- Exact phrase text: `decimal ten ten ten integer`
- Source file: `can u dig it.csv`
- Word paths:
  - `decimal`: cells `91,104,117,130,129,128,143`; coords `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - the same three `ten` instances as P10
  - the same `integer` instance as P10
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: very high

## P12. `binary ten`

- Exact phrase text: `binary ten`
- Source file: `can u dig it.csv`
- Word paths:
  - `binary`: cells `131,130,144,158,172,173`; coords `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `ten`: cells `187,174,161`; coords `F14 -> G13 -> H12`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: medium-high
- Alternate exact variant: `binary` also has `F10 -> F11 -> E11 -> E12 -> E13 -> F13`.

## P13. `decimal tens`

- Exact phrase text: `decimal tens`
- Source file: `can u dig it.csv`
- Word paths:
  - `decimal`: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `tens`: cells `156,169,154,140`; coords `C12 -> B13 -> A12 -> A11`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: medium

## P14. `hexadecimal tens`

- Exact phrase text: `hexadecimal tens`
- Source file: `can u dig it.csv`
- Word paths:
  - `hexadecimal`: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
  - `tens`: `C12 -> B13 -> A12 -> A11`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: medium

## P15. `binary tens`

- Exact phrase text: `binary tens`
- Source file: `can u dig it.csv`
- Word paths:
  - `binary`: `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `tens`: cells `187,174,161,176`; coords `F14 -> G13 -> H12 -> I13`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: medium

## P16. `three ten hundred`

- Exact phrase text: `three ten hundred`
- Source file: `can u dig it.csv`
- Word paths:
  - `three`: cells `30,15,16,29,42`; coords `C3 -> B2 -> C2 -> B3 -> A4`
  - `ten`: cells `57,44,58`; coords `B5 -> C4 -> C5`
  - `hundred`: cells `71,72,59,45,31,17,2`; coords `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- Contiguous under movement rule: yes
- Self-avoiding across phrase: yes
- Bridge words included exactly: not applicable
- Local confidence: medium-high

## P17. `find the start nine go` is exact; `nine step six` is not

- Exact phrase text recorded here for audit significance: `find the start nine go`
- Verified exact path: see P3.
- Counterpoint check: exact `nine step six` has zero matches on the same movement rule.
- Audit significance: this matters because exact glue-bearing phrasing is stronger evidence than a stripped content core.
