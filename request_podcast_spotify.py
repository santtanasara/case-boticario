# -*- coding: utf-8 -*-
"""request podcast spotify

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eA96GWxgUNozlYkRXJ4bzAjt3_4syX9A

Instalação do request e criação do token de acesso

> Indented block
"""

!pip install requests

import requests

# URL para obtenção do token de acesso
url = "https://accounts.spotify.com/api/token"

# Parâmetros da requisição
payload = {
    "grant_type": "client_credentials",
    "client_id": "e15cf346e3b0442c8d49bc021abb9445",
    "client_secret": "826af27bd99a43f1a7964e72277e7760"
}

# Faz a requisição POST
response = requests.post(url, data=payload)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Obtém o token de acesso da resposta em formato JSON
    data = response.json()
    access_token = data["access_token"]
    token_type = data["token_type"]
    # Aqui você pode usar o token de acesso para fazer outras requisições ao Spotify
    # por exemplo, pesquisar podcasts, acessar playlists, etc.
else:
    # Caso ocorra algum erro na requisição, exibe o código de status
    print("Erro na requisição:", response.status_code)

print(data)

"""Busca pelo ID do podcast"""

import re

link = "https://open.spotify.com/show/1oMIHOXsrLFENAeM743g93?si=2994730935fe4877&nd=1"

# Extrair o ID do podcast usando expressões regulares
pattern = r"show\/(\w+)"
match = re.search(pattern, link)

if match:
    podcast_id = match.group(1)
    print("ID do podcast:", podcast_id)
else:
    print("Não foi possível encontrar o ID do podcast.")

"""Trazendo dados do Podcast[link text](https://)"""

import requests

def get_show(show_id, market):
    url = f"https://api.spotify.com/v1/shows/1oMIHOXsrLFENAeM743g93"
    headers = {
        "Authorization": "Bearer BQAWwAwsFzAlKNxAK4LonAZyTpNwZo2QssfblDcU1_Hj4h7brb_P_QrT4ZmNnp6_MXUjLM_HiaTVRuU_i2dPkrzRZelTt9lgnZ6KLpIKSFXYOLReTZNd"
    }
    params = {
        "market": market
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        available_markets = data.get("available_markets", [])
        copyrights = data.get("copyrights", [])
        description = data.get("description", "")
        html_description = data.get("html_description", "")
        explicit = data.get("explicit", False)
        external_urls = data.get("external_urls", {})
        href = data.get("href", "")
        show_id = data.get("id", "")
        images = data.get("images", [])
        is_externally_hosted = data.get("is_externally_hosted", False)
        languages = data.get("languages", [])
        media_type = data.get("media_type", "")
        name = data.get("name", "")
        publisher = data.get("publisher", "")
        show_type = data.get("type", "")
        uri = data.get("uri", "")
        total_episodes = data.get("total_episodes", 0)
        episodes = data.get("episodes", [])
        

        # Print the show information
        print("Available Markets:", available_markets)
        print("Copyrights:", copyrights)
        print("Description:", description)
        print("HTML Description:", html_description)
        print("Explicit:", explicit)
        print("External URLs:", external_urls)
        print("Href:", href)
        print("Show ID:", show_id)
        print("Images:", images)
        print("Externally Hosted:", is_externally_hosted)
        print("Languages:", languages)
        print("Media Type:", media_type)
        print("Name:", name)
        print("Publisher:", publisher)
        print("Type:", show_type)
        print("URI:", uri)
        print("Total Episodes:", total_episodes)
        print("Episodes:", episodes)
    else:
        print("Error in the request:", response.status_code)

# Specify your access token and the required parameters
access_token = "BQAWwAwsFzAlKNxAK4LonAZyTpNwZo2QssfblDcU1_Hj4h7brb_P_QrT4ZmNnp6_MXUjLM_HiaTVRuU_i2dPkrzRZelTt9lgnZ6KLpIKSFXYOLReTZNd"
show_id = "1oMIHOXsrLFENAeM743g93"
market = "BR"

# Call the function to get the show information
get_show(show_id, market)

import os

# Verificar o diretório atual
current_directory = os.getcwd()
print("Diretório atual:", current_directory)

# Listar os arquivos no diretório
files_in_directory = os.listdir()
print("Arquivos no diretório:", files_in_directory)

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('podcast_data.csv')

# Imprimir o conteúdo do DataFrame
print(df)

"""Busca por episódios

```
# This is formatted as code
```


"""

import requests

def get_show_episodes(show_id, market, limit=20, offset=0):
    url = f"https://api.spotify.com/v1/shows/1oMIHOXsrLFENAeM743g93/episodes"
    headers = {
        "Authorization": "Bearer BQBVkfEv3DC32Fka2e6exFjWr29jR_tWyUrUbKzAgl9bcGIec6g_OjK-NrrglfAyvYCG4YCYxPvopQnNZ8faDzUHzQSEJVxsY5PRaJSThUeUzFhS16fC"
    }
    params = {
        "market": market,
        "limit": limit,
        "offset": offset
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Retrieve episode information
        href = data.get("href", "")
        total = data.get("total", 0)
        items = data.get("items", [])

        # Print episode information
        print("Episodes:")
        for episode in items:
            audio_preview_url = episode.get("audio_preview_url", "")
            description = episode.get("description", "")
            html_description = episode.get("html_description", "")
            duration_ms = episode.get("duration_ms", 0)
            explicit = episode.get("explicit", False)
            external_urls = episode.get("external_urls", {})
            episode_id = episode.get("id", "")
            images = episode.get("images", [])
            is_externally_hosted = episode.get("is_externally_hosted", False)
            is_playable = episode.get("is_playable", False)
            language = episode.get("language", "")
            languages = episode.get("languages", [])
            name = episode.get("name", "")
            release_date = episode.get("release_date", "")
            release_date_precision = episode.get("release_date_precision", "")
            resume_point = episode.get("resume_point", {})
            uri = episode.get("uri", "")
            restrictions = episode.get("restrictions", {})

            print("Audio Preview URL:", audio_preview_url)
            print("Description:", description)
            print("HTML Description:", html_description)
            print("Duration (ms):", duration_ms)
            print("Explicit:", explicit)
            print("External URLs:", external_urls)
            print("Episode ID:", episode_id)
            print("Images:", images)
            print("Externally Hosted:", is_externally_hosted)
            print("Playable:", is_playable)
            print("Language:", language)
            print("Languages:", languages)
            print("Name:", name)
            print("Release Date:", release_date)
            print("Release Date Precision:", release_date_precision)
            print("Resume Point:", resume_point)
            print("URI:", uri)
            print("Restrictions:", restrictions)
            print("--------------")
    else:
        print("Error in the request:", response.status_code)

# Specify your access token and the required parameters
access_token = "BQBVkfEv3DC32Fka2e6exFjWr29jR_tWyUrUbKzAgl9bcGIec6g_OjK-NrrglfAyvYCG4YCYxPvopQnNZ8faDzUHzQSEJVxsY5PRaJSThUeUzFhS16fC"
show_id = "1oMIHOXsrLFENAeM743g93"
market = "BR"
limit = 10
offset = 0

# Call the function to get the show episodes
get_show_episodes(show_id, market, limit, offset)

import requests
import pandas as pd

def get_show(show_id, market):
    url = f"https://api.spotify.com/v1/shows/1oMIHOXsrLFENAeM743g93"
    headers = {
        "Authorization": "Bearer BQCIrbHDcVkdHswYewHFjPuLE-KRdNnQntSrK3yxms_P6cvHf3Swe9auAesNqn-Em1TtKb42BQ17bGZGpda3CE4aYXwTbYup7fiYbcyUCuR5ZgK4COJY"
    }
    params = {
        "market": market
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        available_markets = data.get("available_markets", [])
        copyrights = data.get("copyrights", [])
        description = data.get("description", "")
        html_description = data.get("html_description", "")
        explicit = data.get("explicit", False)
        external_urls = data.get("external_urls", {})
        href = data.get("href", "")
        show_id = data.get("id", "")
        images = data.get("images", [])
        is_externally_hosted = data.get("is_externally_hosted", False)
        languages = data.get("languages", [])
        media_type = data.get("media_type", "")
        name = data.get("name", "")
        publisher = data.get("publisher", "")
        show_type = data.get("type", "")
        uri = data.get("uri", "")
        total_episodes = data.get("total_episodes", 0)
        episodes = data.get("episodes", [])

        # Create a DataFrame with the show information
        df = pd.DataFrame({
            "Available Markets": [available_markets],
            "Copyrights": [copyrights],
            "Description": [description],
            "HTML Description": [html_description],
            "Explicit": [explicit],
            "External URLs": [external_urls],
            "Href": [href],
            "Show ID": [show_id],
            "Images": [images],
            "Externally Hosted": [is_externally_hosted],
            "Languages": [languages],
            "Media Type": [media_type],
            "Name": [name],
            "Publisher": [publisher],
            "Type": [show_type],
            "URI": [uri],
            "Total Episodes": [total_episodes],
            "Episodes": [episodes]
        })

        # Save DataFrame to a CSV file
        df.to_csv('podcast_data.csv', index=False)

        print("Podcast data saved to 'podcast_data.csv'")
    else:
        print("Error in the request:", response.status_code)

# Specify your access token and the required parameters
access_token = "BQCIrbHDcVkdHswYewHFjPuLE-KRdNnQntSrK3yxms_P6cvHf3Swe9auAesNqn-Em1TtKb42BQ17bGZGpda3CE4aYXwTbYup7fiYbcyUCuR5ZgK4COJY"
show_id = "1oMIHOXsrLFENAeM743g93"
market = "BR"

# Call the function
# Call the function to get the show information
get_show(show_id, market)

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('podcast_data.csv')

# Imprimir o conteúdo do DataFrame
print(df)

import os

# Listar os arquivos no diretório
files_in_directory = os.listdir()
print("Arquivos no diretório:", files_in_directory)

"""Conectando no bigquery para salvar os dados

"""

!pip install requests google-cloud-bigquery
from google.cloud import bigquery
import requests
import json
import re
from google.colab import files
from google.oauth2 import service_account

!pip install google-cloud-bigquery
!pip install google-auth

from google.cloud import bigquery
from google.colab import auth

auth.authenticate_user()

client = bigquery.Client(project='botica-teste')

query = """
SELECT *
FROM `botica-teste.dataspotify.data-hackers`
"""
query_job = client.query(query)
results = query_job.result()

for row in results:
    print(row)

from google.colab import files

uploaded = files.upload()

from google.cloud import bigquery

# Configurar as credenciais de autenticação
# Substitua "caminho/do/arquivo.json" pelo caminho para o arquivo de credenciais do BigQuery
# Substitua "seu-projeto" pelo ID do seu projeto no Google Cloud
credentials_path = "botica-teste-da4a7b577ad3 (3).json"
project_id = "botica-teste"

# Criar um cliente do BigQuery
client = bigquery.Client.from_service_account_json(credentials_path, project=project_id)

# Carregar o arquivo CSV em uma tabela do BigQuery
dataset_id = "dataspotify"  # Substitua pelo ID do dataset no BigQuery
table_id = "data-hackers"  # Substitua pelo ID da tabela no BigQuery
filename = "podcast_data.csv"  # Substitua pelo nome do arquivo CSV

dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1

with open(filename, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

job.result()  # Aguardar a conclusão do carregamento

print("Dados carregados para a tabela:", table_ref.path)