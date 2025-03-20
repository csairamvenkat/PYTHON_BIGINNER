# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 19:39:52 2025

@author: sai.venkat
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Libraries\Machine Learning\Salary_Data.csv')
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=0)
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=0)
x_train=x_train.values.reshape(-1,1)
x_test=x_test.values.reshape(-1,1)

# Training
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

# Testing
y_pred=regressor.predict(x_test)


plt.scatter(x_test, y_test, color='red')  # Scatter plot for test data
plt.plot(x_train, regressor.predict(x_train), color='blue')  # Regression line
plt.title("Salary vs Experience (Test Set)")
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')  # Corrected ylabel
plt.show()







