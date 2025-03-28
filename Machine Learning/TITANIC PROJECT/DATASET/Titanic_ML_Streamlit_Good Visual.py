import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# titanic = pd.read_csv('../input/train.csv', header = 0, dtype={'Age': np.float64})
titanic = pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Libraries\Machine Learning\TITANIC PROJECT\DATASET\titanic dataset.csv', header = 0, dtype={'Age': np.float64})
titanic.tail()

# Data preprocessing steps as provided by the user

def getNumber(str):
    if str=="male":
        return 1
    else:
        return 2

titanic["Gender"] = titanic["Sex"].apply(getNumber)
del titanic["Sex"]

meanS = titanic[titanic.Survived == 1].Age.mean()
titanic["age"] = np.where(pd.isnull(titanic.Age) & titanic["Survived"] == 1, meanS, titanic["Age"])

meanNS = titanic[titanic.Survived == 0].Age.mean()
titanic.age.fillna(meanNS, inplace=True)

del titanic['Age']

titanic.dropna(inplace=True)

titanic.rename(columns={'age': 'Age', 'Gender': 'Sex'}, inplace=True)

def getEmb(str):
    if str == "S":
        return 1
    elif str == 'Q':
        return 2
    else:
        return 3

titanic["Embark"] = titanic["Embarked"].apply(getEmb)
del titanic['Embarked']
titanic.rename(columns={'Embark': 'Embarked'}, inplace=True)

# Males and females count pie chart
males = (titanic['Sex'] == 1).sum()
females = (titanic['Sex'] == 2).sum()
p = [males, females]

# For Streamlit
fig, ax = plt.subplots(figsize=(6, 6))  # Adjusting size for better visibility
ax.pie(p, labels=['Male', 'Female'], colors=['#66c2ff', '#ffb3e6'], 
       explode=(0.15, 0), startangle=90, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
st.pyplot(fig)

# More detailed pie chart with survived and not survived males and females
MaleS = titanic[(titanic.Sex == 1) & (titanic.Survived == 1)].shape[0]
MaleN = titanic[(titanic.Sex == 1) & (titanic.Survived == 0)].shape[0]
FemaleS = titanic[(titanic.Sex == 2) & (titanic.Survived == 1)].shape[0]
FemaleN = titanic[(titanic.Sex == 2) & (titanic.Survived == 0)].shape[0]

chart = [MaleS, MaleN, FemaleS, FemaleN]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
labels = ["Survived Male", "Not Survived Male", "Survived Female", "Not Survived Female"]
explode = [0, 0.05, 0, 0.1]

# For Streamlit
fig, ax = plt.subplots(figsize=(8, 8))  # Adjusting size for better visibility
ax.pie(chart, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, 
       wedgeprops={'edgecolor': 'black'}, explode=explode, counterclock=False)
ax.axis('equal')
st.pyplot(fig)
