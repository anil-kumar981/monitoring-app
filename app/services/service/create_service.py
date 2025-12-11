from fastapi.responses import JSONResponse
from app.schemas.service_create import ServiceCreate, ServiceOut
from app.database.create_service_db import create_service_db
from sqlalchemy.ext.asyncio import AsyncSession

async def create_services(db: AsyncSession, services: list[ServiceCreate]):
    
    try:
        new_services = await create_service_db(db, services)
        
        return JSONResponse(status_code=201, content={"success":True,"message":"Services created successfully","services": new_services})
    except Exception as e:
        await db.rollback()
        return JSONResponse(status_code=500, content={"success":False,"message": str(e)})
    