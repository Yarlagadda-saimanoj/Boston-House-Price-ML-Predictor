# Boston House Price ML Predictor

Welcome to the Boston House Price ML Predictor! This project uses Machine Learning to predict house prices in the Boston area based on various features.


## About:
This application utilizes a Support Vector Regressor (SVR) model trained on a dataset of Boston housing data to provide you with estimated house prices based on specific features.
* The Support Vector Regression (SVR) model was chosen for this project due to its ability to handle both linear and non-linear relationships in the data, making it suitable for predicting house prices, which often exhibit complex patterns. SVR is also effective in handling high-dimensional datasets and has been widely used in real estate prediction tasks, making it a robust choice for accurate price forecasting.

## How to Use
1. Visit the [Boston House Price ML Predictor](https://boston-house-price-ml-predictor-saimanoj.streamlit.app/) web application.
2. Enter the values for the following features:
   - Crime Rate (CRIM)
   - Proportion of Residential Land Zoned (ZN)
   - Proportion of Non-Retail Business Acres (INDUS)
   - Charles River Dummy (CHAS)
   - Nitric Oxides Concentration (NOX)
   - Average Number of Rooms (RM)
   - Proportion of Owner-Occupied Units Built Before 1940 (AGE)
   - Weighted Distances to Employment Centers (DIS)
3. Click the "Predict" button to get an estimated house price.

## Requirements
To run this application locally, you'll need to have Python and the required libraries installed. You can find a list of dependencies in the [requirements.txt](https://github.com/Yarlagadda-saimanoj/Boston-House-Price-ML-Predictor/blob/main/requirements.txt) file.

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/Yarlagadda-saimanoj/Boston-House-Price-ML-Predictor.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```

## Preview
![Preview](hp.png)

## Tech Stack

- **Languages:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- **Libraries:** ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
  ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
  ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)



## License
This code is distributed under the terms of the [MIT License](https://github.com/Yarlagadda-saimanoj/Boston-House-Price-ML-Predictor/blob/main/LICENSE).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Yarlagadda-saimanoj/Boston-House-Price-ML-Predictor/blob/main/LICENSE)

