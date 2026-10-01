# CivicPulse AI — Real-Time Rainfall Intelligence

A WarriorHacks 2.0 hackathon prototype using real Karnataka Government hourly rainfall telemetry from 2021–2025 and live IMD Bengaluru weather.

## Data
The `data/` folder intentionally contains **one dataset only**:

`rainfall_tel_hr_karnataka_ka_2021_2025.csv`

The dataset contains 683,619 hourly telemetry observations from Karnataka for 2021–2025.

## Live data
At runtime, the Streamlit app requests current weather from the official IMD Bengaluru City station (43295), with a fallback endpoint.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Important
The app does not claim to predict official flood probability. It presents historical rainfall intelligence and live weather context for decision support.
