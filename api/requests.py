import asyncio
from os import makedirs
from os.path import exists, join, splitext
from typing import Any

import aiofiles
from aiohttp import ClientSession

from dota2ai.settings import DATA_DIR


async def get_json(url: str, session: ClientSession) -> list[dict[str, Any]]:
    async with session.get(url=url) as response:
        data: list[dict[str, Any]] = await response.json()

        return data


async def get_image(url: str, session: ClientSession) -> str:
    file = url.split("/")[-1]
    filename, _ = splitext(file)

    image_dir = join(DATA_DIR, filename)

    if not exists(image_dir):
        makedirs(image_dir)

    path = join(image_dir, file)

    if exists(path=path):
        return file

    async with session.get(url=url) as response:
        f = await aiofiles.open(file=path, mode="wb")
        await f.write(await response.read())
        await f.close()

    return file


async def get_images(urls: list[str], session: ClientSession) -> list[str]:
    responses = await asyncio.gather(*[get_image(url=url, session=session) for url in urls])

    return responses
