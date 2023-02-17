import json
from fastapi import Request, HTTPException

from .db.database import SessionLocal
from .auth.models import UserRead


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def auth_required(request: Request):
    cookie = request.cookies
    try:
        user = json.loads(cookie.get("user"))
        yield user
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")
