# 🩺 AI-Powered Health Risk Diagnostic Assistant

An end-to-end Machine Learning application designed to evaluate patient health parameters and predict potential chronic disease risks. Built under the **Healthcare & Digital Health Track** for the Major Project submission.

---

## 📌 Features

- **Predictive AI Engine:** Utilizes a Random Forest Classifier trained on key health metrics (Age, BMI, Blood Pressure, Glucose, Cholesterol).
- **RESTful API Backend:** Fast, lightweight, and robust backend built with **FastAPI** featuring integrated Swagger OpenAPI documentation[cite: 1].
- **Interactive Web UI:** Simple and clean user dashboard developed using **Streamlit**[cite: 1].
- **Real-Time Risk Assessment:** Generates immediate risk classifications and confidence scores.

---

## 🛠️ Technology Stack

| Layer | Technology Used |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy, Joblib[cite: 1] |
| **Backend Framework** | FastAPI, Uvicorn[cite: 1] |
| **Frontend Framework**| Streamlit[cite: 1] |
| **API Client** | Requests[cite: 1] |

---

## 📁 Repository Structure

```text
ai-health-predictor/
│
├── requirements.txt         # Project dependencies
├── model_trainer.py         # Script to train and save the ML model
├── main.py                  # FastAPI backend server
├── app.py                   # Streamlit frontend application
├── health_model.pkl         # Trained model binary artifact
├── TECHNICAL_REPORT.md      # Detailed technical justification & architecture
└── README.md                # Project documentation