from pydantic import BaseModel
from datetime import datetime

class ServiceHealthOut(BaseModel):
    service_id: int
    last_check: datetime
    last_status: bool
    last_status_code: int | None
    last_response_time: float | None
    failure_count: int

    class Config:
        from_attributes = True
