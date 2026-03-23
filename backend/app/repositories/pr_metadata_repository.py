from sqlalchemy.orm import Session

from app.models.pr_metadata import PrMetadata


class PrMetadataRepository:
    def __init__(self, db: Session):
        self.db = db

    def upsert(self, job_id: int, **kwargs) -> PrMetadata:
        instance = self.db.query(PrMetadata).filter(PrMetadata.job_id == job_id).one_or_none()
        if instance is None:
            instance = PrMetadata(job_id=job_id, **kwargs)
        else:
            for key, value in kwargs.items():
                setattr(instance, key, value)
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance
