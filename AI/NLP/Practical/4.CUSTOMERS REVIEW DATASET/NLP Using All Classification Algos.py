# Natural Language Processing

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Load dataset
dataset = pd.read_csv(r"D:\Education\Datascience\PYTHON_BIGINNER\AI\NLP\Practical\4.CUSTOMERS REVIEW DATASET\Restaurant_Reviews.tsv", delimiter='\t', quoting=3)

# Text cleaning
nltk.download('stopwords')
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower().split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    corpus.append(' '.join(review))

# We can also use CountVecrtorization


# # Count Vectorization
# cv = CountVectorizer(max_features=1500)
# X = cv.fit_transform(corpus).toarray()

# TF-IDF Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Train-Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# Metrics
from sklearn.metrics import accuracy_score, confusion_matrix

# Models to test
models = {
    "Logistic Regression": LogisticRegression(),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Linear SVM": SVC(kernel='linear'),
    "RBF SVM": SVC(kernel='rbf'),
    "Naive Bayes": MultinomialNB(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
    "LightGBM": LGBMClassifier()
}

# Run models
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    bias = model.score(X_train, y_train)
    variance = model.score(X_test, y_test)
    cm = confusion_matrix(y_test, y_pred)

    print(f"\n{name}")
    print(f"Accuracy Score: {acc:.4f}")
    print(f"Bias (Train): {bias:.4f}")
    print(f"Variance (Test): {variance:.4f}")
    print(f"Confusion Matrix:\n{cm}")
