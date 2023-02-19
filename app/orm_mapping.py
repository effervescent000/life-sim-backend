from typing import Type

from pydantic import BaseModel

from .auth.models import UserRead, UserWrite
from .db import schema
from .saves.models import SaveRead, SaveWrite


class ModelMapping(BaseModel):
    read: Type[BaseModel]
    write: Type[BaseModel]


ORM_MAP = {
    schema.User: ModelMapping(read=UserRead, write=UserWrite),
    schema.Save: ModelMapping(read=SaveRead, write=SaveWrite),
}
