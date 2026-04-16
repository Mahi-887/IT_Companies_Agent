"""Repository access and registration service."""

from app.models.entities import Repository


class RepoService:
    def register_repository(self, repo_id: str, owner_user_id: str, name: str, github_url: str) -> Repository:
        return Repository(
            id=repo_id,
            owner_user_id=owner_user_id,
            name=name,
            github_url=github_url,
        )

