# Inflation-Forecasting-using-Time-Series-Models-and-Machine-Learning

**Project Overview**
This project focuses on analyzing historical inflation data and forecasting future trends using a combination of time series analysis methods (Prophet and ARIMA) and machine learning models (Random Forest). The inflation data is sourced from the World Bank, and the predictions aim to provide insights into future inflationary trends, particularly for the United States. Additionally, clustering and regression techniques are explored for advanced analysis.

**Objectives**
To explore historical inflation data for multiple countries, with a focus on the United States.
To forecast inflation trends using statistical models like ARIMA and machine learning models like Random Forest.
To visualize inflation trends over time for different countries.
To apply K-Means clustering to group countries based on inflation trends.
To evaluate the performance of models using appropriate metrics and improve the results using hyperparameter tuning.

**Technologies Used**
**Programming Language:** Python
**Libraries:**
**Data manipulation:** pandas, numpy
**Visualization:** matplotlib, seaborn, plotly
**Machine Learning:** sklearn
**Time Series Forecasting:** Prophet, statsmodels (ARIMA)
**IDE:** Jupyter Notebook
**Dataset Source:** World Bank inflation data

**Installation Instructions**

**Install dependencies using pip:**
pip install -r requirements.txt

**Usage**
Data Exploration: The dataset is first explored to check for missing values, understand trends, and identify the relevant columns for analysis. The data focuses on the inflation rates (annual percentage) for various countries over multiple years.

**Time Series Forecasting:**

The Prophet model is used for forecasting the next 10 years of inflation trends for the United States.
The ARIMA model is used for short-term inflation forecasting with historical inflation data.
Random Forest Regression is employed to capture non-linear relationships in the dataset by using lag features.

**Clustering Analysis:**

K-Means clustering groups countries based on inflation patterns over the years.

**Results**

The forecasting models provide accurate projections for the United States' inflation over the next 10 years.
The ARIMA model provides a more granular, short-term forecast with acceptable accuracy.
The Prophet model successfully projects inflation trends using its seasonality and trend components.
Random Forest Regression was used to predict future inflation based on lagged inflation values, yielding competitive results.
K-Means clustering identified different inflation patterns across countries.
Performance Evaluation
ARIMA Model Performance: Evaluated using metrics like AIC, MAE, and RMSE.
Random Forest Regression Performance: Evaluated using R² score, MAE, and RMSE.
Prophet Model Performance: Visual evaluation of trends and seasonality.
Future Enhancements
Incorporate more advanced feature engineering (e.g., adding GDP, unemployment rate) to improve model predictions.
Explore other machine learning algorithms like XGBoost or LSTM for time series prediction.
Extend analysis to multiple countries beyond the United States.
