import pytest

from backend.responses.heroes import Hero
from backend.services.heroes.details import get_details


@pytest.mark.asyncio
async def test_executor() -> None:
    result = await get_details()
    assert isinstance(result, list)
    assert len(result) > 105
    for x in result:
        assert isinstance(x, Hero)
