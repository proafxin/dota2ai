import asyncio
from os.path import exists, join, splitext
from typing import Any

import aiofiles
from aiohttp import ClientSession

from dota2ai.settings import IMAGE_DIR, LABEL_DIR


async def get_json(url: str, session: ClientSession) -> list[dict[str, Any]]:
    async with session.get(url=url) as response:
        data: list[dict[str, Any]] = await response.json()

        return data


async def get_image(url: str, session: ClientSession, n_class: int) -> str:
    file = url.split("/")[-1]
    filename, _ = splitext(p=file)

    image_path = join(IMAGE_DIR, file)

    if exists(path=image_path):
        return file

    label_path = join(LABEL_DIR, f"{filename}.txt")

    async with session.get(url=url) as response:
        f_img = await aiofiles.open(file=image_path, mode="wb")
        await f_img.write(await response.read())
        await f_img.close()

        f_label = await aiofiles.open(file=label_path, mode="w")
        await f_label.write(f"{n_class} 0.5 0.5 1.0 1.0")

    return file


async def get_images(urls: list[str], session: ClientSession) -> list[str]:
    responses = await asyncio.gather(
        *[get_image(url=url, session=session, n_class=n_class) for n_class, url in enumerate(urls)]
    )

    return responses
