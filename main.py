from fastapi import FastAPI, requests
import sqlite3
from models import Query

app = FastAPI(debug=True)
q = Query()


def by_name(name: str):
    with sqlite3.connect("pokemon.db") as conn:
        data = conn.execute(
            q.by_name,
            (name,),
        )
        return data.fetchall()


@app.get("/pokemons/name/{pokemon_name}")
def get_pokemons_by_name(pokemon_name: str):
    return by_name(name=pokemon_name)

@app.post("/pokemons/abilities/{abilities}")
def get_pokemons_by_abilities(abilities: str):
    pass
