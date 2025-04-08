import streamlit as st
import pandas as pd
import pickle
import io

# Set Streamlit page config
st.set_page_config(page_title="Logistic Regression Predictor", layout="centered")

st.title("📊 Logistic Regression Prediction App")
st.write("Upload a CSV file with **Age** and **EstimatedSalary** columns to get predictions.")

# Load the model and scaler
@st.cache_resource
def load_model_and_scaler():
    with open('logistic_model.pkl', 'rb') as model_file:
        classifier = pickle.load(model_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return classifier, scaler

classifier, scaler = load_model_and_scaler()

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV
    data = pd.read_csv(uploaded_file)

    # Drop unwanted columns if they exist
    columns_to_drop = ['User ID', 'Gender', 'Unnamed: 0']
    data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

    if 'Age' not in data.columns or 'EstimatedSalary' not in data.columns:
        st.error("The file must contain 'Age' and 'EstimatedSalary' columns.")
    else:
        # Extract features
        X_new = data[['Age', 'EstimatedSalary']].values

        # Apply the scaler
        X_scaled = scaler.transform(X_new)

        # Predict
        predictions = classifier.predict(X_scaled)

        # Add predictions
        data['PredictedOutput'] = predictions

        # Display result
        st.success("✅ Prediction completed!")
        st.dataframe(data)

        # Download button
        csv_buffer = io.StringIO()
        data.to_csv(csv_buffer, index=False)
        st.download_button(
            label="⬇️ Download CSV with Predictions",
            data=csv_buffer.getvalue(),
            file_name="predicted_output.csv",
            mime="text/csv"
        )
else:
    st.info("Please upload a CSV file to proceed.")
