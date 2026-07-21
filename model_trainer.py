import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score

def train_and_save_model():
    print("Generating synthetic health dataset...")
    np.random.seed(42)
    n_samples = 1000

    # Dataset Features: Age, BMI, Blood Pressure, Glucose Level, Cholesterol
    age = np.random.randint(20, 80, size=n_samples)
    bmi = np.random.uniform(18.5, 40.0, size=n_samples)
    bp = np.random.randint(90, 180, size=n_samples)
    glucose = np.random.randint(70, 200, size=n_samples)
    cholesterol = np.random.randint(150, 300, size=n_samples)

    # Risk Label Logic (1: High Risk, 0: Low Risk)
    risk = (
        (age > 50).astype(int) +
        (bmi > 28.0).astype(int) +
        (bp > 130).astype(int) +
        (glucose > 125).astype(int) +
        (cholesterol > 220).astype(int)
    ) >= 3
    target = risk.astype(int)

    df = pd.DataFrame({
        'age': age,
        'bmi': np.round(bmi, 1),
        'blood_pressure': bp,
        'glucose': glucose,
        'cholesterol': cholesterol,
        'target': target
    })

    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("Training Machine Learning Model (Random Forest)...")
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    print(f"\nModel Trained Successfully!")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"F1-Score: {f1:.2f}")
    print("\nClassification Report:\n", classification_report(y_test, predictions))

    # Save artifact
    joblib.dump(model, 'health_model.pkl')
    print("Saved model file to 'health_model.pkl'")

if __name__ == "__main__":
    train_and_save_model()