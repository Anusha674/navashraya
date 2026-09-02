import geopandas as gpd
from sqlalchemy import create_engine

# --------------------------------------------------
# 1. File location
# --------------------------------------------------

input_file = r"D:\navashraya\data\processed\wayanad_villages.geojson"

# --------------------------------------------------
# 2. Database connection
# --------------------------------------------------

DATABASE_URL = "postgresql://navashraya:navashraya@localhost:5432/navashraya"

engine = create_engine(DATABASE_URL)

# --------------------------------------------------
# 3. Read Wayanad GeoJSON
# --------------------------------------------------

print("Reading Wayanad data...")

gdf = gpd.read_file(input_file)

print("Villages found:", len(gdf))

# --------------------------------------------------
# 4. Clean column names
# --------------------------------------------------

gdf.columns = (
    gdf.columns
    .str.strip()
    .str.replace("\n", "", regex=False)
)

# --------------------------------------------------
# 5. Make sure geometry is WGS84
# --------------------------------------------------

gdf = gdf.to_crs(epsg=4326)

# --------------------------------------------------
# 6. Load into PostGIS
# --------------------------------------------------

print("Loading villages into PostgreSQL/PostGIS...")

gdf.to_postgis(
    name="wayanad_villages",
    con=engine,
    if_exists="replace",
    index=False
)

print("SUCCESS!")
print("Loaded", len(gdf), "villages into PostGIS.")