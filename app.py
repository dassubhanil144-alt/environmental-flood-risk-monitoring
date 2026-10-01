from flask import Flask, render_template
import random
import pandas as pd
import joblib

app = Flask(__name__)

# Load your trained Random Forest model
model = joblib.load("model.pkl")


@app.route("/")
def home():

    # --------------------------------
    # SIMULATED LIVE SENSOR DATA
    # --------------------------------

    rainfall = random.uniform(50, 300)
    water_level = random.uniform(1, 10)
    discharge = random.uniform(500, 5000)
    soil_moisture = random.uniform(20, 100)
    population_density = random.uniform(1000, 10000)

    # --------------------------------
    # CALCULATE HAZARD
    # --------------------------------

    rainfall_score = rainfall / 300
    water_score = water_level / 10
    discharge_score = discharge / 5000

    hazard = (
        0.4 * rainfall_score +
        0.3 * water_score +
        0.3 * discharge_score
    )

    hazard = min(hazard, 1)

    # --------------------------------
    # CALCULATE EXPOSURE
    # --------------------------------

    exposure = population_density / 10000
    exposure = min(exposure, 1)

    # --------------------------------
    # CALCULATE VULNERABILITY
    # --------------------------------

    vulnerability = soil_moisture / 100
    vulnerability = min(vulnerability, 1)

    # --------------------------------
    # MODEL INPUT
    # --------------------------------

    live_input = pd.DataFrame({
        "Vulnerability": [vulnerability],
        "Hazard": [hazard],
        "Exposure": [exposure]
    })

    # --------------------------------
    # REAL ML PREDICTION
    # --------------------------------

    predicted_risk = model.predict(live_input)[0]

    # --------------------------------
    # RISK LEVEL
    # --------------------------------

    if predicted_risk < 0.1:
        risk_level = "Low"

    elif predicted_risk < 0.5:
        risk_level = "Medium"

    else:
        risk_level = "High"

    # --------------------------------
    # SEND DATA TO WEBSITE
    # --------------------------------

    return render_template(
        "index.html",
        rainfall=rainfall,
        water_level=water_level,
        discharge=discharge,
        soil_moisture=soil_moisture,
        population_density=population_density,
        hazard=hazard,
        exposure=exposure,
        vulnerability=vulnerability,
        predicted_risk=predicted_risk,
        risk_level=risk_level
    )

@app.route("/live-data")
def live_data():

    rainfall = random.uniform(50, 300)
    water_level = random.uniform(1, 10)
    discharge = random.uniform(500, 5000)
    soil_moisture = random.uniform(20, 100)
    population_density = random.uniform(1000, 10000)

    rainfall_score = rainfall / 300
    water_score = water_level / 10
    discharge_score = discharge / 5000

    hazard = (
        0.4 * rainfall_score +
        0.3 * water_score +
        0.3 * discharge_score
    )

    exposure = min(population_density / 10000, 1)
    vulnerability = min(soil_moisture / 100, 1)

    live_input = pd.DataFrame({
        "Vulnerability": [vulnerability],
        "Hazard": [hazard],
        "Exposure": [exposure]
    })

    predicted_risk = model.predict(live_input)[0]

    if predicted_risk < 0.1:
        risk_level = "Low"
    elif predicted_risk < 0.5:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "rainfall": rainfall,
        "water_level": water_level,
        "discharge": discharge,
        "soil_moisture": soil_moisture,
        "population_density": population_density,
        "hazard": hazard,
        "exposure": exposure,
        "vulnerability": vulnerability,
        "predicted_risk": predicted_risk,
        "risk_level": risk_level
    }
if __name__ == "__main__":
    app.run(debug=True)