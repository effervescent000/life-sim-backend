from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel, orm_mode=True):
    email: str
    username: Optional[str]


class UserRead(UserBase):
    id: int


class UserWrite(UserBase):
    password: str


class LoginForm(BaseModel):
    email: str
    password: str
