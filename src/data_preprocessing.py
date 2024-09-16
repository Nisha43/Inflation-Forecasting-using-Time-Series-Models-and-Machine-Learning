import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath, skiprows=4)
    return data

def fill_missing_values(data):
    data.ffill(inplace=True)
    return data
