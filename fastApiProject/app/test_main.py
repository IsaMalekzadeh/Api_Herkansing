import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sport Team Management API"}

@pytest.mark.asyncio
async def test_read_teams():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.get("/teams")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Assuming teams are returned as a list

@pytest.mark.asyncio
async def test_read_team():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.get("/teams/1")
    assert response.status_code in [200, 404]  # 200 if the team exists, 404 if not
    if response.status_code == 200:
        assert "id" in response.json()
        assert "name" in response.json()
        assert "city" in response.json()

@pytest.mark.asyncio
async def test_get_teams_by_city():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.get("/teams/by_city/", params={"city": "New York"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Assuming teams are returned as a list

@pytest.mark.asyncio
async def test_create_team():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.post("/teams", json={"name": "Test Team", "city": "Test City"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Test Team"
    assert response.json()["city"] == "Test City"

@pytest.mark.asyncio
async def test_update_team():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.put("/teams/1", json={"name": "Updated Team", "city": "Updated City"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Team"
    assert response.json()["city"] == "Updated City"

@pytest.mark.asyncio
async def test_delete_team():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.delete("/teams/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Team deleted"}

@pytest.mark.asyncio
async def test_login_for_access_token():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.post("/token", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_read_users_me():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        # First, get a token
        token_response = await ac.post("/token", data={"username": "testuser", "password": "testpassword"})
        token = token_response.json()["access_token"]

        # Use the token to access the /users/me endpoint
        response = await ac.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "username" in response.json()
    assert "id" in response.json()
    assert "is_active" in response.json()
