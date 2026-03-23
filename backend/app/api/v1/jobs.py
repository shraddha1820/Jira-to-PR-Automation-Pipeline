from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.job import JobDetailResponse, JobListItem, JobListResponse
from app.services.status_service import StatusService

router = APIRouter()


@router.get("", response_model=JobListResponse)
def list_jobs(db: Session = Depends(get_db)) -> JobListResponse:
    service = StatusService(db)
    jobs = service.list_jobs()
    return JobListResponse(items=[JobListItem.model_validate(job) for job in jobs])


@router.get("/{job_id}", response_model=JobDetailResponse)
def get_job(job_id: int, db: Session = Depends(get_db)) -> JobDetailResponse:
    service = StatusService(db)
    payload = service.get_job_detail(job_id)
    if payload is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return payload
