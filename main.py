import os
import subprocess

print("\n==============================")
print(" DARK WEB MONITORING PIPELINE ")
print("==============================\n")

# ---------- STEP 1: Generate / Collect Raw Data ----------
print("STEP 1: Generating raw data...")
os.system("python data/sample_data_generator.py")

# Optional: If using real crawler later
# os.system("python crawler/run_crawler.py")

# ---------- STEP 2: NLP Preprocessing ----------
print("\nSTEP 2: Running NLP preprocessing...")
os.system("python nlp/run_nlp.py")

# ---------- STEP 3: ML Crime Classification ----------
print("\nSTEP 3: Running ML crime classification...")
os.system("python ml/run_ml.py")

# ---------- STEP 4: Risk Scoring & Alert Generation ----------
print("\nSTEP 4: Running risk analysis...")
os.system("python risk/run_risk.py")

print("\n==============================")
print(" PIPELINE EXECUTION COMPLETED ")
print("==============================")
print("\nNow run the dashboard using:")
print("streamlit run dashboard/app.py\n")