import sys
import os
sys.path.append(os.getcwd())

from data.data_loader import load_processed_data
from data.data_saver import save_processed_data, save_alerts
from risk.risk_calculator import calculate_risk
from risk.alert_generator import generate_alert

df = load_processed_data()
df["risk_level"] = df.apply(calculate_risk, axis=1)

save_processed_data(df)

alerts = []
for _, row in df.iterrows():
    if row["risk_level"] == "HIGH":
        alerts.append(generate_alert(row))

if alerts:
    save_alerts(alerts)

print("Risk analysis and alert generation completed")