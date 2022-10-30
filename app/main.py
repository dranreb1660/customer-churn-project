import pandas as pd
import numpy as np
import pickle as pkl
import uvicorn
from fastapi import FastAPI
from app.customer_churn import CustomerChurn

probability_threshold = 0.275

#create app object
app = FastAPI(title='Customer Churn', version='1.0', description='Random forest model is used for prediction')

def load_artifact(fname):
    with open(fname, mode='rb') as f:
        return pkl.load(f)

le = load_artifact('./models/le.pkl')
classifier = load_artifact('./models/rf_model.pkl')
features = load_artifact('./models/features.pkl')
categorical_columns = load_artifact('./models/categorical_columns.pkl')

#index/ home route
@app.get('/')
@app.get('/home')
def home():
    return {'message': 'System is healthy'}

@app.post('/predict')
def predict_churn(data:CustomerChurn):
    data_dict = data.dict()
    data_df = pd.DataFrame.from_dict([data_dict])
    data_df = data_df[features]
    data_df[categorical_columns] = le.transform(data_df[categorical_columns])

    predicted_prob = classifier.predict_proba(data_df)[:, 1][0]
    print(predicted_prob)
    if predicted_prob >= probability_threshold:
        prediction = 'churn'
    else:
        prediction = 'No churn'

    return {'prediction': f'{prediction}',
            'confidence': f'{np.round(predicted_prob*100, 3)} %'} 

if __name__ == '__main__':
    uvicorn.run(app, port=8000)