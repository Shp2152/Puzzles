# Attachment Experiments

These runs test whether unresolved clue families can attach directly to specific roles in the current winning skeleton.

Winning skeleton under current minimal-assumption scoring:

- `find start nine`
- `nine step six`
- `get nine total`
- `step baseten integer`

## Representation Attachments

### attach_output_hexadecimal

- role: output
- words: `baseten, integer, hexadecimal`
- note: Can hexadecimal attach directly to the base-10 output clause?
- output: `attach_output_hexadecimal.txt`
- has_results: no
- core: none

### attach_output_decimal

- role: output
- words: `baseten, integer, decimal`
- note: Can decimal attach directly to the base-10 output clause?
- output: `attach_output_decimal.txt`
- has_results: no
- core: none

### attach_action_output_hexadecimal

- role: action_output
- words: `step, baseten, integer, hexadecimal`
- note: Can hexadecimal attach to the strongest lower-right output/action clause?
- output: `attach_action_output_hexadecimal.txt`
- has_results: no
- core: none

### attach_action_output_decimal

- role: action_output
- words: `step, baseten, integer, decimal`
- note: Can decimal attach to the strongest lower-right output/action clause?
- output: `attach_action_output_decimal.txt`
- has_results: no
- core: none

### attach_action_hexadecimal

- role: action
- words: `step, integer, six, hexadecimal`
- note: Can hexadecimal attach to the step-by-six clause?
- output: `attach_action_hexadecimal.txt`
- has_results: no
- core: none

### attach_action_decimal

- role: action
- words: `step, integer, six, decimal`
- note: Can decimal attach to the step-by-six clause?
- output: `attach_action_decimal.txt`
- has_results: no
- core: none

### attach_start_hexadecimal

- role: start
- words: `start, nine, hexadecimal`
- note: Can hexadecimal attach to the upper-right start clause?
- output: `attach_start_hexadecimal.txt`
- has_results: no
- core: none

### attach_start_decimal

- role: start
- words: `start, nine, decimal`
- note: Can decimal attach to the upper-right start clause?
- output: `attach_start_decimal.txt`
- has_results: no
- core: none

### attach_total_hexadecimal

- role: total
- words: `get, nine, total, hexadecimal`
- note: Can hexadecimal attach to the total clause?
- output: `attach_total_hexadecimal.txt`
- has_results: no
- core: none

### attach_total_decimal

- role: total
- words: `get, nine, total, decimal`
- note: Can decimal attach to the total clause?
- output: `attach_total_decimal.txt`
- has_results: no
- core: none

## Payload Attachments

### attach_payload_start

- role: start
- words: `start, nine, three, ten, hundred`
- note: Can the payload attach directly to the start clause?
- output: `attach_payload_start.txt`
- has_results: no
- core: none

### attach_payload_action

- role: action
- words: `nine, step, six, three, ten, hundred`
- note: Can the payload attach to the step clause?
- output: `attach_payload_action.txt`
- has_results: no
- core: none

### attach_payload_total

- role: total
- words: `get, nine, total, three, ten, hundred`
- note: Can the payload attach to the total clause?
- output: `attach_payload_total.txt`
- has_results: no
- core: none

### attach_payload_output

- role: output
- words: `baseten, integer, three, ten, hundred`
- note: Can the payload attach directly to the output clause?
- output: `attach_payload_output.txt`
- has_results: no
- core: none

### attach_payload_action_output

- role: action_output
- words: `step, baseten, integer, three, ten, hundred`
- note: Can the payload attach to the strongest lower-right action/output clause?
- output: `attach_payload_action_output.txt`
- has_results: no
- core: none

## Current Read

- successful representation attachments: none
- successful payload attachments: none
- If a family has no successful attachments, it is currently better treated as a separate or confirmatory layer rather than an integrated step of the winning skeleton.
