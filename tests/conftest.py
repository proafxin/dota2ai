from typing import AsyncGenerator

import pytest_asyncio
from blacksheep import Application
from blacksheep.testing import TestClient
from rodi import Container

from api.dependencies import client
from server import app as main_api


@pytest_asyncio.fixture(scope="session")
async def api() -> AsyncGenerator[Application, None]:
    dbname = "test_db"
    service = Container()
    db = client.get_database(name=dbname)
    service.add_instance(db)
    await main_api.start()  # type: ignore

    yield main_api

    await client.drop_database(name_or_database=dbname)
    client.close()
    await main_api.stop()  # type: ignore


@pytest_asyncio.fixture(scope="package")
async def test_client(api: Application) -> AsyncGenerator[TestClient, None]:
    client = TestClient(app=api)
    yield client
