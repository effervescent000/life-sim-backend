from typing import Any

from ..schema import User
from ..auth.models import UserWrite


def user_factory(*, username=None, email=None, password=None) -> dict[str, Any]:
    return {
        "username": username,
        "email": email or "test@email.com",
        "password": password or "a really strong password",
    }


def world_base_state():
    out = []
    user = User(**UserWrite(**user_factory(username="some person")).dict())
    out.append(user)
    return out
