-- Initial DevPulse AI schema scaffold.
-- The tables mirror the documented architecture and keep repo-scoped data
-- separated from vector storage.

create table if not exists users (
    id uuid primary key,
    supabase_user_id text not null unique,
    email text not null unique,
    name text,
    role text not null default 'member',
    created_at timestamptz not null default now()
);

create table if not exists repositories (
    id uuid primary key,
    owner_user_id uuid not null references users(id),
    name text not null,
    github_url text not null,
    default_branch text not null default 'main',
    created_at timestamptz not null default now()
);

create table if not exists documents (
    id uuid primary key,
    repo_id uuid not null references repositories(id),
    source_type text not null,
    title text not null,
    file_path text not null,
    content_hash text not null,
    updated_at timestamptz not null default now()
);

create table if not exists embeddings (
    id uuid primary key,
    repo_id uuid not null references repositories(id),
    document_id uuid not null references documents(id),
    chunk_index integer not null,
    vector_id text not null,
    text_chunk text not null,
    embedding_model text not null
);

create table if not exists tickets (
    id uuid primary key,
    repo_id uuid not null references repositories(id),
    jira_key text not null unique,
    summary text not null,
    status text not null,
    mapped_modules text[] not null default '{}'
);

create table if not exists logs (
    id uuid primary key,
    repo_id uuid not null references repositories(id),
    source text not null,
    severity text not null,
    message text not null,
    metadata jsonb not null default '{}'::jsonb
);

create table if not exists agent_tasks (
    id uuid primary key,
    repo_id uuid not null references repositories(id),
    agent_name text not null,
    task_type text not null,
    status text not null,
    input_payload jsonb not null default '{}'::jsonb,
    output_payload jsonb
);

create table if not exists audit_logs (
    id uuid primary key,
    repo_id uuid not null references repositories(id),
    actor_user_id uuid references users(id),
    action text not null,
    entity_type text not null,
    entity_id text not null,
    created_at timestamptz not null default now()
);

create index if not exists idx_documents_repo_id on documents(repo_id);
create index if not exists idx_embeddings_repo_id on embeddings(repo_id);
create index if not exists idx_embeddings_document_id on embeddings(document_id);
create index if not exists idx_tickets_repo_id on tickets(repo_id);
create index if not exists idx_logs_repo_id on logs(repo_id);
create index if not exists idx_audit_logs_repo_id on audit_logs(repo_id);

