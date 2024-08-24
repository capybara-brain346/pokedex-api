import sqlite3
from fastapi.testclient import TestClient
from api.main import (
    app,
)
from api.utils import get_db

client = TestClient(app)


def get_test_db():
    db = sqlite3.connect(":memory:")
    create_tables(db)
    yield db
    db.close()


def create_tables(db):
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE test_pokemons (
                        name TEXT,
                        type TEXT,
                        species TEXT,
                        height REAL,
                        weight REAL,
                        abilities TEXT,
                        catch_rate INTEGER,
                        base_friendship INTEGER,
                        base_exp INTEGER,
                        growth_rate TEXT,
                        gender TEXT,
                        hp INTEGER,
                        attack INTEGER,
                        defense INTEGER,
                        sp_attack INTEGER,
                        sp_defense INTEGER,
                        speed INTEGER
                    )""")
    # Insert test data
    cursor.execute(
        "INSERT INTO test_pokemons (name, type, species, height, weight, abilities, catch_rate, base_friendship, base_exp, growth_rate, gender, hp, attack, defense, sp_attack, sp_defense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            "Pikachu",
            "Electric",
            "Mouse Pokémon",
            0.4,
            6.0,
            "Static",
            190,
            50,
            112,
            "Medium Fast",
            "50% male, 50% female",
            45,
            80,
            50,
            75,
            60,
            120,
        ),
    )
    cursor.execute(
        "INSERT INTO test_pokemons (name, type, species, height, weight, abilities, catch_rate, base_friendship, base_exp, growth_rate, gender, hp, attack, defense, sp_attack, sp_defense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            "Charizard",
            "Fire",
            "Flame Pokémon",
            1.7,
            90.5,
            "Blaze",
            45,
            70,
            240,
            "Medium Slow",
            "87.5% male, 12.5% female",
            78,
            84,
            78,
            109,
            85,
            100,
        ),
    )
    db.commit()


app.dependency_overrides[get_db] = get_test_db


def test_get_pokemons_by_type_found():
    response = client.get("/pokemons/type/Electric")
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


def test_get_pokemons_by_type_not_found():
    response = client.get("/pokemons/type/Water")
    assert response.status_code == 200
    assert response.json() == {
        "-1": {
            "name": "",
            "type": "",
            "species": "",
            "height": -1.0,
            "weight": -1.0,
            "abilities": "",
            "catch_rate": -1,
            "base_friendship": -1,
            "base_exp": -1,
            "growth_rate": "",
            "gender": "",
            "hp": -1,
            "attack": -1,
            "defense": -1,
            "sp_attack": -1,
            "sp_defense": -1,
            "speed": -1,
        }
    }


def test_get_pokemons_by_type_partial_match():
    response = client.get("/pokemons/type/Fire")
    assert response.status_code == 200
    assert response.json() == {
        "0": {
            "name": "Charizard",
            "type": "Fire",
            "species": "Flame Pokémon",
            "height": 1.7,
            "weight": 90.5,
            "abilities": "Blaze",
            "catch_rate": 45,
            "base_friendship": 70,
            "base_exp": 240,
            "growth_rate": "Medium Slow",
            "gender": "87.5% male, 12.5% female",
            "hp": 78,
            "attack": 84,
            "defense": 78,
            "sp_attack": 109,
            "sp_defense": 85,
            "speed": 100,
        }
    }


def test_get_pokemons_by_type_invalid_request():
    response = client.get("/pokemons/type/")
    assert response.status_code == 404
