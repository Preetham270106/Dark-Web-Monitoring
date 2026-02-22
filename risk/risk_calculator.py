from datetime import datetime
from risk.severity_config import CRIME_SEVERITY, KEYWORD_SEVERITY

def calculate_risk(row):
    score = 0

    category = row["predicted_category"]
    text = row["clean_text"]
    timestamp = row["timestamp"]

    score += CRIME_SEVERITY.get(category, 1)

    for keyword, weight in KEYWORD_SEVERITY.items():
        if keyword in text:
            score += weight

    post_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    age_hours = (datetime.now() - post_time).total_seconds() / 3600

    if age_hours < 24:
        score += 2
    elif age_hours < 72:
        score += 1

    if score >= 8:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    else:
        return "LOW"