from fastapi import APIRouter
from typing import List
from app.services.gis_service import GISService
from app.schemas.schemas import GeoJSONFeatureCollection

router = APIRouter()

@router.get("/villages", response_model=List[str])
def get_villages():
    """
    Returns a sorted list of all village names in Wayanad.
    """
    return GISService.get_all_villages()

@router.get("/villages/geojson", response_model=GeoJSONFeatureCollection)
def get_villages_geojson():
    """
    Returns GeoJSON FeatureCollection of all village boundaries with properties.
    """
    return GISService.get_villages_geojson()
