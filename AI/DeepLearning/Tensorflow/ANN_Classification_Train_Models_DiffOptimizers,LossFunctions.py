import numpy as np
import pandas as pd
import tensorflow as tf
import time
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
os.chdir(new_path)
print("Current Working Directory:", os.getcwd())

# Load dataset
dataset = pd.read_csv("Churn_Modelling.csv")
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

# Save preprocessors
joblib.dump(sc, "scaler.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(ct, "column_transformer.pkl")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train traditional classifiers
classifiers = {
    "Logistic_Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM_Linear": SVC(kernel='linear', probability=True),
    "SVM_RBF": SVC(kernel='rbf', probability=True),
    "Naive_Bayes": GaussianNB(),
    "Decision_Tree": DecisionTreeClassifier(criterion='entropy'),
    "Random_Forest": RandomForestClassifier(n_estimators=100, criterion='entropy')
}

# Try adding XGBoost if available
try:
    from xgboost import XGBClassifier
    classifiers["XGBoost"] = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
except ImportError:
    print("XGBoost not installed.")

for name, model in classifiers.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f"{name}.pkl")

# Define optimizers
optimizers = {
    "SGD": tf.keras.optimizers.SGD(),
    "Adam": tf.keras.optimizers.Adam(),
    "RMSprop": tf.keras.optimizers.RMSprop(),
    "Adagrad": tf.keras.optimizers.Adagrad(),
    "Adadelta": tf.keras.optimizers.Adadelta(),
    "Adamax": tf.keras.optimizers.Adamax(),
    "Nadam": tf.keras.optimizers.Nadam(),
    "FTRL": tf.keras.optimizers.Ftrl()
}

# Define Loss Functions
loss_functions = {
"binary_crossentropy": tf.keras.losses.BinaryCrossentropy(),
"mean_squared_error": tf.keras.losses.MeanSquaredError(),
"hinge": tf.keras.losses.Hinge(),
"squared_hinge": tf.keras.losses.SquaredHinge()
}

# Function to create model
def create_ann():
    ann = tf.keras.models.Sequential([
        tf.keras.layers.Dense(units=6, activation='relu'),
        tf.keras.layers.Dense(units=6, activation='relu'),
        tf.keras.layers.Dense(units=5, activation='relu'),
        tf.keras.layers.Dense(units=4, activation='relu'),
        tf.keras.layers.Dense(units=1, activation='sigmoid')
    ])
    return ann

# Train ANN with different optimizers
for opt_name, optimizer in optimizers.items():
    for lossfunc_name, lossfunc in loss_functions.items():
        print(f"\nTraining ANN with optimizer: {opt_name} and loss function {lossfunc_name}")
        ann = create_ann()
        ann.compile(optimizer=optimizer, loss=lossfunc, metrics=['accuracy'])

        start_time = time.time()
        ann.fit(X_train, y_train, batch_size=32, epochs=200, verbose=0)
        end_time = time.time()

        duration = end_time - start_time
        print(f"Training time for {opt_name} and {lossfunc_name}: {duration:.2f} seconds")

        model_filename = f"ANN_model_{opt_name}.h5"
        ann.save(model_filename)
