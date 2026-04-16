# AI Models and Languages

## Language Stack

### Backend

- Python
- FastAPI
- PostgreSQL SQL
- JSON for API responses

### AI Orchestration

- Python for agent control
- Prompt templates in plain text or structured config

## Model Strategy

### LLM Options

- Gemini 1.5 Pro
- Claude

### Selection Criteria

- Long context support
- Response quality on code tasks
- Cost and availability
- Stability for production use

## Embedding Options

- Instructor-XL
- OpenAI embeddings

### Selection Criteria

- Semantic quality
- Cost
- Speed
- Local development compatibility

## Why Multiple Options

The backend should not depend on one provider only. A provider swap should not change API contracts or data models.

## Prompt Language Policy

- Use English for system prompts
- Keep task prompts simple
- Keep responses concise and reference-heavy

## Code Language Policy

- Keep all backend code in Python
- Keep database schema in SQL migrations
- Keep docs in Markdown

## AI Output Policy

- Always return structured JSON when used by APIs
- Never return raw secrets
- Never generate unsupported stack changes
