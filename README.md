# CivicPulse AI
## Real-Time Rainfall Intelligence for Karnataka & Bengaluru

> A real-data civic intelligence platform that transforms government rainfall telemetry into interactive rainfall insights.

## Introduction

Rainfall is one of the most important environmental factors affecting communities. Changes in rainfall intensity and distribution can influence transportation, drainage systems, infrastructure, water management, and everyday activities.

Government agencies continuously collect rainfall measurements through monitoring stations. These systems generate large amounts of telemetry data containing rainfall measurements, timestamps, station information, administrative information, and geographic coordinates.

Although this information is valuable, raw telemetry data can be difficult to understand without data-processing and visualization tools.

**CivicPulse AI** transforms large-scale government rainfall telemetry into an interactive civic intelligence dashboard.

The project combines:

- Real Karnataka Government rainfall telemetry
- Historical hourly rainfall observations from 2021–2025
- Station-level rainfall analysis
- Geographic rainfall-station visualization
- Historical rainfall trends
- Bengaluru-focused analysis
- Live weather information from the India Meteorological Department (IMD)
- Interactive charts and tables
- A Streamlit-based web dashboard

The project was developed for **WarriorHacks 2.0**.

## Problem Statement

Rainfall monitoring systems produce large quantities of observations from different monitoring stations.

Raw rainfall data can contain hundreds of thousands of records, making it difficult for users to quickly answer questions such as:

- Where are rainfall monitoring stations located?
- How much rainfall has been recorded?
- Which stations have recorded higher rainfall?
- What are the historical rainfall patterns?
- How does rainfall vary across monitoring locations?
- What rainfall observations are associated with Bengaluru?
- What is the current weather situation?

Without a visualization and analysis layer, users would need to manually download, clean, analyze, and visualize the raw dataset.

CivicPulse AI provides this analysis through a single interactive dashboard.

## Proposed Solution

CivicPulse AI converts raw government rainfall telemetry into understandable rainfall intelligence.

The system follows this workflow:

Government Rainfall Data → Data Loading → Data Processing → Geographic Filtering → Station Statistics → Historical Analysis → Visualization → Streamlit Dashboard

Live IMD weather is integrated separately at runtime to provide current weather context.

## Project Objectives

1. Use authentic government rainfall data.
2. Analyze large-scale hourly rainfall telemetry.
3. Make rainfall data easier to understand.
4. Provide station-level rainfall statistics.
5. Visualize rainfall monitoring stations geographically.
6. Analyze historical rainfall patterns.
7. Provide a Bengaluru-focused rainfall view.
8. Integrate live IMD weather information.
9. Build an interactive and user-friendly dashboard.
10. Maintain transparent and reproducible data-processing methods.
11. Create a foundation for future environmental intelligence applications.

## Key Features

### 1. Historical Rainfall Analysis

CivicPulse AI analyzes real hourly rainfall telemetry collected between 2021 and 2025.

Users can explore historical rainfall observations through interactive visualizations and statistical summaries.

### 2. Station-Level Rainfall Analysis

The application groups rainfall observations by monitoring station.

For each station, the dashboard can provide:

- Station name
- District
- Latitude
- Longitude
- Observation count
- Mean hourly rainfall
- Maximum hourly rainfall

### 3. Interactive Rainfall Map

Latitude and longitude values are used to display rainfall monitoring stations on an interactive map.

Users can explore stations geographically and inspect their associated rainfall statistics.

### 4. Historical Rainfall Visualization

The application uses the timestamped rainfall observations to create historical rainfall visualizations.

Primary fields:

- `Data Acquisition Time`
- `Telemetry Hourly Rainfall (mm)`

### 5. Bengaluru-Focused Analysis

The historical dataset covers Karnataka. CivicPulse AI provides additional analysis for observations associated with Bangalore/Bengaluru districts.

### 6. Live IMD Weather

CivicPulse AI integrates the official India Meteorological Department API to retrieve current weather information.

Bengaluru City IMD station:

- Station ID: `43295`

### 7. Historical + Live Information

The platform combines two data layers:

- Historical Karnataka rainfall telemetry from 2021–2025
- Current Bengaluru weather from IMD

## Dataset

CivicPulse AI uses the **Karnataka Government hourly rainfall telemetry dataset covering 2021–2025**.

The repository stores the dataset in compressed form:

`data/rainfall_tel_hr_karnataka_ka_2021_2025.csv.gz`

### Dataset Summary

| Property | Details |
|---|---|
| Source | Karnataka Government rainfall telemetry |
| Geographic coverage | Karnataka |
| Historical period | 2021–2025 |
| Frequency | Hourly |
| Number of observations | 683,619 |
| Original CSV size | Approximately 79.6 MB |
| Compressed size | Approximately 4.3 MB |
| Dataset type | Real government data |
| Rows removed | None |

The dataset was compressed only to make it practical to store and distribute through GitHub. The underlying observations are preserved.

## Dataset Columns

The rainfall telemetry dataset contains:

- `SlNo`
- `Station`
- `Agency`
- `State LGD Code`
- `State`
- `District LGD Code`
- `District`
- `Tehsil`
- `Block`
- `Village`
- `River`
- `Basin`
- `Tributary`
- `Subtributary`
- `SubSubtributary`
- `Local River`
- `Latitude`
- `Longitude`
- `Data Acquisition Time`
- `Telemetry Hourly Rainfall (mm)`

Important fields include:

### Station

Name of the rainfall monitoring station.

### District

Administrative district associated with the observation.

### Latitude and Longitude

Geographic coordinates of the rainfall monitoring station.

### Data Acquisition Time

Timestamp associated with the rainfall telemetry observation.

### Telemetry Hourly Rainfall (mm)

Hourly rainfall measurement in millimeters.

## Data Processing Methodology

### Step 1 — Data Loading

The compressed rainfall dataset is loaded using Pandas.

```python
import pandas as pd

df = pd.read_csv(
    "data/rainfall_tel_hr_karnataka_ka_2021_2025.csv.gz",
    compression="gzip"
)
```

### Step 2 — Timestamp Processing

`Data Acquisition Time` is converted into datetime format for time-based analysis.

### Step 3 — Rainfall Conversion

`Telemetry Hourly Rainfall (mm)` is converted to numeric form for calculations.

### Step 4 — Geographic Processing

Latitude and longitude values are used to identify and visualize monitoring locations.

### Step 5 — Bengaluru Filtering

Observations associated with Bangalore/Bengaluru districts can be selected for focused analysis.

### Step 6 — Station Aggregation

Rainfall observations are grouped by monitoring station.

### Step 7 — Statistical Analysis

Descriptive statistics are calculated, including:

- Mean hourly rainfall
- Maximum hourly rainfall
- Observation count

### Step 8 — Visualization

Processed data is passed to Plotly and Streamlit to generate charts, tables, and maps.

## Rainfall Metrics

### Mean Hourly Rainfall

Mean hourly rainfall represents the average rainfall measurement across the available observations for a station.

### Maximum Hourly Rainfall

Maximum hourly rainfall represents the highest individual hourly rainfall observation recorded by a station within the available historical dataset.

### Observation Count

Observation count represents the number of rainfall telemetry observations available for a station.

## Historical Rainfall Analysis

CivicPulse AI uses timestamped rainfall observations to analyze historical rainfall patterns.

The application uses:

- `Data Acquisition Time` as the temporal variable
- `Telemetry Hourly Rainfall (mm)` as the rainfall measurement

The observations are transformed into time-based visualizations to help users understand changes in rainfall across the historical period.

## Station Analytics

Station-level analysis converts raw telemetry into summarized information.

For each station, the system can calculate:

- Station
- District
- Latitude
- Longitude
- Observation Count
- Mean Hourly Rainfall
- Maximum Hourly Rainfall

## Geographic Visualization

Rainfall stations are displayed using their latitude and longitude coordinates.

The interactive map allows users to:

- Explore station locations
- Identify monitoring coverage
- Inspect station information
- Compare station-level rainfall statistics
- Understand the geographic distribution of rainfall monitoring

## IMD Integration

Historical rainfall data provides long-term context, while IMD data provides current weather information.

CivicPulse AI uses:

- IMD Bengaluru City
- Station ID: `43295`

The application requests current weather information during runtime.

The two data layers are intentionally kept distinct:

**Historical layer:** Karnataka Government rainfall telemetry, 2021–2025.

**Live layer:** Current weather from the official IMD API.

## System Architecture

The overall architecture is:

```text
Karnataka Government Rainfall Telemetry
                |
                v
        Pandas / NumPy
        Data Processing
                |
                v
       Historical Analysis
                |
        +-------+-------+
        |       |       |
        v       v       v
     Charts   Tables   Maps
        |       |       |
        +-------+-------+
                |
                v
         Streamlit App
                ^
                |
        Official IMD API
        Current Weather
```

## Data Science Approach

The project demonstrates a complete data-science workflow:

Data Collection → Data Loading → Data Processing → Data Transformation → Aggregation → Descriptive Statistics → Historical Analysis → Geographic Analysis → Visualization → Interactive Dashboard

The project demonstrates practical use of:

- Data ingestion
- Data preprocessing
- Data transformation
- Aggregation
- Descriptive statistics
- Time-based analysis
- Geographic analysis
- Visualization
- API integration
- Dashboard development

## Future Machine Learning Direction

The current application focuses on rainfall intelligence and does not require a supervised flood-prediction model.

A future version could incorporate verified historical flood-event data.

A potential future dataset could combine:

Rainfall + Weather + Location + Historical Flood Events

Potential features could include:

- Recent rainfall
- Hourly rainfall
- Cumulative rainfall
- Maximum rainfall
- Number of high-rainfall observations
- Historical rainfall statistics
- Geographic characteristics
- Weather variables

Potential models could include:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

## Future Model Evaluation

A future supervised classification model could be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC
- Confusion Matrix
- Cross-validation

Such a model would require verified historical flood-event labels.

## Compressed Dataset

The original CSV is approximately 79.6 MB.

It is stored as:

`rainfall_tel_hr_karnataka_ka_2021_2025.csv.gz`

The compressed dataset is approximately 4.3 MB.

The complete dataset is preserved and can be read directly with Pandas.

```python
import pandas as pd

df = pd.read_csv(
    "data/rainfall_tel_hr_karnataka_ka_2021_2025.csv.gz",
    compression="gzip"
)
```

No manual extraction is required.

## Technology Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly

### Dashboard

- Streamlit

### API

- India Meteorological Department API

### Historical Data

- Karnataka Government rainfall telemetry

### Geographic Analysis

- Latitude
- Longitude
- Interactive mapping

## Project Structure

```text
CivicPulse-AI/
|
├── app.py
├── requirements.txt
├── README.md
|
├── data/
|   └── rainfall_tel_hr_karnataka_ka_2021_2025.csv.gz
|
├── docs/
|   ├── DATA_AND_METHOD.md
|   ├── OFFICIAL_SOURCES.md
|   └── DEVPOST_SUBMISSION.md
|
└── src/
    └── build_historical_features.py
```

## Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Enter the project directory:

```bash
cd CivicPulse-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in a web browser.

## Dashboard Workflow

When the application starts:

1. The compressed rainfall dataset is loaded.
2. Timestamps are converted.
3. Rainfall values are converted.
4. Bengaluru observations are identified.
5. Station statistics are calculated.
6. Historical rainfall visualization is generated.
7. Station-level tables are generated.
8. The interactive map is generated.
9. Current IMD weather is requested.
10. Results are displayed in the dashboard.

## Civic Use Case

CivicPulse AI demonstrates how public environmental data can be transformed into accessible civic technology.

Potential users include:

- Citizens
- Students
- Researchers
- Data analysts
- Developers
- Environmental researchers
- Urban-planning researchers
- Civic-technology developers

The dashboard makes it easier to explore government rainfall information without manually processing the raw dataset.

## WarriorHacks 2.0

CivicPulse AI was developed for **WarriorHacks 2.0**.

The project focuses on transforming large amounts of public environmental data into understandable information.

The project combines:

Real Government Data + Data Engineering + Data Science + Statistical Analysis + Geographic Visualization + API Integration + Interactive Dashboard

## Project Highlights

### Real Government Data

The project uses actual Karnataka Government rainfall telemetry rather than synthetic demonstration data.

### Large-Scale Dataset

The historical dataset contains **683,619 observations** covering 2021–2025.

### Historical Analysis

The application provides historical rainfall analysis from government telemetry.

### Bengaluru Focus

The application provides focused analysis of Bangalore/Bengaluru-related rainfall observations.

### Interactive Visualization

Users can explore rainfall data through charts, tables, and maps.

### Geographic Intelligence

Monitoring stations are visualized using geographic coordinates.

### Live Weather

The project integrates current IMD weather information.

### Reproducible

The repository includes application code, requirements, dataset, documentation, and processing code.

### Extensible

The architecture can be extended with additional datasets, verified flood-event data, advanced analytics, forecasting, machine learning, and alerts.

## Project Results

The implemented project provides:

- Analysis of 683,619 historical rainfall observations
- Historical rainfall analysis covering 2021–2025
- Station-level rainfall statistics
- Mean hourly rainfall calculations
- Maximum hourly rainfall calculations
- Observation counts
- Bengaluru-focused rainfall analysis
- Geographic visualization of monitoring stations
- Interactive rainfall charts
- Interactive station tables
- Live IMD weather integration
- A Streamlit-based interactive dashboard

The project demonstrates a complete workflow from raw government telemetry to an interactive civic application.

## Reproducibility

A developer can:

1. Clone the repository.
2. Install the required packages.
3. Load the included compressed dataset.
4. Run the Streamlit application.
5. Explore the dashboard.

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

## Data Integrity

CivicPulse AI uses real government rainfall telemetry.

The project does not create artificial rainfall observations for the dashboard.

The historical dataset is stored in compressed form for GitHub compatibility.

Compression changes the storage format but does not intentionally remove observations.

## Data Sources

### Karnataka Government Rainfall Telemetry

Historical hourly rainfall telemetry covering 2021–2025.

Official dataset:

https://www.nwdp.nwic.gov.in/en/dataset/rainfall-telemetry-hourly-karnataka-department

### India Meteorological Department

Official IMD API documentation:

https://api.imd.gov.in/public/api_reference.html

Official IMD API:

https://api.imd.gov.in/public/index.php

Bengaluru City station:

https://wis2box.imd.gov.in/oapi/collections/stations/items/0-20000-0-43295?f=html

Additional project source information is provided in:

`docs/OFFICIAL_SOURCES.md`

## Future Scope

CivicPulse AI can be expanded into a broader environmental intelligence platform.

Potential future features include:

### Advanced Rainfall Analytics

- Cumulative rainfall
- Rainfall intensity
- Rainfall thresholds
- Rainfall anomaly detection
- Station comparisons

### Geographic Intelligence

- Ward-level analysis
- Additional geographic layers
- Infrastructure information
- Drainage information
- Flood-prone-area information

### Weather Intelligence

- IMD warnings
- IMD nowcasts
- Additional weather parameters
- Short-term rainfall forecasting

### Machine Learning

- Verified flood-event datasets
- Flood-risk classification
- Rainfall prediction
- Anomaly detection
- Model explainability

### Platform Development

- Cloud deployment
- Mobile-friendly interface
- Automated notifications
- Real-time monitoring
- API-based public access

## Project Significance

CivicPulse AI demonstrates a complete transformation pipeline:

Raw Government Data → Data Engineering → Data Cleaning → Data Analysis → Statistical Processing → Geospatial Analysis → Visualization → Live API Integration → Interactive Civic Application

This demonstrates how data-science and software-engineering techniques can be combined to create practical civic technology from publicly available information.

## Conclusion

CivicPulse AI demonstrates how large-scale government rainfall telemetry can be transformed into an interactive and accessible civic intelligence platform.

The project works with **683,619 real rainfall observations from Karnataka covering 2021–2025** and converts those observations into station-level statistics, historical rainfall analysis, geographic visualization, and interactive dashboard components.

The integration of live IMD weather information adds a current-weather layer to complement the historical rainfall dataset.

The result is a unified platform combining:

- Historical Rainfall
- Station Analytics
- Geographic Visualization
- Bengaluru Analysis
- Live Weather

The project demonstrates practical implementation of Python, Pandas, NumPy, Plotly, Streamlit, geographic data, government datasets, API integration, statistical analysis, and interactive visualization.

CivicPulse AI also establishes a foundation for future environmental intelligence applications. Additional verified datasets could allow the platform to evolve toward more advanced rainfall analytics, forecasting, and machine-learning applications.

> **Turn complex government rainfall data into understandable, accessible, and useful civic intelligence.**

## Project Information

| Item | Details |
|---|---|
| Project | CivicPulse AI |
| Project Type | Civic Data Intelligence Platform |
| Hackathon | WarriorHacks 2.0 |
| Primary Focus | Karnataka & Bengaluru |
| Historical Data | Karnataka Government Rainfall Telemetry |
| Historical Period | 2021–2025 |
| Historical Observations | 683,619 |
| Live Data | India Meteorological Department |
| Programming | Python |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Geographic Analysis | Latitude & Longitude |

## Disclaimer

CivicPulse AI is an educational and hackathon project designed for data exploration, visualization, and civic awareness.

The information presented by the application should be interpreted as rainfall and weather information derived from the project's data sources.

For real-world emergency situations, users should follow official advisories and instructions issued by the India Meteorological Department, BBMP, Karnataka Government, and relevant authorities.

---

## CivicPulse AI

**Real Government Rainfall Data → Data Science → Civic Intelligence**

Built for **WarriorHacks 2.0**
