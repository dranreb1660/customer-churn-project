import streamlit as st
import requests
import json


def run():
    st.title('Customer Churn Classifier')
    gender = st.selectbox('Gender', ['Male', 'Female'])  
    SeniorCitizen = st.selectbox('Senior Citizen', ['No', 'Yes'])   
    Partner  = st.selectbox('Maried', ['No', 'Yes'])  
    Dependents  = st.selectbox('Has Dependents', ['No', 'Yes'])  
    PhoneService = st.selectbox('Phone Service', ['No', 'Yes'])  
    MultipleLines   = st.selectbox('MultipleLines', ['No phone service', 'No', 'Yes'])
    InternetService = st.selectbox('InternetService', ['DSL', 'Fiber optic', 'No'])
    OnlineSecurity  = st.selectbox('OnlineSecurity', ['No', 'Yes', 'No internet service'])
    OnlineBackup    = st.selectbox('OnlineBackup', ['Yes', 'No', 'No internet service'])
    DeviceProtection= st.selectbox('Device Protection', ['No', 'Yes', 'No internet service'])
    TechSupport     = st.selectbox('TechSupport', ['No', 'Yes', 'No internet service'])
    StreamingTV     = st.selectbox('StreamingTV', ['No', 'Yes', 'No internet service'])
    StreamingMovies = st.selectbox('Streaming Movies', ['No', 'Yes', 'No internet service'])
    Contract        = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling= st.selectbox('Paperless Billing', ['No', 'Yes'])
    PaymentMethod   = st.selectbox('PaymentMethod', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    tenure          = st.text_input('Tenure')
    MonthlyCharges  = st.text_input('Monthly Charges')
    TotalCharges    = st.text_input('Total Charges')


    data = {
        'gender' :   gender,
        'SeniorCitizen' : SeniorCitizen , 
        'Partner'  : Partner,  
        'Dependents'  :Dependents,  
        'PhoneService' : PhoneService,  
        'MultipleLines'   : MultipleLines, 
        'InternetService' : InternetService, 
        'OnlineSecurity'  : OnlineSecurity,
        'OnlineBackup'    : OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport'     : TechSupport,
        'StreamingTV'     : StreamingTV,
        'StreamingMovies' : StreamingMovies,
        'Contract'        : Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod'   : PaymentMethod,
        'tenure'          : tenure,
        'MonthlyCharges'  : MonthlyCharges,
        'TotalCharges'    : TotalCharges,
        }

    if st.button('Predict'):
        response = requests.post('http://0.0.0.0:80/predict', json=data)
        prediction = response.text
        st.success(f'The prediction form model: {prediction}')

if __name__ == '__main__':
    run()

