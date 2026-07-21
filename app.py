import streamlit as st
import requests

st.set_page_config(
    page_title="Healthcare AI Diagnostics",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 AI Health Risk Diagnostic Assistant")
st.markdown("Provide patient vital signs to analyze chronic disease risk level.")

st.divider()

# Input Form
with st.form("patient_form"):
    st.subheader("Patient Vitals Entry")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age (Years)", min_value=1, max_value=120, value=35)
        bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=50.0, value=24.5)
        bp = st.number_input("Blood Pressure (mmHg)", min_value=50, max_value=220, value=120)
        
    with col2:
        glucose = st.number_input("Glucose Level (mg/dL)", min_value=40, max_value=350, value=95)
        cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=400, value=190)

    submitted = st.form_submit_button("Run Risk Assessment")

if submitted:
    payload = {
        "age": age,
        "bmi": bmi,
        "blood_pressure": bp,
        "glucose": glucose,
        "cholesterol": cholesterol
    }
    
    API_URL = "http://127.0.0.1:8000/predict"
    
    try:
        response = requests.post(API_URL, json=payload, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            risk_label = data["risk_label"]
            confidence = data["confidence_score"] * 100
            
            st.divider()
            st.subheader("Diagnostic Assessment Result")
            
            if data["risk_prediction"] == 1:
                st.error(f"⚠️ **Result:** {risk_label}")
                st.warning(f"Confidence Level: {confidence:.2f}%")
                st.write("Recommendation: High risk indicators detected. Suggest follow-up medical testing.")
            else:
                st.success(f"✅ **Result:** {risk_label}")
                st.info(f"Confidence Level: {confidence:.2f}%")
                st.write("Recommendation: Patient vitals are within standard ranges.")
        else:
            st.error(f"API Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Error connecting to backend API! Ensure FastAPI is running on `http://127.0.0.1:8000`.")