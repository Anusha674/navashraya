DROP TABLE IF EXISTS village_safety_score;

CREATE TABLE village_safety_score AS

WITH scored AS (

    SELECT
        v.id,
        v.name AS village,
        v.population,
        mh.multihazard_score,

        -- Lower hazard = better
        (100 - mh.multihazard_score) AS hazard_safety,

        -- Population capacity proxy
        CASE
            WHEN v.population <= 15000 THEN 100
            WHEN v.population <= 25000 THEN 70
            WHEN v.population <= 35000 THEN 40
            ELSE 20
        END AS capacity_score

    FROM villages v

    JOIN village_multihazard_score mh
        ON LOWER(TRIM(v.name))
         = LOWER(TRIM(mh.village))
)

SELECT
    id,
    village,
    population,
    multihazard_score,

    ROUND(hazard_safety::numeric, 2) AS hazard_safety,

    capacity_score,

    ROUND(
        (
            0.70 * hazard_safety
            +
            0.30 * capacity_score
        )::numeric,
        2
    ) AS safety_score,

    CASE
        WHEN (
            0.70 * hazard_safety
            +
            0.30 * capacity_score
        ) >= 70
            THEN 'Highly Suitable'

        WHEN (
            0.70 * hazard_safety
            +
            0.30 * capacity_score
        ) >= 55
            THEN 'Suitable'

        WHEN (
            0.70 * hazard_safety
            +
            0.30 * capacity_score
        ) >= 40
            THEN 'Moderately Suitable'

        ELSE 'Low Suitability'
    END AS suitability_level

FROM scored;