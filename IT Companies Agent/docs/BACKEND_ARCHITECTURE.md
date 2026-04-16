# Backend Architecture

## Architecture Type

Modular monolith with agentic services.

## Main Modules

- `auth_service`
- `repo_ingestion_service`
- `embedding_service`
- `rag_query_service`
- `agent_orchestrator`
- `webhook_listener`
- `debug_analyzer`

## Request Flow

1. A client authenticates through Supabase Auth.
2. The backend validates the JWT and repo access.
3. The query service routes the request to RAG or a specialized agent.
4. The response returns explanation, references, and confidence data.

## Data Flow

### GitHub to Answer

GitHub repo -> ingestion service -> chunking -> embeddings -> ChromaDB + PostgreSQL metadata -> query retrieval -> LLM answer.

### Webhook to Documentation

Git push webhook -> diff analysis -> impacted docs detection -> summary generation -> documentation update record.

## Service Boundaries

### Ingestion Layer

Handles repo sync, document sync, Slack ingest, and Jira fetch jobs.

### Retrieval Layer

Handles embeddings, vector search, metadata filters, and context assembly.

### Agent Layer

Coordinates Librarian, Architect, Debugger, and Manager agents.

### API Layer

Exposes clean JSON endpoints for frontend and automation.

## Scalability Notes

- Keep ingestion async
- Keep query path low-latency
- Use metadata filters before vector search where possible
- Keep agent calls bounded and deterministic
