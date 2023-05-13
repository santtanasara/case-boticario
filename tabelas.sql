#CRIAÇÃO DA TABELA COMPLETA DO PODCAST

CREATE TABLE botica-teste.dataspotify.data-hackers(
  `Available Markets` STRING,
  `Copyrights` STRING,
  `Description` STRING,
  `HTML Description` STRING,
  `Explicit` BOOLEAN,
  `External URLs` STRING,
  `Href` STRING,
  `Show ID` STRING,
  `Images` STRING,
  `Externally Hosted` BOOLEAN,
  `Languages` STRING,
  `Media Type` STRING,
  `Name` STRING,
  `Publisher` STRING,
  `Type` STRING,
  `URI` STRING,
  `Total Episodes` INTEGER,
  `Episodes` STRING
);

#CRIAÇÃO TABELA COMPLETA EPISODIOS

CREATE TABLE botica-teste.nova_tabela2 (
  Audio_Preview_URL STRING,
  Description STRING,
  HTML_Description STRING,
  Duration_ms INTEGER,
  Explicit BOOLEAN,
  External_URLs STRING,
  Episode_ID STRING,
  Images STRING,
  Externally_Hosted BOOLEAN,
  Playable BOOLEAN,
  Language STRING,
  Languages STRING,
  Name STRING,
  Release_Date STRING,
  Release_Date_Precision STRING,
  Resume_Point STRING,
  URI STRING,
  Restrictions STRING
);


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
