from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_abilities_match(client: TestClient = client):
    response = client.get("/pokemons/abilities/Static")
    json_data = response.json()
    assert response.status_code == 200
    assert any(pokemon["name"] == "Pikachu" for pokemon in json_data.values())


def test_abilities_no_match(client: TestClient = client):
    response = client.get("/pokemons/abilities/NonexistentAbility")
    assert response.status_code == 404
    assert response.json() == {
        "-1": {
            "name": "NULL",
            "type": "NULL",
            "species": "NULL",
            "height": "NULL",
            "weight": "NULL",
            "abilities": "NULL",
            "catch_rate": "NULL",
            "base_friendship": "NULL",
            "base_exp": "NULL",
            "growth_rate": "NULL",
            "gender": "NULL",
            "hp": "NULL",
            "attack": "NULL",
            "defense": "NULL",
            "sp_attack": "NULL",
            "sp_defense": "NULL",
            "speed": "NULL",
        }
    }


def test_abilities_case_insensitive(client: TestClient = client):
    response = client.get("/pokemons/abilities/static")
    json_data = response.json()
    assert response.status_code == 200
    assert any(pokemon["name"] == "Pikachu" for pokemon in json_data.values())


def test_abilities_special_characters(client: TestClient = client):
    response = client.get("/pokemons/abilities/Static!")
    assert response.status_code == 404
    assert response.json() == {
        "-1": {
            "name": "NULL",
            "type": "NULL",
            "species": "NULL",
            "height": "NULL",
            "weight": "NULL",
            "abilities": "NULL",
            "catch_rate": "NULL",
            "base_friendship": "NULL",
            "base_exp": "NULL",
            "growth_rate": "NULL",
            "gender": "NULL",
            "hp": "NULL",
            "attack": "NULL",
            "defense": "NULL",
            "sp_attack": "NULL",
            "sp_defense": "NULL",
            "speed": "NULL",
        }
    }


def test_abilities_trailing_spaces(client: TestClient = client):
    response = client.get("/pokemons/abilities/Static%20")
    json_data = response.json()
    assert response.status_code == 200
    assert any(pokemon["name"] == "Pikachu" for pokemon in json_data.values())
