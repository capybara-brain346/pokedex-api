import requests
from bs4 import BeautifulSoup
import polars as pl
import time


class PokemonDataCollector:
    def __init__(self, base_url, csv_input_path, csv_output_path):
        self.base_url = base_url
        self.csv_input_path = csv_input_path
        self.csv_output_path = csv_output_path
        self.pokemon_info = []

    def clean_pokemon_name(self, name: str) -> str:
        return name.strip().lower().replace(" ", "-")

    def fetch_pokemon_data(self, pokemon_name: str):
        cleaned_name = self.clean_pokemon_name(pokemon_name)
        pokemon_url = f"{self.base_url}/{cleaned_name}"
        print(f"Collecting info for {pokemon_name}")

        try:
            resp = requests.get(url=pokemon_url)
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

        soup = BeautifulSoup(resp.text, "html.parser")
        info = {"Name": pokemon_name}

        tables = soup.find_all("table", class_="vitals-table")
        for table in tables:
            for row in table.find_all("tr"):
                header = row.find("th").text.strip()
                value = row.find("td").text.strip()

                if header in info:
                    if header == "Type":
                        types = " ".join([t.text for t in row.find_all("a")])
                        info["Type"] = types
                    elif header == "Abilities":
                        abilities = " ".join(
                            [a.text.strip() for a in row.find_all("a")]
                        )
                        info["Abilities"] = abilities
                    else:
                        info[header] = value
                else:
                    info[header] = value

        return info

    def collect_data(self):
        pokemon_names_df = pl.read_csv(self.csv_input_path)
        pokemon_names = pokemon_names_df["Pokemon Names"].to_list()

        for pokemon_name in pokemon_names[800:]:
            data = self.fetch_pokemon_data(pokemon_name)
            if data:
                self.pokemon_info.append(data)
            time.sleep(0.5)

    def save_to_csv(self):
        df = pl.DataFrame(self.pokemon_info)
        df.write_csv(self.csv_output_path)
        print(f"Data successfully saved to {self.csv_output_path}")


if __name__ == "__main__":
    collector = PokemonDataCollector(
        base_url="https://pokemondb.net/pokedex",
        csv_input_path="data/pokemon_names.csv",
        csv_output_path="data/pokemon_info7.csv",
    )
    collector.collect_data()
    collector.save_to_csv()
