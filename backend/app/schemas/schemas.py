from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
from enum import Enum

class DataStatus(str, Enum):
    REAL = "REAL"
    DERIVED = "DERIVED"
    PROXY = "PROXY"
    SYNTHETIC = "SYNTHETIC"

class DataProvenanceInfo(BaseModel):
    source: str
    status: DataStatus
    notes: Optional[str] = None

class VillageHazardResponse(BaseModel):
    village: str
    population: Optional[int] = None
    multihazard_score: Optional[float] = None
    safety_score: Optional[float] = None
    suitability_level: Optional[str] = None
    flood_exposed_percent: float = 0.0
    landslide_score: float = 0.0
    hazard_level: str
    provenance: Dict[str, DataStatus] = Field(
        default_factory=lambda: {
            "village_boundaries": DataStatus.REAL,
            "population": DataStatus.REAL,
            "landslide_susceptibility": DataStatus.DERIVED,
            "flood_exposure": DataStatus.DERIVED,
            "multihazard_fusion": DataStatus.DERIVED
        }
    )

class RelocationItem(BaseModel):
    rank: int
    destination: str
    distance_km: float
    population: int
    multihazard_score: float
    safety_score: float
    relocation_score: float
    suitability_level: str
    provenance: Dict[str, DataStatus] = Field(
        default_factory=lambda: {
            "distance_calculation": DataStatus.DERIVED,
            "relocation_score": DataStatus.DERIVED
        }
    )

class RelocationResponse(BaseModel):
    source_village: str
    recommendations: List[RelocationItem]

class GeoJSONProperties(BaseModel):
    id: int
    name: str
    population: Optional[int] = None

class GeoJSONFeature(BaseModel):
    type: str = "Feature"
    geometry: Dict[str, Any]
    properties: GeoJSONProperties

class GeoJSONFeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: List[GeoJSONFeature]
