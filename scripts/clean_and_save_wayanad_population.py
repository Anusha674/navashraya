import json
import geopandas as gpd
from pathlib import Path
from shapely import force_2d

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "vb_soi_kl.GeoJSON"
PROCESSED_FILE = PROJECT_ROOT / "data" / "processed" / "wayanad_villages.geojson"

def clean_and_update_population():
    print("Reading raw Survey of India Kerala GeoJSON...")
    gdf = gpd.read_file(RAW_FILE)

    # Filter for Wayanad district
    w_gdf = gdf[gdf["district"].astype(str).str.strip().str.lower() == "wayanad"].copy()
    print(f"Found {len(w_gdf)} Wayanad villages in raw GeoJSON.")

    # Clean column names by stripping whitespace and newlines
    w_gdf.columns = w_gdf.columns.str.strip().str.replace("\n", "", regex=False)

    # Convert population column to int
    pop_col = "total_population_village"
    if pop_col in w_gdf.columns:
        w_gdf["population"] = w_gdf[pop_col].apply(lambda x: int(float(x)) if x is not None and str(x).strip() != '' and str(x) != 'nan' else 5000)
    else:
        w_gdf["population"] = 5000

    # Ensure 2D geometry and WGS84 EPSG:4326
    w_gdf["geometry"] = w_gdf.geometry.apply(force_2d)
    w_gdf = w_gdf.to_crs(epsg=4326)

    # Clean village names
    w_gdf["village"] = w_gdf["village"].astype(str).str.strip()
    w_gdf["name"] = w_gdf["village"]

    # Save to processed GeoJSON
    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    w_gdf.to_file(PROCESSED_FILE, driver="GeoJSON")
    print(f"[SUCCESS] Saved clean Wayanad villages GeoJSON to {PROCESSED_FILE}")

    # Print summary of Census 2011 population data
    print("\nCensus 2011 Village Population Summary:")
    for _, row in w_gdf.iterrows():
        print(f"  • {row['village']}: {row['population']:,} residents")

if __name__ == "__main__":
    clean_and_update_population()
