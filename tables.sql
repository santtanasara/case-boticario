CREATE OR REPLACE TABLE botica-teste.dataspotify.datahackers_all_episodes AS
WITH datahackers_table AS (
  SELECT
    name AS Nome_do_podcast,
    description AS description,
    show_id AS id,
    total_episodes AS total_episodes
  FROM
    `botica-teste.dataspotify.data-hackers`
),
all_episodes_boticario AS (
  SELECT
    Episode_ID AS id,
    Name AS name,
    Description AS description,
    Release_Date AS release_date,
    Duration_ms AS duration_ms,
    Language AS language,
    Explicit AS explicit,
    'programa' AS type
  FROM
    `botica-teste.dataspotify.episodios`
  WHERE
    Description LIKE '%Grupo Boticário%'
)
SELECT
  datahackers_table.Nome_do_podcast,
  datahackers_table.description,
  datahackers_table.id,
  datahackers_table.total_episodes,
  all_episodes_boticario.id AS episode_id,
  all_episodes_boticario.name AS episode_name,
  all_episodes_boticario.release_date,
  all_episodes_boticario.duration_ms,
  all_episodes_boticario.language,
  all_episodes_boticario.explicit,
  all_episodes_boticario.type
FROM
  datahackers_table
JOIN
  all_episodes_boticario
ON
  datahackers_table.id = all_episodes_boticario.id;
