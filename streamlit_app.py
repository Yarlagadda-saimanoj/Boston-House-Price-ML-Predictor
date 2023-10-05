import streamlit as st
import joblib
import numpy as np
import os

model_path = 'svr_model.pkl'
image_path = 'hp.png'

svr_model = joblib.load(model_path)
st.image(image_path, use_column_width=True)

st.title("Boston House Price Prediction App")

crim = st.number_input("Crime Rate (CRIM):")
zn = st.number_input("Proportion of Residential Land Zoned (ZN):")
indus = st.number_input("Proportion of Non-Retail Business Acres (INDUS):")
chas = st.number_input("Charles River Dummy (CHAS):")
nox = st.number_input("Nitric Oxides Concentration (NOX):")
rm = st.number_input("Average Number of Rooms (RM):")
age = st.number_input("Proportion of Owner-Occupied Units Built Before 1940 (AGE):")
dis = st.number_input("Weighted Distances to Employment Centers (DIS):")

if st.button("Predict"):
    input_data = np.array([[crim, zn, indus, chas, nox, rm, age, dis]])
    predicted_value = svr_model.predict(input_data)
    st.write(f'Predicted House Price: ${predicted_value[0] * 1000:.2f}')

st.markdown("""
    <div style="text-align:center;">
        Made with ❤️ by <a href="https://www.linkedin.com/in/sai-manoj-yarlagadda-a6159b225/">Sai Manoj Yarlagadda</a>
    </div>
    """, unsafe_allow_html=True)
