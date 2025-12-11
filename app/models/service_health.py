from sqlalchemy import Column,String,Float, DateTime, ForeignKey, Integer
from app.core.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class ServiceHealth(Base):
    __tablename__ = "service_health"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    last_status = Column(String, nullable=False)
    last_checked = Column(DateTime(timezone=True), default=lambda: datetime.now(datetime.timezone.utc))
    last_status_code = Column(Integer, nullable=False)
    last_response_time = Column(Float, nullable=False) 
    failure_count = Column(Integer, default=0)

    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    service = relationship("Service", back_populates="health_checks")