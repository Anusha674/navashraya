import geopandas as gpd
from sqlalchemy import create_engine

# Landslide shapefile
input_file = r"D:\navashraya\data\raw\landslide\Wayanad\Wayanad_GSI_LS.shp"

# Database
DATABASE_URL = "postgresql://navashraya:navashraya@localhost:5432/navashraya"

engine = create_engine(DATABASE_URL)

print("Reading landslide data...")

gdf = gpd.read_file(input_file)

print("Features found:", len(gdf))

# Convert to WGS84 to match village data
gdf = gdf.to_crs(epsg=4326)

print("CRS:", gdf.crs)

# Load into PostGIS
print("Loading into PostGIS...")

gdf.to_postgis(
    name="wayanad_landslide",
    con=engine,
    if_exists="replace",
    index=False
)

print("SUCCESS!")
print("Loaded", len(gdf), "landslide zones.")