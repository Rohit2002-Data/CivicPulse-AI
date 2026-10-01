# CivicPulse AI 🌧️
## Real-Time Bengaluru Flood Intelligence

Final real-data hackathon package.

### Real data included
1. **BBMP/KSRSAC flood-vulnerable locations** — the actual KML supplied for this project.
2. **Karnataka Department Rainfall Telemetry, 2021–2025** — the actual 683,619-row CSV supplied for this project.
3. **IMD live weather** — queried at runtime from the official IMD API for Bengaluru-City station 43295.

### Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

### What the application does
- Maps officially identified flood-vulnerable locations.
- Links each location to its nearest Karnataka rainfall telemetry station.
- Provides historical station-level rainfall statistics.
- Requests current IMD weather at runtime.
- Calculates a transparent **Flood Attention Score** from vulnerability + current rainfall context.

### Scientific transparency
The supplied datasets do not contain verified time-stamped flood-event labels. Therefore this project does **not** pretend that a supervised ML model predicts flood probability. It is a real-time decision-support prototype.

A future ML version should join rainfall telemetry with verified historical flood-event outcomes before training and validating a predictive model.

### Official sources
- BBMP/KSRSAC: https://data.opencity.in/dataset/flooding-locations-in-bengaluru-urban
- IMD API: https://api.imd.gov.in/public/api_reference.html
- National Water Data Portal: https://www.nwdp.nwic.gov.in/en/dataset/rainfall-telemetry-hourly-karnataka-department

**Not an official emergency-warning system. Follow government alerts.**
