from pydantic import BaseModel


class Query(BaseModel):
    name_query: str = "SELECT * FROM pokemons WHERE name=%s"
    type_query: str = "SELECT * FROM pokemons WHERE type ILIKE %s"
    ability_query: str = "SELECT * FROM pokemons WHERE abilities ILIKE %s"
    size_query: str = "SELECT * FROM pokemons WHERE {column} {operator} %s"
    size_query_both: str = (
        "SELECT * FROM pokemons WHERE height {operator_h} %s AND weight {operator_w} %s"
    )
    species_query: str = "SELECT * FROM pokemons WHERE species ILIKE %s"
    growth_rate_query: str = "SELECT * FROM pokemons WHERE growth_rate ILIKE %s"
    catch_rate_query: str = "SELECT * FROM pokemons WHERE catch_rate {operator} %s"
    base_friendship_query: str = (
        "SELECT * FROM pokemons WHERE base_friendship {operator} %s"
    )
    base_experience_query: str = "SELECT * FROM pokemons WHERE base_exp {operator} %s"


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
