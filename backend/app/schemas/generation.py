from pydantic import BaseModel

from app.schemas.common import ORMModel, TimestampMixin


class GeneratedFilePayload(BaseModel):
    file_path: str
    change_type: str = "modified"
    before_content: str | None = None
    after_content: str
    diff_text: str
    applied_successfully: bool = True


class GeneratedFileRead(ORMModel, TimestampMixin):
    id: int
    job_id: int
    file_path: str
    change_type: str
    before_content: str | None = None
    after_content: str
    diff_text: str
    applied_successfully: bool
