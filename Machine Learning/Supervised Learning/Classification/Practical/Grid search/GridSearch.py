import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sns
from matplotlib.colors import ListedColormap

# Load dataset
ds = pd.read_csv(r'D:\Education\Datascience\PYTHON_BIGINNER\Machine Learning\Supervised Learning\Classification\Practical\Grid search\Social_Network_Ads.csv')
x = ds.iloc[:, 2:4].values
y = ds.iloc[:, -1].values

# Feature scaling
sc = StandardScaler()
x = sc.fit_transform(x)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Initial SVC training
classifier = SVC()
classifier.fit(x_train, y_train)

# Predictions
y_pred = classifier.predict(x_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Heatmap for confusion matrix
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Accuracy and classification report
print("Accuracy Score: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Bias and variance
bias = classifier.score(x_train, y_train)
variance = classifier.score(x_test, y_test)
print("Training Accuracy (Bias): {:.2f}%".format(bias * 100))
print("Test Accuracy (Variance): {:.2f}%".format(variance * 100))

# K-fold cross-validation
accuracies = cross_val_score(estimator=classifier, X=x_train, y=y_train, cv=5)
print('Cross-Val Accuracy: {:.2f}%'.format(accuracies.mean() * 100))
print('Cross-Val Std Dev: {:.2f}%'.format(accuracies.std() * 100))

# Grid Search for best parameters
parameters = [
    {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
    {'C': [1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]}
]
grid_search = GridSearchCV(estimator=SVC(), param_grid=parameters, scoring='accuracy', cv=10)
grid_search.fit(x_train, y_train)
best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_
print('Best Accuracy from Grid Search: {:.2f}%'.format(best_accuracy * 100))
print('Best Parameters:', best_parameters)

# Use best estimator for final visualization and prediction
best_model = grid_search.best_estimator_
best_model.fit(x_train, y_train)

# Visualization function
def plot_decision_boundary(model, x_set, y_set, title):
    x1, x2 = np.meshgrid(
        np.arange(start=x_set[:, 0].min() - 1, stop=x_set[:, 0].max() + 1, step=0.01),
        np.arange(start=x_set[:, 1].min() - 1, stop=x_set[:, 1].max() + 1, step=0.01)
    )
    plt.contourf(x1, x2, model.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(x1.min(), x1.max())
    plt.ylim(x2.min(), x2.max())

    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                    c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()

# Plot training set
plot_decision_boundary(best_model, x_train, y_train, 'SVM (Training set)')

# Plot test set
plot_decision_boundary(best_model, x_test, y_test, 'SVM (Test set)')
