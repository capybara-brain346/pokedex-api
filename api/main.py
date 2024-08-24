import sqlite3
from fastapi import FastAPI, Depends
from api.models import Query, ResponseModel
from api.utils import get_db, format_response, separate_operator_and_number

app = FastAPI(debug=True)
q = Query()


@app.get("/pokemons/name/{name}")
def get_pokemons_by_name(
    name: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    cursor.execute(q.name_query, (name,))
    response = cursor.fetchall()
    response_model = format_response(response=response)

    return response_model if response_model else {-1: response_model}


@app.get("/pokemons/abilities/{abilities}")
def get_pokemons_by_abilities(
    abilities: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    abilities_binding = f"%{abilities}%"
    cursor.execute(q.ability_query, [abilities_binding])
    response = cursor.fetchall()
    response_model = format_response(response=response)

    return response_model if response_model else {-1: response_model}


@app.get("/pokemons/type/{pokemon_type}")
def get_pokemons_by_type(
    pokemon_type: str, db: sqlite3.Connection = Depends(get_db)
) -> dict[int, ResponseModel]:
    cursor = db.cursor()
    type_binding = f"%{pokemon_type}%"
    cursor.execute(q.type_query, [type_binding])
    response = cursor.fetchall()
    response_model = format_response(response=response)

    return response_model if response_model else {-1: response_model}


@app.get("/pokemons/size")
def get_pokemons_by_size(
    height: str | None = None,
    weight: str | None = None,
    db: sqlite3.Connection = Depends(get_db),
) -> dict[int, ResponseModel]:
    cursor = db.cursor()

    response_model = ResponseModel()
    if height and weight:
        operator_h, value_h = separate_operator_and_number(height)
        operator_w, value_w = separate_operator_and_number(weight)

        cursor.execute(
            q.size_query_both.format(operator_h=operator_h, operator_w=operator_w),
            [value_h, value_w],
        )
        response = cursor.fetchall()
        response_model = format_response(response=response)
        return response_model
    elif height:
        operator, value = separate_operator_and_number(height)

        cursor.execute(
            q.size_query.format(column="height", operator=operator),
            [value],
        )
        response = cursor.fetchall()
        response_model = format_response(response=response)
        return response_model
    elif weight:
        operator, value = separate_operator_and_number(weight)
        print(operator, value)
        print(
            q.size_query.format(column="weight", operator=operator),
            [value],
        )
        cursor.execute(
            q.size_query.format(column="weight", operator=operator),
            [value],
        )
        response = cursor.fetchall()
        response_model = format_response(response=response)
        return response_model

    return {-1: response_model}
