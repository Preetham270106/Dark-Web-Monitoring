import pandas as pd
from datetime import datetime, timedelta
import random

sources = [
    "forum_alpha.onion",
    "market_beta.onion",
    "leaks_gamma.onion"
]

texts = [
    "Selling ransomware builder with full documentation",
    "Fresh credit card dumps from US banks",
    "Database dump of 2 million user credentials",
    "Discussion about DDoS attack techniques",
    "Listing of illegal firearms and ammunition",
    "Selling cocaine and LSD via encrypted channels"
]

categories = [
    "Cyber Attack",
    "Financial Fraud",
    "Data Leak",
    "Cyber Attack",
    "Weapons Trade",
    "Drug Trafficking"
]

data = []

for i in range(30):
    index = random.randint(0, len(texts) - 1)
    data.append({
        "source_url": sources[random.randint(0, 2)],
        "timestamp": (datetime.now() - timedelta(days=random.randint(0, 10))).strftime("%Y-%m-%d %H:%M:%S"),
        "raw_text": texts[index],
        "true_category": categories[index]
    })

df = pd.DataFrame(data)
df.to_csv("data/raw_data.csv", index=False)

print("Sample raw_data.csv generated successfully")