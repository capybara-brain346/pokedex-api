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

    name_query: str = "SELECT * FROM test_pokemons WHERE name=?"
    type_query: str = "SELECT * FROM test_pokemons WHERE type like ?"
    ability_query: str = "SELECT * FROM test_pokemons WHERE abilities like ?"
    size_query: str = "SELECT * FROM test_pokemons WHERE {column} {operator} ?"
    size_query_both: str = "SELECT * FROM test_pokemons WHERE height {operator_h} ? AND weight {operator_w} ?"
