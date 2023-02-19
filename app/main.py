from fastapi import FastAPI

from .auth import routes as auth_routes
from .saves import routes as saves_routes

# from .database import Base, engine

# Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_routes.router)
app.include_router(saves_routes.router)
