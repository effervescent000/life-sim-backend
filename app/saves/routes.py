from fastapi import APIRouter, Depends
from sqlalchemy import select

from sqlalchemy.orm import Session
from typing import Any, Sequence

from .models import SaveRead, SaveWrite, SaveBase
from ..deps import get_db, auth_required
from ..tags import Tags
from ..db.schema import Save as SaveORM
from ..utils.http_utils import bad_request

from app.db.queries import upsert_models

router = APIRouter(prefix="/saves", tags=[Tags.saves])


@router.get("/")
async def get_saves(
    db: Session = Depends(get_db), user: dict[str, Any] = Depends(auth_required)
) -> list[SaveRead]:
    selection = select(SaveORM).where(SaveORM.user_id == user["id"])
    result = db.scalars(selection).all()
    out = [SaveRead.from_orm(r) for r in result]
    return out


@router.post("/")
async def post_save(
    saves: Sequence[SaveBase],
    db: Session = Depends(get_db),
    user: dict[str, Any] = Depends(auth_required),
) -> Sequence[SaveRead]:
    try:
        records = [SaveWrite(**save.dict(), user_id=user["id"]) for save in saves]
    except ValueError as e:
        return bad_request(message=f"Validation error: {e}")

    try:
        result: list[SaveRead] = upsert_models(db, orm=SaveORM, data=records)
    except:
        return bad_request(message="Error upserting models")

    return result
