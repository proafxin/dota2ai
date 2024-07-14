from blacksheep import Request
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from backend.responses.heroes import HeroResponse


async def populate_details(
    request: Request, client: AsyncIOMotorClient, db: AsyncIOMotorDatabase
) -> list[HeroResponse]:
    print(client)
    print(client.list_database_names())
    print(type(client))
    print(db)
    print(type(db))
    print(db.name)
    return []
