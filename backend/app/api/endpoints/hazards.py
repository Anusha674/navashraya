from fastapi import APIRouter
from app.services.gis_service import GISService
from app.schemas.schemas import VillageHazardResponse

router = APIRouter()

@router.get("/village/{village}", response_model=VillageHazardResponse)
def get_village_hazard(village: str):
    """
    Retrieves current multi-hazard, flood, landslide metrics and data provenance for a village.
    """
    return GISService.get_village_hazard(village)
