import json
import pandas as pd
import geopandas as gpd
from pathlib import Path
from typing import Tuple, Dict, Any
from app.gis.feature_extractor import GISFeatureExtractor

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
GEOJSON_FILE = PROJECT_ROOT / "data" / "processed" / "wayanad_villages.geojson"
OUTPUT_CSV = PROJECT_ROOT / "data" / "processed" / "wayanad_ml_features.csv"

class GISPipeline:
    """
    GIS Preprocessing Pipeline for Wayanad Habitation Relocation System.
    """

    def __init__(self, geojson_path: Path = GEOJSON_FILE):
        self.geojson_path = geojson_path

    def load_spatial_data(self) -> gpd.GeoDataFrame:
        """
        Loads Wayanad villages spatial GeoJSON.
        """
        if not self.geojson_path.exists():
            raise FileNotFoundError(f"Spatial data file not found at {self.geojson_path}")
        gdf = gpd.read_file(self.geojson_path)
        if gdf.crs is None or gdf.crs.to_epsg() != 4326:
            gdf = gdf.to_crs(epsg=4326)
        return gdf

    def build_feature_dataset(self) -> pd.DataFrame:
        """
        Processes all village geometries and builds tabular ML feature matrix.
        """
        gdf = self.load_spatial_data()
        records = []

        for idx, row in gdf.iterrows():
            vname = row.get("village") or row.get("name") or f"Village_{idx}"
            geom = row.geometry
            if geom is None:
                continue

            features = GISFeatureExtractor.process_village_features(vname, geom)
            
            # Target binary classification proxy (1 = High/Critical Landslide Susceptibility, 0 = Low/Moderate)
            # High slope (>28 deg) & high elevation (>950m) represent high susceptibility zones in Wayanad
            features["landslide_label"] = 1 if (features["slope"] > 25.0 and features["elevation"] > 900.0) else 0
            records.append(features)

        df = pd.DataFrame(records)
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"[GISPipeline] Successfully built and saved {len(df)} feature records to {OUTPUT_CSV}")
        return df

if __name__ == "__main__":
    pipeline = GISPipeline()
    pipeline.build_feature_dataset()
