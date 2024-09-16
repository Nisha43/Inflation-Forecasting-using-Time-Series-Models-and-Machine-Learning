import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_prediction(inflation_series):
    model = ARIMA(inflation_series, order=(1, 1, 1))
    model_fit = model.fit()
    return model_fit
