from typing import Any
from passlib.hash import pbkdf2_sha256 as passlib

from ..schema import User
from ..auth.models import UserWrite


def user_factory(
    *, username=None, email=None, password=None, hash_password=False
) -> dict[str, Any]:
    return {
        "username": username,
        "email": email or "test@email.com",
        "password": passlib.hash(password or "a really strong password")
        if hash_password
        else (password or "a really strong password"),
    }


def world_base_state():
    out = []
    user = User(**UserWrite(**user_factory(username="some person")).dict())
    out.append(user)
    return out
