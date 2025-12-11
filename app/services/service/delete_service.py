from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.delete_service_db import delete_service_db
from app.database.get_service_by_id_db import get_by_id_db

async def delete_service(service_id: int, db: AsyncSession):
    try:
        if not service_id or service_id < 0:
            return JSONResponse(content={"success":False,"message":"Invalid service ID"}, status_code=400)
        
        ext_service = await get_by_id_db(service_id, db)
        
        if ext_service:
            await delete_service_db(ext_service, db)
        else:
            return JSONResponse(content={"success":False,"message":"Service not found"}, status_code=404)
        
        return JSONResponse(content={"message": "Service deleted successfully"} , status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"success":False,"message": str(e)})
