from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PrMetadata(Base):
    __tablename__ = "pr_metadata"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), unique=True, index=True)
    branch_name: Mapped[str] = mapped_column(String(255))
    commit_message: Mapped[str] = mapped_column(String(255))
    pr_title: Mapped[str] = mapped_column(String(255))
    pr_body: Mapped[str] = mapped_column(Text)
    pr_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    is_simulated: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    job = relationship("Job", back_populates="pr_metadata")
