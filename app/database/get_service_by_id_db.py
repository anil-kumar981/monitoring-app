from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.service import Service

async def get_by_id_db(service_id: int, db: AsyncSession):
    res = await db.execute(select(Service).where(Service.id == service_id))
    return res.scalar_one_or_none()