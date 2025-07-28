import joblib
import pandas as pd

# import the ml model
with open('model/model.joblib', 'rb') as f:
    model = joblib.load(f)

#mlflow
MODEL_VERSION= "0.1.0"

#get class lables from the model (important for matching probabilities to class names)

class_lables = model.classes_.tolist()

def predict_output(user_input: dict):

    df = pd.DataFrame(user_input)
    # prediction
    predict= model.predict(df)[0]

    #get probabilities for all class

    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    #Creating maping: {classname : probabilities}\
    class_probs = dict(
        zip(
            class_lables, map(
                lambda x: round(x, 4), probabilities 
            )
        )
    )

    return{
        'predicted_category': predict,
        'confidence': round(confidence, 4),
        'class_probabilities': class_probs
    }