import streamlit as st
import joblib
import numpy as np

# Define the URL for the raw pkl file on GitHub
model_url = 'https://github.com/Yarlagadda-saimanoj/Boston-House-Price-ML-Predictor/raw/main/streamlit-app/svr_model.pkl'

# Load the SVR model from the raw pkl file
svr_model = joblib.load(model_url)

st.title("Boston House Price Prediction App")

# Collect input values for all 8 features
crim = st.number_input("Crime Rate (CRIM):")
zn = st.number_input("Proportion of Residential Land Zoned (ZN):")
indus = st.number_input("Proportion of Non-Retail Business Acres (INDUS):")
chas = st.number_input("Charles River Dummy (CHAS):")
nox = st.number_input("Nitric Oxides Concentration (NOX):")
rm = st.number_input("Average Number of Rooms (RM):")
age = st.number_input("Proportion of Owner-Occupied Units Built Before 1940 (AGE):")
dis = st.number_input("Weighted Distances to Employment Centers (DIS):")

# Add a button to trigger prediction
if st.button("Predict"):
    # Create input data array
    input_data = np.array([[crim, zn, indus, chas, nox, rm, age, dis]])

    # Make predictions
    predicted_value = svr_model.predict(input_data)

    st.write(f'Predicted House Price: ${predicted_value[0] * 1000:.2f}')
