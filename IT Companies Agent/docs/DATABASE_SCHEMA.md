# Database Schema

## Design Goals

- Normalize relational data
- Store embeddings separately
- Support repo-based access control
- Keep audit history

## Core Tables

### users

- `id`
- `supabase_user_id`
- `email`
- `name`
- `role`
- `created_at`

### repositories

- `id`
- `owner_user_id`
- `name`
- `github_url`
- `default_branch`
- `created_at`

### documents

- `id`
- `repo_id`
- `source_type`
- `title`
- `file_path`
- `content_hash`
- `updated_at`

### embeddings

- `id`
- `repo_id`
- `document_id`
- `chunk_index`
- `vector_id`
- `text_chunk`
- `embedding_model`

### tickets

- `id`
- `repo_id`
- `jira_key`
- `summary`
- `status`
- `mapped_modules`

### logs

- `id`
- `repo_id`
- `source`
- `severity`
- `message`
- `metadata`

### agent_tasks

- `id`
- `repo_id`
- `agent_name`
- `task_type`
- `status`
- `input_payload`
- `output_payload`

### audit_logs

- `id`
- `repo_id`
- `actor_user_id`
- `action`
- `entity_type`
- `entity_id`
- `created_at`

## Indexing Strategy

- Index `repo_id` on all scoped tables
- Index `document_id` on embeddings
- Index `jira_key` on tickets
- Index `created_at` on logs and audits
- Add full text search only where needed

## Vector Mapping

Every embedding row must map back to one document and one repository.

## Access Control

All reads and writes are validated by repository membership and JWT identity.
