"""Query endpoints for codebase and knowledge retrieval."""

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope
from app.schemas.query import QueryRequest
from app.services.rag_query_service import RagQueryService

router = APIRouter(tags=["query"])
rag_service = RagQueryService()


@router.post("/query", response_model=ApiEnvelope)
async def query_codebase(payload: QueryRequest) -> ApiEnvelope:
    result = await rag_service.answer(payload)
    return ApiEnvelope.create_success(
        message="Query processed",
        data=result.data,
        references=result.references,
        confidence=result.confidence,
    )

