from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.session import engine

from app.core.base import Base
from app.routes.service_routes.api_delete_route import router as api_delete_route
from app.routes.service_routes.api_register_route import router as api_register_route
from app.routes.service_routes.api_update_route import router as api_update_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code can be added here
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  
    yield
    # Shutdown code can be added here

app = FastAPI(lifespan=lifespan)

def create_app():
    app.include_router(api_register_route, prefix="/services", tags=["Create Service"])
    app.include_router(api_delete_route, prefix="/services", tags=["Delete Service"])
    app.include_router(api_update_route, prefix="/services", tags=["Update Service"])
    return app