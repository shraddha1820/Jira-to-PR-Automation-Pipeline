from sqlalchemy.orm import Session

from app.models.workflow_status_history import WorkflowStatusHistory


class WorkflowHistoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, job_id: int, stage: str, status: str, message: str | None = None) -> WorkflowStatusHistory:
        record = WorkflowStatusHistory(job_id=job_id, stage=stage, status=status, message=message)
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record
