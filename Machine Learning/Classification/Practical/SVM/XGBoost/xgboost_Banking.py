import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# data import 
dataset=pd.read_csv(r"D:\Education\Datascience\PYTHON_BIGINNER\Machine Learning\Classification\Practical\SVM\XGBoost\Churn_Modelling.csv")
X=dataset.iloc[:,3:-1].values
y=dataset.iloc[:,-1].values

print(X)
print(y)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X[:,2]=le.fit_transform(X[:,2])
print(X)

# one hot code encode for Geography
# converting everything to integers
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')
x=np.array(ct.fit_transform(X))
print(x)


# data split and training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
 
#XG Boost Training

from xgboost import XGBClassifier
classifier=XGBClassifier(n_estimator=200,max_depth=4,learning_rate=0.0001)
classifier.fit(X_train,y_train)


# Predicting the test set results
y_pred=classifier.predict(X_test)


# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print("confusion_matrix :" ,cm)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print("Accuracy Score",ac)

bias=classifier.score(X_train,y_train)
print("bias :",bias)





