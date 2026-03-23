from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint_returns_ok():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"


def test_manual_trigger_creates_job():
    payload = {
        "ticket_id": "DEMO-101",
        "summary": "Fix missing email validation",
        "description": "Missing email returns 500",
        "acceptance_criteria": ["Return 400"],
        "priority": "High",
        "labels": ["bug"],
    }
    response = client.post("/api/v1/jira/trigger", json=payload)
    assert response.status_code == 202
    data = response.json()
    assert "job_id" in data
    assert data["status"] == "queued"
