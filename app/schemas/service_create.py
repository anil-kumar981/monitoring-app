from typing import Optional
from pydantic import BaseModel, HttpUrl

class ServiceCreate(BaseModel):
    name: str
    url: HttpUrl
    timeout: Optional[int] = 5
    description: Optional[str] = None
    is_active: Optional[bool] = True

class ServiceOut(ServiceCreate):
    id: int

    class Config:
        from_attributes = True