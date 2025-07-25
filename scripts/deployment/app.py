from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import pickle
import numpy as np
import os

app = FastAPI(title="Fraud Detection API")

# Cargar modelo
model = load("best_model.joblib")

# Cargar scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

class InputFeatures(BaseModel):
    features: list[float]

class Prediction(BaseModel):
    prediction: int

@app.post("/predict", response_model=Prediction)
def predict(input_data: InputFeatures):
    raw = np.array(input_data.features).reshape(1, -1)
    transformed = scaler.transform(raw) 
    y_pred = model.predict(transformed)
    return {"prediction": int(y_pred[0])}