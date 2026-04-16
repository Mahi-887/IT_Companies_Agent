# AI Memory System

## Purpose

This document defines how DevPulse AI stores working context so any future agent can resume without getting stuck.

## Memory Objectives

- Preserve repository-specific knowledge
- Preserve agent handoff state
- Preserve daily execution state
- Avoid repeated reasoning on the same questions

## Memory Layers

### 1. Session Memory

Short-lived memory for the current task.

- Active request
- Current repo scope
- Retrieved context ids
- Temporary reasoning notes

### 2. Task Memory

Persistent memory for reusable work.

- Completed agent tasks
- Query outputs
- Retrieved references
- Confidence score
- Failure notes

### 3. Knowledge Memory

Long-lived indexed knowledge.

- Code chunks
- Documentation chunks
- Ticket summaries
- Slack conversation summaries
- Debug patterns

### 4. Execution Memory

State for day-by-day project continuation.

- Last completed step
- Next starting point
- Open backend task
- Date and time log

## Storage Plan

### PostgreSQL

Store:

- task status
- agent outputs
- memory metadata
- execution checkpoints
- audit trail

### ChromaDB

Store:

- embeddings for code
- embeddings for docs
- embeddings for ticket and Slack summaries

## Required Memory Fields

```json
{
  "repo_id": "uuid",
  "memory_type": "task|knowledge|execution",
  "source_type": "code|doc|ticket|slack|debug|tracker",
  "source_id": "string",
  "summary": "string",
  "references": [],
  "confidence": 0.0,
  "created_at": "timestamp"
}
```

## Agent Handoff Rules

- Every agent must write a final summary before closing
- Every agent must define the next starting point
- Every agent must include repository scope in its memory record
- No agent should rely on hidden scratchpad state

## Resume Rules

When a new agent starts:

1. Read the latest execution memory
2. Read the latest incomplete task
3. Load the last successful references
4. Continue from the saved next step

## Stuck Prevention Rules

- Save partial progress before long-running work
- Record failure reason if a task cannot complete
- Keep handoff notes short and explicit
- Prefer structured fields over long free text

## Minimum Handoff Template

```md
## Agent Handoff

- Repo:
- Completed:
- In progress:
- Blockers:
- Next starting point:
- References:
```

## Daily Integration

`AI_WORKFLOW_TRACKER.md` is the human-readable execution memory. Database records are the machine-readable execution memory. Both must stay aligned.
