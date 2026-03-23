from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class GeneratedFile(Base):
    __tablename__ = "generated_files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), index=True)
    file_path: Mapped[str] = mapped_column(String(500))
    change_type: Mapped[str] = mapped_column(String(50), default="modified")
    before_content: Mapped[str | None] = mapped_column(Text, nullable=True)
    after_content: Mapped[str] = mapped_column(Text)
    diff_text: Mapped[str] = mapped_column(Text)
    applied_successfully: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    job = relationship("Job", back_populates="generated_files")
