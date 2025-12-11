from typing import Optional
from pydantic import BaseModel, HttpUrl


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[HttpUrl] = None
    timeout: Optional[int] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None