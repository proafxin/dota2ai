from blacksheep import Request
from motor.motor_asyncio import AsyncIOMotorDatabase

from api.responses.heroes import HeroResponse
from api.services.heroes.details import populate


async def populate_details(request: Request, db: AsyncIOMotorDatabase) -> list[HeroResponse]:
    return await populate(db=db)
