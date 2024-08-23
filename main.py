"""
Main API Module
"""

import sqlite3
import re
from typing import List, Annotated
from fastapi import FastAPI, Depends
from models import Query, ResponseModel

app = FastAPI(debug=True)
q = Query()


def get_db():
    db = sqlite3.connect("pokemon.db")
    try:
        yield db
    finally:
        db.close()


def format_response(response: List[any]) -> dict[int, ResponseModel]:
    return {
        row_id: ResponseModel(
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
        for row_id, row in enumerate(response)
    }


def separate_operator_and_number(
    size_request: str,
) -> tuple[str, float] | None:
    pattern: str = r"(>=|<=|>|<|=)(\d*\.?\d+)"

    match = re.match(pattern, size_request)

    if match:
        operator, number = match.groups()
        return (operator, float(number))
    else:
        raise ValueError("Invalid size_request format. Ensure the format is correct.")


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

        cursor.execute(
            q.size_query.format(column="weight", operator=operator),
            [weight],
        )
        response = cursor.fetchall()
        response_model = format_response(response=response)
        return response_model

    return {-1: response_model}
