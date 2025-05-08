import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
import warnings
import os
warnings.filterwarnings('ignore')

# Set your desired path
new_path = r"D:\Education\Datascience\PYTHON_BIGINNER\AI\DeepLearning\Tensorflow"

# Change the working directory
os.chdir(new_path)

# Verify the change
print("Current Working Directory:", os.getcwd())

# Load dataset
dataset = pd.read_csv(r"D:\Education\Datascience\PYTHON_BIGINNER\AI\DeepLearning\Tensorflow\Churn_Modelling.csv")
X = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values

# Encode categorical data
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Feature Scaling
sc = StandardScaler()
X = sc.fit_transform(X)

# Save the scaler and encoders
joblib.dump(sc, "scaler.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(ct, "column_transformer.pkl")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train traditional classifiers and save them
classifiers = {
    "Logistic_Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM_Linear": SVC(kernel='linear', probability=True),
    "SVM_RBF": SVC(kernel='rbf', probability=True),
    "Naive_Bayes": GaussianNB(),
    "Decision_Tree": DecisionTreeClassifier(criterion='entropy'),
    "Random_Forest": RandomForestClassifier(n_estimators=100, criterion='entropy')
}

# Optional: XGBoost
try:
    from xgboost import XGBClassifier
    classifiers["XGBoost"] = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
except ImportError:
    print("XGBoost not installed.")

for name, model in classifiers.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f"{name}.pkl")

# Save the ANN model
ann = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=6, activation='relu'),
    tf.keras.layers.Dense(units=6, activation='relu'),
    tf.keras.layers.Dense(units=5, activation='relu'),
    tf.keras.layers.Dense(units=4, activation='relu'),
    tf.keras.layers.Dense(units=1, activation='sigmoid')
])
ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
ann.fit(X_train, y_train, batch_size=32, epochs=200, verbose=0)
ann.save("ANN_model.h5")

