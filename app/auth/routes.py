from fastapi import APIRouter, Depends
from passlib.hash import pbkdf2_sha256 as hash

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
    return [UserRead.from_orm(user) for user in db.scalars(select(User))]


@router.post("/")
async def add_user(
    user: UserWrite,
    db: Session = Depends(get_db),
) -> UserRead:
    out = User(**user.dict())
    db.add(out)
    db.commit()
    return UserRead.from_orm(out)


@router.post("/login")
async def login(login_attempt: UserWrite, db: Session = Depends(get_db)):
    user = db.scalars(
        select(User).where(User.email == login_attempt.email)
    ).one_or_none()
    if not user:
        raise bad_request(message="Incorrect username or password")
    # TODO hash this, we're just pretending for now
    hashed_password = login_attempt.password
    if hashed_password != user.password:
        raise bad_request(message="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}
