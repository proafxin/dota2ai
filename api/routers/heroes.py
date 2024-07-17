from blacksheep import Request
from motor.motor_asyncio import AsyncIOMotorDatabase

from api.responses.heroes import HeroResponse
from api.services.heroes import all_images, get_all, populate


async def populate_details(request: Request, db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    return await populate(db=db)


async def all(request: Request, db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    return await get_all(db=db)


async def images(request: Request, db: AsyncIOMotorDatabase) -> list[str]:
    return await all_images(db=db)
