from typing import Optional
from pydantic import BaseModel

from ..db.models import MirrorModel
from ..db.schema import User as UserORM


class UserBase(BaseModel, orm_mode=True):
    email: str
    username: Optional[str] = None


class UserRead(UserBase):
    id: int


class UserWrite(UserBase):
    password: str


class LoginForm(BaseModel):
    email: str
    password: str
