from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from sqlalchemy import select

from .models import SaveRead, SaveWrite
from ..deps import get_db, auth_required
from ..tags import Tags
from ..db.schema import Save as SaveORM
from ..db.queries import select_mirror_models
from ..utils.http_utils import bad_request

router = APIRouter(prefix="/saves", tags=[Tags.saves])


@router.get("/")
async def get_saves(db: Session = Depends(get_db), user=Depends(auth_required)):
    return "something here"
