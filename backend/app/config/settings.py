from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Jira-to-PR Automation Demo"
    app_env: Literal["local", "dev", "prod", "test"] = "local"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    database_url: str = Field(
        default="postgresql+psycopg2://postgres:postgres@db:5432/ai_jira_demo"
    )
    redis_url: str = "redis://redis:6379/0"
    celery_broker_url: str = "redis://redis:6379/0"
    celery_result_backend: str = "redis://redis:6379/1"

    llm_mode: Literal["mock", "real"] = "mock"
    llm_provider: Literal["mock", "openai"] = "mock"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4.1-mini"

    github_enabled: bool = False
    github_token: str | None = None
    github_repo: str | None = None
    github_owner: str | None = None

    demo_repo_path: str = "/app/demo_repo"
    prompts_dir: str = "app/prompts"
    mock_data_dir: str = "app/mock_data"

    log_level: str = "INFO"
    cors_origins: str = "http://localhost:3000,http://frontend:3000"

    @property
    def cors_origins_list(self) -> list[str]:
        return [item.strip() for item in self.cors_origins.split(",") if item.strip()]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
