from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.generation import GeneratedFileRead
from app.schemas.jira import JiraFields
from app.schemas.planner import PlannerResultRead
from app.schemas.pr import PrMetadataRead
from app.schemas.validation import ValidationResultRead


class ManualJobCreateRequest(BaseModel):
    ticket_id: str = Field(..., examples=["DEMO-101"])
    summary: str
    description: str = ""
    acceptance_criteria: list[str] = Field(default_factory=list)
    priority: str | None = None
    labels: list[str] = Field(default_factory=list)


class JobCreateResponse(BaseModel):
    job_id: int
    status: str


class ParsedTicketRead(BaseModel):
    id: int
    job_id: int
    ticket_id: str
    summary: str
    description: str
    acceptance_criteria: list[str]
    priority: str | None
    labels: list[str]

    model_config = {"from_attributes": True}


class StatusHistoryRead(BaseModel):
    stage: str
    status: str
    message: str | None = None
    created_at: datetime | None = None

    model_config = {"from_attributes": True}


class JobListItem(BaseModel):
    id: int
    source: str
    status: str
    jira_ticket_id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}


class JobListResponse(BaseModel):
    items: list[JobListItem]


class JobDetailResponse(BaseModel):
    id: int
    source: str
    status: str
    jira_ticket_id: str | None = None
    error_message: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    parsed_ticket: ParsedTicketRead | None = None
    planner_result: PlannerResultRead | None = None
    generated_files: list[GeneratedFileRead] = Field(default_factory=list)
    validation_results: list[ValidationResultRead] = Field(default_factory=list)
    pr_metadata: PrMetadataRead | None = None
    status_history: list[StatusHistoryRead] = Field(default_factory=list)

    model_config = {"from_attributes": True}
