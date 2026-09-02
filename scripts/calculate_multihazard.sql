DROP TABLE IF EXISTS village_multihazard_score;

CREATE TABLE village_multihazard_score AS

SELECT
    l.id,
    l.village,

    l.susceptibility_score AS landslide_score,

    f.flood_exposed_percent AS flood_score,

    ROUND(
        (
            0.5 * l.susceptibility_score
            +
            0.5 * f.flood_exposed_percent
        )::numeric,
        2
    ) AS multihazard_score,

    CASE
        WHEN (
            0.5 * l.susceptibility_score
            +
            0.5 * f.flood_exposed_percent
        ) >= 60
            THEN 'Critical'

        WHEN (
            0.5 * l.susceptibility_score
            +
            0.5 * f.flood_exposed_percent
        ) >= 40
            THEN 'High'

        WHEN (
            0.5 * l.susceptibility_score
            +
            0.5 * f.flood_exposed_percent
        ) >= 20
            THEN 'Moderate'

        ELSE 'Low'
    END AS hazard_level

FROM village_landslide_score l

JOIN village_flood_exposure f
    ON LOWER(TRIM(l.village))
     = LOWER(TRIM(f.village));