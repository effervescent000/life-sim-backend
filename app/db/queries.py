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
