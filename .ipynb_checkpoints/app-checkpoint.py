import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("water_quality_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Smart Water Quality Prediction", layout="centered")

st.title("💧 Smart Water Quality Prediction")
st.write("Input water parameters below to evaluate whether the sample is safe for human consumption.")

col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH Level (0-14)", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
    hardness = st.number_input("Hardness (mg/L)", min_value=0.0, value=196.0, step=1.0)
    solids = st.number_input("Total Dissolved Solids (ppm)", min_value=0.0, value=20000.0, step=100.0)
    chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, value=7.1, step=0.1)
    sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, value=333.0, step=1.0)

with col2:
    conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, value=426.0, step=1.0)
    organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, value=14.2, step=0.1)
    trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, value=66.3, step=0.1)
    turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, value=3.9, step=0.1)

if st.button("Predict Water Quality"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]
    prediction_proba = model.predict_proba(scaled_data)[0][1] * 100

    st.write("---")
    if prediction == 1:
        st.success(f"✅ **Potable (Safe to Drink)** — Model Confidence: {prediction_proba:.2f}%")
    else:
        st.error(f"❌ **Not Potable (Unsafe to Drink)** — Model Confidence: {100 - prediction_proba:.2f}%")