import os
from enum import Enum
from os.path import abspath, dirname, join


class APIKeyName(str, Enum):
    STEAM_API_KEY = "STEAM_API_KEY"


if APIKeyName.STEAM_API_KEY.value not in os.environ:
    raise ValueError("STEAM_API_KEY not set")

STEAM_API_KEY = os.environ[APIKeyName.STEAM_API_KEY.value]

BASE_DIR = join(dirname(abspath(__file__)), "../")
DATA_DIR = join(BASE_DIR, "data/")
DOTA_APP_ID = "570"
STEAM_API_BASE_URL = "https://api.steampowered.com"
