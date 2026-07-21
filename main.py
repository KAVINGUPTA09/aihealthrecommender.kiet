from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np
import os

app = FastAPI(
    title="AI Health Diagnostics API",
    description="Backend API service for disease risk prediction.",
    version="1.0.0"
)

MODEL_PATH = "health_model.pkl"

# Load Model
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

class PatientVitals(BaseModel):
    age: int = Field(..., ge=1, le=120, description="Patient age in years")
    bmi: float = Field(..., ge=10.0, le=60.0, description="Body Mass Index")
    blood_pressure: int = Field(..., ge=50, le=250, description="Systolic Blood Pressure (mmHg)")
    glucose: int = Field(..., ge=40, le=400, description="Fasting Glucose Level (mg/dL)")
    cholesterol: int = Field(..., ge=100, le=500, description="Serum Cholesterol (mg/dL)")

@app.get("/")
def root():
    return {"status": "Active", "message": "Health Risk Prediction Service Online"}

@app.get("/health")
def health_check():
    return {"model_loaded": model is not None}

@app.post("/predict")
def predict_health_risk(vitals: PatientVitals):
    if model is None:
        raise HTTPException(status_code=500, detail="Model file not found. Train model first.")
    
    input_data = np.array([[
        vitals.age,
        vitals.bmi,
        vitals.blood_pressure,
        vitals.glucose,
        vitals.cholesterol
    ]])
    
    prediction = int(model.predict(input_data)[0])
    probabilities = model.predict_proba(input_data)[0]
    confidence = float(np.max(probabilities))
    
    status = "High Risk" if prediction == 1 else "Low Risk"
    
    return {
        "status": "Success",
        "risk_prediction": prediction,
        "risk_label": status,
        "confidence_score": round(confidence, 4)
    }