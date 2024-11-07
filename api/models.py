from pydantic import BaseModel


class Query(BaseModel):
    name_query: str = "SELECT * FROM POKEMONS WHERE name=?"
    type_query: str = "SELECT * FROM POKEMONS WHERE type like ?"
    ability_query: str = "SELECT * FROM POKEMONS WHERE abilities like ?"
    size_query: str = "SELECT * FROM POKEMONS WHERE {column} {operator} ?"
    size_query_both: str = (
        "SELECT * FROM POKEMONS WHERE height {operator_h} ? AND weight {operator_w} ?"
    )
    species_query: str = "SELECT * FROM POKEMONS WHERE species like ?"
    growth_rate_query: str = "SELECT * FROM POKEMONS WHERE growth_rate like ?"
    catch_rate_query: str = "SELECT * FROM POKEMONS WHERE catch_rate {operator} ?"
    base_friendship_query: str = (
        "SELECT * FROM POKEMONS WHERE base_friendship {operator} ?"
    )
    base_experience_query: str = "SELECT * FROM POKEMONS WHERE base_exp {operator} ?"


class ResponseModel(BaseModel):
    """
    Represents the data structure for a Pokémon response model.
    """

    name: str = "NULL"
    type: str = "NULL"
    species: str = "NULL"
    height: float = -1.0
    weight: float = -1.0
    abilities: str = "NULL"
    catch_rate: int = -1
    base_friendship: int = -1
    base_exp: int = -1
    growth_rate: str = "NULL"
    gender: str = "NULL"
    hp: int = -1
    attack: int = -1
    defense: int = -1
    sp_attack: int = -1
    sp_defense: int = -1
    speed: int = -1
