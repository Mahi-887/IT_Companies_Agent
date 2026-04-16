"""Schemas for repository ingestion."""

from dataclasses import dataclass


@dataclass(slots=True)
class IngestRepoRequest:
    repo_id: str
    github_url: str
    default_branch: str = "main"

