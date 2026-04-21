# Failure Modes

This file records the strongest pipelines that still fail and why.

## F1. `find the start ...` controls the lower-right engine

- attempted pipeline:
  - `find the start nine go ahead` -> lower-right engine
- failure category:
  - controller phrase not objective enough
- exact reason:
  - no objective referent maps the detached `start/go/ahead` chain to one specific lower-right branch or component entry

## F2. `find the start nine` selects the `get nine ...` branch

- attempted pipeline:
  - `find the start nine` -> `get nine tens` or `get nine total`
- failure category:
  - no unique referent
- exact reason:
  - top `nine` and lower-right `nine` are disconnected instances

## F3. `find the hexadecimal ...` uniquely selects `90`

- attempted pipeline:
  - `find the hexadecimal ...` -> `get nine tens` -> `90`
- failure category:
  - multiple equally valid pipeline readings
- exact reason:
  - the same controller family also supports:
  - `find the hexadecimal ten ten ten integer by six`
  - `find the hexadecimal ten ten ten to integer`
  - `find the hexadecimal or ten integer by six`
  - `find the hexadecimal or tens integer by six`

## F4. `get ones` acts on selected engine output

- attempted pipeline:
  - selected engine output -> `get ones`
- failure category:
  - extraction handoff unsupported
- exact reason:
  - no exact phrase licenses applying the detached `get ones` family to a lower-right result

## F5. Upper-left `three ten hundred(s)` acts on selected engine output

- attempted pipeline:
  - selected engine output -> `three ten hundred(s)`
- failure category:
  - extraction handoff unsupported
- exact reason:
  - no exact phrase licenses that handoff

## F6. `90` is the final answer because it is the best selected branch

- attempted pipeline:
  - controller-selected `get nine tens` -> `90` -> final answer
- failure category:
  - final-report role not licensed
- exact reason:
  - no exact phrase says the branch result itself is the final report target

## F7. `2` is the final answer from `binary ten`

- attempted pipeline:
  - `binary ten` -> `2`
- failure category:
  - controller phrase not objective enough
- exact reason:
  - the new strongest controller evidence favors hexadecimal, not binary

## Failure-Mode Takeaway

- The strongest surviving failures are no longer about missing top-to-engine structure.
- They are about:
  - competing exact continuations inside the controller-selected hexadecimal family
  - unsupported detached extraction handoffs
  - lack of a licensed final-report stage
