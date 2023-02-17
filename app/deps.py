from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer

from .db.database import SessionLocal
from .auth.models import UserRead
from .auth.helpers import decode_jwt


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def auth_required(request: Request):
    if not request.headers:
        raise HTTPException(status_code=401, detail="Not authorized")
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Not authorized")
    scheme, token = auth_header.split(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(status_code=400, detail="Invalid header")
    try:
        return decode_jwt(token)
    except:
        raise HTTPException(status_code=400, detail="Invalid token")
