import time

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_mixin

from .database import Base


@declarative_mixin
class WithAutoIntPK:
    """SQLA Mixin for a simple int column ID."""

    id = Column(Integer, primary_key=True, autoincrement=True)


@declarative_mixin
class WithAuditTimes:
    created_at = Column(Integer, default=lambda: int(time.time()))
    updated_at = Column(Integer, onupdate=lambda: int(time.time()))


class User(Base, WithAutoIntPK, WithAuditTimes):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    username = Column(String)
    password = Column(String)

    saves = relationship("Save", back_populates="user")


class Save(Base, WithAuditTimes, WithAutoIntPK):
    __tablename__ = "saves"

    title = Column(String, default="Untitled")

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="saves")
