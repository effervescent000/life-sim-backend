from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from .models import UserRead, UserWrite
from ..deps import get_db
from ..tags import Tags
from ..schema import User

router = APIRouter(prefix="/users", tags=[Tags.users])


@router.get("/")
async def get_users(db: Session = Depends(get_db)) -> list[UserRead]:
    stmnt = select(User)
    return [UserRead.from_orm(user) for user in db.scalars(stmnt)]


@router.post("/new")
async def add_user(
    user: UserWrite,
    db: Session = Depends(get_db),
) -> UserRead:
    out = User(**user.dict())
    db.add(out)
    db.commit()
    return UserRead.from_orm(out)
