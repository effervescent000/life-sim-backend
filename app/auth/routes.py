from typing import Any

from fastapi import APIRouter, Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import pbkdf2_sha256 as passlib
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db.schema import User
from ..deps import get_db
from ..tags import Tags
from ..utils.http_utils import bad_request
from .helpers import make_access_token, sign_jwt
from .models import LoginForm, UserRead, UserWrite

router = APIRouter(prefix="/auth", tags=[Tags.users])
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.get("/")
async def get_users(db: Session = Depends(get_db)) -> list[UserRead]:
    return [UserRead.from_orm(user) for user in db.scalars(select(User)).all()]


@router.post("/")
async def add_user(
    user: UserWrite,
    db: Session = Depends(get_db),
) -> UserRead:
    out = User(
        **{**user.dict(exclude={"password"}), "password": passlib.hash(user.password)}
    )
    db.add(out)
    db.commit()
    return UserRead.from_orm(out)


@router.post("/login")
async def login(
    login_attempt: LoginForm, db: Session = Depends(get_db)
) -> dict[str, Any]:
    result = db.scalars(select(User).where(User.email == login_attempt.email)).first()
    if not result:
        raise bad_request(message="Incorrect username or password")
    if passlib.verify(login_attempt.password, str(result.password)) is False:
        raise bad_request(message="Incorrect username or password")
    user = UserRead.from_orm(result)
    return make_access_token(user=user, jwt=sign_jwt(user))
