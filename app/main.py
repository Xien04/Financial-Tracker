from fastapi import FastAPI

from app.api.routes import api_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)
app.include_router(api_router, prefix="/api")
