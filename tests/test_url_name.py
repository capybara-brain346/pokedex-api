from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_name_url(client: TestClient = client):
    response = client.get("/pokemons/name/Pikachu")
    assert response.status_code == 200
    assert response.json() == {
        "0": {
            "name": "Pikachu",
            "type": "Electric",
            "species": "Mouse Pokémon",
            "height": 0.4,
            "weight": 6.0,
            "abilities": "Static",
            "catch_rate": 190,
            "base_friendship": 50,
            "base_exp": 112,
            "growth_rate": "Medium Fast",
            "gender": "50% male, 50% female",
            "hp": 45,
            "attack": 80,
            "defense": 50,
            "sp_attack": 75,
            "sp_defense": 60,
            "speed": 120,
        }
    }


def test_name_fail(client: TestClient = client):
    response = client.get("/pokemons/name/Invalid")
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


def test_name_case_insensitive(client: TestClient = client):
    response = client.get("/pokemons/name/pIkAcHu")
    assert response.status_code == 200
    assert response.json() == {
        "0": {
            "name": "Pikachu",
            "type": "Electric",
            "species": "Mouse Pokémon",
            "height": 0.4,
            "weight": 6.0,
            "abilities": "Static",
            "catch_rate": 190,
            "base_friendship": 50,
            "base_exp": 112,
            "growth_rate": "Medium Fast",
            "gender": "50% male, 50% female",
            "hp": 45,
            "attack": 80,
            "defense": 50,
            "sp_attack": 75,
            "sp_defense": 60,
            "speed": 120,
        }
    }


def test_name_special_characters(client: TestClient = client):
    response = client.get("/pokemons/name/Pikachu!")
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


def test_name_trailing_spaces(client: TestClient = client):
    response = client.get("/pokemons/name/Pikachu%20")
    assert response.status_code == 200
    assert response.json() == {
        "0": {
            "name": "Pikachu",
            "type": "Electric",
            "species": "Mouse Pokémon",
            "height": 0.4,
            "weight": 6.0,
            "abilities": "Static",
            "catch_rate": 190,
            "base_friendship": 50,
            "base_exp": 112,
            "growth_rate": "Medium Fast",
            "gender": "50% male, 50% female",
            "hp": 45,
            "attack": 80,
            "defense": 50,
            "sp_attack": 75,
            "sp_defense": 60,
            "speed": 120,
        }
    }
