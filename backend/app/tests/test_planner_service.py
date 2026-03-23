from app.services.planner_service import PlannerService


def test_planner_returns_structured_output():
    parsed_ticket = {
        "ticket_id": "DEMO-101",
        "summary": "Fix email validation",
        "description": "Missing email returns 500",
        "acceptance_criteria": ["Return 400"],
        "priority": "High",
        "labels": ["bug"],
    }
    result = PlannerService().build_plan(parsed_ticket)
    assert result.provider in {"mock", "openai"}
    assert result.task_summary
    assert isinstance(result.implementation_plan, list)
