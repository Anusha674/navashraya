DROP TABLE IF EXISTS village_flood_exposure;

CREATE TABLE village_flood_exposure AS

WITH village_areas AS (
    SELECT
        id,
        name AS village,
        geometry,
        ST_Area(
            ST_Transform(geometry, 32643)
        ) AS village_area
    FROM villages
),

flood_intersections AS (
    SELECT
        v.id,
        v.village,
        v.village_area,

        COALESCE(
            ST_Area(
                ST_Intersection(
                    ST_Transform(v.geometry, 32643),
                    ST_Transform(f.geometry, 32643)
                )
            ),
            0
        ) AS flood_area

    FROM village_areas v

    LEFT JOIN flood_zones f
        ON f.flood_type = 'Flood plain'
        AND ST_Intersects(v.geometry, f.geometry)
)

SELECT
    id,
    village,

    ROUND(
        (
            SUM(flood_area) /
            NULLIF(MAX(village_area), 0)
        )::numeric * 100,
        2
    ) AS flood_exposed_percent

FROM flood_intersections

GROUP BY
    id,
    village

ORDER BY
    flood_exposed_percent DESC;