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


def test_get_pokemons_by_catch_rate_equal(client: TestClient = client):
    response = client.get("/pokemons/catch_rate?pokemon_catch_rate==190")
    assert response.status_code == 200

    json_data = response.json()
    assert any(pokemon["name"] == "Pikachu" for pokemon in json_data.values())
    assert all(pokemon["catch_rate"] == 190 for pokemon in json_data.values())


def test_get_pokemons_by_catch_rate_greater_than(client: TestClient = client):
    response = client.get("/pokemons/catch_rate?pokemon_catch_rate=>70")
    assert response.status_code == 200

    json_data = response.json()
    assert any(pokemon["name"] == "Pikachu" for pokemon in json_data.values())
    assert all(pokemon["catch_rate"] > 70 for pokemon in json_data.values())


def test_get_pokemons_by_catch_rate_less_than(client: TestClient = client):
    response = client.get("/pokemons/catch_rate?pokemon_catch_rate=<50")
    assert response.status_code == 200

    json_data = response.json()
    assert any(pokemon["name"] == "Charizard" for pokemon in json_data.values())
    assert all(pokemon["catch_rate"] <= 70 for pokemon in json_data.values())


def test_get_pokemons_by_catch_rate_non_existing_rate(client: TestClient = client):
    response = client.get("/pokemons/catch_rate?pokemon_catch_rate==500")
    assert response.status_code == 200

    json_data = response.json()
    assert json_data == {
        "-1": {
            "name": "NULL",
            "type": "NULL",
            "species": "NULL",
            "height": -1.0,
            "weight": -1.0,
            "abilities": "NULL",
            "catch_rate": -1,
            "base_friendship": -1,
            "base_exp": -1,
            "growth_rate": "NULL",
            "gender": "NULL",
            "hp": -1,
            "attack": -1,
            "defense": -1,
            "sp_attack": -1,
            "sp_defense": -1,
            "speed": -1,
        }
    }
