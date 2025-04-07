import os
from typing import Any

import requests

from backend.services.queries import match_query, matches_query

BASE_STRATZ_URL = "https://api.stratz.com/graphql"
STRATZ_API_KEY = os.environ["STRATZ_API_KEY"]


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def query_graphql(query: str):
    headers = {
        "Authorization": f"Bearer {STRATZ_API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "STRATZ_API",
    }

    response = requests.post(BASE_STRATZ_URL, json={"query": query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def match_data(match_id: int) -> dict[str, Any]:
    query = match_query(match_id)
    data = query_graphql(query)
    return data


def matches_data(match_ids: list[int]) -> dict[str, Any]:
    query = matches_query(match_ids)
    data = query_graphql(query)
    return data
