from app.schemas.planner import PlannerOutput
from app.services.llm.base import BasePlannerProvider


class MockPlannerProvider(BasePlannerProvider):
    def plan(self, parsed_ticket: dict) -> PlannerOutput:
        summary = parsed_ticket["summary"]
        ticket_id = parsed_ticket["ticket_id"]
        return PlannerOutput(
            task_summary=f"Implement bug fix for {ticket_id}: {summary}",
            likely_affected_files=["app/api.py", "tests/test_email_validation.py"],
            implementation_plan=[
                "Inspect the endpoint handling email input.",
                "Add explicit validation for missing email.",
                "Return HTTP 400 instead of internal server error.",
                "Update unit test coverage for missing email.",
            ],
            risk_level="low",
            validation_checklist=["run unit tests", "run lint"],
            provider="mock",
            raw_response={"mode": "mock", "ticket_id": ticket_id},
        )
