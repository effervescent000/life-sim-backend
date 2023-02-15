from typing import Any

from ..schema import User
from ..auth.models import UserWrite


def user_factory(
    *, id=None, username=None, email=None, password=None
) -> dict[str, Any]:
    return {
        "id": id,
        "username": username,
        "email": email or "test@email.com",
        "password": password or "a really strong password",
    }


def world_base_state():
    out = []
    out.append(User(**UserWrite(**user_factory(username="some person")).dict()))
    return out
