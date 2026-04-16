# System Architecture Detailed

## High-Level View

DevPulse AI uses a modular backend with three main layers:

- API layer
- Retrieval and ingestion layer
- Agent orchestration layer

## Service-to-Service Interaction

### API Layer

Receives requests from clients and validates auth and repo scope.

### Ingestion Services

Pull data from GitHub, Jira, Slack, and internal docs.

### Embedding Service

Chunks content and stores vectors in ChromaDB with relational metadata in PostgreSQL.

### Query Service

Runs retrieval, assembles context, and calls the LLM.

### Agent Orchestrator

Selects Librarian, Architect, Debugger, or Manager when specialized reasoning is needed.

## Core Data Flow

GitHub -> ingestion -> chunking -> embeddings -> ChromaDB -> query retrieval -> LLM response -> JSON API output.

## Agent Orchestration Flow

1. Classify request type.
2. Retrieve relevant context.
3. Decide whether an agent is needed.
4. Run the agent with bounded context.
5. Store task output and confidence.

## Scalability Considerations

- Keep ingestion asynchronous
- Cache repeated query contexts
- Use repo-level partitions in metadata
- Keep vector search local in development
- Move heavy jobs to queued workers later
