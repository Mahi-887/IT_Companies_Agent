"""Schemas for query requests."""

from dataclasses import dataclass


@dataclass(slots=True)
class QueryRequest:
    repo_id: str
    query: str
    context_type: str = "codebase"

