import xml.etree.ElementTree as ET
import pandas as pd
import streamlit as st
import plotly.express as px


# Load Apple Health export
tree = ET.parse("export.xml")
root = tree.getroot()

# Store all records
records = []

# Find every Record element anywhere in the XML
for record in root.iter("Record"):
    records.append(record.attrib)

# Convert to dataframe
df = pd.DataFrame(records)

# --------------------------
# STEP DATA
# --------------------------

steps_df = df[
    df["type"] == "HKQuantityTypeIdentifierStepCount"
].copy()

steps_df["startDate"] = pd.to_datetime(steps_df["startDate"])
steps_df["value"] = pd.to_numeric(steps_df["value"])

daily_steps = steps_df.groupby(
    steps_df["startDate"].dt.date
)["value"].sum().reset_index()

daily_steps.columns = ["date", "steps"]

# -------------------------
# DAILY STEP GRAPH
# -------------------------

st.header("Daily Step Count")

fig = px.line(
    daily_steps,
    x="date",
    y="steps",
    title="Daily Step Count"
)

fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# LOW ACTIVITY DAYS
# -------------------------

daily_steps["low_activity"] = (
    daily_steps["steps"] < 4000
)

burnout_days = daily_steps[
    daily_steps["low_activity"]
]

avg_steps = int(daily_steps["steps"].mean())
max_steps = int(daily_steps["steps"].max())
low_days = burnout_days.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Daily Steps",
    f"{avg_steps:,}"
)

col2.metric(
    "Highest Activity Day",
    f"{max_steps:,}"
)

col3.metric(
    "Low Recovery Days",
    low_days
)

st.header("Potential Low Recovery Days")

st.dataframe(burnout_days)

daily_steps.to_csv(
    "daily_steps.csv",
    index=False
)
# -------------------------
# PAGE SETTINGS
# -------------------------

st.set_page_config(
    page_title="Recovery Inequity Dashboard",
    layout="wide"
)

st.title("Recovery Inequity Dashboard")


st.markdown("""
This dashboard explores how wearable health data can reveal
patterns of recovery instability, stress, and burnout
in college students.
""")


# -------------------------
# STEP COUNT DATA
# -------------------------

steps_df = df[
    df["type"] == "HKQuantityTypeIdentifierStepCount"
].copy()

# Make sure data exists
if steps_df.empty:
    st.error("No step count data found.")
    st.stop()

# Convert dates
steps_df["startDate"] = pd.to_datetime(
    steps_df["startDate"],
    errors="coerce"
)

# Convert values to numbers
steps_df["value"] = pd.to_numeric(
    steps_df["value"],
    errors="coerce"
)

# Remove bad rows
steps_df = steps_df.dropna(
    subset=["startDate", "value"]
)

# Group by date
daily_steps = steps_df.groupby(
    steps_df["startDate"].dt.date
)["value"].sum().reset_index()

daily_steps.columns = ["date", "steps"]
