from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.service_create import ServiceCreate
from app.models.service import Service

async def create_service_db(db: AsyncSession, service: list[ServiceCreate]) :
    new_services = [
            Service(
            name=s.name,
            url=str(s.url),
            is_active=s.is_active,
            description=s.description
        )
        for s in service
    ]
    db.add_all(new_services)
    await db.commit()
    for s in new_services:
        await db.refresh(s)
    return new_services