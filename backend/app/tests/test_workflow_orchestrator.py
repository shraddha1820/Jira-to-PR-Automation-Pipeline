from app.schemas.job import ManualJobCreateRequest
from app.services.jira_parser_service import JiraParserService
from app.services.planner_service import PlannerService


def test_manual_parse_and_plan_path_smoke():
    request = ManualJobCreateRequest(
        ticket_id="DEMO-101",
        summary="Fix missing email validation",
        description="Missing email returns 500",
        acceptance_criteria=["Return 400"],
        priority="High",
        labels=["bug"],
    )
    parsed = JiraParserService().parse_manual_payload(request)
    plan = PlannerService().build_plan(parsed)
    assert parsed["ticket_id"] == "DEMO-101"
    assert plan.risk_level in {"low", "medium", "high"}
