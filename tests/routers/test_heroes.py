from http import HTTPStatus

import pytest
from blacksheep import Application
from blacksheep.testing import TestClient

from api.responses.heroes import HeroResponse


@pytest.mark.asyncio
async def test_populate_details(test_client: TestClient, api: Application) -> None:
    url = "/populate/details"

    response = await test_client.post(path=url)

    assert response.status == HTTPStatus.OK
    data = await response.json()
    assert isinstance(data, list)
    for x in data:
        assert isinstance(x, dict)
        assert HeroResponse.model_validate(x)


@pytest.mark.asyncio
async def test_get_all(test_client: TestClient, api: Application) -> None:
    url = "/heroes"
    response = await test_client.get(path=url)

    assert response.status == HTTPStatus.OK
    data = await response.json()
    assert isinstance(data, list)
    for x in data:
        assert isinstance(x, dict)
