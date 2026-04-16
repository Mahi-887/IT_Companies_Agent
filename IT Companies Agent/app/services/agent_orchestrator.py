"""Agent selection and execution boundary."""

from app.schemas.debug import DebugAnalyzeRequest
from app.schemas.query import QueryRequest


class AgentOrchestrator:
    def select_agent(self, task_type: str) -> str:
        mapping = {
            "query": "librarian",
            "architecture": "architect",
            "debug": "debugger",
            "ticket": "manager",
        }
        return mapping.get(task_type, "librarian")

    def route_query(self, request: QueryRequest) -> str:
        return self.select_agent("query")

    def route_debug(self, request: DebugAnalyzeRequest) -> str:
        return self.select_agent("debug")

