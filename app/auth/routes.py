from fastapi import APIRouter, Depends
from passlib.hash import pbkdf2_sha256 as passlib

from sqlalchemy.orm import Session
from sqlalchemy import select

from .models import UserRead, UserWrite
from ..deps import get_db
from ..tags import Tags
from ..schema import User
from ..utils.http_utils import bad_request

router = APIRouter(prefix="/auth", tags=[Tags.users])
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


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
async def login(login_attempt: UserWrite, db: Session = Depends(get_db)):
    user = db.scalars(select(User).where(User.email == login_attempt.email)).first()
    if not user:
        raise bad_request(message="Incorrect username or password")
    if passlib.verify(login_attempt.password, str(user.password)) is False:
        raise bad_request(message="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}
