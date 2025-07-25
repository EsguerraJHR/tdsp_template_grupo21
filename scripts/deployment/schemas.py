from pydantic import BaseModel
from typing import List

class InputFeatures(BaseModel):
    features: List[float]

class Prediction(BaseModel):
    prediction: int