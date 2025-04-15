import USAHousingPredictor as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Load data
@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

st.set_page_config(layout="wide")
st.title("ML Prediction App")

# Sidebar Filters
st.sidebar.header("Select the filters")

test_size = st.sidebar.selectbox("Select the test size", options=[0.2, 0.25, 0.3], format_func=lambda x: f"{x}")
scaler_option = st.sidebar.selectbox("Select the Scaling Technique", options=["Standard Scaler", "MinMax Scaler"])

model_type = st.sidebar.selectbox(
    "Select the ML model you wish to use for prediction",
    options=[
        "K Nearest Neighbour (KNN)",
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "Linear Regression"
    ]
)

# File Upload
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)

    st.subheader("Raw Dataset")
    st.dataframe(data)

    # Assume features and target column
    target_column = st.selectbox("Select target column", options=data.columns)

    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Convert categorical variables
    X = pd.get_dummies(X)

    # Scale data
    if scaler_option == "Standard Scaler":
        scaler = StandardScaler()
    else:
        scaler = MinMaxScaler()

    X_scaled = scaler.fit_transform(X)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=42)

    # Model selection
    if model_type == "K Nearest Neighbour (KNN)":
        model = KNeighborsClassifier() if y.nunique() <= 10 else KNeighborsRegressor()
    elif model_type == "Logistic Regression":
        model = LogisticRegression()
    elif model_type == "Decision Tree":
        model = DecisionTreeClassifier() if y.nunique() <= 10 else DecisionTreeRegressor()
    elif model_type == "Random Forest":
        model = RandomForestClassifier() if y.nunique() <= 10 else RandomForestRegressor()
    elif model_type == "Linear Regression":
        model = LinearRegression()

    # Fit & Predict
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Prepare future predicted dataset
    result_df = pd.DataFrame(X_test, columns=X.columns)
    result_df["Prediction"] = predictions

    st.subheader("Future predicted dataset is")
    st.dataframe(result_df.reset_index(drop=True))

    # Download button
    csv = result_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Predictions", data=csv, file_name='predictions.csv', mime='text/csv')
