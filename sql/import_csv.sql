-- SQLite
.mode csv
.import data/pokemon.csv pokemons

SELECT * FROM pokemons;

PRAGMA table_info(pokemons);


SELECT COUNT(*) FROM pokemons;
