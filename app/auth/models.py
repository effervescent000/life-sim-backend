from typing import Optional
from pydantic import BaseModel

from ..db.models import MirrorModel
from ..db.schema import User as UserORM


class UserBase(MirrorModel[UserORM], orm=UserORM):
    email: str
    username: Optional[str] = None

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs, orm=cls.orm)


class UserRead(UserBase):
    id: int


class UserWrite(UserBase):
    password: str


class LoginForm(BaseModel):
    email: str
    password: str
