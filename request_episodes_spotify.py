# -*- coding: utf-8 -*-
"""request_episodes_spotify

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z1o78BKeQWaalLH71RFY3l7Clc0TLKzV
"""

from google.colab import files

uploaded = files.upload()

import re
import requests
import pandas as pd
from google.cloud import bigquery
from google.colab import auth
import os

CLIENT_ID = "e15cf346e3b0442c8d49bc021abb9445"
CLIENT_SECRET = "826af27bd99a43f1a7964e72277e7760"
PODCAST_LINK = "https://open.spotify.com/show/1oMIHOXsrLFENAeM743g93?si=2994730935fe4877&nd=1"
MARKET = "BR"
CREDENTIALS_PATH = "botica-teste-b1342f1ca89d.json"
PROJECT_ID = "botica-teste"
DATASET_ID = "dataspotify"
TABLE_ID = "episodios"

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

def get_podcast_id(link):
    pattern = r"show/(\w+)"
    match = re.search(pattern, link)
    if match:
        podcast_id = match.group(1)
        return podcast_id
    else:
        raise Exception("Failed to find podcast ID")

def get_show_episodes(podcast_id, market, access_token):
    url = f"https://api.spotify.com/v1/shows/{podcast_id}/episodes"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "market": market
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        episodes = []

        for episode in items:
            episodes.append({
                "Audio_Preview_URL": episode.get("audio_preview_url", ""),
                "Description": episode.get("description", ""),
                "HTML_Description": episode.get("html_description", ""),
                "Duration_ms": episode.get("duration_ms", 0),
                "Explicit": episode.get("explicit", False),
                "External_URLs": episode.get("external_urls", {}),
                "Episode_ID": episode.get("id", ""),
                "Images": episode.get("images", []),
                "Externally_Hosted": episode.get("is_externally_hosted", False),
                "Playable": episode.get("is_playable", False),
                "Language": episode.get("language", ""),
                "Languages": episode.get("languages", []),
                "Name": episode.get("name", ""),
                "Release_Date": episode.get("release_date", ""),
                "Release_Date_Precision": episode.get("release_date_precision", ""),
                "Resume_Point": episode.get("resume_point", {}),
                "URI": episode.get("uri", ""),
                "Restrictions": episode.get("restrictions", {})
            })

        df = pd.DataFrame(episodes)
        df.to_csv('episodes_data.csv', index=False)
        print("Episodes data saved to 'episodes_data.csv'")
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
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE  # Substituir dados existentes

    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()
    print("Data loaded into BigQuery table:", table_id)

# Obtém o access token do Spotify
access_token = get_access_token()

# Obtém o ID do podcast a partir do link
podcast_id = get_podcast_id(PODCAST_LINK)

# Obtém os episódios do show de podcast
get_show_episodes(podcast_id, MARKET, access_token)

# Faz o upload dos dados para o BigQuery
upload_to_bigquery(CREDENTIALS_PATH, PROJECT_ID, DATASET_ID, TABLE_ID, 'episodes_data.csv')