from app.core.constants import DEFAULT_BRANCH_PREFIX, DEFAULT_COMMIT_PREFIX
from app.schemas.planner import PlannerOutput
from app.schemas.pr import PrPayload


class GitPrService:
    def generate_pr_payload(self, parsed_ticket: dict, planner_result: PlannerOutput) -> PrPayload:
        ticket_id = parsed_ticket["ticket_id"].lower().replace(" ", "-")
        slug = parsed_ticket["summary"].lower().replace(" ", "-")[:50]
        branch_name = f"{DEFAULT_BRANCH_PREFIX}/{ticket_id}-{slug}"
        commit_message = f"{DEFAULT_COMMIT_PREFIX}: fix {parsed_ticket['ticket_id']} email validation"
        pr_title = f"[{parsed_ticket['ticket_id']}] Fix missing email validation"
        pr_body = "\n".join(
            [
                f"## Summary\n{planner_result.task_summary}",
                "## Planned changes",
                *[f"- {step}" for step in planner_result.implementation_plan],
                "## Validation",
                *[f"- {item}" for item in planner_result.validation_checklist],
            ]
        )
        return PrPayload(
            branch_name=branch_name,
            commit_message=commit_message,
            pr_title=pr_title,
            pr_body=pr_body,
            pr_url=None,
            is_simulated=True,
        )
