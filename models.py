"""
Module for defining SQL query templates used for retrieving Pokémon data.

This module contains the Query class, which provides SQL query templates
for various types of queries on the Pokémon database. The templates include
queries for selecting Pokémon by name, type, abilities, and size parameters.
The class also supports querying by both height and weight with specific
operators.

The Query class uses Pydantic for data validation and provides default SQL
query strings for common database operations.
"""

from pydantic import BaseModel


class Query(BaseModel):
    """
    Contains SQL query templates for retrieving Pokémon data from the database.

    Attributes:
        name_query (str): SQL query template to select Pokémon by name.
        type_query (str): SQL query template to select Pokémon by type.
        ability_query (str): SQL query template to select Pokémon by abilities.
        size_query (str): SQL query template to select Pokémon based on
        a size parameter (height or weight) with a specified operator.
        size_query_both (str): SQL query template to select Pokémon based on
        both height and weight with specified operators for each.

    Notes:
        - `{column}` and `{operator}` in `size_query` are
        placeholders for dynamic SQL column names and comparison operators.
        - `{operator_h}` and `{operator_w}` in `size_query_both` are
        placeholders for height and weight comparison operators.
    """

    name_query: str = "SELECT * FROM pokemons WHERE name=?"
    type_query: str = "SELECT * FROM pokemons WHERE type like ?"
    ability_query: str = "SELECT * FROM POKEMONS WHERE abilities like ?"
    size_query: str = "SELECT * FROM POKEMONS WHERE {column} {operator} ?"
    size_query_both: str = (
        "SELECT * FROM POKEMONS WHERE height {operator_h} ? AND weight {operator_w} ?"
    )


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
