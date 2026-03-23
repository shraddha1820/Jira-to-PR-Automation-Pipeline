from app.api import create_user


def test_valid_email_succeeds():
    response = create_user({"email": "demo@example.com"})
    assert response["ok"] is True
    assert response["email"] == "demo@example.com"
