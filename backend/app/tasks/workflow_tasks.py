from app.celery_app import celery_app
from app.db.session import SessionLocal
from app.services.workflow_orchestrator import WorkflowOrchestrator
from app.tasks.retry_policies import WORKFLOW_TASK_RETRY_KWARGS


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_kwargs=WORKFLOW_TASK_RETRY_KWARGS)
def run_workflow_job(self, job_id: int) -> None:
    db = SessionLocal()
    try:
        WorkflowOrchestrator(db).run(job_id)
    finally:
        db.close()



def enqueue_workflow_job(job_id: int):
    return run_workflow_job.delay(job_id)
