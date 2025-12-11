from sqlalchemy.ext.asyncio import AsyncSession
from app.models.service import Service

async def delete_service_db(data: Service, db: AsyncSession):
    await db.delete(data)
    await db.commit()
    return True
    
