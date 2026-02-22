from datetime import datetime

def generate_alert(row):
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_url": row["source_url"],
        "category": row["predicted_category"],
        "risk": row["risk_level"],
        "message": f"High risk {row['predicted_category']} activity detected"
    }