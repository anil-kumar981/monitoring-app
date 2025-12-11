from datetime import datetime
from time import timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.core.base import Base
from sqlalchemy.orm import relationship

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    timeout = Column(Integer, default=5) 
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # ONE-TO-MANY RELATIONSHIP WITH SERVICELOG
    logs = relationship("ServiceLog", back_populates="service", cascade="all, delete-orphan")

    # ONE-TO-MANY RELATIONSHIP WITH SERVICEHEALTH
    health_checks = relationship("ServiceHealth", back_populates="service", cascade="all, delete-orphan")