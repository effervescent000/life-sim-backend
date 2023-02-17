from sqlalchemy import select
from sqlalchemy.sql import Select
from typing import Optional

from ..db.models import MirrorModel
from ..db.schema import Save as SaveORM


class SaveBase(MirrorModel[SaveORM], orm=SaveORM):
    id: Optional[int] = None
    title: Optional[str]
    active: bool

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs, orm=cls.orm)

    @classmethod
    def select_with_id(cls, id: int) -> Select:
        return select(cls.orm).where(cls.orm.user_id == id)


class SaveRead(SaveBase):
    ...


class SaveWrite(SaveBase):
    user_id: int
