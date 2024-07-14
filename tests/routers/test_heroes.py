from blacksheep import Application
from blacksheep.testing import TestClient


async def test_populate_details(test_client: TestClient, api: Application) -> None:
    url = "/populate/details"

    response = await test_client.post(path=url)

    assert response.status == 200
