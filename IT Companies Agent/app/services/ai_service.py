import google.generativeai as genai
from app.core.config import get_settings

_ai_service_instance = None

def get_ai_service() -> "AiService":
    global _ai_service_instance
    if _ai_service_instance is None:
        _ai_service_instance = AiService()
    return _ai_service_instance

class AiService:
    def __init__(self):
        settings = get_settings()
        genai.configure(api_key=settings.ag_api_key)
        self.model = genai.GenerativeModel(settings.google_model)

    async def generate_response(self, prompt: str) -> str:
        response = await self.model.generate_content_async(prompt)
        return response.text

    async def get_embeddings(self, text: str) -> list[float]:
        result = await genai.embed_content_async(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_document"
        )
        return result['embedding']
