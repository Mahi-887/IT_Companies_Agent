# Scalability Plan

## Local to Production Path

### Phase 1

- Single FastAPI app
- Local ChromaDB
- Supabase Postgres
- Manual background jobs

### Phase 2

- Add async workers
- Add job retries
- Add caching for repeated queries

### Phase 3

- Move heavy ingestion into queue-based processing
- Partition data by repository
- Add stronger observability

## Vector DB Scaling

- Keep chunks small and stable
- Index by repo and source type
- Prune stale embeddings

## Async Task Handling

- Use background tasks for ingestion and webhook processing
- Keep long-running AI work off the request path

## Future Queue Scope

- Queue is a future improvement, not required for initial delivery
- Introduce only when webhook or ingestion load justifies it

## Caching Strategy

- Cache repo metadata
- Cache recent query results
- Cache top retrieval results for repeated questions
