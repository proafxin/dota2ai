import pytest

from dota2ai.collector.executor import get_heroes


@pytest.mark.asyncio
async def test_executor() -> None:
    result = await get_heroes()
    assert isinstance(result, list)
    assert len(result) == 0
