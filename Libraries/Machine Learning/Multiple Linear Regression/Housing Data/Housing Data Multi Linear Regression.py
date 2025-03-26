import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

df=pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Libraries\Machine Learning\Multiple Linear Regression\Housing Data\House_data.csv')
# sqft living is dependent variable i.e.y
Y=df['sqft_living']
X=df.drop(['sqft_living','date','id'], axis=1)


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)


Y_Pred=regressor.predict(X_test)

m_slope=regressor.coef_
print(m_slope)

c_intercept=regressor.intercept_
print(c_intercept)

X = np.append(arr=np.ones((X.shape[0], 1)).astype(int), values=X, axis=1)

