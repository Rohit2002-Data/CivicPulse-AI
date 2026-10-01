# CivicPulse AI — Devpost Draft

## Inspiration
Bengaluru has officially identified locations vulnerable to flooding, but static vulnerability maps do not automatically tell communities what deserves attention when weather conditions change.

## What it does
CivicPulse AI connects the official BBMP/KSRSAC vulnerability layer with Karnataka Government hourly rainfall telemetry and live IMD weather information.

The user can:
- explore official vulnerable locations,
- see the nearest rainfall telemetry station,
- inspect historical rainfall context,
- see current IMD conditions,
- receive a transparent current attention score,
- understand the difference between official observations and derived analytics.

## Technical craft
Python, Pandas, NumPy, Streamlit, Plotly, Requests, geospatial nearest-neighbor calculations, rolling rainfall feature engineering and live API integration.

## Data transparency
The project uses the real government datasets supplied by the participant. It does not fabricate flood-event labels. The attention score is explicitly a decision-support indicator, not an official flood probability.

## Future work
Add verified historical flood-event timestamps, drainage/water-level telemetry, elevation and drainage-network features, and then train and validate a temporal/spatial ML model.
