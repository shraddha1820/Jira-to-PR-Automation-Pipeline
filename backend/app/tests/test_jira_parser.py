from app.schemas.jira import JiraFields, JiraWebhookPayload
from app.services.jira_parser_service import JiraParserService


def test_parse_webhook_payload_extracts_expected_fields():
    payload = JiraWebhookPayload(
        ticket_id="DEMO-101",
        fields=JiraFields(
            summary="Fix email validation",
            description="Email missing returns 500",
            priority="High",
            labels=["bug"],
            acceptance_criteria=["Return 400"],
        ),
    )
    result = JiraParserService().parse_webhook_payload(payload)
    assert result["ticket_id"] == "DEMO-101"
    assert result["summary"] == "Fix email validation"
    assert result["acceptance_criteria"] == ["Return 400"]
