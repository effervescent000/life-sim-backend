from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel, orm_mode=True):
    email: str
    name: Optional[str]


class UserRead(UserBase):
    id: int


class UserWrite(UserBase):
    hashed_password: str
