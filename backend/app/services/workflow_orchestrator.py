import json
import logging

from sqlalchemy.orm import Session

from app.core.enums import JobStatus, WorkflowStage
from app.repositories.generated_file_repository import GeneratedFileRepository
from app.repositories.job_repository import JobRepository
from app.repositories.parsed_ticket_repository import ParsedTicketRepository
from app.repositories.planner_result_repository import PlannerResultRepository
from app.repositories.pr_metadata_repository import PrMetadataRepository
from app.repositories.validation_result_repository import ValidationResultRepository
from app.services.code_generation_service import CodeGenerationService
from app.services.git_pr_service import GitPrService
from app.services.jira_parser_service import JiraParserService
from app.services.planner_service import PlannerService
from app.services.status_service import StatusService
from app.services.validation_service import ValidationService
from app.schemas.job import ManualJobCreateRequest
from app.schemas.jira import JiraWebhookPayload

logger = logging.getLogger(__name__)


class WorkflowOrchestrator:
    def __init__(self, db: Session):
        self.db = db
        self.jobs = JobRepository(db)
        self.status = StatusService(db)
        self.parsed_repo = ParsedTicketRepository(db)
        self.planner_repo = PlannerResultRepository(db)
        self.generated_repo = GeneratedFileRepository(db)
        self.validation_repo = ValidationResultRepository(db)
        self.pr_repo = PrMetadataRepository(db)
        self.parser = JiraParserService()
        self.planner = PlannerService()
        self.generator = CodeGenerationService()
        self.validator = ValidationService()
        self.git_pr = GitPrService()

    def run(self, job_id: int) -> None:
        job = self.jobs.get(job_id)
        if job is None:
            logger.error("Job not found", extra={"job_id": job_id})
            return

        try:
            self.status.update_job_status(job_id, JobStatus.processing.value, WorkflowStage.parsing.value, "Parsing Jira payload")
            parsed_ticket = self._parse_job_payload(job)
            self.parsed_repo.upsert(job_id, **parsed_ticket)

            self.status.update_job_status(job_id, JobStatus.processing.value, WorkflowStage.planning.value, "Building implementation plan")
            plan = self.planner.build_plan(parsed_ticket)
            self.planner_repo.upsert(job_id, **plan.model_dump())

            self.status.update_job_status(job_id, JobStatus.processing.value, WorkflowStage.code_generation.value, "Applying code changes in sandbox")
            generated_files = self.generator.apply_changes(parsed_ticket, plan)
            self.generated_repo.replace_all(job_id, [item.model_dump() for item in generated_files])

            self.status.update_job_status(job_id, JobStatus.processing.value, WorkflowStage.validation.value, "Running validation checks")
            validation_results = self.validator.run(generated_files)
            self.validation_repo.replace_all(job_id, [item.model_dump() for item in validation_results])

            self.status.update_job_status(job_id, JobStatus.processing.value, WorkflowStage.pr_generation.value, "Generating PR payload")
            pr_payload = self.git_pr.generate_pr_payload(parsed_ticket, plan)
            self.pr_repo.upsert(job_id, **pr_payload.model_dump())

            final_status = JobStatus.completed.value
            if not all(item.passed for item in validation_results):
                final_status = JobStatus.completed_with_warnings.value
            self.status.update_job_status(job_id, final_status, WorkflowStage.finished.value, "Workflow completed")
        except Exception as exc:  # noqa: BLE001
            self.jobs.update(job, status=JobStatus.failed.value, error_message=str(exc))
            self.status.update_job_status(job_id, JobStatus.failed.value, WorkflowStage.failed.value, str(exc))
            logger.exception("Workflow failed", extra={"job_id": job_id})
            raise

    def _parse_job_payload(self, job) -> dict:
        payload = json.loads(job.raw_payload)
        if job.source == "jira_webhook":
            return self.parser.parse_webhook_payload(JiraWebhookPayload.model_validate(payload))
        return self.parser.parse_manual_payload(ManualJobCreateRequest.model_validate(payload))
