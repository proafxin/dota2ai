from typing import Any

from aiohttp import ClientConnectionError, ClientError, ClientPayloadError, ClientSession


async def get(urls: list[str], session: ClientSession) -> list[list[dict[str, Any]]]:
    responses: list[list[dict[str, Any]]] = []
    for url in urls:
        try:
            async with session.get(url=url) as response:
                data: list[dict[str, Any]] = await response.json()
                responses.append(data)
        except (ClientPayloadError, ClientConnectionError, ClientError, ClientError) as _:
            raise

    return responses
