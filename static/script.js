function updateDashboard() {

    fetch("/live-data")
        .then(response => response.json())
        .then(data => {

            document.getElementById("rainfall").textContent =
                data.rainfall.toFixed(2) + " mm";

            document.getElementById("water_level").textContent =
                data.water_level.toFixed(2) + " m";

            document.getElementById("discharge").textContent =
                data.discharge.toFixed(2) + " m³/s";

            document.getElementById("soil_moisture").textContent =
                data.soil_moisture.toFixed(2) + " %";

            document.getElementById("population_density").textContent =
                data.population_density.toFixed(0);

            document.getElementById("hazard").textContent =
                data.hazard.toFixed(3);

            document.getElementById("exposure").textContent =
                data.exposure.toFixed(3);

            document.getElementById("vulnerability").textContent =
                data.vulnerability.toFixed(3);

            document.getElementById("predicted_risk").textContent =
                (data.predicted_risk * 100).toFixed(1) + "%";

            document.getElementById("risk_level").textContent =
                "Risk Level: " + data.risk_level;
        });
}


// Update every 5 seconds
setInterval(updateDashboard, 5000);