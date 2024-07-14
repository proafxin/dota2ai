from datetime import datetime, timezone

from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorDatabase

from api.requests import get
from api.responses.heroes import Hero, HeroResponse


async def get_details() -> list[Hero]:
    async with ClientSession() as session:
        response = await get(urls=["https://api.opendota.com/api/heroes"], session=session)

        return [Hero(**data) for data in response[0]]


async def populate(db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    heroes = await get_details()
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
