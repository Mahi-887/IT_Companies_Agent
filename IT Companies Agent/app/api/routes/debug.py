"""Debug analysis endpoints."""

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope
from app.schemas.debug import DebugAnalyzeRequest
from app.services.debug_analyzer import DebugAnalyzer

router = APIRouter(tags=["debug"])
debug_analyzer = DebugAnalyzer()


@router.post("/debug/analyze", response_model=ApiEnvelope)
def analyze_debug_signal(payload: DebugAnalyzeRequest) -> ApiEnvelope:
    result = debug_analyzer.analyze(payload)
    return ApiEnvelope.success(message="Debug analysis complete", data=result)

