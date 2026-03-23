from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.base import Base
from app.db.session import engine
from app.models.generated_file import GeneratedFile
from app.models.job import Job
from app.models.parsed_ticket import ParsedTicket
from app.models.planner_result import PlannerResult
from app.models.pr_metadata import PrMetadata
from app.models.validation_result import ValidationResult
from app.models.workflow_status_history import WorkflowStatusHistory



def init_db() -> None:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError:
        # Local dev should still boot even if the DB is not ready yet.
        return


if __name__ == "__main__":
    init_db()
