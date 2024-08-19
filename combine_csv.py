"""
Modules to combine multiple csv into one.
"""

import glob
import pandas as pd


def combine_csv_files(file_pattern: str, output_file: str) -> None:
    """
    Combines multiple CSV files into a single CSV file.

    Args:
        file_pattern (str): The file pattern to match CSV files (e.g., '*.csv').
        output_file (str): The name of the output file where the combined data will be saved.

    Returns:
        None: This function does not return any value.

    Notes:
        - Uses `glob` to find all files matching the given pattern.
        - Reads each CSV file into a DataFrame and concatenates them.
        - Saves the combined DataFrame to the specified output file.
        - Prints a message indicating the number of files combined and the output file name.
    """

    csv_files = glob.glob(file_pattern)
    df_list = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print(f"Combined {len(csv_files)} files into {output_file}")


if __name__ == "__main__":
    combine_csv_files("data/final_data/*.csv", "pokemon_combined.csv")
