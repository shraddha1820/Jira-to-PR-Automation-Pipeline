from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    source: Mapped[str] = mapped_column(String(50), default="manual")
    status: Mapped[str] = mapped_column(String(50), default="queued", index=True)
    jira_ticket_id: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
    raw_payload: Mapped[str] = mapped_column(Text)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    parsed_ticket = relationship("ParsedTicket", back_populates="job", uselist=False, cascade="all, delete-orphan")
    planner_result = relationship("PlannerResult", back_populates="job", uselist=False, cascade="all, delete-orphan")
    generated_files = relationship("GeneratedFile", back_populates="job", cascade="all, delete-orphan")
    validation_results = relationship("ValidationResult", back_populates="job", cascade="all, delete-orphan")
    pr_metadata = relationship("PrMetadata", back_populates="job", uselist=False, cascade="all, delete-orphan")
    status_history = relationship("WorkflowStatusHistory", back_populates="job", cascade="all, delete-orphan")
