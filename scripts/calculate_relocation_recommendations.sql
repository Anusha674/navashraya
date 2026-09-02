DROP TABLE IF EXISTS village_relocation_recommendations;

CREATE TABLE village_relocation_recommendations AS

WITH village_distances AS (

    SELECT
        source.id AS source_id,
        source.name AS source_village,

        destination.id AS destination_id,
        destination.name AS destination_village,

        -- Centroid-to-centroid distance in kilometres
        ROUND(
            (
                ST_Distance(
                    ST_Transform(
                        ST_Centroid(source.geometry),
                        32643
                    ),
                    ST_Transform(
                        ST_Centroid(destination.geometry),
                        32643
                    )
                ) / 1000.0
            )::numeric,
            2
        ) AS distance_km,

        ds.population,
        ds.multihazard_score,
        ds.safety_score,
        ds.suitability_level

    FROM villages source

    CROSS JOIN villages destination

    JOIN village_safety_score ds
        ON ds.id = destination.id

    WHERE source.id <> destination.id
),

candidate_scores AS (

    SELECT
        *,

        -- Closer destination = higher score
        GREATEST(
            0,
            100 - (distance_km * 5)
        ) AS distance_score,

        -- Relocation score
        (
            0.60 * safety_score
            +
            0.25 * GREATEST(
                0,
                100 - (distance_km * 5)
            )
            +
            0.15 *
            CASE
                WHEN population <= 15000 THEN 100
                WHEN population <= 25000 THEN 70
                WHEN population <= 35000 THEN 40
                ELSE 20
            END
        ) AS relocation_score

    FROM village_distances

    WHERE suitability_level IN (
        'Highly Suitable',
        'Suitable'
    )
)

SELECT
    source_id,
    source_village,
    destination_id,
    destination_village,

    distance_km,
    population,
    multihazard_score,
    safety_score,
    suitability_level,

    ROUND(
        relocation_score::numeric,
        2
    ) AS relocation_score,

    ROW_NUMBER() OVER (
        PARTITION BY source_id
        ORDER BY relocation_score DESC
    ) AS recommendation_rank

FROM candidate_scores;