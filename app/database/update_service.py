from sqlalchemy.ext.asyncio import AsyncSession
from app.models.service import Service
from app.schemas.service_update import ServiceUpdate

async def update_service_db(ext_service: Service, update_data: ServiceUpdate, db: AsyncSession):
    update_fields = update_data.model_dump(exclude_unset=True)
    
    for field, value in update_fields.items():
        setattr(ext_service, field, value)

    await db.commit()
    await db.refresh(ext_service)

    return ext_service