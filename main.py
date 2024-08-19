from fastapi import FastAPI, Depends
import sqlite3
from models import Query, ResponseModel
from typing import List

app = FastAPI(debug=True)
q = Query()


def get_db():
    db = sqlite3.connect("pokemon.db")
    try:
        yield db
    finally:
        db.close()


def format_response(response: List[any]) -> List[ResponseModel]:
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
    cursor = db.cursor()
    cursor.execute(q.name_query, (name,))
    response = cursor.fetchall()
    response_clean = format_response(response=response)

    return response_clean


@app.post("/pokemons/abilities/{abilities}")
def get_pokemons_by_abilities(
    abilities: str, db: sqlite3.Connection = Depends(get_db)
) -> List[ResponseModel]:
    cursor = db.cursor()
    abilities_binding = f"%{abilities}%"
    cursor.execute(q.ability_query, [abilities_binding])
    response = cursor.fetchall()
    response_clean = format_response(response=response)

    return response_clean


@app.post("/pokemons/type/{type}")
def get_pokemons_by_type(
    type: str, db: sqlite3.Connection = Depends(get_db)
) -> List[ResponseModel]:
    cursor = db.cursor()
    type_binding = f"%{type}%"
    cursor.execute(q.type_query, [type_binding])
    response = cursor.fetchall()
    response_clean = format_response(response=response)

    return response_clean


@app.post("/pokemons/size")
def get_pokemons_by_size(
    parameter: str,
    height: str | None = None,
    weight: str | None = None,
    db: sqlite3.Connection = Depends(get_db),
) -> List[ResponseModel]:
    cursor = db.cursor()

    print(height[0], height[1:])
    if parameter == "h":
        column = "height"
        operator = height[0]
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
    return response_clean
