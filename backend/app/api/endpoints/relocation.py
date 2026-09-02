from fastapi import APIRouter
from app.services.gis_service import GISService
from app.schemas.schemas import RelocationResponse

router = APIRouter()

@router.get("/relocation/{village}", response_model=RelocationResponse)
def get_relocation_recommendations(village: str):
    """
    Retrieves ranked safe destination village recommendations for a vulnerable source village.
    """
    return GISService.get_relocation_recommendations(village)
