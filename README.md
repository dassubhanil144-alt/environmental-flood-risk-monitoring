
# AI-Powered Environmental Flood Risk Monitoring & Early Warning Dashboard

A machine-learning based environmental monitoring and flood-risk assessment system built using Python, Random Forest, and Flask.

## Overview

Flood-prone areas require timely assessment of environmental conditions to identify potentially hazardous situations.

This project analyzes environmental risk using three main indicators:

* Vulnerability
* Hazard
* Exposure

A Random Forest Regression model is trained to estimate flood risk from these indicators. The trained model is then integrated into a Flask-based web dashboard that displays environmental readings and continuously updates the predicted risk.

The current web application uses simulated environmental sensor values to demonstrate the complete monitoring and prediction workflow.

---

## Problem Statement

Environmental parameters such as rainfall, water level, river discharge, soil moisture, and population exposure can provide useful information about potential flood conditions. However, interpreting these parameters together can be difficult without an integrated analytical system.

The objective of this project is to develop a software-based environmental flood-risk monitoring system that:

1. Processes environmental and risk-related data.
2. Calculates hazard, exposure, and vulnerability indicators.
3. Uses machine learning to estimate flood risk.
4. Displays the results through a web dashboard.
5. Demonstrates continuously changing environmental conditions using simulated sensor data.

---

## System Workflow

```text
Environmental Parameters
          |
          v
   Hazard Calculation
          |
          v
   Exposure Calculation
          |
          v
 Vulnerability Calculation
          |
          v
   Random Forest Model
          |
          v
    Risk Prediction
          |
          v
    Flask Web Dashboard
          |
          v
   Live Risk Monitoring
```

---

## Features

* Environmental parameter monitoring
* Hazard score calculation
* Exposure calculation
* Vulnerability calculation
* Random Forest-based flood-risk prediction
* Flask web dashboard
* Simulated live environmental data
* Automatic dashboard updates
* Risk level classification
* Environmental risk visualization

---

## Machine Learning Model

The project uses a **Random Forest Regressor** to estimate flood risk.

### Input Features

* Vulnerability
* Hazard
* Exposure

### Target Variable

```text
Risk
```

The dataset contains **742 records** with the main fields:

```text
ID
Vulnerability
Hazard
Exposure
Risk
```

---

## Model Training

The dataset was divided into training and testing sets using an 80:20 split.

```text
Training samples: 593
Testing samples: 149
```

The Random Forest model was configured as:

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

---

## Model Evaluation

The model achieved the following results on the test data:

```text
Mean Absolute Error: 0.0092
R² Score: 0.9687
```

These results represent the performance of the model on the project's test split.

---

## Feature Importance

The trained model produced the following feature importance values:

```text
Exposure        0.790189
Hazard          0.179457
Vulnerability   0.030354
```

These values describe how the trained model used the available features when making predictions on this dataset.

---

## Environmental Monitoring

The Flask application simulates environmental readings to demonstrate the monitoring pipeline.

The simulated parameters include:

* Rainfall
* Water Level
* River Discharge
* Soil Moisture
* Population Density

These values are processed to derive:

```text
Hazard
Exposure
Vulnerability
```

The resulting values are passed to the trained Random Forest model to generate a predicted risk value.

---

## Risk Prediction

The model produces a numerical risk value which is converted into a risk level for display on the dashboard.

```text
Predicted Risk
      |
      v
  Risk Level
      |
      +---- Low
      |
      +---- Medium
      |
      +---- High
```

---

## Web Dashboard

The Flask dashboard displays:

* Rainfall
* Water Level
* River Discharge
* Soil Moisture
* Population Density
* Hazard
* Exposure
* Vulnerability
* Predicted Risk
* Risk Level

The dashboard periodically requests new simulated data through the Flask `/live-data` endpoint, allowing the displayed environmental values and prediction to change automatically.

### Dashboard Preview

![Environmental Flood Risk Dashboard](Screenshots/dashboard.png)

---

## Technologies Used

### Programming & Data Science

* Python
* Pandas
* Scikit-learn
* Random Forest
* Joblib
* Jupyter Notebook

### Web Development

* Flask
* HTML
* CSS
* JavaScript

---

## Project Structure

```text
environmental-flood-risk-monitoring/
│
├── data/
│
├── model/
│   └── train_model.ipynb
│
├── Screenshots/
│   └── dashboard.png
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/dassubhanil144-alt/environmental-flood-risk-monitoring.git
```

### 2. Open the project directory

```bash
cd environmental-flood-risk-monitoring
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the dashboard

Open the following address in your web browser:

```text
http://127.0.0.1:5000
```

---

## How It Works

The application generates simulated environmental readings:

```text
Rainfall
Water Level
River Discharge
Soil Moisture
Population Density
```

These values are converted into the three model inputs:

```text
Vulnerability
Hazard
Exposure
```

The Random Forest model then predicts the environmental risk:

```text
Vulnerability
       +
     Hazard
       +
    Exposure
       |
       v
Random Forest Model
       |
       v
Predicted Risk
       |
       v
Risk Level
```

The prediction is finally displayed on the Flask web dashboard.

---

## Current Limitations

* Environmental readings are simulated rather than collected from physical sensors.
* The machine-learning model is trained on the available project dataset.
* The dashboard is intended as an educational and portfolio prototype.
* The system has not been validated as an operational flood-warning system.
* Real-world deployment would require reliable environmental measurements and field validation.

---

## Future Improvements

Future versions of the project could include:

* Integration with real IoT environmental sensors
* Real-time rainfall and water-level measurements
* Location-based risk monitoring
* Historical data storage
* Database integration
* Automated notifications and alerts
* Interactive geographical risk visualization
* Improved validation using real-world environmental data
* Online deployment

---

## Project Background

This project was initially developed while exploring an environmental monitoring problem for a student hackathon and was later continued as an independent machine-learning and web-development project.

The current implementation focuses on the machine-learning, data-processing, simulated monitoring, and web-dashboard components.

---

## Author

**Subhanil Das**

CSE - Data Science

---

## Disclaimer

This project is an educational and portfolio prototype.

The predictions generated by this system should not be used as an operational flood-warning system or as a replacement for official disaster-management and emergency information.
