import sqlite3
from fastapi import FastAPI, Depends, status, Response
from api.models import Query, ResponseModel
from api.utils import (
    get_db,
    format_response,
    separate_operator_and_number,
    clean_request,
)

app = FastAPI(debug=True)
q = Query()

# get by name
@app.get("/pokemons/name/{name}")
def get_pokemons_by_name(
    name: str,
    response: Response,
    db: sqlite3.Connection = Depends(get_db),
) -> dict[int, ResponseModel]:
    name = clean_request(name)
    cursor = db.cursor()
    cursor.execute(q.name_query, (name,))
    data = cursor.fetchall()
    data_model = format_response(data=data)
    if data_model:
        response.status_code = status.HTTP_200_OK
        return data_model
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {-1: data_model}

# get by abilities
@app.get("/pokemons/abilities/{abilities}")
def get_pokemons_by_abilities(
    abilities: str, response: Response, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    abilities = clean_request(abilities)
    cursor = db.cursor()
    abilities_binding = f"%{abilities}%"
    cursor.execute(q.ability_query, [abilities_binding])
    data = cursor.fetchall()
    data_model = format_response(data=data)

    if data_model:
        response.status_code = status.HTTP_200_OK
        return data_model
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {-1: data_model}

#get by type
@app.get("/pokemons/type/{pokemon_type}")
def get_pokemons_by_type(
    pokemon_type: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    binding = f"%{pokemon_type}%"
    cursor.execute(q.type_query, [binding])
    response = cursor.fetchall()
    response_model = format_response(data=response)

    return response_model if response_model else {-1: response_model}

# get by size
@app.get("/pokemons/size")
def get_pokemons_by_size(
    response: Response,
    height: str = "",
    weight: str = "",
    db: sqlite3.Connection = Depends(get_db),
) -> dict[int, ResponseModel]:
    cursor = db.cursor()

    data_model = ResponseModel()
    if height and weight: # if query param contain both height and weight
        operator_h, value_h = separate_operator_and_number(height)
        operator_w, value_w = separate_operator_and_number(weight)

        cursor.execute( # build sql query (will change in future)
            q.size_query_both.format(operator_h=operator_h, operator_w=operator_w),
            [value_h, value_w],
        )
        data = cursor.fetchall()
        data_model = format_response(data=data)
        return data_model

    elif height: #if query param contains only height
        operator, value = separate_operator_and_number(height)

        cursor.execute(
            q.size_query.format(column="height", operator=operator),
            [value],
        )
        data = cursor.fetchall()
        data_model = format_response(data=data)
        return data_model

    elif weight: # if query param only contains weight
        operator, value = separate_operator_and_number(weight)
        cursor.execute(
            q.size_query.format(column="weight", operator=operator),
            [value],
        )
        data = cursor.fetchall()
        data_model = format_response(data=data)
        return data_model

    response.status_code = status.HTTP_404_NOT_FOUND
    return {-1: data_model}

# get by species
@app.get("/pokemons/species/{pokemon_species}")
def get_pokemons_by_species(
    pokemon_species: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    binding = f"%{pokemon_species}%" # to format string to be used in a sql LIKE clause eg. WHERE species LIKE %{}%
    cursor.execute(q.species_query, [binding])
    response = cursor.fetchall()
    response_model = format_response(data=response)

    return response_model if response_model else {-1: response_model}

# get by growth rate
@app.get("/pokemons/growth_rate/{pokemon_growth_rate}")
def get_pokemons_by_growth_rate(
    pokemon_growth_rate: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    binding = f"%{pokemon_growth_rate}%"
    cursor.execute(q.growth_rate_query, [binding])
    response = cursor.fetchall()
    response_model = format_response(data=response)

    return response_model if response_model else {-1: response_model}

# get by catch rate
@app.get("/pokemons/catch_rate")
def get_pokemons_by_catch_rate(
    pokemon_catch_rate: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    operator, value = separate_operator_and_number(pokemon_catch_rate)
    cursor.execute(q.catch_rate_query.format(operator=operator), [value])
    response = cursor.fetchall()
    response_model = format_response(data=response)

    return response_model if response_model else {-1: response_model}

# get by base friendship
@app.get("/pokemons/base_friendship")
def get_pokemons_by_base_friendship(
    pokemon_base_friendship: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    operator, value = separate_operator_and_number(pokemon_base_friendship)
    cursor.execute(q.base_friendship_query.format(operator=operator), [value])
    response = cursor.fetchall()
    response_model = format_response(data=response)

    return response_model if response_model else {-1: response_model}

# get by base experience
@app.get("/pokemons/base_experience")
def get_pokemons_by_base_experience(
    pokemon_base_experience: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    operator, value = separate_operator_and_number(pokemon_base_experience)
    cursor.execute(q.base_experience_query.format(operator=operator), [value])
    response = cursor.fetchall()
    response_model = format_response(data=response)

    return response_model if response_model else {-1: response_model}
