from typing import Any

from aiohttp import ClientSession


async def get(urls: list[str], session: ClientSession) -> list[list[dict[str, Any]]]:
    responses: list[list[dict[str, Any]]] = []
    for url in urls:
        async with session.get(url=url) as response:
            data: list[dict[str, Any]] = await response.json()
            responses.append(data)

    return responses
