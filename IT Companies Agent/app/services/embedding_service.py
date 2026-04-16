"""Embedding service boundary."""

from app.schemas.common import Reference


class EmbeddingService:
    def chunk_document(self, text: str) -> list[str]:
        return [text] if text else []

    def to_reference(self, file_path: str, line_start: int, line_end: int) -> Reference:
        return Reference(file_path=file_path, line_start=line_start, line_end=line_end)

