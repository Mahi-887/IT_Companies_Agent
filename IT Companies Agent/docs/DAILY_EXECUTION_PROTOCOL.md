# Daily Execution Protocol

## Goal

Every working day should produce measurable backend progress within the 1.5 hour window.

## Session Order

1. Read the last completed tracker entry
2. Continue from the exact next step
3. Finish one concrete backend task
4. Update the tracker
5. Set the next starting point

## Daily Rule Set

- One session, one primary backend objective
- No undefined tasks
- No silent scope expansion
- No frontend editing from Codex
- Backend progress must be visible in docs or implementation

## Weekly Cycle

- Day 1 and Day 2: design
- Day 3 to Day 5: implementation
- Day 6: integration
- Day 7: testing and documentation update

## Tracker Format

```md
## Day N

- Date:
- Start time:
- End time:
- Completed tasks:
- Pending tasks:
- Next starting point:
```

## Resume Rule

The AI must resume from the last completed step, not from the top of the plan.

## Ownership Rule

- Codex owns backend, database, AI, and docs
- Antigravity reads backend contracts and owns frontend changes
- Neither side edits the other side's code
