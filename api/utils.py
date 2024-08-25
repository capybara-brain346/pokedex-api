import sqlite3
from api.models import ResponseModel
from typing import List
import re


def get_db():
    db = sqlite3.connect("pokemon.db")
    try:
        yield db
    finally:
        db.close()


def format_response(data: List[any]) -> dict[int, ResponseModel]:
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
        for row_id, row in enumerate(data)
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


def clean_request(request_obj: str) -> str:
    return request_obj.strip().title()
