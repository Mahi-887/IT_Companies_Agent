"""Schemas for debug analysis."""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DebugAnalyzeRequest:
    repo_id: str
    message: str
    logs: list[str]
    metadata: dict[str, Any]

