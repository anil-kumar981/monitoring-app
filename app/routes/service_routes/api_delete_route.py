from fastapi import APIRouter, Depends
from app.core.get_db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.service.delete_service import delete_service
router = APIRouter()

@router.delete("/delete")
async def api_delete_route(id: int,db:AsyncSession = Depends(get_db)):
    return await delete_service(id, db)  # Assuming delete_services is defined elsewhere