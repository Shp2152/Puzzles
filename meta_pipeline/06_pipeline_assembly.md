# Pipeline Assembly

Only hypotheses that survived the controller and extraction tests are assembled here.

Grounding labels used below:

- grounded
- weak
- unsupported

## P1. Attached Controller -> Engine Branch -> Local Output

### Stages

1. controller stage:
   - exact `find the hexadecimal or get nine tens`
2. engine stage:
   - exact `get nine tens`
3. output stage:
   - local computation `9` tens -> `90`

### What each stage contributes

- stage 1 contributes an objective representation selector (`hexadecimal`) and a grounded branch phrase (`get nine tens`)
- stage 2 contributes the executable local branch semantics
- stage 3 yields `90`

### Handoff quality

- controller -> branch:
  - grounded by one exact phrase
- branch -> local output:
  - grounded locally
- local output -> final answer:
  - weak
  - no exact final-report phrase licenses stopping at `90`

### Candidate integer

- `90`

### Robustness rating

- low-moderate

## P2. Attached Controller -> Hexadecimal Engine Family -> Unresolved Execution

### Stages

1. controller stage:
   - exact `find the hexadecimal ten ten ten integer by six`
   - exact `find the hexadecimal ten ten ten to integer`
2. engine stage:
   - hexadecimal representation-object family
3. execution stage:
   - unresolved

### What each stage contributes

- stage 1 objectively selects the hexadecimal family
- stage 2 supplies the representation engine
- stage 3 fails because the exact syntax still allows competing continuations

### Candidate integer(s)

- none promoted

### Robustness rating

- low

## P3. Top Meta Controller -> Lower-Right Engine -> Detached `get ones`

### Stages

1. top meta stage:
   - `find the start nine go ahead`
2. engine stage:
   - lower-right local output candidate `90`
3. extraction stage:
   - detached `get ones`

### Handoff quality

- top meta -> engine:
  - weak to unsupported
- engine -> `get ones`:
  - unsupported

### Candidate integer

- forced result would be `0`

### Robustness rating

- unsupported

## P4. Attached Hex Controller -> Engine -> Upper-Left Place-Value Layer

### Stages

1. controller stage:
   - exact `find the hexadecimal ...`
2. engine stage:
   - hexadecimal family or `get nine tens` branch
3. extraction stage:
   - detached `three ten hundred(s)` family

### Handoff quality

- controller -> engine:
  - grounded
- engine -> upper-left extraction:
  - unsupported

### Candidate integer(s)

- none promoted

### Robustness rating

- unsupported

## P5. Self-Contained Lower-Right Engine With Detached Phrases Only As Meta Comments

### Stages

1. detached top phrases act only as meta comments
2. lower-right branch `get nine tens` executes locally to `90`

### Handoff quality

- no explicit handoff needed
- but no exact final-report role is gained either

### Candidate integer

- `90`

### Robustness rating

- low

## Pipeline Takeaway

- P1 is the strongest full pipeline assembled in this pass.
- It is better than the earlier `90` story because the controller side is now grounded by an exact `find the hexadecimal or get nine tens` phrase.
- It is still not enough to justify `90` as the final answer, because final-report status remains weak and competing exact hexadecimal continuations still exist.
