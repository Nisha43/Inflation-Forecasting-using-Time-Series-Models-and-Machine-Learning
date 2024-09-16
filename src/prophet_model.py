from prophet import Prophet

def prophet_forecast(inflation_df):
    model = Prophet()
    model.fit(inflation_df)
    future = model.make_future_dataframe(periods=10, freq='Y')
    forecast = model.predict(future)
    return forecast
