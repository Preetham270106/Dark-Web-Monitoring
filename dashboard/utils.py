import pandas as pd

def load_processed_data():
    try:
        return pd.read_csv("data/processed_data.csv")
    except:
        return pd.DataFrame()

def load_alerts():
    try:
        return pd.read_csv("data/alerts.csv")
    except:
        return pd.DataFrame()