import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AQI Simple Reflex Agent",
    page_icon="🌍",
    layout="wide"
)

# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("Indian_Climate_Dataset_2024_2025.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# ============================================================
# SIMPLE REFLEX AGENT - AQI CATEGORY
# ============================================================

def aqi_category(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderate"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    else:
        return "Severe"


# ============================================================
# TEMPERATURE CLASSIFICATION
# ============================================================

def temperature_decision(temperature):

    if temperature >=37:
        return "Hot"

    elif temperature >=30 and temperature <37:
        return "Mild"

    else:
        return "Cool"


# ============================================================
# TOMORROW AQI PREDICTION
# ============================================================

def predict_tomorrow_aqi(current_aqi, row):

    predicted_aqi = current_aqi

    rules_fired = []

    # Rule 1: Low wind speed
    if row["Wind_Speed (km/h)"] < 5:
        predicted_aqi += 15
        rules_fired.append(
            "Low wind speed → AQI increased by 15"
        )

    # Rule 2: High humidity
    if row["Humidity (%)"] > 70:
        predicted_aqi += 10
        rules_fired.append(
            "High humidity → AQI increased by 10"
        )

    # Rule 3: Rainfall
    if row["Rainfall (mm)"] > 0:
        predicted_aqi -= 20
        rules_fired.append(
            "Rainfall present → AQI decreased by 20"
        )

    # Keep AQI between 0 and 500
    predicted_aqi = max(0, min(500, predicted_aqi))

    return round(predicted_aqi, 2), rules_fired


# ============================================================
# TITLE
# ============================================================

st.title("🌍 AQI Simple Reflex Agent")

st.write(
    "Select a state, city and date to analyze the current "
    "air quality and generate a basic rule-based prediction "
    "for tomorrow's AQI."
)

st.divider()

# ============================================================
# STATE DROPDOWN
# ============================================================

states = sorted(df["State"].dropna().unique())

selected_state = st.selectbox(
    "📍 Select State",
    states
)

# ============================================================
# CITY DROPDOWN
# ============================================================

state_data = df[df["State"] == selected_state]

cities = sorted(state_data["City"].dropna().unique())

selected_city = st.selectbox(
    "🏙️ Select City",
    cities
)

# Filter city
city_data = state_data[
    state_data["City"] == selected_city
]

# ============================================================
# DATE DROPDOWN
# ============================================================

dates = sorted(city_data["Date"].dt.date.unique())

selected_date = st.selectbox(
    "📅 Select Date",
    dates
)

# Get selected row
selected_data = city_data[
    city_data["Date"].dt.date == selected_date
]

if len(selected_data) == 0:

    st.error("No data available for the selected date.")

else:

    row = selected_data.iloc[0]

    # ========================================================
    # CURRENT CONDITIONS
    # ========================================================

    st.divider()

    st.subheader(
        f"📊 Current Conditions — {selected_city}, {selected_state}"
    )

    col1, col2, col3, col4 = st.columns(4)

    temperature = row["Temperature_Avg (°C)"]
    humidity = row["Humidity (%)"]
    wind_speed = row["Wind_Speed (km/h)"]
    rainfall = row["Rainfall (mm)"]
    current_aqi = row["AQI"]

    # Temperature
    with col1:
        st.metric(
            "🌡️ Temperature",
            f"{temperature:.1f} °C"
        )

    # Humidity
    with col2:
        st.metric(
            "💧 Humidity",
            f"{humidity:.1f} %"
        )

    # Wind
    with col3:
        st.metric(
            "💨 Wind Speed",
            f"{wind_speed:.1f} km/h"
        )

    # AQI
    with col4:
        st.metric(
            "🌫️ Current AQI",
            f"{current_aqi}"
        )

    # ========================================================
    # TEMPERATURE AGENT
    # ========================================================

    temp_decision = temperature_decision(temperature)

    st.subheader("🌡️ Temperature Simple Reflex Decision")

    if temp_decision == "Hot":

        st.error(
            f"🔥 HOT — Temperature is {temperature:.1f}°C"
        )

    elif temp_decision == "Mild":

        st.warning(
            f"🌤️ MILD — Temperature is {temperature:.1f}°C"
        )

    else:

        st.info(
            f"❄️ COOL — Temperature is {temperature:.1f}°C"
        )

    # ========================================================
    # AQI RESULT
    # ========================================================

    st.subheader("🌫️ Current AQI Analysis")

    calculated_category = aqi_category(current_aqi)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current AQI",
            f"{current_aqi}"
        )

    with col2:

        st.metric(
            "AQI Category",
            calculated_category
        )


    # ========================================================
    # TOMORROW AQI PREDICTION
    # ========================================================

    st.divider()

    st.subheader("🔮 Tomorrow's AQI Prediction")

    predicted_aqi, rules_fired = predict_tomorrow_aqi(
        current_aqi,
        row
    )

    predicted_category = aqi_category(predicted_aqi)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Predicted Tomorrow AQI",
            f"{predicted_aqi}"
        )

    with col2:

        st.metric(
            "Predicted Category",
            predicted_category
        )

    # ========================================================
    # RULES FIRED
    # ========================================================

    st.subheader("🧠 Agent Reasoning")

    if len(rules_fired) == 0:

        st.info(
            "No prediction adjustment rules were triggered."
        )

    else:

        st.write(
            "The following prediction rules were triggered:"
        )

        for rule in rules_fired:

            st.write("✅ " + rule)

    # ========================================================
    # ENVIRONMENT DATA
    # ========================================================

    st.divider()

    st.subheader("📋 Selected Environment Data")

    display_data = pd.DataFrame({
        "Parameter": [
            "State",
            "City",
            "Date",
            "Temperature",
            "Humidity",
            "Rainfall",
            "Wind Speed",
            "Current AQI",
            "AQI Category",
            "Temperature Decision",
            "Predicted Tomorrow AQI",
            "Predicted Tomorrow Category"
        ],

        "Value": [
            selected_state,
            selected_city,
            str(selected_date),
            f"{temperature:.1f} °C",
            f"{humidity:.1f} %",
            f"{rainfall:.1f} mm",
            f"{wind_speed:.1f} km/h",
            current_aqi,
            calculated_category,
            temp_decision,
            predicted_aqi,
            predicted_category
        ]
    })

    st.dataframe(
        display_data,
        use_container_width=True,
        hide_index=True
    )