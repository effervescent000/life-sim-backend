from pydantic import BaseModel
from typing import Optional


class SaveBase(BaseModel, orm_mode=True):
    id: Optional[int] = None
    title: Optional[str]
    active: bool


class SaveRead(SaveBase):
    ...


class SaveWrite(SaveBase):
    user_id: int
