"""Schemas for webhook payloads."""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class GitHubWebhookEvent:
    event_type: str
    repo_id: str
    payload: dict[str, Any]

