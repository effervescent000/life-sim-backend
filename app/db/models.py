from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.sql import Select
from typing import ClassVar, Generic, Type, TypeVar

from .database import Base


TOrmModel = TypeVar("TOrmModel", bound=Base)


# class MirrorModel(BaseModel, Generic[TOrmModel]):
#     orm: ClassVar[Type[TOrmModel]]  # type: ignore
#     use_scalars: ClassVar[bool] = True

#     def __init_subclass__(cls, *, orm: Type[TOrmModel], **kwargs) -> None:
#         if not orm:
#             raise TypeError("Must provide orm as a kwarg")

#         if orm.metadata is not Base.metadata:
#             raise TypeError(
#                 "Can't bind to a non-SQLA model or"
#                 " to a model not inheriting from Base."
#             )
#         super().__init_subclass__(**kwargs)

#         cls.orm = orm

#     class Config:
#         orm_mode = True

#     def to_orm(self) -> TOrmModel:
#         return self.orm(**self.dict())

#     @classmethod
#     def select_with_id(cls, id: int) -> Select:
#         return select(cls.orm).where(cls.orm.save_id == id)
