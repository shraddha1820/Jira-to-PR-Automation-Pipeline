from sqlalchemy.orm import Session

from app.models.planner_result import PlannerResult


class PlannerResultRepository:
    def __init__(self, db: Session):
        self.db = db

    def upsert(self, job_id: int, **kwargs) -> PlannerResult:
        instance = self.db.query(PlannerResult).filter(PlannerResult.job_id == job_id).one_or_none()
        if instance is None:
            instance = PlannerResult(job_id=job_id, **kwargs)
        else:
            for key, value in kwargs.items():
                setattr(instance, key, value)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance
