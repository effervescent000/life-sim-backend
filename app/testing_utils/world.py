from typing import Any, Optional
from passlib.hash import pbkdf2_sha256 as passlib

from ..db.schema import User, Save
from ..auth.helpers import sign_jwt
from ..auth.models import UserRead


def user_factory(
    *,
    username: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None,
    hash_password: bool = False,
    id: int,
) -> dict[str, Any]:
    return {
        "id": id,
        "username": username,
        "email": email or "test@email.com",
        "password": passlib.hash(password or "a really strong password")
        if hash_password
        else (password or "a really strong password"),
    }


def save_factory(
    *, title: Optional[str] = None, active: bool = False, user_id: int, id: int
) -> dict[str, Any]:
    return {
        "id": id,
        "title": title or "Untitled",
        "active": active or False,
        "user_id": user_id,
    }


USER_PRIMARY = user_factory(username="some person", hash_password=True, id=1)
USER_SECONDARY = user_factory(username="a different user", hash_password=True, id=10)
SAVE_PRIMARY = save_factory(id=1, user_id=USER_PRIMARY["id"])
SAVE_SECONDARY = save_factory(id=10, user_id=USER_SECONDARY["id"])


def world_base_state():
    out = [User(**USER_PRIMARY), Save(**SAVE_PRIMARY), Save(**SAVE_SECONDARY)]
    return out


AUTH_HEADERS_USER_PRIMARY = {
    "Authorization": f"Bearer {sign_jwt(UserRead(**USER_PRIMARY))}"
}
