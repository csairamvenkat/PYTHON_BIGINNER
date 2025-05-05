# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
print(os.getcwd())  
os.chdir(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Classification\Practical\Social Media Prediction using Classification Algo')

dataset = pd.read_csv(r'Social_Network_Ads.csv')
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Importing the dataset

#this datasset contian information of user and socianl network, those features are - userid,gender,age,salary,purchased
#social network has several business client which can put their into social networks and one of the client is car company , this company has newly lunched XUV in rediculous price or high price
#we will see which of the user in this social network are going to buy brand new xuv car
#Last column tell us user purchased the car yes-1 // no-0 & we are going to build the model that is goint to predict if the user is going to buy xuv or not based on 2 variable based on age & estimated salery
#so our matrix of feature is only these 2 column & we gonna find some corelation b/w age and estimated salary of user and his decission to purchase the car [yes or no]
#so i need 2 index and rest of index i will remove for this i have to use slicing operator
#1 means - the user going to buy the car & 0 means - user is not going to buy the car

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
#for this observation let me selcted as 100 observaion for test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

#we are going to predict which users are going to predit xuv, 

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) 
#we mentioned feature scaling only to independent variable not dependent variable at all

#datapreprocessing done guys upto this part 

#******************************************************************************************

#Next step is we are going to build the logistic model and appy this model into our dataset 
#This is linear model library thats why we called from sklear.linear_model

# Training the Logistic Regression model on the Training set

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
#we have to fit the logistic regression model to our training set

# Predicting the Test set results
y_pred = classifier.predict(X_test)
#now you compare X_test with y_pred, x-test we ha,ve age and salary , 
#if u look at the first observation this user is not be able to buy the car but if you look at observation 7 then that user is going to buy the car
#in this case logistic regression model classify the which users are going to buy the car or not 

#we build our logistic model and fit it to the training set & we predict our test set result 


from sklearn.metrics import confusion_matrix
lrcm = confusion_matrix(y_test, y_pred)
print("Logistic Regression Confusion Matrix :",lrcm)

from sklearn.metrics import accuracy_score
lrac = accuracy_score(y_test, y_pred)
print("Logistic Regression Accuracy :",lrac)

# This is to get the Classification Report
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print("Classififcation Report  :",cr)

bias = classifier.score(X_train,y_train)
print("Bias :",bias)

variance = classifier.score(X_test, y_test)
print("variance :",variance)



#SVM


from sklearn.svm import SVC

svmmodel = SVC(kernel='linear')  # You can change kernel to 'rbf', 'poly', etc.
svmmodel.fit(X_train, y_train)

# Predict
y_pred = svmmodel.predict(X_test)

# Accuracy
print("SVM Accuracy:", accuracy_score(y_test, y_pred))


# KNN
from sklearn.neighbors import KNeighborsClassifier


for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k,p=1)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"k={k}, Accuracy={accuracy_score(y_test, y_pred):.2f}")
    
import pickle
from sklearn.preprocessing import StandardScaler

# Assuming 'sc' is your StandardScaler that was already fit on X_train
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Dictionary to hold all models and the scaler
all_models_and_scaler = {
    'logistic_regression': classifier,
    'svm': svmmodel,
    'knn_k=5': KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train),  # Use any preferred k
    'scaler': sc  # Add the scaler used to standardize features
}

# Save everything to a single pickle file
with open('classification_models_and_scaler.pkl', 'wb') as file:
    pickle.dump(all_models_and_scaler, file)

print("All models and scaler saved in 'classification_models_and_scaler.pkl'")
   