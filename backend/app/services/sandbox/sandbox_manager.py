from pathlib import Path

from app.config.settings import get_settings


class SandboxManager:
    def __init__(self):
        settings = get_settings()
        self.repo_path = Path(settings.demo_repo_path).resolve()

    def get_repo_path(self) -> Path:
        return self.repo_path
