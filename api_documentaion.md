# 🔌 API Documentation

## Overview
The **AI Health Diagnostics Backend API** is built using FastAPI. It serves prediction endpoints, performs automatic input validation via Pydantic, and generates interactive OpenAPI documentation.

* **Base URL:** `https://ai-health-backend.onrender.com` *(Replace with your actual Render URL)*
* **Swagger UI Docs:** `https://ai-health-backend.onrender.com/docs`
* **ResssssssssssDoc Format:** `https://ai-health-backend.onrender.com/redoc`

---

## API Endpoints

### 1. Root Health Check
Verifies that the API service is active and accessible.

* **Method:** `GET`
* **Endpoint:** `/`
* **Response (200 OK):**
```json
{
  "status": "Active",
  "message": "Health Risk Prediction Service Online"
}