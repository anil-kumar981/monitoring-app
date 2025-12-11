from fastapi import APIRouter, Depends
from app.core.get_db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.service_update import ServiceUpdate
from app.services.service.update_service import update_service

router = APIRouter()

@router.patch("/update/{service_id}")
async def api_update_route(id:int,update_data:ServiceUpdate,
    db: AsyncSession = Depends(get_db)
):
   return await update_service(id, update_data, db)  # Assuming update_service is defined elsewhere