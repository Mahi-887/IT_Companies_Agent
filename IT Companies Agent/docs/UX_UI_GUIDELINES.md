# UX UI Guidelines

## Frontend Scope

Frontend work is handled separately. The backend must only expose stable contracts for a minimal chat-based dashboard.

## UI Expectations

- Chat-first interface
- Repo selector
- Query panel
- Source references panel
- Debug result panel

## Backend Dependency Mapping

Frontend may call:

- `POST /query`
- `POST /ingest/repo`
- `POST /webhook/github`
- `POST /debug/analyze`
- `GET /tickets/suggestions`

## Required Data Formats

- JSON responses
- File path references
- Confidence values
- Error messages that are machine readable

## Separation Rule

Frontend can read backend outputs only. It cannot modify backend logic, schema, or agent flow.
