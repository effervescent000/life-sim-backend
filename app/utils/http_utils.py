from fastapi import HTTPException


def bad_request(message: str, status_code: int = 400):
    return HTTPException(status_code=status_code, detail=message)
