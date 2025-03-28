import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



 # ctrl + i to get help regarding that library/class/func etc

dataset=pd.read_csv(r"C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Libraries\Machine Learning\Data.csv")

x=dataset.iloc[:,:-1].values #independent variable
y=dataset.iloc[:,3].values  #dependent variable-->On this other values are dependent

from sklearn.impute import SimpleImputer

# fit and transform 
# Simple imputer transformer  which fills missing numeric data with strategy specified
# imputer=SimpleImputer() # parameter tuning-->system provided-->since its numeric mean strategy is used
# imputer=SimpleImputer(strategy='median')  # hyper parameter tuning -->changing from mean to other 
imputer=SimpleImputer(strategy='most_frequent')  # hyper parameter tuning -->changing from mean to other 
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

# label encoder is  a transformer/imputation technique which converts categorical to numeric.Used for independent variable
from sklearn.preprocessing import LabelEncoder  # Label encoder converts string to numeric value.Its one of the transformer (one hot encoding,label encoder)

# independent variable
labelEncoder_x=LabelEncoder()
labelEncoder_x.fit_transform(x[:,0]) 
x[:,0]=labelEncoder_x.fit_transform(x[:,0])

# dependent variable
labelEncoder_y=LabelEncoder()
labelEncoder_y.fit_transform(y) 
y=labelEncoder_x.fit_transform(y)

# Split Ratio
# we can provide both train and test size or either 1 of them
# if random_state=0 then same set of records is considered for every execution,if we remove random_state then data is sampled randomly
# if random_state=0 is not specified then model cannot be accurate.
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=0)
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


