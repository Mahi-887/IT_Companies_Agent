"""Routes for repository management."""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db_session
from app.core.dependencies import get_current_user
from app.core.security import AuthContext
from app.models.entities import Repository
from app.repositories.repo_store import RepoStore

router = APIRouter(prefix="/repositories", tags=["Repositories"])

class RepositoryCreate(BaseModel):
    name: str
    github_url: str
    default_branch: str = "main"

class RepositoryResponse(BaseModel):
    id: str
    owner_user_id: str
    name: str
    github_url: str
    default_branch: str

@router.post("", response_model=RepositoryResponse, status_code=status.HTTP_201_CREATED)
async def create_repository(
    repo_in: RepositoryCreate,
    db: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[AuthContext, Depends(get_current_user)]
):
    repo_store = RepoStore(db)
    
    # Generate ID for the new repository
    repo_id = str(uuid.uuid4())
    
    repo = Repository(
        id=repo_id,
        owner_user_id=current_user.user_id,
        name=repo_in.name,
        github_url=repo_in.github_url,
        default_branch=repo_in.default_branch
    )
    
    created_repo = await repo_store.create(repo)
    return created_repo

@router.get("/{repo_id}", response_model=RepositoryResponse)
async def get_repository(
    repo_id: str,
    db: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[AuthContext, Depends(get_current_user)]
):
    repo_store = RepoStore(db)
    repo = await repo_store.get_by_id(repo_id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
    if repo.owner_user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to access this repository")
    return repo

@router.get("", response_model=list[RepositoryResponse])
async def list_repositories(
    db: Annotated[AsyncSession, Depends(get_db_session)],
    current_user: Annotated[AuthContext, Depends(get_current_user)]
):
    repo_store = RepoStore(db)
    repos = await repo_store.get_all(owner_user_id=current_user.user_id)
    return repos
