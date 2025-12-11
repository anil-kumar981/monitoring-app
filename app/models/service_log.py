import datetime
from sqlalchemy import Boolean,String, Column, Float, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.core.base import Base


class ServiceLog(Base):
    __tablename__ = "service_logs"

    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(datetime.timezone.utc))
    is_up = Column(Boolean, nullable=False)  # 1 for up, 0 for down
    response_time = Column(Float, nullable=False)  # in milliseconds
    error_message = Column(String, nullable=True)

    service = relationship("Service", back_populates="logs")