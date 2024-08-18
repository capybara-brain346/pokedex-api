from pydantic import BaseModel


class Query(BaseModel):
    by_name: str = "SELECT * FROM pokemons WHERE name=?"
    by_type: str = "SELECT * FROM pokemons WHERE type like '%?%'"
    

