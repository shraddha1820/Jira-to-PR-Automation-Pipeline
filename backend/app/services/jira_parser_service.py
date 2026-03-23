from app.schemas.job import ManualJobCreateRequest
from app.schemas.jira import JiraWebhookPayload


class JiraParserService:
    def parse_webhook_payload(self, payload: JiraWebhookPayload) -> dict:
        return {
            "ticket_id": payload.ticket_id,
            "summary": payload.fields.summary,
            "description": payload.fields.description,
            "acceptance_criteria": payload.fields.acceptance_criteria,
            "priority": payload.fields.priority,
            "labels": payload.fields.labels,
        }

    def parse_manual_payload(self, payload: ManualJobCreateRequest) -> dict:
        return {
            "ticket_id": payload.ticket_id,
            "summary": payload.summary,
            "description": payload.description,
            "acceptance_criteria": payload.acceptance_criteria,
            "priority": payload.priority,
            "labels": payload.labels,
        }
