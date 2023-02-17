from jwt import encode, decode

from ..config import settings

from .models import UserRead


def make_access_token(user: UserRead, jwt: bytes):
    return {"access_token": jwt, "user": user, "token_type": "bearer"}


def sign_jwt(value: int):
    return encode({"id": value}, settings.jwt_secret)


def decode(jwt: str):
    return decode(jwt)
