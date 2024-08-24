from pydantic import BaseModel


class Query(BaseModel):
    name_query: str = "SELECT * FROM test_pokemons WHERE name=?"
    type_query: str = "SELECT * FROM test_pokemons WHERE type like ?"
    ability_query: str = "SELECT * FROM test_pokemons WHERE abilities like ?"
    size_query: str = "SELECT * FROM test_pokemons WHERE {column} {operator} ?"
    size_query_both: str = "SELECT * FROM test_pokemons WHERE height {operator_h} ? AND weight {operator_w} ?"
