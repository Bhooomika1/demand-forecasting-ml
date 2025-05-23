# Demand Forecasting Using Machine Learning
Overview
This project demonstrates how to forecast product demand using multiple machine learning models including ARIMA, LSTM, and Random Forest. The aim is to predict sales for retail stores by leveraging historical sales data, promotions, holidays, and pricing.

Features
Time series forecasting using ARIMA for univariate sales prediction

Deep learning with LSTM to capture complex temporal dependencies

Random Forest regression to use multiple features for robust demand prediction

Data preprocessing, feature engineering, and visualization

Model comparison and evaluation using metrics like RMSE and MAE

Dataset
The dataset contains:

Date of sales

Store ID

Product/item ID

Units sold (target variable)

Price, promotions, holiday flags as additional features

Note: Dataset used is included in this repo (Full_Demand_Forecasting_Dataset.xlsx).

Technologies Used
Python 3.x

Pandas, NumPy

Statsmodels (for ARIMA)

TensorFlow/Keras (for LSTM)

Scikit-learn (for Random Forest)

Matplotlib/Seaborn (for visualization)

How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/Bhooomika1/demand-forecasting-ml.git
Install dependencies:

nginx
Copy
Edit
pip install -r requirements.txt
Run the Jupyter notebooks or Python scripts in the repo to preprocess data, train models, and generate forecasts.

Project Structure
Full_Demand_Forecasting_Dataset.xlsx — Sales dataset

inventory.py — Sample Python script for inventory/demand forecasting

notebooks/ — (optional) folder for Jupyter notebooks if you add them

README.md — This file

Future Improvements
Hyperparameter tuning for models

Adding more advanced models (Prophet, Transformers)

Deployment as a web app or API for real-time forecasting
