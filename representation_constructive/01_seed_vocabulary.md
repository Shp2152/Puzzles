# Seed Vocabulary

All coordinates below are from `can u dig it.csv:1-14` and were verified with `representation_constructive/exact_instance_search.py`.

## Starting Seed

User-provided starting seed:

- `hexadecimal`
- `decimal`
- `binary`
- `base`
- `baseten`
- `ten`
- `tens`
- `ones`
- `hundred`
- `hundreds`
- `integer`
- `by`
- `six`
- `find`
- `add`
- `get`
- `total`
- `start`
- `three`

## Justified Expansion

These additions were kept only because they participate in exact raw-grid phrases that attach directly to the representation family or to nearby imperative fragments.

- `step`
  - exact `step by six` at `N9 -> N10 -> M10 -> L11 / L12 -> M13 / L14 -> N14`
  - exact `step baseten integer` at `N9 -> N10 -> M10 -> L11 / L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12 / I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
  - exact `step into integer by six` at `I13 -> I14 -> J14 -> J13 / I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> N14`
- `into`
  - exact `into integer by six` at `I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> N14`
  - exact `step into integer by six` at `I13 -> I14 -> J14 -> J13 / I12 -> H12 -> H11 -> I10 / J11 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12 / L12 -> M13 / L14 -> N14`
- `the`
  - exact `find the start` at `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1`
  - exact `find the start nine` at the same first three word instances plus `M2 -> M3 -> L4 -> K4`
- `nine`
  - exact `find the start nine` at `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4`
  - exact `get nine total` at `F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10`
  - exact `binary get nine total` at `F10 -> E10 -> E11 -> E12 -> E13 -> F13 / F12 -> G13 -> F14 / E14 -> D13 -> C14 -> D14 / C13 -> D12 -> C12 -> B11 -> B10`
  - exact `binary get nine tens` at the same first three word instances plus `C13 -> B13 -> A12 -> A11` or `C13 -> B13 -> A12 -> B12`
- `go`
  - exact `find the start nine go` at `E1 -> F1 -> G1 -> H1 / I1 -> J1 -> J2 / K1 -> K2 -> L1 -> M1 -> N1 / M2 -> M3 -> L4 -> K4 / J3 -> K3`

## Seed Words With Strong Lower-Right Representation Roles

- `hexadecimal`
  - strong lower-right instance: `I3 -> I4 -> I5 -> I6 -> H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- `decimal`
  - strong lower-right instance: `H7 -> G8 -> F9 -> E10 -> D10 -> C10 -> D11`
- `binary`
  - two lower-right instances:
  - `F10 -> E10 -> E11 -> E12 -> E13 -> F13`
  - `F10 -> F11 -> E11 -> E12 -> E13 -> F13`
- `base`
  - lower-right instance: `L12 -> L13 -> K14 -> J14`
- `baseten`
  - lower-right instance: `L12 -> L13 -> K14 -> J14 -> I14 -> H13 -> H12`
- `integer`
  - strongest lower-right instance: `I12 -> I11 -> J10 -> K10 -> L10 -> M11 -> M12`
- `by`
  - lower-right instance: `L12 -> M13`
- `six`
  - lower-right instance: `L14 -> M14 -> N14`

## Seed Words With Place-Value Roles

- `ones`
  - singleton instance: `K3 -> L4 -> M5 -> M6`
- `tens`
  - lower-left branchable instances from `C13 -> B13 -> A12 -> A11` and `C13 -> B13 -> A12 -> B12`
  - lower-right branchable instances from `F14 -> G13 -> H12 -> I13` and `I14 -> H13 -> H12 -> I13`
- `hundred`
  - upper-left instances:
  - `B6 -> C6 -> C5 -> D4 -> D3 -> D2 -> C1`
  - `B6 -> C6 -> D5 -> D4 -> D3 -> D2 -> C1`
- `hundreds`
  - upper-left instances extending the same paths to `B1`

## Boundary Decisions

- Kept: `step`, `into`, `the`, `nine`, `go`.
- Not promoted from this pass: `open`, `point`, `or`, `to`, `in`.
  - Reason: they were not needed to state the strongest exact phrases that survived the raw-grid search here.

## Search Vocabulary Used For The Constructive Pass

- Original seed plus the justified expansion above:
- `hexadecimal decimal binary base baseten ten tens ones hundred hundreds integer by six find add get total start three step into the nine go`
