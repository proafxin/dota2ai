import asyncio
from typing import Any

from aiohttp import ClientSession

from dota2ai.settings import DOTA_APP_ID, STEAM_API_BASE_URL, STEAM_API_KEY


def form_match_history_url(match_id: int) -> str:
    return f"{STEAM_API_BASE_URL}/IDOTA2Match_{DOTA_APP_ID}/GetMatchHistoryBySequenceNum/v1?match_id={match_id}&key={STEAM_API_KEY}"


def form_match_history_urls(start_id: int, n_matches: int) -> list[str]:
    return [form_match_history_url(match_id=start_id + i + 1) for i in range(n_matches)]


async def get(url: str, session: ClientSession) -> dict[str, Any]:
    async with session.get(url=url) as response:
        data = await response.json()

    return data["result"]["matches"]


async def get_multiple(urls: list[str]) -> list[dict[str, Any]]:
    async with ClientSession() as session:
        responses = await asyncio.gather(
            *[get(url=url, session=session) for url in urls]
        )

        return responses
