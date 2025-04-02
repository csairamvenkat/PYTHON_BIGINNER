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









