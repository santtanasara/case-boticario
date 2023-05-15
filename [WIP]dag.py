from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.sensors.bigquery import BigQueryTableSensor

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 5, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('create_bigquery_tables', default_args=default_args, schedule_interval=None) as dag:
    # Tabela 1: botica-teste.dataspotify.datahackers
    create_table_datahackers = BigQueryExecuteQueryOperator(
        task_id='create_table_datahackers',
        sql="""
        CREATE OR REPLACE TABLE `botica-teste.dataspotify.datahackers`
        AS
        SELECT
          name AS Nome_do_podcast,
          description AS description,
          show_id AS id,
          total_episodes AS total_episodes
        FROM
          `botica-teste.dataspotify.data-hackers`
        """,
        use_legacy_sql=False,
        write_disposition='WRITE_TRUNCATE',
        destination_dataset_table='botica-teste.dataspotify.datahackers'
    )

    # Tabela 2: botica-teste.dataspotify.all_episodes_boticario
    create_table_episodes = BigQueryExecuteQueryOperator(
        task_id='create_table_episodes',
        sql="""
        CREATE OR REPLACE TABLE `botica-teste.dataspotify.all_episodes_boticario`
        AS
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
        """,
        use_legacy_sql=False,
        write_disposition='WRITE_TRUNCATE',
        destination_dataset_table='botica-teste.dataspotify.all_episodes_boticario'
    )

    # Sensor para verificar a conclusão da criação da tabela 2
    check_table_episodes = BigQueryTableSensor(
        task_id='check_table_episodes',
        project_id='botica-teste',
        dataset_id='dataspotify',
        table_id='all_episodes_boticario',
        poke_interval=30,
        timeout=1200
    )

    create_table_datahackers >> create_table_episodes >> check_table_episodes
