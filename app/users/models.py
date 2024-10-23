from datetime import datetime
from typing import TYPE_CHECKING
import uuid
from sqlalchemy import JSON, ForeignKey, Integer, Column, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa
from sqlalchemy.sql import func
from app.database import Base



class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, index=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    fio: Mapped[str]
    telephone: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_administrator: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f"Пользователь {self.email}"


class RefreshSessionModel(Base):
    __tablename__ = "refresh_session"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    refresh_token: Mapped[uuid.UUID] = mapped_column(UUID, index=True)
    expires_in: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True), server_default=func.now()
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID, sa.ForeignKey("users.id", ondelete="CASCADE")
    )