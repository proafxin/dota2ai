import asyncio
from typing import Any

from backend.services.steam_dota2 import form_match_history_urls, get_multiple

urls = form_match_history_urls(start_id=8244708904, n_matches=10)

data: list[dict[str, Any]] = asyncio.run(get_multiple(urls=urls))
# print(df.head())
print(data[0])
print(data[0][0].keys())
