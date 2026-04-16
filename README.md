# DevPulse AI — Intelligent Engineering Shadow

> A production-ready backend that answers codebase questions, tracks knowledge, updates documentation, and helps developers debug with context.

---

## Table of Contents

- [Overview](#overview)
- [Why DevPulse AI?](#why-devpulse-ai)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Frontend](#frontend)
- [Security](#security)
- [Cross-Platform Support](#cross-platform-support)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

---

## Overview

**DevPulse AI** is an engineering shadow system — not a generic chatbot. It is designed to understand repository structure, internal documentation, issue history, team context, and runtime signals within a single backend workflow.

Large engineering teams lose time because new developers cannot navigate codebases quickly and senior developers repeatedly answer the same internal questions. DevPulse AI solves this by providing an AI-powered layer on top of your codebase that any developer can query in natural language.

## Why DevPulse AI?

| Pain Point | DevPulse AI Solution |
|---|---|
| New developers take weeks to onboard | Answer architecture questions in minutes |
| Senior engineers answer the same questions repeatedly | Automated knowledge base reduces dependency by ~60% |
| Stale documentation | Auto-documentation triggered by Git commits |
| Debugging is slow — logs and past fixes are disconnected | Context-aware debug analysis matches logs to known patterns |
| Jira tickets lack context about code ownership | Smart ticket mapping suggests modules and owners |

**Success Metrics:**
- Reduce onboarding time from weeks to < 3 days
- Reduce senior developer dependency by 60%
- Increase code navigation speed by 70%
- Automate 80% of documentation updates

---

## Features

### 1. Knowledge Query (RAG)
Ask natural language questions and receive answers with file references, code snippets, and confidence notes — all scoped to the selected repository.

### 2. Auto Documentation Generator
Git commits and repository changes trigger documentation refresh workflows, keeping internal docs synchronized with the codebase.

### 3. Context-Aware Debug Analyzer
Runtime logs and environment context are matched against past incidents, config dependencies, and likely fixes.

### 4. Smart Ticket Mapping
Jira tickets are mapped to likely modules, code owners, and relevant historical context automatically.

### 5. Repository Ingestion
Repositories can be ingested and vector-indexed without any custom model training.

---

## Architecture

```
┌─────────────────────────────────────────────┐
│                  Frontend                   │
│          (HTML / CSS / Vanilla JS)          │
└──────────────────┬──────────────────────────┘
                   │ REST API (JSON)
┌──────────────────▼──────────────────────────┐
│            FastAPI Backend                  │
│  ┌──────────┐ ┌──────────┐ ┌─────────────┐ │
│  │  Query   │ │  Ingest  │ │   Debug /   │ │
│  │  Router  │ │  Router  │ │  Webhook    │ │
│  └────┬─────┘ └────┬─────┘ └──────┬──────┘ │
│       │            │              │         │
│  ┌────▼────────────▼──────────────▼──────┐  │
│  │          Service Layer                │  │
│  │  AIService │ AuthService │ RepoService│  │
│  └────────────────────────────────────────┘ │
│  ┌────────────┐  ┌───────────────────────┐  │
│  │ PostgreSQL │  │  ChromaDB (vectors)   │  │
│  │  (SQLite   │  │  for semantic search  │  │
│  │   dev)     │  └───────────────────────┘  │
│  └────────────┘                             │
└─────────────────────────────────────────────┘
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11+, FastAPI |
| AI / LLM | Google Gemini (`gemini-1.5-flash`) |
| Vector Store | ChromaDB |
| Database | SQLite (dev) / PostgreSQL (prod) |
| ORM & Migrations | SQLAlchemy 2, Alembic |
| Auth | JWT (PyJWT) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |

---

## Getting Started

### Prerequisites

- Python **3.11** or higher
- `pip` / a virtual environment tool (`venv`, `uv`, etc.)
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Mahi-887/IT_Companies_Agent.git
cd "IT_Companies_Agent/IT Companies Agent"

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# 3. Install dependencies
pip install -e .
```

### Environment Variables

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

| Variable | Description | Required |
|---|---|---|
| `AG_API_KEY` | Google Gemini API key | ✅ Yes |
| `DEVPULE_JWT_SECRET` | Strong random secret for JWT signing | ✅ Yes |
| `DATABASE_URL` | Database connection string | No (defaults to SQLite) |
| `DEVPULE_PROJECT_NAME` | Application name | No |
| `DEVPULE_PROJECT_VERSION` | Application version | No |
| `DEVPULE_API_PREFIX` | API prefix | No (defaults to `/api/v1`) |
| `DEVPULE_GOOGLE_MODEL` | Gemini model name | No (defaults to `gemini-1.5-flash`) |
| `ENV` | Set to `development` to enable dev-only endpoints | No |

> **Never commit your `.env` file.** It is already in `.gitignore`.

### Running the Application

```bash
# Start the backend (from the "IT Companies Agent" directory)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open `frontend/index.html` in a browser, or serve it via any static file server:

```bash
# Quick static server (Python)
python -m http.server 3000 --directory frontend
```

Navigate to `http://localhost:3000` in your browser.

---

## API Reference

The API is available under the `/api/v1` prefix. Visit `http://localhost:8000/docs` for the interactive Swagger UI.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/health` | Health check |
| `POST` | `/api/v1/query` | Submit a codebase query |
| `POST` | `/api/v1/ingest` | Ingest a repository |
| `POST` | `/api/v1/webhook` | Process a GitHub webhook event |
| `POST` | `/api/v1/debug` | Analyze logs for debugging |
| `GET` | `/api/v1/repositories` | List indexed repositories |
| `POST` | `/api/v1/tickets` | Map a Jira ticket to code context |
| `GET` | `/api/v1/auth/demo-token` | Get a demo token (dev mode only) |

---

## Frontend

The frontend is a lightweight single-page application:

- **`frontend/index.html`** — app shell with sidebar navigation
- **`frontend/style.css`** — dark-theme design with full mobile responsiveness
- **`frontend/app.js`** — API client, chat UI logic, and sidebar toggle

### Responsive Design

The UI adapts to all screen sizes:
- **Desktop (> 768 px):** Fixed sidebar + main chat area side-by-side
- **Tablet / Mobile (≤ 768 px):** Sidebar hidden by default; tap the ☰ hamburger button to reveal it as an overlay

---

## Security

- **Secrets**: All secrets are loaded from environment variables via `.env`. No secrets are hard-coded.
- **JWT**: Tokens are signed using the `DEVPULE_JWT_SECRET` variable. The application will refuse to start a demo-token endpoint without this being set.
- **`.gitignore`**: `.env`, database files (`*.db`), vector store directories, and other sensitive artifacts are excluded from version control.
- **Demo endpoint**: `/api/v1/auth/demo-token` is only available when `ENV=development` is set.

---

## Cross-Platform Support

DevPulse AI is designed to run identically on **Windows**, **Linux**, and **macOS**:

- Python 3.11+ and all dependencies are cross-platform
- SQLite is used as the default database — no external database install required for development
- File paths use Python's `pathlib` / OS-neutral conventions
- The frontend uses standard web fonts with system-font fallbacks (no platform-specific assets)
- Virtual environment activation commands differ by OS — see [Installation](#installation) above

---

## Project Structure

```
IT Companies Agent/
├── app/
│   ├── api/
│   │   ├── router.py           # Central route registry
│   │   └── routes/             # Individual route handlers
│   ├── core/
│   │   ├── config.py           # Settings loaded from env
│   │   ├── db.py               # Database session factory
│   │   ├── dependencies.py     # FastAPI dependency injection
│   │   ├── errors.py           # Custom exception handlers
│   │   └── security.py         # JWT utilities
│   ├── models/                 # SQLAlchemy ORM models
│   ├── repositories/           # Database access layer
│   ├── schemas/                # Pydantic request/response schemas
│   ├── services/               # Business logic (AI, auth, repo, ...)
│   └── main.py                 # Application factory
├── frontend/
│   ├── index.html              # App shell
│   ├── style.css               # Responsive dark-theme styles
│   └── app.js                  # UI logic & API client
├── docs/                       # Architecture & PRD documents
├── migrations/                 # Alembic database migrations
├── tests/                      # Pytest test suite
├── .env.example                # Environment variable template
├── pyproject.toml              # Project metadata & dependencies
└── seed_db.py                  # Development seed data
```

---

## Contributing

1. Fork the repository and create a feature branch
2. Copy `.env.example` → `.env` and fill in required values
3. Install dependencies: `pip install -e .`
4. Run tests: `pytest`
5. Open a pull request with a clear description of your change
