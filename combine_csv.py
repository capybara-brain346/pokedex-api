import glob
import pandas as pd


def combine_csv_files(file_pattern: str, output_file: str) -> None:
    csv_files = glob.glob(file_pattern)
    df_list = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print(f"Combined {len(csv_files)} files into {output_file}")


if __name__ == "__main__":
    combine_csv_files("data/final_data/*.csv", "pokemon_combined.csv")
