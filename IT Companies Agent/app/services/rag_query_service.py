"""Retrieval augmented query service."""

from dataclasses import dataclass

from app.schemas.common import ApiEnvelope, Reference
from app.schemas.query import QueryRequest
from app.services.ai_service import get_ai_service


@dataclass(slots=True)
class QueryResult:
    data: dict
    references: list[Reference]
    confidence: float


class RagQueryService:
    def __init__(self):
        self.ai_service = get_ai_service()

    async def answer(self, request: QueryRequest) -> QueryResult:
        # Initial implementation: Simple prompt-based response
        # Using structured prompt to mitigate injection (P4.2)
        system_instruction = "You are DevPulse AI, an intelligent engineering shadow assisting a developer."
        
        # Sanitize query by stripping potential escape characters/instructions
        sanitized_query = request.query.replace("Ignore previous", "[REDACTED]").strip()
        
        prompt = f"""
        {system_instruction}
        Repository: {request.repo_id}
        Context: Codebase query
        
        Instruction: Answer the user's question based on the repository context.
        User Question: {sanitized_query}
        
        Answer:
        """
        
        ai_response = await self.ai_service.generate_response(prompt)
        
        answer = {
            "answer": ai_response,
            "repo_id": request.repo_id,
            "query": request.query,
            "context_type": request.context_type,
        }
        
        # Mock references for now - in full RAG these would come from ChromaDB
        references = [Reference(file_path="app/services/rag_query_service.py", line_start=1, line_end=1)]
        
        return QueryResult(data=answer, references=references, confidence=0.9)

