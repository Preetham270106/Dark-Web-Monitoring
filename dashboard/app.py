import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dashboard.utils import load_processed_data, load_alerts

st.set_page_config(
    page_title="Dark Web Threat Intelligence Dashboard",
    layout="wide"
)

st.title("🛡️ Dark Web Monitoring for Cyber Crime Prevention")
st.caption("AI-Based Threat Intelligence & Risk Analysis Dashboard")

processed_df = load_processed_data()
alerts_df = load_alerts()

# ================= SUMMARY METRICS =================
st.markdown("## 📊 System Overview")

col1, col2, col3 = st.columns(3)

col1.metric("📄 Total Posts Analyzed", len(processed_df))
col2.metric("🚨 High Risk Alerts", len(alerts_df))
col3.metric(
    "🧠 Crime Categories",
    processed_df["predicted_category"].nunique() if not processed_df.empty else 0
)

st.divider()

# ================= BAR CHART =================
st.markdown("## 📈 Crime Category Distribution")

if not processed_df.empty:
    category_counts = processed_df["predicted_category"].value_counts()

    colors = [
        "#1f77b4", "#ff7f0e", "#2ca02c",
        "#d62728", "#9467bd", "#8c564b",
        "#e377c2"
    ]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        category_counts.index,
        category_counts.values,
        color=colors[:len(category_counts)]
    )

    ax.set_xlabel("Crime Category")
    ax.set_ylabel("Number of Occurrences")
    ax.set_title("Detected Cyber Crime Categories")

    ax.bar_label(bars, padding=3)
    plt.xticks(rotation=30)

    st.pyplot(fig)
else:
    st.info("No processed data available")

st.divider()

# ================= PIE CHART =================
st.markdown("## ⚠️ Risk Level Distribution")

if "risk_level" in processed_df.columns:
    risk_counts = processed_df["risk_level"].value_counts()

    pie_colors = ["#d62728", "#ffbf00", "#2ca02c"]

    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(
        risk_counts,
        labels=risk_counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=pie_colors,
        explode=[0.08 if r == "HIGH" else 0 for r in risk_counts.index],
        shadow=True
    )

    ax2.set_title("Threat Risk Level Breakdown")
    st.pyplot(fig2)
else:
    st.info("Risk data not available")

st.divider()

# ================= ALERT TABLE =================
st.markdown("## 🚨 High Risk Threat Alerts")

if not alerts_df.empty:
    st.dataframe(
        alerts_df.sort_values("timestamp", ascending=False),
        use_container_width=True
    )
else:
    st.success("✅ No high-risk threats detected")

st.divider()

# ================= DATA VIEW =================
with st.expander("🔍 View Processed Threat Intelligence Data"):
    if not processed_df.empty:
        st.dataframe(processed_df.tail(25), use_container_width=True)