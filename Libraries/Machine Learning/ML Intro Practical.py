import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





dataset=pd.read_csv(r"C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Libraries\Machine Learning\Data.csv")

x=dataset.iloc[:,:-1].values #independent variable
y=dataset.iloc[:,3].values  #dependent variable-->On this other values are dependent

from sklearn.impute import SimpleImputer
# imputer=SimpleImputer() # parameter tuning-->system provided
# imputer=SimpleImputer(strategy='median')  # hyper parameter tuning -->changing from mean to other 
imputer=SimpleImputer(strategy='most_frequent')  # hyper parameter tuning -->changing from mean to other 
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])


