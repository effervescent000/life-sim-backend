from typing import Generic, Type, TypeVar
from pydantic import BaseModel
from .db import schema
from .auth.models import UserRead, UserWrite

# TBaseModel = TypeVar("TBaseModel", bound=BaseModel)


class ModelMapping(BaseModel):
    read: Type[BaseModel]
    write: Type[BaseModel]


ORM_MAP = {schema.User: ModelMapping(read=UserRead, write=UserWrite)}
