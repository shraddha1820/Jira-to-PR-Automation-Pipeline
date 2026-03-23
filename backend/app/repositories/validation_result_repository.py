from sqlalchemy.orm import Session

from app.models.validation_result import ValidationResult


class ValidationResultRepository:
    def __init__(self, db: Session):
        self.db = db

    def replace_all(self, job_id: int, items: list[dict]) -> list[ValidationResult]:
        self.db.query(ValidationResult).filter(ValidationResult.job_id == job_id).delete()
        records = [ValidationResult(job_id=job_id, **item) for item in items]
        self.db.add_all(records)
        self.db.commit()
        for record in records:
            self.db.refresh(record)
        return records
