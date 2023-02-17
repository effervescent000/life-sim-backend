from jwt import encode, decode

from ..config import settings

from .models import UserRead


def make_access_token(user: UserRead, jwt: str):
    return {"access_token": jwt, "user": user, "token_type": "bearer"}


def sign_jwt(value: UserRead):
    return encode(value.dict(), settings.jwt_secret, algorithm=settings.jwt_algo)


def decode_jwt(jwt: str):
    return decode(jwt, key=settings.jwt_secret, algorithms=[settings.jwt_algo])
