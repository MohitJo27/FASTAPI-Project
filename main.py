from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse 
from model.predict import model, predict_output, MODEL_VERSION
import pandas as pd

app = FastAPI(title=" Insurance ", version= "0.0.01")
       
# Home end point

@app.get('/')
async def home():
    return{
        "Message": "Insurance Premium Predictor API"
    }

# Helth check
@app.get('/health')
async def health_check():
    return {
        'status': "OK",
        "Version": MODEL_VERSION,
        "Model_Loaded": model is not None
    }

## API for prediction
@app.post('/predict', response_model= PredictionResponse)
async def predict(data: UserInput) -> JSONResponse:
    try:
        user_input = pd.DataFrame([{
            'BMI': data.BMI,
            'age_group': data.age_group,
            'lifestyle_risk': data.lifestyle_risk,
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation

        }])

        pred = predict_output(user_input)
        return JSONResponse(status_code= 200, content= {'response': pred})
    
    except Exception as e:
        print(f"error in /delete: {e}") # consol log

        return JSONResponse(status_code= 500, content={
            'error': "Something went wrong!",
            "detail": str(e) 
        })    