from pydantic import BaseModel

from app.schemas.common import ORMModel, TimestampMixin


class PrPayload(BaseModel):
    branch_name: str
    commit_message: str
    pr_title: str
    pr_body: str
    pr_url: str | None = None
    is_simulated: bool = True


class PrMetadataRead(ORMModel, TimestampMixin):
    id: int
    job_id: int
    branch_name: str
    commit_message: str
    pr_title: str
    pr_body: str
    pr_url: str | None = None
    is_simulated: bool
