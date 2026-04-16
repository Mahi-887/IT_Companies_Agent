"""Core domain entities used across services."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class Repository:
    id: str
    owner_user_id: str
    name: str
    github_url: str
    default_branch: str = "main"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class Document:
    id: str
    repo_id: str
    source_type: str
    title: str
    file_path: str
    content_hash: str
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(slots=True)
class AgentTask:
    id: str
    repo_id: str
    agent_name: str
    task_type: str
    status: str
    input_payload: dict[str, Any]
    output_payload: dict[str, Any] | None = None

