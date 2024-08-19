"""
Main API Module
"""

import sqlite3
from typing import List
from fastapi import FastAPI, Depends
from models import Query, ResponseModel

app = FastAPI(debug=True)
q = Query()


def get_db():
    """
    Opens a connection to the SQLite database and yields it for use.

    The connection is automatically closed after use, ensuring proper resource management.

    Yields:
        sqlite3.Connection: An open connection to the SQLite database.

    Closes:
        The database connection is closed after the operation is complete.
    """

    db = sqlite3.connect("pokemon.db")
    try:
        yield db
    finally:
        db.close()


def format_response(response: List[any]) -> List[ResponseModel]:
    """
    Transforms a raw database response into a list of ResponseModel instances.

    Args:
        response (List[any]): A list of tuples,
        each representing a row from the database query result.

    Returns:
        List[ResponseModel]: A list of ResponseModel instances
        where each instance corresponds to a row in the database.
    """

    return [
        ResponseModel(
            name=row[0],
            type=row[1],
            species=row[2],
            height=row[3],
            weight=row[4],
            abilities=row[5],
            catch_rate=row[6],
            base_friendship=row[7],
            base_exp=row[8],
            growth_rate=row[9],
            gender=row[10],
            hp=row[11],
            attack=row[12],
            defense=row[13],
            sp_attack=row[14],
            sp_defense=row[15],
            speed=row[16],
        )
        for row in response
    ]


@app.get("/pokemons/name/{name}")
def get_pokemons_by_name(
    name: str, db: sqlite3.Connection = Depends(get_db)
) -> List[ResponseModel]:
    """
    Retrieves a list of Pokémon from the database
    that match the specified name.

    Args:
        name (str): The name of the Pokémon to search for.
        db (sqlite3.Connection, optional): The database connection,
        provided by dependency injection.

    Returns:
        List[ResponseModel]: A list of ResponseModel instances
        representing the Pokémon that match the specified name.
    """

    cursor = db.cursor()
    cursor.execute(q.name_query, (name,))
    response = cursor.fetchall()
    response_clean = format_response(response=response)

    return response_clean


@app.get("/pokemons/abilities/{abilities}")
def get_pokemons_by_abilities(
    abilities: str, db: sqlite3.Connection = Depends(get_db)
) -> List[ResponseModel]:
    """
    Retrieves a list of Pokémon from the database
    that have the specified abilities.

    Args:
        abilities (str): A substring of abilities
        to search for in the database.
        db (sqlite3.Connection, optional): The database connection,
        provided by dependency injection.

    Returns:
        List[ResponseModel]: A list of ResponseModel instances representing the
        Pokémon that have abilities matching the specified substring.
    """

    cursor = db.cursor()
    abilities_binding = f"%{abilities}%"
    cursor.execute(q.ability_query, [abilities_binding])
    response = cursor.fetchall()
    response_clean = format_response(response=response)

    return response_clean


@app.get("/pokemons/type/{pokemon_type}")
def get_pokemons_by_type(
    pokemon_type: str, db: sqlite3.Connection = Depends(get_db)
) -> List[ResponseModel]:
    """
    Retrieves a list of Pokémon from the database
    that match the specified type.

    Args:
        pokemon_type (str): A substring of the type to
        search for in the database.
        db (sqlite3.Connection, optional): The database connection,
        provided by dependency injection.

    Returns:
        List[ResponseModel]: A list of ResponseModel instances
        representing the Pokémon that match the specified type.
    """

    cursor = db.cursor()
    type_binding = f"%{pokemon_type}%"
    cursor.execute(q.type_query, [type_binding])
    response = cursor.fetchall()
    response_clean = format_response(response=response)

    return response_clean


@app.get("/pokemons/size")
def get_pokemons_by_size(
    parameter: str,
    height: str | None = None,
    weight: str | None = None,
    db: sqlite3.Connection = Depends(get_db),
) -> List[ResponseModel] | str:
    """
    Retrieves a list of Pokémon from the database
    based on size parameters such as height or weight.

    Args:
        parameter (str): A parameter to specify the
        size criteria ('h' for height, 'w' for weight, 'wh' for both).

        height (str, optional): A string specifying the
        height and comparison operator (e.g., '>1.2').

        weight (str, optional): A string specifying the
        weight and comparison operator (e.g., '<10.0').

        db (sqlite3.Connection, optional): The database connection,
        provided by dependency injection.

    Returns:
        List[ResponseModel] | str:
            - A list of ResponseModel instances representing Pokémon
            that match the specified size criteria if valid.
            - A string "Invalid Parameter" if the provided
            parameter is not recognized.
    """

    cursor = db.cursor()

    print(height[0], height[1:])
    if parameter == "h":
        column = "height"
        operator = height[0]
        response_clean = ResponseModel()

        cursor.execute(
            q.size_query.format(column=column, operator=operator),
            [float(height[1:])],
        )
        response = cursor.fetchall()
        response_clean = format_response(response=response[1:])
    elif parameter == "w":
        column = "weight"
        operator = weight[0]
        cursor.execute(
            q.size_query.format(column=column, operator=operator),
            [float(weight[1:])],
        )
        response = cursor.fetchall()
        response_clean = format_response(response=response[1:])
    elif parameter == "wh":
        operator_h = height[0]
        operator_w = weight[0]
        cursor.execute(
            q.size_query_both.format(operator_h=operator_h, operator_w=operator_w),
            [float(height[1:]), float(weight[1:])],
        )
        response = cursor.fetchall()
        response_clean = format_response(response=response[1:])
    else:
        return "Invalid Paramter"
    return response_clean
