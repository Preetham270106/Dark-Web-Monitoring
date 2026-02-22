import pandas as pd
import os

def save_processed_data(dataframe):
    dataframe.to_csv("data/processed_data.csv", index=False)

def save_alerts(alerts_list):
    df = pd.DataFrame(alerts_list)
    file_exists = os.path.isfile("data/alerts.csv")

    df.to_csv(
        "data/alerts.csv",
        mode="a",
        index=False,
        header=not file_exists
    )