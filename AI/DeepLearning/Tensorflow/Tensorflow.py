# -*- coding: utf-8 -*-
"""
Created on Thu May  8 19:53:29 2025

@author: csair
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load the dataset
data = pd.read_csv(r"D:\Education\Datascience\PYTHON_BIGINNER\AI\DeepLearning\Tensorflow\customer_churn_sample.csv")

# Step 2: Drop CustomerID (not useful for prediction)
data.drop("CustomerID", axis=1, inplace=True)

# Step 3: Convert TotalCharges to numeric
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data = data.dropna()

# Step 4: Encode categorical variables
cat_cols = ['Gender', 'Partner', 'Dependents', 'PhoneService', 'InternetService', 'Contract']
for col in cat_cols:
    data[col] = LabelEncoder().fit_transform(data[col])

# Step 5: Encode target variable (Churn)
data['Churn'] = data['Churn'].map({'No': 0, 'Yes': 1})

# Step 6: Split features and target
X = data.drop("Churn", axis=1)
y = data["Churn"]

# Step 7: Scale numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Step 8: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 9: Build TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, input_shape=(X.shape[1],), activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Step 10: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 11: Train the model
model.fit(X_train, y_train, epochs=50, batch_size=4, verbose=1)

# Step 12: Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.2f}")
