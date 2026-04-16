# Agent Workflows

## Agent Set

### Librarian Agent

- Ingests docs, Slack, and knowledge sources
- Builds search-ready memory

### Architect Agent

- Parses code structure
- Maps dependencies
- Explains system logic

### Debugger Agent

- Analyzes errors, logs, and config
- Suggests likely fixes with context

### Manager Agent

- Reads Jira tickets
- Maps work to modules and ownership

## Orchestration Rules

- Use the smallest agent that can answer the request
- Fall back to RAG before invoking multi-step reasoning
- Save agent outputs in `agent_tasks`
- Preserve repo scope in every step

## Workflow Example

1. User asks a question.
2. Query service retrieves context.
3. Orchestrator selects one agent or a chain.
4. Agent returns answer and references.
5. Result is written to history for reuse.

## Memory Rules

- Prefer short task memory
- Reuse prior repo context
- Persist completed task outputs
- Keep long-term memory in relational records plus vector chunks

## Handoff Rules

- Every agent must save a completion summary
- Every agent must write the next starting point
- Every agent must store blockers if the task is incomplete
- Every agent must save references used for the decision

## Confidence Handling

- High confidence: direct answer
- Medium confidence: answer plus caveat
- Low confidence: return partial findings and ask for more context
