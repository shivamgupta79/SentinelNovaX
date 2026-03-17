import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_query_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/query?disease=dengue&region=hyderabad")
    assert response.status_code == 200
    assert "SentinelNovaX" in response.json()
