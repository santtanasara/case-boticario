from google.colab import files

uploaded = files.upload()

import re
import requests
import pandas as pd
from google.cloud import bigquery
from google.colab import auth
import os

#Credenciais de acesso 
CLIENT_ID = "e15cf346e3b0442c8d49bc021abb9445"
CLIENT_SECRET = "826af27bd99a43f1a7964e72277e7760"  #salvar para nao exibir no código.
PODCAST_LINK = "https://open.spotify.com/show/1oMIHOXsrLFENAeM743g93?si=2994730935fe4877&nd=1"
MARKET = "BR"
CREDENTIALS_PATH = "botica-teste-b1342f1ca89d.json"
PROJECT_ID = "botica-teste"
DATASET_ID = "dataspotify"
TABLE_ID = "data-hackers"

#Função para aceesso ao token
def get_access_token():
    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        data = response.json()
        access_token = data["access_token"]
        return access_token
    else:
        raise Exception("Failed to obtain access token")

# Função para o id do podcast
def get_podcast_id(link):
    pattern = r"show/(\w+)"
    match = re.search(pattern, link)
    if match:
        podcast_id = match.group(1)
        return podcast_id
    else:
        raise Exception("Failed to find podcast ID")        

# Função para coleta dos episodios e transformação 
def get_show(show_id, market):
    url = f"https://api.spotify.com/v1/shows/{show_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "market": market
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

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
        df = pd.DataFrame(episodes)
        df.to_csv('podcast_data.csv', index=False)
        print("Episodes data saved to 'podcast_data.csv'")
    else:
        raise Exception(f"Error in the request: {response.status_code}")
def upload_to_bigquery(credentials_path, project_id, dataset_id, table_id, filename):
    auth.authenticate_user()
    client = bigquery.Client.from_service_account_json(credentials_path, project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE  

    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  

    print("Data loaded into BigQuery table:", table_ref.path)


# Obtém o access token do Spotify
access_token = get_access_token()

# Obtém o ID do podcast a partir do link
podcast_id = get_podcast_id(PODCAST_LINK)

# Faz o upload dos dados para o BigQuery
upload_to_bigquery(CREDENTIALS_PATH, PROJECT_ID, DATASET_ID, TABLE_ID, 'podcast_data.csv')
