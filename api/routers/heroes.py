from blacksheep import Request
from motor.motor_asyncio import AsyncIOMotorDatabase

from api.responses.heroes import HeroResponse
from api.services.heroes.details import get_all, populate


async def populate_details(request: Request, db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    return await populate(db=db)


async def all(request: Request, db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    return await get_all(db=db)
