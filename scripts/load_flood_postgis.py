import geopandas as gpd
import psycopg2
from pathlib import Path
from shapely import wkb
from shapely import force_2d

PROJECT_ROOT = Path(__file__).resolve().parent.parent

file = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wayanad_flood_zones.geojson"
)

print("Reading flood GeoJSON...")

gdf = gpd.read_file(file)

print("Features:", len(gdf))

# Remove Z dimension
gdf["geometry"] = gdf.geometry.apply(force_2d)

# Make sure CRS is WGS84
gdf = gdf.to_crs(epsg=4326)

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="navashraya",
    user="navashraya",
    password="navashraya"
)

cur = conn.cursor()

# Remove old table
cur.execute("""
DROP TABLE IF EXISTS flood_zones;
""")

# Create table
cur.execute("""
CREATE TABLE flood_zones (
    id SERIAL PRIMARY KEY,
    flood_id TEXT,
    flood_type TEXT,
    geometry geometry(MultiPolygon, 4326)
);
""")

print("Table created.")

# Insert features
for _, row in gdf.iterrows():

    geom_wkb = row.geometry.wkb

    cur.execute("""
        INSERT INTO flood_zones
        (flood_id, flood_type, geometry)
        VALUES (
            %s,
            %s,
            ST_GeomFromWKB(%s, 4326)
        );
    """, (
        str(row["flood_id"]),
        row["flood_type"],
        psycopg2.Binary(geom_wkb)
    ))

conn.commit()

cur.close()
conn.close()

print("\n===== FLOOD IMPORT COMPLETE =====")
print("Inserted:", len(gdf), "features")