from pydantic import BaseModel

class CustomerChurn(BaseModel):
    gender          : str  
    SeniorCitizen   : str  
    Partner         : str  
    Dependents      : str  
    PhoneService    : str  
    MultipleLines   : str  
    InternetService : str  
    OnlineSecurity  : str  
    OnlineBackup    : str  
    DeviceProtection: str  
    TechSupport     : str  
    StreamingTV     : str  
    StreamingMovies : str  
    Contract        : str  
    PaperlessBilling: str  
    PaymentMethod   : str  
    tenure          : str  
    MonthlyCharges  : float
    TotalCharges    : float
