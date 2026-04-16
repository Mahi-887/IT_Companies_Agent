# AI Flow

## Purpose

This document defines how DevPulse AI handles a request from ingestion to answer delivery.

## End-to-End Flow

### 1. Ingest

- Pull repository content from GitHub
- Collect docs, tickets, Slack context, and logs
- Store normalized metadata in PostgreSQL
- Store searchable chunks in ChromaDB

### 2. Index

- Split content into stable chunks
- Generate embeddings for each chunk
- Attach `repo_id`, `document_id`, source type, and line references

### 3. Retrieve

- Accept a user query
- Classify the request as code, docs, debugging, or ticket mapping
- Pull top matching chunks from vector search
- Filter by repository access and freshness

### 4. Reason

- Build a compact prompt with retrieved context
- Use an LLM to synthesize an answer
- If needed, route to a specialized agent

### 5. Respond

- Return JSON with explanation
- Include file paths, lines, and references
- Include confidence score and fallback notes

### 6. Persist

- Save the query result
- Save task metadata
- Save confidence and retrieval trace for later reuse

## AI Request Types

- Code navigation
- Debug analysis
- Documentation generation
- Ticket mapping
- Ownership lookup

## AI Decision Rules

- Use RAG first
- Use agents only when the task needs specialized reasoning
- Never answer without repository scope
- Prefer citations over guessing

## Failure Flow

If the model is uncertain:

1. Return partial results
2. Show the most relevant files
3. Ask for missing context if needed
4. Record the failure mode in `agent_tasks`

## Output Contract

```json
{
  "success": true,
  "answer": "string",
  "references": [
    {
      "file_path": "string",
      "line_start": 1,
      "line_end": 20
    }
  ],
  "confidence": 0.82,
  "fallback_used": false
}
```
