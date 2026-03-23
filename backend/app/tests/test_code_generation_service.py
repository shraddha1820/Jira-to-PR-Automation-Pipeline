from pathlib import Path

from app.schemas.planner import PlannerOutput
from app.services.code_generation_service import CodeGenerationService


class DummySandbox:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path

    def get_repo_path(self) -> Path:
        return self.repo_path


def test_code_generation_patches_api_and_test(tmp_path):
    repo = tmp_path / "demo_repo"
    (repo / "app").mkdir(parents=True)
    (repo / "tests").mkdir(parents=True)
    (repo / "app" / "api.py").write_text(
        'def create_user(payload: dict) -> dict:\n'
        '    email = payload["email"]\n'
        '    return {"ok": True, "email": email}\n'
    )
    (repo / "tests" / "test_email_validation.py").write_text(
        'from app.api import create_user\n\n'
        'def test_valid_email_succeeds():\n'
        '    response = create_user({"email": "demo@example.com"})\n'
        '    assert response["ok"] is True\n'
    )

    service = CodeGenerationService()
    service.sandbox = DummySandbox(repo)

    plan = PlannerOutput(
        task_summary="Fix missing email validation",
        likely_affected_files=["app/api.py", "tests/test_email_validation.py"],
        implementation_plan=["Add email guard"],
        risk_level="low",
        validation_checklist=["unit tests"],
    )

    files = service.apply_changes({"ticket_id": "DEMO-101", "summary": "Fix missing email validation"}, plan)

    assert len(files) == 2
    updated_api = (repo / "app" / "api.py").read_text()
    updated_test = (repo / "tests" / "test_email_validation.py").read_text()
    assert 'payload.get("email")' in updated_api
    assert 'test_missing_email_returns_400' in updated_test
