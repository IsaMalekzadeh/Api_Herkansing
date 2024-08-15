import requests

BASE_URL = "http://127.0.0.1:8000"

def test_read_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sport Team Management API"}

def test_read_teams():
    response = requests.get(f"{BASE_URL}/teams")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_team():
    # Eerst een team aanmaken om te testen
    create_response = requests.post(f"{BASE_URL}/teams", json={"name": "Test Team", "city": "Test City"})
    assert create_response.status_code == 200
    team_id = create_response.json()["id"]

    response = requests.get(f"{BASE_URL}/teams/{team_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Team"

def test_get_teams_by_city():
    response = requests.get(f"{BASE_URL}/teams/by_city/?city=Test City")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


##### niet get endpoints


def test_create_team():
    response = requests.post(f"{BASE_URL}/teams", json={"name": "New Team", "city": "New City"})
    assert response.status_code == 200
    assert response.json()["name"] == "New Team"

def test_update_team():
    # Eerst een team aanmaken om te testen
    create_response = requests.post(f"{BASE_URL}/teams", json={"name": "Update Test Team", "city": "Update City"})
    assert create_response.status_code == 200
    team_id = create_response.json()["id"]

    # Team updaten
    response = requests.put(f"{BASE_URL}/teams/{team_id}", json={"name": "Updated Team", "city": "Updated City"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Team"

def test_delete_team():
    # Eerst een team aanmaken om te testen
    create_response = requests.post(f"{BASE_URL}/teams", json={"name": "Delete Test Team", "city": "Delete City"})
    assert create_response.status_code == 200
    team_id = create_response.json()["id"]

    # Team verwijderen
    response = requests.delete(f"{BASE_URL}/teams/{team_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Team deleted"
