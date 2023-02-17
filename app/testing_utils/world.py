from typing import Any
from passlib.hash import pbkdf2_sha256 as passlib

from ..db.schema import User


def user_factory(
    *, username=None, email=None, password=None, hash_password=False, id
) -> dict[str, Any]:
    return {
        "id": id,
        "username": username,
        "email": email or "test@email.com",
        "password": passlib.hash(password or "a really strong password")
        if hash_password
        else (password or "a really strong password"),
    }


def save_factory(*, title=None, active=None, user_id, id):
    return {
        "id": id,
        "title": title or "Untitled",
        "active": active or False,
        "user_id": user_id,
    }


def world_base_state():
    out = []
    user = User(**user_factory(username="some person", hash_password=True, id=1))
    out.append(user)
    return out
