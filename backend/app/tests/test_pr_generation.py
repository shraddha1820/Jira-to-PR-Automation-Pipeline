from app.schemas.planner import PlannerOutput
from app.services.git_pr_service import GitPrService


def test_pr_payload_generation():
    parsed_ticket = {
        "ticket_id": "DEMO-101",
        "summary": "Fix missing email validation",
    }
    plan = PlannerOutput(
        task_summary="Fix missing email validation",
        likely_affected_files=["app/api.py"],
        implementation_plan=["Add missing email guard"],
        risk_level="low",
        validation_checklist=["run unit tests"],
    )
    result = GitPrService().generate_pr_payload(parsed_ticket, plan)
    assert result.branch_name.startswith("feature/")
    assert "DEMO-101" in result.pr_title
    assert result.is_simulated is True
