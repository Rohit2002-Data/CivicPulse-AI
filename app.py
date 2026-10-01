import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import requests
import plotly.express as px

st.set_page_config(page_title="CivicPulse AI", page_icon="🌧️", layout="wide")

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "rainfall_tel_hr_karnataka_ka_2021_2025.csv.gz"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA)
    df["Data Acquisition Time"] = pd.to_datetime(
        df["Data Acquisition Time"], errors="coerce"
    )
    df["Telemetry Hourly Rainfall (mm)"] = pd.to_numeric(
        df["Telemetry Hourly Rainfall (mm)"], errors="coerce"
    )
    return df

df = load_data()

# Official IMD Bengaluru City station.
@st.cache_data(ttl=600)
def imd_current():
    urls = [
        "https://api.imd.gov.in/api/v1/current_wx?id=43295",
        "https://mausam.imd.gov.in/api/current_wx_api.php?id=43295",
    ]
    last_error = None
    for u in urls:
        try:
            r = requests.get(
                u, timeout=12,
                headers={"User-Agent": "CivicPulse-AI-Hackathon/1.0"}
            )
            r.raise_for_status()
            data = r.json()
            return (data[0] if isinstance(data, list) and data else data), u, None
        except Exception as e:
            last_error = str(e)
    return {}, None, last_error

weather, weather_url, weather_error = imd_current()

def num(keys):
    for key in keys:
        if key in weather:
            try:
                return float(str(weather[key]).replace(",", "").replace("%", ""))
            except Exception:
                pass
    return None

rain24 = num(["Last 24 hrs Rainfall", "Last_24_hrs_Rainfall", "rainfall", "Rainfall"])
temp = num(["Temperature", "temperature", "Temp", "temp"])
hum = num(["Humidity", "humidity", "RH", "rh"])

st.title("🌧️ CivicPulse AI")
st.subheader("Real-Time Bengaluru Rainfall Intelligence")
st.caption(
    "Karnataka Government hourly rainfall telemetry (2021–2025) + "
    "official IMD Bengaluru live weather"
)

# Filter Bengaluru-area observations.
blr = df[
    df["District"].astype(str).str.contains("Bangalore", case=False, na=False)
].copy()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Telemetry rows", f"{len(df):,}")
c2.metric("Bengaluru observations", f"{len(blr):,}")
c3.metric("IMD 24h rainfall", "—" if rain24 is None else f"{rain24:.1f} mm")
c4.metric("IMD temperature", "—" if temp is None else f"{temp:.1f} °C")

st.markdown("### 📊 Historical rainfall intelligence")

if len(blr):
    hourly = (
        blr.groupby(blr["Data Acquisition Time"].dt.date)["Telemetry Hourly Rainfall (mm)"]
        .mean()
        .reset_index(name="mean_hourly_rainfall_mm")
    )
    hourly["Data Acquisition Time"] = pd.to_datetime(hourly["Data Acquisition Time"])

    fig = px.line(
        hourly,
        x="Data Acquisition Time",
        y="mean_hourly_rainfall_mm",
        title="Bengaluru-area mean hourly telemetry rainfall",
        labels={
            "Data Acquisition Time": "Date",
            "mean_hourly_rainfall_mm": "Mean hourly rainfall (mm)"
        },
    )
    fig.update_layout(height=430, margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, use_container_width=True)

    station_summary = (
        blr.groupby(["Station", "District", "Latitude", "Longitude"], dropna=False)
        .agg(
            observations=("Telemetry Hourly Rainfall (mm)", "count"),
            mean_hourly_rainfall_mm=("Telemetry Hourly Rainfall (mm)", "mean"),
            max_hourly_rainfall_mm=("Telemetry Hourly Rainfall (mm)", "max"),
        )
        .reset_index()
        .sort_values("max_hourly_rainfall_mm", ascending=False)
    )

    st.markdown("### 🛰️ Rainfall stations")
    st.dataframe(
        station_summary.head(50),
        use_container_width=True,
        height=360,
    )

    st.markdown("### 📍 Station map")
    map_df = station_summary.dropna(subset=["Latitude", "Longitude"]).copy()
    fig_map = px.scatter_mapbox(
        map_df,
        lat="Latitude",
        lon="Longitude",
        size="observations",
        hover_name="Station",
        hover_data={
            "District": True,
            "mean_hourly_rainfall_mm": ":.2f",
            "max_hourly_rainfall_mm": ":.2f",
            "Latitude": False,
            "Longitude": False,
        },
        zoom=9.5,
        height=520,
    )
    fig_map.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=0, r=0, t=0, b=0),
    )
    st.plotly_chart(fig_map, use_container_width=True)

else:
    st.warning("No Bangalore-area observations were found in the supplied dataset.")

if weather_error:
    st.warning("Live IMD data could not be fetched right now. Historical telemetry remains available.")

st.markdown("---")
st.markdown("### Data provenance")
st.write(
    "Historical data: Karnataka Department hourly rainfall telemetry, 2021–2025. "
    "Live weather: IMD Bengaluru City station (43295)."
)
st.caption(
    "This dashboard is a hackathon decision-support prototype. It is not an official "
    "flood warning system. Follow official IMD/BBMP/KSDMA alerts for emergency decisions."
)
