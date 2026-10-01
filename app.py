import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import requests
import plotly.express as px

st.set_page_config(page_title="CivicPulse AI",page_icon="🌧️",layout="wide")
BASE=Path(__file__).resolve().parent
LOC=BASE/"data/bbmp_flood_locations_with_nearest_station.csv"
ST=BASE/"data/bengaluru_rainfall_station_summary.csv"

loc=pd.read_csv(LOC)
stations=pd.read_csv(ST)

# Runtime IMD connection. APIs may require network access/availability.
@st.cache_data(ttl=600)
def imd_current():
    urls=[
        "https://api.imd.gov.in/api/v1/current_wx?id=43295",
        "https://mausam.imd.gov.in/api/current_wx_api.php?id=43295"
    ]
    for u in urls:
        try:
            x=requests.get(u,timeout=12,headers={"User-Agent":"CivicPulse-AI-Hackathon/1.0"})
            x.raise_for_status()
            d=x.json()
            return (d[0] if isinstance(d,list) and d else d),u,None
        except Exception as e: err=str(e)
    return {},None,err

weather,url,err=imd_current()

def num(keys):
    for k in keys:
        if k in weather:
            try:return float(str(weather[k]).replace(",","").replace("%",""))
            except:pass
    return None
rain24=num(["Last 24 hrs Rainfall","Last_24_hrs_Rainfall","rainfall","Rainfall"])
temp=num(["Temperature","temperature","Temp","temp"])
hum=num(["Humidity","humidity","RH","rh"])

st.title("🌧️ CivicPulse AI")
st.subheader("Real-Time Bengaluru Flood Intelligence")
st.caption("BBMP/KSRSAC flood vulnerability + Karnataka Government hourly rainfall + IMD live weather")

c1,c2,c3,c4=st.columns(4)
c1.metric("Official vulnerable points",len(loc))
c2.metric("24h IMD rainfall","—" if rain24 is None else f"{rain24:.1f} mm")
c3.metric("Temperature","—" if temp is None else f"{temp:.1f} °C")
c4.metric("Humidity","—" if hum is None else f"{hum:.0f}%")

# Historical rainfall context
st.markdown("### 📊 Historical rainfall intelligence")
st.write("The supplied Karnataka Department telemetry file contains hourly observations from 2021–2025. The app uses those observations to provide station-level historical context; it does not invent flood-event labels.")

# Map with vulnerability + nearest station
if rain24 is None:
    current_factor=0
else:
    current_factor=min(max(rain24/60,0),1)

m=loc.copy()
m["attention_score"]=np.clip(35+55*current_factor+10*np.clip(1-m["station_distance_km"]/10,0,1),0,100)
m["status"]=pd.cut(m["attention_score"],[-1,40,65,101],labels=["Monitor","Elevated","High Attention"]).astype(str)

left,right=st.columns([1.35,1])
with left:
    st.markdown("### 📍 Bengaluru vulnerability map")
    fig=px.scatter_mapbox(m,lat="latitude",lon="longitude",color="status",
        hover_name="location_name",hover_data={"ward_name":True,"zone":True,
        "nearest_station":True,"station_distance_km":":.2f","attention_score":":.0f",
        "latitude":False,"longitude":False},zoom=10.3,height=600,
        color_discrete_map={"Monitor":"#2ca02c","Elevated":"#ffbf00","High Attention":"#d62728"})
    fig.update_layout(mapbox_style="open-street-map",margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig,use_container_width=True)

with right:
    st.markdown("### 🛰️ Rainfall stations")
    st.dataframe(stations.head(30),use_container_width=True,height=350)
    st.markdown("### What is official vs derived?")
    st.info("Official: BBMP/KSRSAC vulnerability points, Karnataka telemetry rainfall, IMD weather. Derived: nearest-station mapping, rolling rainfall features, and the transparent attention score.")

st.markdown("---")
choice=st.selectbox("Inspect a vulnerable location",m["location_name"].astype(str).tolist())
x=m[m["location_name"].astype(str)==choice].iloc[0]
a,b,c,d=st.columns(4)
a.metric("Attention",f"{x.attention_score:.0f}/100")
b.metric("Ward",str(x.ward_name))
c.metric("Zone",str(x.zone))
d.metric("Nearest station",str(x.nearest_station))
st.write(f"**Location:** {x.location_name}")
st.write(f"**Coordinates:** {x.latitude:.6f}, {x.longitude:.6f}")
st.write(f"**Distance to nearest rainfall station:** {x.station_distance_km:.2f} km")

if x.attention_score>=65: st.error("HIGH ATTENTION — monitor this known vulnerable location against current weather and official warnings.")
elif x.attention_score>=40: st.warning("ELEVATED ATTENTION — monitor rainfall and official warnings.")
else: st.success("MONITOR — no elevated attention from the current rainfall signal.")

st.caption("Prototype only. This is not an official emergency warning. Follow IMD/BBMP/KSDMA official alerts.")
