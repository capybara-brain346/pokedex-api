import psycopg2
import pandas as pd
import os

neon_db_url = os.getenv("POSTGRES_CONNECTION_STRING")

csv_file_path = r"data\final_data\pokemon_combined.csv"

try:
    conn = psycopg2.connect(neon_db_url)
    cur = conn.cursor()

    with open(csv_file_path, "r") as f:
        cur.copy_expert("COPY pokemons FROM stdin WITH CSV HEADER DELIMITER as ','", f)

    conn.commit()
    cur.close()
    conn.close()

    print("Data successfully copied from CSV to Neon PostgreSQL.")
except Exception as e:
    print(f"Error: {e}")
