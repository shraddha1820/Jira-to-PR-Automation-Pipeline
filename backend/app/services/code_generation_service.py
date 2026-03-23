from pathlib import Path

from app.schemas.generation import GeneratedFilePayload
from app.schemas.planner import PlannerOutput
from app.services.sandbox.diff_service import DiffService
from app.services.sandbox.file_editor import FileEditor
from app.services.sandbox.sandbox_manager import SandboxManager


class CodeGenerationService:
    def __init__(self):
        self.sandbox = SandboxManager()
        self.editor = FileEditor()
        self.diff_service = DiffService()

    def apply_changes(self, parsed_ticket: dict, planner_result: PlannerOutput) -> list[GeneratedFilePayload]:
        repo_path = self.sandbox.get_repo_path()
        api_path = repo_path / "app" / "api.py"
        test_path = repo_path / "tests" / "test_email_validation.py"

        generated_files: list[GeneratedFilePayload] = []

        api_before = self.editor.read(api_path)
        api_after = self._patched_api_content(api_before)
        self.editor.write(api_path, api_after)
        generated_files.append(
            GeneratedFilePayload(
                file_path="app/api.py",
                before_content=api_before,
                after_content=api_after,
                diff_text=self.diff_service.build_diff(api_before, api_after, "app/api.py"),
            )
        )

        test_before = self.editor.read(test_path)
        test_after = self._patched_test_content(test_before)
        self.editor.write(test_path, test_after)
        generated_files.append(
            GeneratedFilePayload(
                file_path="tests/test_email_validation.py",
                before_content=test_before,
                after_content=test_after,
                diff_text=self.diff_service.build_diff(test_before, test_after, "tests/test_email_validation.py"),
            )
        )
        return generated_files

    def _patched_api_content(self, current_content: str | None) -> str:
        return (
            current_content
            or ""
        ).replace(
            'email = payload["email"]\n    return {"ok": True, "email": email}',
            'email = payload.get("email")\n    if not email:\n        return {"ok": False, "error": "email is required", "status_code": 400}\n    return {"ok": True, "email": email}',
        )

    def _patched_test_content(self, current_content: str | None) -> str:
        if current_content and "test_missing_email_returns_400" in current_content:
            return current_content
        return (current_content or "") + (
            "\n\ndef test_missing_email_returns_400():\n"
            "    from app.api import create_user\n"
            "    response = create_user({})\n"
            "    assert response[\"status_code\"] == 400\n"
        )
