from dataclasses import dataclass


@dataclass
class UserPayload:
    email: str | None = None
