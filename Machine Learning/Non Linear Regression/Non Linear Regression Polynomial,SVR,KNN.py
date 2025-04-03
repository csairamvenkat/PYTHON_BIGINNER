import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
dataset=pd.read_csv(r"C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Non Linear Regression\emp_sal.csv")
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values


#Simple Linear Regression
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()  
lin_reg.fit(x,y)


plt.scatter(x, y, color='red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.title('Linear Regression Model')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

m=lin_reg.coef_
print(m)

c=lin_reg.intercept_
print(c)


simplelinear=lin_reg.predict([[6.5]])
print(simplelinear)

# polynomial regression  (Non Linear)

# By default the degree is 2 for polynomial

#degree 2

from  sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures()
x_poly=poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)

lin_reg_2=LinearRegression()    
lin_reg_2.fit(x_poly,y)



poly_pred_degree2=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_pred_degree2)


# Poly Visualization


plt.scatter(x, y, color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression Model Degree 1')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


#degree 2

from  sklearn.preprocessing import PolynomialFeatures
# Hyper parameter Tuning
poly_reg=PolynomialFeatures(degree=2)
x_poly=poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)

lin_reg_2=LinearRegression()    
lin_reg_2.fit(x_poly,y)



poly_pred_degree2=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_pred_degree2)


# Poly Visualization


plt.scatter(x, y, color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression Model Degree 2')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


# degree 3


from  sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=3)
x_poly=poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)

lin_reg_2=LinearRegression()    
lin_reg_2.fit(x_poly,y)



poly_pred_degree3=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_pred_degree3)


# Poly Visualization


plt.scatter(x, y, color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression Model Degree 3')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


# degree 4


from  sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)

lin_reg_2=LinearRegression()    
lin_reg_2.fit(x_poly,y)



poly_pred_degree4=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_pred_degree4)


# Poly Visualization


plt.scatter(x, y, color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression Model  Degree 4')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


# degree 5


from  sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree= 5)
x_poly=poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)

lin_reg_2=LinearRegression()    
lin_reg_2.fit(x_poly,y)


poly_pred_degree5=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_pred_degree5)


# Poly Visualization


plt.scatter(x, y, color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression Model  Degree 5')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


# degree 6

poly_pred=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_pred)

from  sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree =6)
x_poly=poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)

lin_reg_2=LinearRegression()    
lin_reg_2.fit(x_poly,y)



poly_pred_degree6=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_pred_degree6)


# Poly Visualization


plt.scatter(x, y, color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Polynomial Regression Model Degree 6')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()


# Note : Degrees are applied based on company standards how much they pay for the experience.



# Support Vector Regression Model (SVR)

# Here dependent variable is continious so we used svr

from sklearn.svm import SVR  #( ctrl+i  for help)
svr_reg=SVR()
svr_reg.fit(x,y)   # here we considered kernel,gamma=auto and c=1.0
svr_model_pred=svr_reg.predict([[6.5]])
print(svr_model_pred)




# Hyper parameter Tuning

from sklearn.svm import SVR  #( ctrl+i  for help)
svr_reg_poly=SVR(kernel="poly",degree=4,gamma="auto",C=1.0)
svr_reg_poly.fit(x,y)   # here we considered kernel,gamma=auto and c=1.0
svr_model_pred_hyperparamtuning_poly=svr_reg_poly.predict([[6.5]])
print(svr_model_pred_hyperparamtuning_poly)



# Try for different Kernel,degree and gamma and c
from sklearn.svm import SVR  #( ctrl+i  for help)
svr_reg_linear=SVR(kernel="linear",degree=5,gamma="auto",C=2.0)
svr_reg_linear.fit(x,y)   # here we considered kernel,gamma=auto and c=1.0
svr_model_pred_hyperparamtuning_linear=svr_reg_linear.predict([[6.5]])
print(svr_model_pred_hyperparamtuning_linear)

from sklearn.svm import SVR  #( ctrl+i  for help)
svr_reg_rbf=SVR(kernel="rbf",degree=5,gamma="auto",C=1.0)
svr_reg_rbf.fit(x,y)   # here we considered kernel,gamma=auto and c=1.0
svr_model_pred_hyperparamtuning_rbf=svr_reg_rbf.predict([[6.5]])
print(svr_model_pred_hyperparamtuning_rbf)


# K-Nearest Neighbour

#paramtere Tuning

from sklearn.neighbors import KNeighborsRegressor
knn_reg=KNeighborsRegressor()
knn_reg.fit(x,y)
knn_model_pred=knn_reg.predict([[6.5]])
print(knn_model_pred)


# hyper parameter tuning

from sklearn.neighbors import KNeighborsRegressor
knn_reg=KNeighborsRegressor(n_neighbors=4,weights='uniform')
knn_reg.fit(x,y)
knn_model_pred_hyperparam_tuning=knn_reg.predict([[6.5]])
print(knn_model_pred_hyperparam_tuning)

from sklearn.neighbors import KNeighborsRegressor
knn_reg=KNeighborsRegressor(n_neighbors=10,weights='uniform')
knn_reg.fit(x,y)
knn_model_pred_hyperparam_tuning_10neighbour=knn_reg.predict([[6.5]])
print(knn_model_pred_hyperparam_tuning_10neighbour)


from sklearn.neighbors import KNeighborsRegressor
knn_reg=KNeighborsRegressor(n_neighbors=25,weights='uniform')
knn_reg.fit(x,y)
knn_model_pred_hyperparam_tuning_25neighbour=knn_reg.predict([[6.5]])
print(knn_model_pred_hyperparam_tuning_25neighbour)





print("simplelinear",simplelinear)
print("poly_pred_degree2",poly_pred_degree2)
print('poly_pred_degree3',poly_pred_degree3)
print('poly_pred_degree4',poly_pred_degree4)
print('poly_pred_degree5',poly_pred_degree5)
print('poly_pred_degree6',poly_pred_degree6)
print('svr_model_pred',svr_model_pred)
print('svr_model_pred_hyperparamtuning_poly',svr_model_pred_hyperparamtuning_poly)
print("knn_model_pred_hyperparam_tuning",knn_model_pred_hyperparam_tuning)
print('svr_model_pred_hyperparamtuning_rbf',svr_model_pred_hyperparamtuning_rbf)
print('svr_model_pred_hyperparamtuning_linear',svr_model_pred_hyperparamtuning_linear)
print('knn_model_pred',knn_model_pred)
print('knn_model_pred_hyperparam_tuning_10neighbour',knn_model_pred_hyperparam_tuning_10neighbour)
print('knn_model_pred_hyperparam_tuning_25neighbour',knn_model_pred_hyperparam_tuning_25neighbour)








