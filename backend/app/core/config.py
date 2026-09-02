from pydantic import BaseModel
from typing import List

class Settings(BaseModel):
    PROJECT_NAME: str = "NAVASHRAYA"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Research-Backed AI + GIS Disaster Relocation Decision Support Platform"
    
    # Database Configuration
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "navashraya"
    POSTGRES_USER: str = "navashraya"
    POSTGRES_PASSWORD: str = "navashraya"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # CORS Configuration
    CORS_ORIGINS: List[str] = [
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "*"
    ]

settings = Settings()

