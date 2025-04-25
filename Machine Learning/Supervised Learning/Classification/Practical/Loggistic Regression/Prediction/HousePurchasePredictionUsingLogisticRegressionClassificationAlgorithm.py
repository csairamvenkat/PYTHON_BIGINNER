import streamlit as st
import pandas as pd
import pickle
import io

# Set Streamlit page config
st.set_page_config(page_title="Logistic Regression Predictor", layout="centered")

st.title("📊 House Purchase Prediction Using Logistic Regression Classification Algorithm ")

# Load the model and scaler
@st.cache_resource
def load_model_and_scaler():
    with open('logistic_model.pkl', 'rb') as model_file:
        classifier = pickle.load(model_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return classifier, scaler

classifier, scaler = load_model_and_scaler()

# UI for prediction method
st.subheader("Choose input method:")
input_method = st.radio("Select input type", ['📁 Upload CSV', '✍️ Manual Input'])

# ===============================
# OPTION 1: CSV File Upload
# ===============================
if input_method == '📁 Upload CSV':
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Drop unwanted columns if they exist
        columns_to_drop = ['User ID', 'Gender', 'Unnamed: 0']
        data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

        if 'Age' not in data.columns or 'EstimatedSalary' not in data.columns:
            st.error("CSV must contain 'Age' and 'EstimatedSalary' columns.")
        else:
            X_new = data[['Age', 'EstimatedSalary']].values
            X_scaled = scaler.transform(X_new)
            predictions = classifier.predict(X_scaled)
            data['PredictedOutput'] = predictions

            st.success("✅ Predictions completed!")
            st.dataframe(data)

            # Download option
            csv_buffer = io.StringIO()
            data.to_csv(csv_buffer, index=False)
            st.download_button(
                label="⬇️ Download CSV with Predictions",
                data=csv_buffer.getvalue(),
                file_name="predicted_output.csv",
                mime="text/csv"
            )

# ===============================
# OPTION 2: Manual Input
# ===============================
elif input_method == '✍️ Manual Input':
    st.subheader("Enter data for a single prediction:")
    
    age = st.number_input("Enter Age", min_value=1, max_value=120, value=30)
    salary = st.number_input("Enter Estimated Salary", min_value=1000, max_value=1000000, value=50000)

    if st.button("🔮 Predict"):
        input_data = [[age, salary]]
        input_scaled = scaler.transform(input_data)
        prediction = classifier.predict(input_scaled)[0]
        st.success(f"🧠 Predicted Output: **{prediction}**")
