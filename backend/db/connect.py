import os

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(host=os.environ["MONGO_HOST"], port=int(os.environ["MONGO_PORT"]))  # type: ignore
