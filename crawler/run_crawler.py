from crawler.onion_crawler import crawl_onion
import pandas as pd
import os

onion_sites = [
    "http://exampleforum.onion",
    "http://examplemarket.onion"
]

results = []

for site in onion_sites:
    data = crawl_onion(site)
    if data:
        results.append(data)

if results:
    df = pd.DataFrame(results)

    file_path = "data/raw_data.csv"
    file_exists = os.path.isfile(file_path)

    df.to_csv(
        file_path,
        mode="a",
        index=False,
        header=not file_exists
    )

    print("Crawling completed and data saved")
else:
    print("No data collected")