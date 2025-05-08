import streamlit as st
import numpy as np
import joblib
import tensorflow as tf
# import os
# st.write("Current Working Directory:", os.getcwd())

# Load transformers
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")
column_transformer = joblib.load("column_transformer.pkl")



# Load models
models = {
    "Logistic Regression": joblib.load("Logistic_Regression.pkl"),
    "K-NN": joblib.load("KNN.pkl"),
    "SVM (Linear)": joblib.load("SVM_Linear.pkl"),
    "SVM (RBF Kernel)": joblib.load("SVM_RBF.pkl"),
    "Naive Bayes": joblib.load("Naive_Bayes.pkl"),
    "Decision Tree": joblib.load("Decision_Tree.pkl"),
    "Random Forest": joblib.load("Random_Forest.pkl"),
    "ANN": tf.keras.models.load_model("ANN_model.h5")
}

# UI
st.title("Customer Churn Prediction")
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
credit_score = st.number_input("Credit Score", 300, 900, 600)
age = st.number_input("Age", 18, 100, 35)
tenure = st.number_input("Tenure", 0, 10, 3)
balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
num_products = st.number_input("Number of Products", 1, 4, 2)
has_cr_card = st.selectbox("Has Credit Card", ["Yes", "No"]) == "Yes"
is_active = st.selectbox("Is Active Member", ["Yes", "No"]) == "Yes"
estimated_salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)
selected_model = st.selectbox("Choose Model", list(models.keys()))

# Predict
if st.button("Predict Churn"):
    raw_input = [[geography, gender, credit_score, age, tenure, balance,
                  num_products, int(has_cr_card), int(is_active), estimated_salary]]
    
    raw_input[0][1] = label_encoder.transform([raw_input[0][1]])[0]
    transformed_input = column_transformer.transform(raw_input)
    scaled_input = scaler.transform(transformed_input)

    model = models[selected_model]
    if selected_model == "ANN":
        pred = (model.predict(scaled_input) > 0.5)[0][0]
    else:
        pred = model.predict(scaled_input)[0]

    st.success(f"Prediction: {'Will Churn' if pred == 1 else 'Will Not Churn'}")
