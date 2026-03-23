from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.job import JobCreateResponse, ManualJobCreateRequest
from app.schemas.jira import JiraWebhookPayload
from app.services.status_service import StatusService
from app.tasks.workflow_tasks import enqueue_workflow_job

router = APIRouter()


@router.post("/webhook", response_model=JobCreateResponse, status_code=status.HTTP_202_ACCEPTED)
def receive_jira_webhook(payload: JiraWebhookPayload, db: Session = Depends(get_db)) -> JobCreateResponse:
    service = StatusService(db)
    job = service.create_job_from_webhook(payload)
    enqueue_workflow_job(job.id)
    return JobCreateResponse(job_id=job.id, status=job.status)


@router.post("/trigger", response_model=JobCreateResponse, status_code=status.HTTP_202_ACCEPTED)
def trigger_manual_job(payload: ManualJobCreateRequest, db: Session = Depends(get_db)) -> JobCreateResponse:
    service = StatusService(db)
    job = service.create_job_from_manual_request(payload)
    enqueue_workflow_job(job.id)
    return JobCreateResponse(job_id=job.id, status=job.status)
