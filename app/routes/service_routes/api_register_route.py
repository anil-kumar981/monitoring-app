from fastapi import APIRouter, Depends
from app.core.get_db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.service_create import ServiceCreate
from app.services.service.create_service import create_services

router = APIRouter()

@router.post("/register")
async def api_register_route(
    services: list[ServiceCreate],
    db: AsyncSession = Depends(get_db)
):
   return await create_services(db, services)
