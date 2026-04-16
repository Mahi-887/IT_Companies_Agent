# API Contracts

## Response Standard

All endpoints return JSON with:

- `success`
- `message`
- `data`
- `references`
- `confidence`
- `errors`

## Endpoints

### POST /query

Natural language query over code, docs, tickets, and logs.

Request:

```json
{
  "repo_id": "uuid",
  "query": "Where is authentication handled?",
  "context_type": "codebase"
}
```

Response:

```json
{
  "success": true,
  "message": "Relevant auth flow found",
  "data": {
    "answer": "Authentication is handled in auth_service and Supabase middleware.",
    "snippets": []
  },
  "references": [
    {
      "file_path": "app/services/auth_service.py",
      "line_start": 12,
      "line_end": 48
    }
  ],
  "confidence": 0.86,
  "errors": []
}
```

### POST /ingest/repo

Starts repository ingestion and indexing.

### POST /webhook/github

Receives push events and triggers doc refresh workflows.

### POST /debug/analyze

Analyzes logs, env values, and known issue history.

### GET /tickets/suggestions

Returns suggested module tags, owners, and related files for Jira tickets.

## Contract Rules

- Keep payloads small
- Always return references when available
- Never expose raw secrets
- Always scope by `repo_id`
- Keep errors machine-readable
