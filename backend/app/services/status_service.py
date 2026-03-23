import json

from sqlalchemy.orm import Session

from app.core.enums import JobStatus, WorkflowStage
from app.repositories.job_repository import JobRepository
from app.repositories.workflow_history_repository import WorkflowHistoryRepository
from app.schemas.job import JobDetailResponse, ManualJobCreateRequest
from app.schemas.jira import JiraWebhookPayload
from app.services.jira_parser_service import JiraParserService


class StatusService:
    def __init__(self, db: Session):
        self.db = db
        self.jobs = JobRepository(db)
        self.history = WorkflowHistoryRepository(db)
        self.parser = JiraParserService()

    def create_job_from_webhook(self, payload: JiraWebhookPayload):
        job = self.jobs.create(
            source="jira_webhook",
            status=JobStatus.queued.value,
            jira_ticket_id=payload.ticket_id,
            raw_payload=payload.model_dump_json(),
        )
        self.history.create(job.id, WorkflowStage.received.value, JobStatus.queued.value, "Webhook payload accepted")
        return job

    def create_job_from_manual_request(self, payload: ManualJobCreateRequest):
        job = self.jobs.create(
            source="manual",
            status=JobStatus.queued.value,
            jira_ticket_id=payload.ticket_id,
            raw_payload=payload.model_dump_json(),
        )
        self.history.create(job.id, WorkflowStage.received.value, JobStatus.queued.value, "Manual ticket accepted")
        return job

    def update_job_status(self, job_id: int, status: str, stage: str, message: str | None = None):
        job = self.jobs.get(job_id)
        if job is None:
            return None
        self.jobs.update(job, status=status)
        self.history.create(job_id, stage, status, message)
        return job

    def list_jobs(self):
        return self.jobs.list_all()

    def get_job_detail(self, job_id: int) -> JobDetailResponse | None:
        job = self.jobs.get_detail(job_id)
        if job is None:
            return None
        return JobDetailResponse.model_validate(job)
