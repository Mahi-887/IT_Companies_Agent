# DevPulse AI

DevPulse AI is a backend-only, agentic engineering assistant for codebase navigation, auto-documentation, and contextual debugging.

## Vision

DevPulse AI solves the most common engineering problem across IT companies: developer onboarding delay and internal knowledge debt. The system acts as an intelligent engineering shadow that understands code, docs, tickets, Slack context, and debugging signals, then returns repository-scoped answers with references.

## Core Outcomes

- Reduce onboarding time from weeks to less than 3 days
- Reduce senior developer dependency by 60 percent
- Increase code navigation speed by 70 percent
- Automate documentation updates from repository changes

## Product Scope

- FastAPI backend
- PostgreSQL via Supabase
- ChromaDB for local-first vector storage
- RAG-based AI workflows
- GitHub, Jira, Slack, and Resend integrations
- Supabase Auth for email OTP login

## Operating Model

- Codex owns backend, database, AI workflows, and documentation
- Antigravity owns frontend implementation
- Codex can read frontend context but must not edit frontend code
- Antigravity can read backend APIs but must not edit backend code
- All coordination happens through backend contracts and workflow docs

## Core Capabilities

- Codebase query with file references and confidence scoring
- Auto documentation generation from GitHub change events
- Context-aware debugging using logs, config, and prior fixes
- Jira ticket mapping to modules, ownership, and historical context
- AI memory and handoff support for uninterrupted daily execution

## Recommended Read Order

1. `docs/PRD.md`
2. `docs/BACKEND_ARCHITECTURE.md`
3. `docs/DATABASE_SCHEMA.md`
4. `docs/API_CONTRACTS.md`
5. `docs/AI_FLOW.md`
6. `docs/AI_MEMORY_SYSTEM.md`
7. `ai_workflow/README.md`

## Documentation

- [PRD](docs/PRD.md)
- [Backend Architecture](docs/BACKEND_ARCHITECTURE.md)
- [API Contracts](docs/API_CONTRACTS.md)
- [Database Schema](docs/DATABASE_SCHEMA.md)
- [Agent Workflows](docs/AGENT_WORKFLOWS.md)
- [Implementation Plan](docs/IMPLEMENTATION_PLAN.md)
- [Detailed System Architecture](docs/SYSTEM_ARCHITECTURE_DETAILED.md)
- [AI Features](docs/AI_FEATURES.md)
- [AI Tech Stack](docs/AI_TECH_STACK.md)
- [AI Flow](docs/AI_FLOW.md)
- [AI Generation Pipeline](docs/AI_GENERATION_PIPELINE.md)
- [AI Models and Languages](docs/AI_MODELS_AND_LANGUAGES.md)
- [AI Memory System](docs/AI_MEMORY_SYSTEM.md)
- [Daily Execution Protocol](docs/DAILY_EXECUTION_PROTOCOL.md)
- [Market and Business Case](docs/MARKET_AND_BUSINESS_CASE.md)
- [UX UI Guidelines](docs/UX_UI_GUIDELINES.md)
- [Security and Auth](docs/SECURITY_AND_AUTH.md)
- [Scalability Plan](docs/SCALABILITY_PLAN.md)
- [Upcoming Features](docs/UPCOMING_FEATURES.md)
- [AI Workflow Tracker](docs/AI_WORKFLOW_TRACKER.md)

## AI Workflow Folder

- [AI Workflow Index](ai_workflow/README.md)
- [Master Flow](ai_workflow/MASTER_FLOW.md)
- [Daily Schedule](ai_workflow/DAILY_SCHEDULE.md)
- [Backlog](ai_workflow/BACKLOG.md)
- [Current Handoff State](ai_workflow/HANDOFF_STATE.md)
- [Session Template](ai_workflow/SESSION_TEMPLATE.md)
- [Day 1 Log](ai_workflow/daily/2026-04-11.md)
- [Day 2 Log](ai_workflow/daily/2026-04-12.md)

## Principles

- Keep the stack minimal.
- Prefer RAG over model training.
- Keep backend modular, not microservice-heavy.
- Store all knowledge with repo-based access control.
- Make every API response useful for the frontend and automation.

## Daily Execution Rule

Every day is a 1.5 hour backend session. The active AI agent must read the latest handoff state, complete one concrete backend objective, update the daily log, and set the exact next starting point before ending the session.
