def create_user(payload: dict) -> dict:
    email = payload["email"]
    return {"ok": True, "email": email}
