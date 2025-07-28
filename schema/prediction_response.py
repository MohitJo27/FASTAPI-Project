from pydantic import BaseModel, Field
from typing import Dict, Literal

class PredictionResponse(BaseModel):
    predicted_category: Literal['High', 'Mediumn','Low'] = Field(
        ...,
        title= "Predicted Category",
        description= "The predicted insurance premium category",
        gt= 0,
        lt= 1,
        example= "High"
    )

    confidence: float = Field(
        ...,
        title= "Confidence Score",
        description= "Model's confidence scores for the predicted class (range: 0 to 1)",
        example= '0.332'
    )

    class_probabilities: Dict[str, float] = Field(
        ...,
        title="Class Probabilities",
        description= "Probabilities distributions across all possible classes",
        example= {
            'Low': 0.01,
            'Mediumn': 0.43,
            'High': 0.02
            }
    )