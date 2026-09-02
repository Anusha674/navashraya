DROP TABLE IF EXISTS village_landslide_exposure;

CREATE TABLE village_landslide_exposure AS

WITH village_areas AS (
    SELECT
        id,
        village,
        geometry,
        ST_Area(geometry::geography) AS village_area
    FROM wayanad_villages
),

intersections AS (
    SELECT
        v.id,
        v.village,
        l."Susceptibi",
        ST_Area(
            ST_Intersection(v.geometry, l.geometry)::geography
        ) AS affected_area
    FROM village_areas v
    JOIN wayanad_landslide l
        ON ST_Intersects(v.geometry, l.geometry)
),

area_summary AS (
    SELECT
        id,
        village,

        SUM(
            CASE
                WHEN "Susceptibi" = 'High'
                THEN affected_area
                ELSE 0
            END
        ) AS high_area,

        SUM(
            CASE
                WHEN "Susceptibi" = 'Moderate'
                THEN affected_area
                ELSE 0
            END
        ) AS moderate_area,

        SUM(
            CASE
                WHEN "Susceptibi" = 'Low'
                THEN affected_area
                ELSE 0
            END
        ) AS low_area

    FROM intersections
    GROUP BY id, village
)

SELECT
    v.id,
    v.village,

    ROUND(
        (
            COALESCE(a.high_area, 0) /
            v.village_area * 100
        )::numeric,
        2
    ) AS high_percent,

    ROUND(
        (
            COALESCE(a.moderate_area, 0) /
            v.village_area * 100
        )::numeric,
        2
    ) AS moderate_percent,

    ROUND(
        (
            COALESCE(a.low_area, 0) /
            v.village_area * 100
        )::numeric,
        2
    ) AS low_percent

FROM village_areas v
LEFT JOIN area_summary a
    ON v.id = a.id

ORDER BY v.village;