"""Repository ingestion endpoints."""

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope
from app.schemas.ingest import IngestRepoRequest
from app.services.repo_ingestion_service import RepoIngestionService

router = APIRouter(tags=["ingest"])
ingestion_service = RepoIngestionService()


@router.post("/ingest/repo", response_model=ApiEnvelope)
def ingest_repository(payload: IngestRepoRequest) -> ApiEnvelope:
    result = ingestion_service.plan_ingestion(payload)
    return ApiEnvelope.success(message="Ingestion planned", data=result)

