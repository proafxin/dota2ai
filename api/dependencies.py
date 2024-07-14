"""
Use this module to register required services.
Services registered inside a `rodi.Container` are automatically injected into request
handlers.

For more information and documentation, see `rodi` Wiki and examples:
    https://github.com/Neoteroi/rodi/wiki
    https://github.com/Neoteroi/rodi/tree/main/examples
"""

import os

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from rodi import Container

client: AsyncIOMotorClient = AsyncIOMotorClient(
    host=os.environ["MONGO_HOST"],
    port=int(os.environ["MONGO_PORT"]),
    username=os.environ["MONGO_USER"],
    password=os.environ["MONGO_PASSWORD"],
)
db: AsyncIOMotorDatabase = getattr(client, "dota2")


def configure_dependencies() -> Container:
    container = Container()
    container.add_instance(client)
    container.add_instance(db)

    return container
