import pandas as pd


def load_data_from_csv(path):
    # Load the newly uploaded CSV file to examine the first few rows and the structure of the data
    new_data = pd.read_csv(path)

    return new_data


def save_data_to_csv(data, path):
    # Save the cleaned data to a new file
    data.to_csv(path, index=False)
    print(f"Data saved to {path}")
    return path
