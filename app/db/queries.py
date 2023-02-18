from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Sequence, Type, TypeVar, Any

from app.db.database import Base
from app.orm_mapping import ORM_MAP


TBaseModel = TypeVar("TBaseModel", bound=BaseModel)
TOrmModel = TypeVar("TOrmModel", bound=Base)


def select_models(
    db: Session,
    save_id: int,
    orm: Type[TOrmModel],
) -> list[BaseModel]:
    selection = select(orm).where(orm.save_id == save_id)
    result = db.scalars(selection).all()
    out = [ORM_MAP[orm].read.from_orm(r) for r in result]
    return out


def upsert_models(
    db: Session, orm: Type[TOrmModel], data: Sequence[BaseModel]
) -> list[Any]:
    mutations: list[Any] = []

    for x in data:
        mutated = db.merge(orm(**x.dict()))
        db.commit()
        mutations.append(ORM_MAP[orm].read.from_orm(mutated))
    return mutations
