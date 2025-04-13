# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 19:31:14 2025

@author: sai.venkat
"""

import pandas as pd
import numpy as np

dataset=pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Classification\Practical\SVM\logit classification.csv')
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




# Training SVM Model
from sklearn.svm import SVC
classifier=SVC()   
''' using kernel param we can hyper parameter tune the model for svc algo'''
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)


'''

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
'''


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
print('classification report :',cr)


# Random state=0 gives max accuracy

print("Confusion Matrix :",cm)
print("Accuracy : ",ac)
print('bias :',bias)
print("variance : ",variance)
print('classification report :',cr)

import os 
os.getcwd()
# All Ml models should be scalled for better model accuracy

# If underfitting /over fitting occurs we use cross validation technique

import os

# Custom path
custom_path = r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Classification\Practical\SVM'

# Change the working directory
os.chdir(custom_path)



#future predcictions
ds1=pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Classification\Practical\SVM\final1-PredictmodelGenerated.csv')
ds2=ds1.copy()

ds1=ds1.iloc[:,[3,4]].values

# Scalling shd be done for test data aswell to get accurate predictions

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
M=sc.fit_transform(ds1)

y_pred1=pd.DataFrame()

ds2['y_pred1']=classifier.predict(M)

ds2.to_csv('pred_model.csv')



# Confirm the change
print("✅ Working directory changed to:", os.getcwd())

import pickle

# Save the model
with open('logistic_model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)

# Save the scaler
with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(sc, scaler_file)

print("✅ Model and scaler saved as 'logistic_model.pkl' and 'scaler.pkl'")



kernels = ['sigmoid', 'poly', 'rbf', 'linear']
gammas = ['auto', 'scale']
degree_range = range(1, 11)
c_range = range(1, 11)
# Collect results
results = []

# Loop through combinations
for kernel in kernels:
    for gamma in gammas:
        for C in c_range:
            # For 'poly' kernel, loop through degrees
            if kernel == 'poly':
                for degree in degree_range:
                    model = SVC(kernel=kernel, gamma=gamma, C=C, degree=degree)
                    model.fit(x_train, y_train)
                    predictions = model.predict(x_test)
                    acc = accuracy_score(y_test, predictions)
               #     print(f"Kernel: {kernel}, Gamma: {gamma}, C: {C}, Degree: {degree}, Accuracy: {acc:.4f}")
                    results.append({
                     'Kernel': kernel,
                     'Gamma': gamma,
                     'C': C,
                     'Degree': degree,
                     'Accuracy': acc
                 })
            else:
                model = SVC(kernel=kernel, gamma=gamma, C=C)
                model.fit(x_train, y_train)
                predictions = model.predict(x_test)
                acc = accuracy_score(y_test, predictions)
              #  print(f"Kernel: {kernel}, Gamma: {gamma}, C: {C}, Accuracy: {acc:.4f}")
                results.append({
                     'Kernel': kernel,
                     'Gamma': gamma,
                     'C': C,
                     'Degree': degree,
                     'Accuracy': acc
                 })
                # Create DataFrame and write to CSV
df = pd.DataFrame(results)
os.chdir(custom_path)
df.to_csv('svm_hyperparameter_results.csv', index=False)

print("Results written to svm_hyperparameter_results.csv")

results.sort(reverse=True)

# select topmost accuracy and with hyper param tuned






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


