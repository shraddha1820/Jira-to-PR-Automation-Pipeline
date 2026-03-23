from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.job import Job


class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **kwargs) -> Job:
        job = Job(**kwargs)
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def update(self, job: Job, **kwargs) -> Job:
        for key, value in kwargs.items():
            setattr(job, key, value)
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def get(self, job_id: int) -> Job | None:
        return self.db.get(Job, job_id)

    def get_detail(self, job_id: int) -> Job | None:
        stmt = (
            select(Job)
            .where(Job.id == job_id)
            .options(
                joinedload(Job.parsed_ticket),
                joinedload(Job.planner_result),
                joinedload(Job.generated_files),
                joinedload(Job.validation_results),
                joinedload(Job.pr_metadata),
                joinedload(Job.status_history),
            )
        )
        return self.db.execute(stmt).unique().scalar_one_or_none()

    def list_all(self) -> list[Job]:
        stmt = select(Job).order_by(Job.created_at.desc())
        return list(self.db.execute(stmt).scalars().all())
