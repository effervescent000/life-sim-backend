from sqlalchemy.orm import Session
from typing import Type, TypeVar, Any

from .models import MirrorModel

TMirrorModel = TypeVar("TMirrorModel", bound=MirrorModel[Any])


def select_mirror_models(
    db: Session, id: int, model: Type[TMirrorModel]
) -> list[TMirrorModel]:
    selection = model.select_with_id(id)
    records: Any = db.execute(selection)
    if model.use_scalars:
        records = records.scalars()
    return [model.from_orm(record) for record in records.all()]


def upsert_mirror_models(
    db: Session, read_model: Type[TMirrorModel], write_models: list[TMirrorModel]
) -> list[TMirrorModel]:
    mutations: list[TMirrorModel] = []

    for model in write_models:
        mutated = db.merge(model.to_orm())
        db.commit()
        mutations.append(read_model.from_orm(mutated))

    return mutations
