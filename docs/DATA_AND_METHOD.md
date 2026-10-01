# Data and Method

## Historical dataset
CivicPulse AI uses one historical dataset:
**Karnataka Department — Rainfall Telemetry Hourly — 2021–2025**.

The CSV contains hourly telemetry rainfall observations and station metadata.

## Live weather
The app retrieves current weather for Bengaluru City from the official IMD API at runtime.

## Derived analytics
The app calculates station-level observation counts, mean hourly rainfall, and maximum hourly rainfall from the supplied historical telemetry. These are descriptive statistics, not official flood probabilities.

## Limitation
No verified historical flood-event labels are included in this repository, so the project does not train a supervised flood-probability model.
