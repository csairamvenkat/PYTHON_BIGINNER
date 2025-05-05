# Import libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Prepare dataset
data = {
    'Position': [
        'Jr Software Engineer', 'Sr Software Engineer', 'Team Lead', 'Manager',
        'Sr manager', 'Region Manager', 'AVP', 'VP', 'CTO', 'CEO'
    ],
    'Level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]
}

df = pd.read_csv(r'C:\Users\sai.venkat\OneDrive\DataScience\Python\PYTHON_BIGINNER\Machine Learning\Classification\Practical\Tree Algorithm\emp_sal.csv') #pd.DataFrame(data)

# Create salary class bins
df['SalaryClass'] = pd.cut(
    df['Salary'],
    bins=[0, 70000, 150000, 300000, float('inf')],
    labels=['Low', 'Medium', 'High', 'Very High']
)

# Encode class labels
le = LabelEncoder()
df['SalaryClassEncoded'] = le.fit_transform(df['SalaryClass'])

# Features and target
X = df[['Level']]
y = df['SalaryClassEncoded']


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)

# Predict test set
y_pred = clf.predict(X_test)

# Accuracy and error
accuracy = accuracy_score(y_test, y_pred)
error = 1 - accuracy
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Error Rate: {error * 100:.2f}%\n")

# Classification report with explicit label order
print("Classification Report:")
print(classification_report(
    y_test, y_pred,
    labels=[0, 1, 2, 3],
    target_names=le.classes_,
    zero_division=0
))

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=[0, 1, 2, 3]))

# Predict a specific level
level_to_predict = 6.5
predicted_class_encoded = clf.predict([[level_to_predict]])
predicted_class = le.inverse_transform(predicted_class_encoded)
print(f"\nPredicted salary class for level {level_to_predict}: {predicted_class[0]}")

# Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Level', y='SalaryClassEncoded', data=df, color='red', label='Actual')
plt.plot(df['Level'], clf.predict(X), color='blue', label='Predicted')
plt.yticks(ticks=range(len(le.classes_)), labels=le.classes_)
plt.xlabel('Level')
plt.ylabel('Salary Class')
plt.title('Decision Tree Classification - Level vs Salary Class')
plt.legend()
plt.grid(True)
plt.show()
