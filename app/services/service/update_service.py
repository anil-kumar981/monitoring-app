from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.get_service_by_id_db import get_by_id_db
from app.database.update_service import update_service_db
from app.schemas.service_update import ServiceUpdate

async def update_service(service_id: int, update_data: ServiceUpdate, db: AsyncSession):
    try:
        if not service_id or service_id < 0:
            return JSONResponse(status_code=400,
                                content={"success": False, "message": "Invalid service ID"})

        update_fields = update_data.model_dump(exclude_unset=True)
        if not update_fields:
            return JSONResponse(status_code=400,
                                content={"success": False, "message": "No update data provided"})

        existing_service = await get_by_id_db(service_id, db)

        if not existing_service:
            return JSONResponse(status_code=404,
                                content={"success": False, "message": "Service not found"})

        # Update the DB entity
        result = await update_service_db(existing_service, update_data, db)

        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Service updated successfully",
                "service": result.as_dict()
            }
        )

    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"success": False, "message": str(e)})