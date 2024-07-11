import pytest

from template.hello import hello


@pytest.mark.asyncio
async def test_hello() -> None:
    res = await hello()

    assert isinstance(res, str)
    assert "hello" in res.lower()
