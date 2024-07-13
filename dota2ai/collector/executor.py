from typing import Any

from aiohttp import ClientSession


async def get_heroes() -> list[dict[str, Any]]:
    session = ClientSession()
    await session.close()
    return []
