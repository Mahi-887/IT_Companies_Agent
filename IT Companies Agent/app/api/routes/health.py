"""Health and readiness endpoints."""

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope

router = APIRouter(tags=["health"])


@router.get("/health", response_model=ApiEnvelope)
def health_check() -> ApiEnvelope:
    return ApiEnvelope.create_success(message="Service is healthy", data={"status": "ok"})

