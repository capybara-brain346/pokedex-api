CREATE TABLE pokemons_test (
    name VARCHAR,
    type VARCHAR,
    species VARCHAR,
    height FLOAT,
    weight FLOAT,
    abilities VARCHAR,
    catch_rate INT,
    base_friendship INT,
    base_exp INT,
    growth_rate VARCHAR,
    gender VARCHAR,
    hp INT,
    attack INT,
    defense INT,
    sp_attack INT,
    sp_defense INT,
    speed INT 
)

DELETE FROM pokemons_test WHERE name='Name';

DELETE FROM pokemons_test
WHERE name NOT IN (
    SELECT name
    FROM pokemons_test
    LIMIT 20
)