"""Shared API response envelope and reference models."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Reference:
    file_path: str
    line_start: int
    line_end: int


@dataclass(slots=True)
class ApiEnvelope:
    success: bool = True
    message: str = ""
    data: dict[str, Any] = field(default_factory=dict)
    references: list[Reference] = field(default_factory=list)
    confidence: float | None = None
    errors: list[str] = field(default_factory=list)

    @classmethod
    def create_success(
        cls,
        message: str,
        data: dict[str, Any] | None = None,
        references: list[Reference] | None = None,
        confidence: float | None = None,
    ) -> "ApiEnvelope":
        return cls(
            success=True,
            message=message,
            data=data or {},
            references=references or [],
            confidence=confidence,
            errors=[],
        )

