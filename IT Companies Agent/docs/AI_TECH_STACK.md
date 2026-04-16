# AI Tech Stack

## LLM Choice

Use Gemini 1.5 Pro or Claude depending on availability, latency, and task quality.

### Reasoning

- Both handle long context well
- Both support strong instruction following
- Provider choice can be switched without changing the backend design

## Embeddings

Use Instructor-XL or OpenAI embeddings depending on cost and deployment constraints.

## Vector DB

ChromaDB is used for local-first development and fast iteration.

## Why No Full Training

- Faster to ship
- Lower infrastructure cost
- Easier to update with fresh repo data
- Safer for internal knowledge workflows

## Local vs Cloud Strategy

### Local

- FastAPI
- ChromaDB
- Docker optional
- Local development and testing

### Cloud

- Supabase Postgres
- Supabase Auth
- LLM provider
- GitHub, Jira, Slack, and Resend APIs

## Practical Rule

Prefer the simplest AI stack that gives reliable citations and stable retrieval.
