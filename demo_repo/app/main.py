from app.api import create_user


def handler(payload: dict) -> dict:
    return create_user(payload)
