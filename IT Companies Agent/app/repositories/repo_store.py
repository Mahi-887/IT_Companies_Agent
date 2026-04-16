"""CRUD operations for the Repository entity."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db_models import RepositoryModel
from app.models.entities import Repository


class RepoStore:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, repo_id: str) -> Repository | None:
        result = await self.db.execute(select(RepositoryModel).where(RepositoryModel.id == repo_id))
        model = result.scalar_one_or_none()
        if model:
            return Repository(
                id=model.id,
                owner_user_id=model.owner_user_id,
                name=model.name,
                github_url=model.github_url,
                default_branch=model.default_branch,
                created_at=model.created_at
            )
        return None

    async def get_all(self, owner_user_id: str | None = None) -> list[Repository]:
        query = select(RepositoryModel)
        if owner_user_id:
            query = query.where(RepositoryModel.owner_user_id == owner_user_id)
        
        result = await self.db.execute(query)
        models = result.scalars().all()
        return [
            Repository(
                id=m.id,
                owner_user_id=m.owner_user_id,
                name=m.name,
                github_url=m.github_url,
                default_branch=m.default_branch,
                created_at=m.created_at
            )
            for m in models
        ]

    async def create(self, repo: Repository) -> Repository:
        model = RepositoryModel(
            id=repo.id,
            owner_user_id=repo.owner_user_id,
            name=repo.name,
            github_url=repo.github_url,
            default_branch=repo.default_branch,
            created_at=repo.created_at
        )
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return repo
