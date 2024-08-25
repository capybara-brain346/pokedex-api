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

    Attributes:
        name (str): The name of the Pokémon.
                    Default is "NULL".
        type (str): The type of the Pokémon.
                    Default is "NULL".
        species (str): The species of the Pokémon. Default is "NULL".
        height (float | str): The height of the Pokémon,
        which can be a float or "NULL" as a string. Default is "NULL".
        weight (float | str): The weight of the Pokémon,
        which can be a float or "NULL" as a string. Default is "NULL".
        abilities (str): The abilities of the Pokémon. Default is "NULL".
        catch_rate (int | str): The catch rate of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        base_friendship (int | str): The base friendship of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        base_exp (int | str): The base experience points of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        growth_rate (str): The growth rate of the Pokémon. Default is "NULL".
        gender (str): The gender of the Pokémon. Default is "NULL".
        hp (int | str): The HP stat of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        attack (int | str): The attack stat of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        defense (int | str): The defense stat of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        sp_attack (int | str): The special attack stat of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        sp_defense (int | str): The special defense stat of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
        speed (int | str): The speed stat of the Pokémon,
        which can be an integer or "NULL" as a string. Default is "NULL".
    """

    # TODO improve validation
    name: str = "NULL"
    type: str = "NULL"
    species: str = "NULL"
    height: float | str = "NULL"
    weight: float | str = "NULL"
    abilities: str = "NULL"
    catch_rate: int | str = "NULL"
    base_friendship: int | str = "NULL"
    base_exp: int | str = "NULL"
    growth_rate: str | str = "NULL"
    gender: str = "NULL"
    hp: int | str = "NULL"
    attack: int | str = "NULL"
    defense: int | str = "NULL"
    sp_attack: int | str = "NULL"
    sp_defense: int | str = "NULL"
    speed: int | str = "NULL"
