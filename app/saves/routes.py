from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from typing import Any

from .models import SaveRead, SaveWrite, SaveBase
from ..deps import get_db, auth_required
from ..tags import Tags
from ..db.schema import Save as SaveORM
from ..db.queries import select_mirror_models, upsert_mirror_models
from ..utils.http_utils import bad_request

router = APIRouter(prefix="/saves", tags=[Tags.saves])


@router.get("/")
async def get_saves(
    db: Session = Depends(get_db), user: dict[str, Any] = Depends(auth_required)
):
    result = select_mirror_models(db, user["id"], SaveRead)
    return result


@router.post("/")
async def post_save(
    saves: list[SaveBase],
    db: Session = Depends(get_db),
    user: dict[str, Any] = Depends(auth_required),
):
    try:
        records = [SaveWrite(**save.dict(), user_id=user["id"]) for save in saves]
    except ValueError:
        return bad_request(message="Validation error")

    try:
        result = upsert_mirror_models(db, read_model=SaveRead, write_models=records)  # type: ignore
    except:
        return bad_request(message="Error upserting models")

    return result
