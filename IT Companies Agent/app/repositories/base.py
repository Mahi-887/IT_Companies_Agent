"""Repository interfaces for persistence layers."""

from abc import ABC, abstractmethod
from typing import Any


class BaseRepository(ABC):
    @abstractmethod
    def save(self, payload: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

