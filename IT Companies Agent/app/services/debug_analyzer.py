"""Debug analysis service."""

from dataclasses import dataclass

from app.schemas.debug import DebugAnalyzeRequest


@dataclass(slots=True)
class DebugResult:
    repo_id: str
    summary: str
    confidence: float


class DebugAnalyzer:
    def analyze(self, request: DebugAnalyzeRequest) -> DebugResult:
        return DebugResult(
            repo_id=request.repo_id,
            summary="Debug analysis pipeline is ready to connect logs, config, and prior incidents.",
            confidence=0.5,
        )

