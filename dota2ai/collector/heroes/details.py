from typing import Any

from aiohttp import ClientSession

from dota2ai.collector.send import get


async def hero_details(session: ClientSession) -> list[dict[str, Any]]:
    return await get(urls=["https://api.opendota.com/api/heroes"], session=session)
