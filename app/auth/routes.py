from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select

from .models import UserRead, UserWrite
from ..deps import get_db
from ..tags import Tags
from ..schema import User
from ..utils.http_utils import bad_request

router = APIRouter(prefix="/auth", tags=[Tags.users])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.get("/")
async def get_users(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> list[UserRead]:
    stmnt = select(User)
    return [UserRead.from_orm(user) for user in db.scalars(stmnt)]


@router.post("/")
async def add_user(
    user: UserWrite,
    db: Session = Depends(get_db),
) -> UserRead:
    out = User(**user.dict())
    db.add(out)
    db.commit()
    return UserRead.from_orm(out)


@router.post("/token")
async def login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.scalars(
        select(User).where(User.email == form_data.username)
    ).one_or_none()
    if not user:
        raise bad_request(message="Incorrect username or password")
    user = UserWrite(**user.dict())
    hashed_password = form_data.password
    if hashed_password != user.hashed_password:
        raise bad_request(message="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}
