#imports necessários para autenticação

!pip install google-cloud-bigquery

from google.cloud import bigquery
from google.colab import auth

auth.authenticate_user()

client = bigquery.Client(project='botica-teste')

#importando os arquivos

from google.colab import files

uploaded_files = files.upload()

#criando o dataframe:

import pandas as pd
dataframes = []
for filename in uploaded_files.keys():
    df = pd.read_excel(filename)
    dataframes.append(df)
    print(f"Arquivo {filename} carregado. Total de linhas: {len(df)}")

#união dos arquivos

merged_df = pd.concat(dataframes, ignore_index=True)
print(f"Dataframe unificado. Total de linhas: {len(merged_df)}")

#dedup dos dados

merged_df = pd.concat(dataframes, ignore_index=True)
print(f"Dataframe unificado. Total de linhas: {len(merged_df)}")

#instalção do oauth para inseção dos dados nas tabelas do BQ
!pip install google-auth
from google.oauth2 import service_account

# Caminho para o arquivo JSON da chave de acesso
credentials_path = '/content/botica-teste-da4a7b577ad3.json'

# Carrega as credenciais do serviço a partir do JSON
credentials = service_account.Credentials.from_service_account_file(credentials_path)

project_id = "botica-teste"  
table_id = "vendas.dados-vendas" 

# Salva o dataframe no BigQuery
deduplicated_df.to_gbq(destination_table=table_id, project_id=project_id, if_exists="replace", credentials=credentials)

print("Dados salvos com sucesso no BigQuery!")

#query para verificar se os dados foram salvos 
query = """
SELECT *
FROM `botica-teste.vendas.dados-vendas`
LIMIT 10
"""
query_job = client.query(query)
results = query_job.result()

for row in results:
    print(row)


#criação das tabelas:

from google.cloud import bigquery

# Cria uma lista com as consultas SQL para cada tabela
queries = [
    """
    CREATE OR REPLACE TABLE `botica-teste.vendas.tabela_vendas_ano_mes` AS
    SELECT EXTRACT(YEAR FROM data_venda) AS Ano, EXTRACT(MONTH FROM data_venda) AS Mes, SUM(QTD_VENDA) AS Consol_Vendas
    FROM `botica-teste.vendas.dados-vendas` 
    GROUP BY Ano, Mes
    """,
    """
    CREATE OR REPLACE TABLE `botica-teste.vendas.tabela_vendas_marca_linha` AS
    SELECT marca, linha, SUM(QTD_VENDA) AS Consol_Vendas
    FROM `botica-teste.vendas.dados-vendas` 
    GROUP BY marca, linha
    """,
    """
    CREATE OR REPLACE TABLE `botica-teste.vendas.tabela_vendas_marca_ano_mes` AS
    SELECT marca, EXTRACT(YEAR FROM data_venda) AS Ano, EXTRACT(MONTH FROM data_venda) AS Mes, SUM(QTD_VENDA) AS Consol_Vendas
    FROM `botica-teste.vendas.dados-vendas` 
    GROUP BY marca, Ano, Mes
    """,
    """
    CREATE OR REPLACE TABLE `botica-teste.vendas.tabela_vendas_linha_ano_mes` AS
    SELECT linha, EXTRACT(YEAR FROM data_venda) AS Ano, EXTRACT(MONTH FROM data_venda) AS Mes, SUM(QTD_VENDA) AS Consol_Vendas
    FROM `botica-teste.vendas.dados-vendas` 
    GROUP BY linha, Ano, Mes
    """
]

# Cria uma instância do cliente do BigQuery
client = bigquery.Client(project='botica-teste')

# Executa as consultas para criar as tabelas
for query in queries:
    client.query(query).result()

print("Tabelas criadas com sucesso!")
