from fastapi.testclient import TestClient
from api.main import app
from api.utils import get_db
import sqlite3

client = TestClient(app)


def get_test_db():
    db = sqlite3.connect(":memory:")
    create_tables(db)
    yield db
    db.close()


# TODO: Populate test db with more values
def create_tables(db):
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE pokemons (
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
    cursor.execute(
        "INSERT INTO pokemons (name, type, species, height, weight, abilities, catch_rate, base_friendship, base_exp, growth_rate, gender, hp, attack, defense, sp_attack, sp_defense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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
        "INSERT INTO pokemons (name, type, species, height, weight, abilities, catch_rate, base_friendship, base_exp, growth_rate, gender, hp, attack, defense, sp_attack, sp_defense, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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


def test_get_pokemons_by_growth_rate_existing_growth_rate(client: TestClient = client):
    response = client.get("/pokemons/growth_rate/Medium Fast")
    assert response.status_code == 200

    json_data = response.json()

    assert any(pokemon["name"] == "Pikachu" for pokemon in json_data.values())
    assert all(
        "Medium Fast" in pokemon["growth_rate"] for pokemon in json_data.values()
    )


def test_get_pokemons_by_growth_rate_multiple_growth_rates(client: TestClient = client):
    response = client.get("/pokemons/growth_rate/Medium Slow")
    assert response.status_code == 200

    json_data = response.json()

    assert any(pokemon["name"] == "Charizard" for pokemon in json_data.values())
    assert all(
        "Medium Slow" in pokemon["growth_rate"] for pokemon in json_data.values()
    )


def test_get_pokemons_by_growth_rate_non_existing_growth_rate(
    client: TestClient = client,
):
    response = client.get("/pokemons/growth_rate/InvalidGrwothRate")
    assert response.status_code == 200

    json_data = response.json()

    assert json_data == {
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


def test_get_pokemons_by_growth_rate_partial_growth_rate(client: TestClient = client):
    response = client.get("/pokemons/growth_rate/Medium")
    assert response.status_code == 200

    json_data = response.json()

    assert any(
        pokemon["name"] == "Pikachu" or pokemon["name"] == "Charizard"
        for pokemon in json_data.values()
    )


def test_get_pokemons_by_growth_rate_invalid_growth_rate(client: TestClient = client):
    response = client.get("/pokemons/growth_rate/InvalidGrowthRate123")
    assert response.status_code == 200

    json_data = response.json()

    assert json_data == {
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
