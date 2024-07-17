import asyncio
from os.path import exists, join
from typing import Any

import aiofiles
from aiohttp import ClientSession

from dota2ai.settings import DATA_DIR


async def get_json(url: str, session: ClientSession) -> list[dict[str, Any]]:
    async with session.get(url=url) as response:
        data: list[dict[str, Any]] = await response.json()

        return data


async def get_image(url: str, session: ClientSession) -> str:
    filename = url.split("/")[-1]
    path = join(DATA_DIR, filename)

    if exists(path=path):
        return filename

    async with session.get(url=url) as response:
        file = await aiofiles.open(file=path, mode="wb")
        await file.write(await response.read())
        await file.close()

    return filename


async def get_images(urls: list[str], session: ClientSession) -> list[str]:
    responses = await asyncio.gather(*[get_image(url=url, session=session) for url in urls])

    return responses
