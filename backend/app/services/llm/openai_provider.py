from app.schemas.planner import PlannerOutput
from app.services.llm.base import BasePlannerProvider


class OpenAIPlannerProvider(BasePlannerProvider):
    def __init__(self, api_key: str | None, model: str):
        self.api_key = api_key
        self.model = model

    def plan(self, parsed_ticket: dict) -> PlannerOutput:
        # Real provider intentionally kept minimal for demo safety.
        # The rest of the system remains stable even if this is not configured.
        return PlannerOutput(
            task_summary=f"[real-mode placeholder] {parsed_ticket['summary']}",
            likely_affected_files=["app/api.py"],
            implementation_plan=["Call real provider and validate structured JSON response."],
            risk_level="medium",
            validation_checklist=["run unit tests"],
            provider="openai",
            raw_response={"mode": "real_placeholder", "model": self.model},
        )
