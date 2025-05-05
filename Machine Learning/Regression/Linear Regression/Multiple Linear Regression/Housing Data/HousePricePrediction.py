import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load the dataset
@st.cache_data
def load_data():
    # Simulate the cleaned dataset
    # data = {
    #     'price': [221900, 538000, 180000, 604000, 510000, 1225000, 257500, 291850],
    #     'bedrooms': [3, 3, 2, 4, 3, 4, 3, 3],
    #     'sqft_living': [1180, 2570, 770, 1960, 1680, 5420, 1715, 1060],
    #     'sqft_lot': [5650, 7242, 10000, 5000, 8080, 101930, 6819, 9711]
    # }
    # return pd.DataFrame(data)
    data=pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Libraries\Machine Learning\Multiple Linear Regression\Housing Data\House_data.csv')
    return data

# Prepare data
data = load_data()
X = data[['bedrooms', 'sqft_living', 'sqft_lot']]  # independent
y = data['price']  # To be Predicted hence its dependent

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("🏠 House Price Prediction")
st.write("Enter the details below to predict the house price.")

# Input fields
bedrooms = st.number_input("Bedrooms", min_value=1.0, max_value=10.0, value=1.0,step=0.5)
sqft_living = st.number_input("Living Area (sqft)", min_value=500, max_value=10000, value=1500,step=100)
sqft_lot = st.number_input("Lot Area (sqft)", min_value=1000, max_value=200000, value=5000,step=50)

# Prediction
if st.button("Predict Price"):
    input_features = np.array([[bedrooms, sqft_living, sqft_lot]])
    predicted_price = model.predict(input_features)[0]

    st.success(f"Estimated House Price: ${predicted_price:,.2f}")

# Model evaluation
st.subheader("Model Performance")
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"R² Score: {r2:.2f}")

st.dataframe(data)  # Display the dataset
