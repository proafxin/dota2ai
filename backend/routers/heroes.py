from blacksheep import Request, get, post
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from backend.responses.heroes import HeroResponse


@get("/")
async def index() -> str:
    return "Hello world"


@post("/populate/details")
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
