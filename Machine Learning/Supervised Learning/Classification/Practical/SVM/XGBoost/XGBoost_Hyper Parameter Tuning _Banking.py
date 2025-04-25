# -- coding: utf-8 --
"""
Created on Mon Apr 21 19:05:24 2025

@author: ADMIN
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ds=pd.read_csv(r'C:/Users/ADMIN/Downloads/Churn_Modelling.csv')
ds=pd.read_csv(r"D:\Education\Datascience\PYTHON_BIGINNER\Machine Learning\Classification\Practical\SVM\XGBoost\Churn_Modelling.csv")
x=ds.iloc[:, 3:-1].values
y=ds.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
# x[:,2]=le.fit_transform(x[:,2])

x[:,2]=le.fit_transform(x[:,2])
print(x)

#converting everything to integers
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')
x=np.array(ct.fit_transform(x))
print(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from xgboost import XGBClassifier
classifier=XGBClassifier(n_estimator=400,max_depth=4,learning_rate=0.45)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print(ac)

bias=classifier.score(x_train,y_train)
print(bias)

variance=classifier.score(x_test,y_test)
print(variance)