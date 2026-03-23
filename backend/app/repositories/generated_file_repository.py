from sqlalchemy.orm import Session

from app.models.generated_file import GeneratedFile


class GeneratedFileRepository:
    def __init__(self, db: Session):
        self.db = db

    def replace_all(self, job_id: int, items: list[dict]) -> list[GeneratedFile]:
        self.db.query(GeneratedFile).filter(GeneratedFile.job_id == job_id).delete()
        records = [GeneratedFile(job_id=job_id, **item) for item in items]
        self.db.add_all(records)
        self.db.commit()
        for record in records:
            self.db.refresh(record)
        return records
