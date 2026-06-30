from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI PDF Assistant 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }