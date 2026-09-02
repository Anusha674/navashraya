from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import villages, hazards, relocation

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "running"
    }

# Mount API Routers
app.include_router(villages.router, prefix="/api", tags=["Villages"])
app.include_router(hazards.router, prefix="/api", tags=["Hazards"])
app.include_router(relocation.router, prefix="/api", tags=["Relocation"])