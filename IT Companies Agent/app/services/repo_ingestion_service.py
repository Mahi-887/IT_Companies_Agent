"""Repository ingestion planning service."""

from dataclasses import dataclass

from app.schemas.ingest import IngestRepoRequest


@dataclass(slots=True)
class IngestionPlan:
    repo_id: str
    github_url: str
    default_branch: str
    stages: list[str]


class RepoIngestionService:
    def plan_ingestion(self, request: IngestRepoRequest) -> IngestionPlan:
        return IngestionPlan(
            repo_id=request.repo_id,
            github_url=request.github_url,
            default_branch=request.default_branch,
            stages=[
                "fetch_repository_metadata",
                "scan_documents",
                "chunk_and_embed_content",
                "persist_metadata",
            ],
        )

