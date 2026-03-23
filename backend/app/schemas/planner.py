from pydantic import BaseModel, Field

from app.schemas.common import ORMModel, TimestampMixin


class PlannerOutput(BaseModel):
    task_summary: str
    likely_affected_files: list[str] = Field(default_factory=list)
    implementation_plan: list[str] = Field(default_factory=list)
    risk_level: str
    validation_checklist: list[str] = Field(default_factory=list)
    provider: str = "mock"
    raw_response: dict = Field(default_factory=dict)


class PlannerResultRead(ORMModel, TimestampMixin):
    id: int
    job_id: int
    task_summary: str
    likely_affected_files: list[str]
    implementation_plan: list[str]
    risk_level: str
    validation_checklist: list[str]
    provider: str
    raw_response: dict
