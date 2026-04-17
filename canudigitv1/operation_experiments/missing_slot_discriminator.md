# Missing Slot Discriminator

This report compares candidate fillers for the single unresolved slot in the current winning skeleton:

- `find start nine`
- `nine step six`
- `get nine total`
- `step baseten integer`

Question being ranked:

- What exact object or value is being stepped / totaled?

## Scoring Model

For each filler family:

- `best_clause_score` uses the strongest local clause in that family
- `role_points` measures how well the family connects to the fixed skeleton roles
- `attachment_points` rewards successful direct attachment experiments
- `attachment_failure_penalty` penalizes families with direct attachment experiments that all failed
- `assumption_penalty` penalizes extra interpretation choices needed to use the family as the missing filler

## Ranked Fillers

| Rank | Filler family | Total | Best clause | Role points | Attachment points | Attachment failure penalty | Assumption penalty |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Integer Object | 24 | 21 | 7 | 0 | 0 | 4 |
| 2 | Three-Ten-Hundred Payload | -1 | 16 | 1 | 0 | 6 | 12 |
| 3 | Representation-Coded Object | -7 | 6 | 5 | 0 | 6 | 12 |

## Details

### 1. Integer Object

- total score: 24
- strongest local clause: `step integer six` (support_score=21, region=lower-right)
- score breakdown: best_clause=21, role_links=7, attachments=0, attachment_failure=-0, assumptions=-4
- role compatibility:
  start: `step integer six` -> `find start nine` | +0 | none
  action: `step integer six` -> `nine step six` | +3 | lexical shared=six, step overlap=8 distance=0
  total: `step baseten integer` -> `get nine total` | +1 | spatial shared=- overlap=0 distance=1
  output: `step integer six` -> `step baseten integer` | +3 | lexical shared=integer, step overlap=9 distance=0
- added assumptions:
  Still must explain exactly what total is computed over the stepped integers.

### 2. Three-Ten-Hundred Payload

- total score: -1
- strongest local clause: `three ten hundred` (support_score=16, region=upper-left)
- score breakdown: best_clause=16, role_links=1, attachments=0, attachment_failure=-6, assumptions=-12
- role compatibility:
  start: `three ten hundred` -> `find start nine` | +1 | spatial shared=- overlap=0 distance=1
  action: `three ten hundred` -> `nine step six` | +0 | none
  total: `three ten hundred` -> `get nine total` | +0 | none
  output: `three ten hundred` -> `step baseten integer` | +0 | none
- direct attachment experiments:
  attach_payload_start: failed
  attach_payload_action: failed
  attach_payload_total: failed
  attach_payload_output: failed
  attach_payload_action_output: failed
- added assumptions:
  Must decide how `three ten hundred` should be interpreted numerically.
  Must explain why no direct attachment experiment to the winning skeleton succeeds.
  Must explain why the upper-left payload should plug into the otherwise lower-right procedure.

### 3. Representation-Coded Object

- total score: -7
- strongest local clause: `decimal ten ten ten integer` (support_score=6, region=central/mixed)
- score breakdown: best_clause=6, role_links=5, attachments=0, attachment_failure=-6, assumptions=-12
- role compatibility:
  start: `decimal ten ten ten integer` -> `find start nine` | +0 | none
  action: `decimal ten ten ten integer` -> `nine step six` | +1 | spatial shared=- overlap=3 distance=0
  total: `decimal ten ten ten integer` -> `get nine total` | +1 | spatial shared=- overlap=8 distance=0
  output: `decimal ten ten ten integer` -> `step baseten integer` | +3 | lexical shared=integer overlap=7 distance=0
- direct attachment experiments:
  attach_output_hexadecimal: failed
  attach_output_decimal: failed
  attach_action_output_hexadecimal: failed
  attach_action_output_decimal: failed
  attach_action_hexadecimal: failed
  attach_action_decimal: failed
  attach_start_hexadecimal: failed
  attach_start_decimal: failed
  attach_total_hexadecimal: failed
  attach_total_decimal: failed
- added assumptions:
  Must decide which representation clause is the active one (`hexadecimal` vs `decimal`).
  Must explain why no direct attachment experiment to the winning skeleton succeeds.
  Must explain whether the representation family is an input object, a second-stage interpretation, or merely confirmation.

## Current Read

Interpret this ranking cautiously:

- A higher score means a family fills the missing slot with fewer new assumptions and better integration into the current skeleton.
- A low score does not mean the family is fake. It can still be intentional while operating as a separate or later clue layer.
