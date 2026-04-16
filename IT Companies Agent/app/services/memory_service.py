"""Memory checkpoint service.

This will eventually persist session and task memory for agent handoffs.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class MemoryCheckpoint:
    repo_id: str
    key: str
    value: str


class MemoryService:
    def save_checkpoint(self, checkpoint: MemoryCheckpoint) -> MemoryCheckpoint:
        return checkpoint

