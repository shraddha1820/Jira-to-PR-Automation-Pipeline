from pydantic import BaseModel, Field


class JiraFields(BaseModel):
    summary: str
    description: str = ""
    priority: str | None = None
    labels: list[str] = Field(default_factory=list)
    acceptance_criteria: list[str] = Field(default_factory=list)


class JiraWebhookPayload(BaseModel):
    ticket_id: str = Field(..., examples=["DEMO-101"])
    fields: JiraFields
