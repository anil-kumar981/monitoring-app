from pydantic import BaseModel
from datetime import datetime

class ServiceLogOut(BaseModel):
    id: int
    service_id: int
    status_code: int | None
    response_time: float | None
    is_up: bool
    error_message: str | None
    created_at: datetime

    class Config:
        from_attributes = True
