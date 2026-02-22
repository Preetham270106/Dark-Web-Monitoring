import pandas as pd

def load_raw_data():
    return pd.read_csv("data/raw_data.csv")

def load_processed_data():
    return pd.read_csv("data/processed_data.csv")

def load_alerts():
    return pd.read_csv("data/alerts.csv")