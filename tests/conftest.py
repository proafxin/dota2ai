import os
from typing import AsyncGenerator

import pytest_asyncio
from blacksheep import Application
from blacksheep.testing import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from rodi import Container

from server import app as main_api


@pytest_asyncio.fixture(scope="session")
async def db_client() -> AsyncGenerator[AsyncIOMotorClient, None]:
    client = AsyncIOMotorClient(
        host=os.environ["MONGO_HOST"],
        port=int(os.environ["MONGO_PORT"]),
        username=os.environ["MONGO_USER"],
        password=os.environ["MONGO_PASSWORD"],
    )
    yield client


@pytest_asyncio.fixture(scope="session")
async def api(db_client: AsyncIOMotorClient) -> AsyncGenerator[Application, None]:
    dbname = "test_db"
    service = Container()
    db = db_client.get_database(name=dbname)
    service.add_instance(db)
    await main_api.start()  # type: ignore

    yield main_api

    await db_client.drop_database(name_or_database=dbname)
    db_client.close()


@pytest_asyncio.fixture(scope="session")
async def test_client(api: Application) -> AsyncGenerator[TestClient, None]:
    client = TestClient(app=api)
    yield client
