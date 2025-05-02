from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load('model/model.joblib')
vectorizer = joblib.load('model/vectorizer.joblib')

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    vec = vectorizer.transform([input.text])
    prediction = model.predict(vec)[0]
    sentiment = "Positive" if prediction == 1 else "Negative"
    return {"sentiment": sentiment}

