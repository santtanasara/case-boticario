QUERY

#CRIANDO A TABELA 5 DE DESCRIÇÃO DO PODCAST


CREATE TABLE botica-teste.dataspotify.datahackers AS
SELECT
  name AS Nome_do_podcast,
  description AS description,
  show_id AS id,
  total_episodes AS total_episodes
FROM
  `botica-teste.dataspotify.data-hackers`;

 # Tabela 6: Resultado de todos os episódios. e Tabela 7: Apenas com os resultados dos episódios com participação do Grupo Boticário.  


CREATE TABLE botica-teste.dataspotify.all_episodes_boticario AS
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
  Description LIKE '%Grupo Boticário%';
