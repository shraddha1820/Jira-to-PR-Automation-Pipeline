from pydantic import BaseModel

from app.schemas.common import ORMModel, TimestampMixin


class ValidationStepOutput(BaseModel):
    step_name: str
    passed: bool
    exit_code: int = 0
    output: str


class ValidationResultRead(ORMModel, TimestampMixin):
    id: int
    job_id: int
    step_name: str
    passed: bool
    exit_code: int
    output: str
