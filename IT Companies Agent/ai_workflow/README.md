# AI Workflow Index

## Purpose

This folder is the operational control center for daily AI execution. Any AI agent starting work must begin here to avoid repeating context gathering or getting stuck.

## Read Order

1. `HANDOFF_STATE.md`
2. `BACKLOG.md`
3. Latest file inside `daily/`
4. Relevant backend docs in `docs/`

## Folder Contents

- `MASTER_FLOW.md`
- `DAILY_SCHEDULE.md`
- `BACKLOG.md`
- `HANDOFF_STATE.md`
- `SESSION_TEMPLATE.md`
- `daily/`

## Rules

- Never start from scratch if a handoff exists
- Always continue from the saved next starting point
- Always update the daily log after the session
- Always move unfinished work back into backlog
