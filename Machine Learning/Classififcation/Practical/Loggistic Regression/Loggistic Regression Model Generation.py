# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 19:31:14 2025

@author: sai.venkat
"""

import pandas as pd
import numpy as np

dataset=pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Classififcation\Practical\Loggistic Regression\Input Data To Train\logit classification.csv')
# InDependent Variable
x=dataset.iloc[:,[2,3]].values
#Dependent variable
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
# case1 and case 2
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# case 3 and 4
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)


# Scalling   Standard Scaller-- case 1 and 3

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


#  Normalizing--case 2 and 4

# from sklearn.preprocessing import Normalizer
# nm=Normalizer()
# x_train=nm.fit_transform(x_train)
# x_test=nm.transform(x_test)

# Logistic Regression Classification Algo .It is also called logit, MaxEnt

# case 5 no scalling no normalizing

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression() 
classifier.fit(x_train,y_train)


y_pred=classifier.predict(x_test)


# Confusion Matrix

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_pred)
print("Confusion Matrix :",cm)


# Here tp=57  tn=17  fp= 1 fn =5 for standard scaller

# Model Accuracy
from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print("Accuracy : ",ac)

# Model Accuracy , Bias and variance is used to get overfitting or underfitting

# bias
bias=classifier.score(x_train,y_train)
print('bias :',bias)


# Variance
variance=classifier.score(x_test,y_test)
print("variance : ",variance)

#classification_report

from sklearn.metrics import classification_report
cr=classification_report(y_test,y_pred)
print('cr :',cr)


# All Ml models should be scalled for better model accuracy

# If underfitting /over fitting occurs we use cross validation technique



import pickle
import os

save_dir =r"C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Classififcation\Practical\Loggistic Regression\Pickle Files"

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)



# Save the trained logistic regression model
with open('logistic_model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)
    file_path = os.path.join(save_dir, 'logistic_model.pkl')
# Save the scaler (optional but useful when deploying the model)
with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(sc, scaler_file)
    file_path = os.path.join(save_dir, 'scaler.pkl')

print("Model and scaler saved as 'logistic_model.pkl' and 'scaler.pkl'")



''' 
y 2 pkls generated ??


ChatGPT said:
Yes! Based on your code, 2 .pkl files are generated intentionally:

✅ 1. logistic_model.pkl
This contains the trained Logistic Regression model (classifier).
You’ll use this to make predictions later without retraining the model.

✅ 2. scaler.pkl
This contains the StandardScaler object (sc) used to scale your features.
It’s important because you must scale future input data the same way before prediction.

🔁 Why both are needed?
If you skip saving the scaler:

You risk feeding unscaled or differently scaled data to the model.

That causes poor predictions, even if the model itself is fine.

'''


