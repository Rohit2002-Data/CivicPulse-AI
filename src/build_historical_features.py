import pandas as pd
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
RAIN=BASE/'data'/'rainfall_telemetry_karnataka_2021_2025.csv'
OUT=BASE/'data'/'rainfall_station_historical_features.csv'

r=pd.read_csv(RAIN)
r['Telemetry Hourly Rainfall (mm)']=pd.to_numeric(r['Telemetry Hourly Rainfall (mm)'],errors='coerce').fillna(0)
r['Latitude']=pd.to_numeric(r['Latitude'],errors='coerce')
r['Longitude']=pd.to_numeric(r['Longitude'],errors='coerce')
r['_time']=pd.to_datetime(r['Data Acquisition Time'],errors='coerce')
r=r.dropna(subset=['Station','Latitude','Longitude','_time']).sort_values(['Station','_time'])

g=r.groupby('Station',group_keys=False)
r['rain_3h_mm']=g['Telemetry Hourly Rainfall (mm)'].transform(lambda s:s.rolling(3,min_periods=1).sum())
r['rain_6h_mm']=g['Telemetry Hourly Rainfall (mm)'].transform(lambda s:s.rolling(6,min_periods=1).sum())
r['rain_24h_mm']=g['Telemetry Hourly Rainfall (mm)'].transform(lambda s:s.rolling(24,min_periods=1).sum())

summary=r.groupby(['Station','Latitude','Longitude']).agg(
    observations=('Telemetry Hourly Rainfall (mm)','size'),
    mean_hourly_mm=('Telemetry Hourly Rainfall (mm)','mean'),
    max_hourly_mm=('Telemetry Hourly Rainfall (mm)','max'),
    p95_hourly_mm=('Telemetry Hourly Rainfall (mm)',lambda s:s.quantile(.95)),
    mean_24h_mm=('rain_24h_mm','mean'),
    max_24h_mm=('rain_24h_mm','max'),
    heavy_hours=('Telemetry Hourly Rainfall (mm)',lambda s:(s>=15).sum()),
    extreme_hours=('Telemetry Hourly Rainfall (mm)',lambda s:(s>=25).sum())
).reset_index()

summary.to_csv(OUT,index=False)
print(f'Saved {len(summary)} station summaries to {OUT}')
