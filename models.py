from pydantic import BaseModel


class Query(BaseModel):
    name_query: str = "SELECT * FROM pokemons WHERE name=?"
    type_query: str = "SELECT * FROM pokemons WHERE type like ?"
    ability_query: str = "SELECT * FROM POKEMONS WHERE abilities like ?"
    size_query: str = "SELECT * FROM POKEMONS WHERE {column} {operator} ?"
    size_query_both: str = "SELECT * FROM POKEMONS WHERE height {operator_h} ? AND weight {operator_w} ?"


class ResponseModel(BaseModel):
    name: str
    type: str
    species: str
    height: float | str
    weight: float | str
    abilities: str
    catch_rate: int | str
    base_friendship: int | str
    base_exp: int | str
    growth_rate: str | str
    gender: str
    hp: int | str
    attack: int | str
    defense: int | str
    sp_attack: int | str
    sp_defense: int | str
    speed: int | str
