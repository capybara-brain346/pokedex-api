import polars as pl


def main() -> None:
    df: pl.DataFrame = pl.read_csv("data/pokemon_info7.csv")
    OUTPUT_PATH: str = "data/pokemon6.csv"
    selected_columns: list[str] = [
        "Name",
        "Type",
        "Species",
        "Height",
        "Weight",
        "Abilities",
        "Catch rate",
        "Base Friendship",
        "Base Exp.",
        "Growth Rate",
        "Gender",
        "HP",
        "Attack",
        "Defense",
        "Sp. Atk",
        "Sp. Def",
        "Speed",
    ]
    df = df.select(selected_columns)
    try:
        df.write_csv(OUTPUT_PATH)
        print(f"Data successfully saved to {OUTPUT_PATH}")
    except ValueError as e:
        print(f"Error has occured: {e}")


if __name__ == "__main__":
    main()
