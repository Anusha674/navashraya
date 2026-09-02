import geopandas as gpd
import psycopg2
from pathlib import Path
from shapely import force_2d

PROJECT_ROOT = Path(__file__).resolve().parent.parent

file = PROJECT_ROOT / "data" / "processed" / "wayanad_villages.geojson"

print("Reading Wayanad villages...")

gdf = gpd.read_file(file)

print("Features:", len(gdf))
print("CRS:", gdf.crs)

# Make sure geometry is 2D
gdf["geometry"] = gdf.geometry.apply(force_2d)

# Convert to WGS84
gdf = gdf.to_crs(epsg=4326)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="navashraya",
    user="navashraya",
    password="navashraya"
)

cur = conn.cursor()

# Recreate villages table
cur.execute("""
DROP TABLE IF EXISTS villages;
""")

cur.execute("""
CREATE TABLE villages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150),
    population INTEGER,
    geometry geometry(MultiPolygon, 4326)
);
""")

print("Table created.")

for _, row in gdf.iterrows():

    population = row.get("total_population_village")

    if population is not None:
        population = int(population)

    cur.execute("""
        INSERT INTO villages
        (name, population, geometry)
        VALUES (
            %s,
            %s,
            ST_Multi(
                ST_GeomFromWKB(%s, 4326)
            )
        );
    """, (
        row["village"],
        population,
        psycopg2.Binary(row.geometry.wkb)
    ))

conn.commit()

cur.close()
conn.close()

print("\n===== VILLAGES IMPORT COMPLETE =====")
print("Inserted:", len(gdf), "villages")