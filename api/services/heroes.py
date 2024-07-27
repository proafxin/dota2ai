from datetime import datetime, timezone
from os.path import join

import yaml
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorDatabase

from api.requests import get_images, get_json
from api.responses.heroes import Hero, HeroResponse
from api.services.name_mapping import HEROES
from dota2ai.settings import DATA_DIR


async def clean_name(name: str) -> str:
    if name in HEROES:
        return HEROES[name]

    return name.lower().strip().replace(" ", "_")


async def get_all_from_opendota() -> list[Hero]:
    async with ClientSession() as session:
        response = await get_json(url="https://api.opendota.com/api/heroes", session=session)

        return [Hero(**data, cleaned_name=await clean_name(name=data["localized_name"])) for data in response]


async def populate(db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    heroes = await get_all_from_opendota()
    collection_name = "heroes"
    if hasattr(db, collection_name):
        await db[collection_name].drop()

    collection = db[collection_name]

    responses: list[HeroResponse] = []
    for hero in heroes:
        response = HeroResponse(
            **hero.model_dump(),
            created_at=datetime.now(tz=timezone.utc),
            updated_at=datetime.now(tz=timezone.utc),
        )
        responses.append(response)

    await collection.insert_many([response.model_dump() for response in responses])

    return responses


async def get_all(db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    collection_name = "heroes"
    collection = db[collection_name]
    cursor = collection.find({})

    return [HeroResponse(**hero) for hero in await cursor.to_list(None)]


async def all_images(db: AsyncIOMotorDatabase) -> list[str]:
    heroes = get_all(db=db)

    async with ClientSession() as session:
        urls: list[str] = []
        class_file = join(DATA_DIR, "classes.txt")
        classes: list[str] = []
        for hero in await heroes:
            url = f"https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/heroes/{hero.cleaned_name}.png"
            urls.append(url)
            classes.append(hero.cleaned_name)

        with open(file=class_file, mode="w") as f:
            f.write("\n".join(classes))

        data = {
            "path": "../data/",
            "train": "images/",
            "val": "images/",
            "test": "images/",
            "names": {n_class: _class for n_class, _class in enumerate(classes)},
        }
        with open(file=join(DATA_DIR, "dota2.yaml"), mode="w") as dataset:
            yaml.dump(data=data, stream=dataset)

        responses = await get_images(urls=urls, session=session)

        return responses
