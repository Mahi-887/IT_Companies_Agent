# Security and Auth

## Authentication

Supabase Auth is the identity layer using email or OTP login.

## JWT Handling

- Validate JWT on every protected request
- Reject expired or malformed tokens
- Attach verified user identity to request context

## Authorization

Access is scoped by repository membership.

## API Security Rules

- Require auth for all internal data endpoints
- Never expose raw secrets in responses
- Validate request payloads with strict schemas
- Limit webhook endpoints to trusted sources

## Rate Limiting

- Apply basic per-user rate limits
- Apply tighter limits on query and debug endpoints
- Throttle ingestion and webhook bursts

## Data Access Control

- Every repo-scoped table must include `repo_id`
- Queries must filter by repo membership
- Audit all access to sensitive records
