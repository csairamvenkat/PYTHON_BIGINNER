# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

print(os.getcwd())

# Load dataset
dataset = pd.read_csv(r"D:\Education\Datascience\PYTHON_BIGINNER\Machine Learning\Clustering\Mall_Customers.csv")
X = dataset.iloc[:, [3, 4]].values  # Selecting Annual Income and Spending Score

# Elbow method to find optimal number of clusters
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method")
plt.xlabel("No. Of Clusters")
plt.ylabel('WCSS')
plt.show()

# Apply K-means with 5 clusters
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=0)
y_means = kmeans.fit_predict(X)
print(y_means)

# Plot clusters (corrected y_kmeans to y_means)
plt.scatter(X[y_means == 0, 0], X[y_means == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_means == 1, 0], X[y_means == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[y_means == 2, 0], X[y_means == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X[y_means == 3, 0], X[y_means == 3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(X[y_means == 4, 0], X[y_means == 4, 1], s=100, c='magenta', label='Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


# Verify that y_means length matches the dataset
if len(y_means) != len(dataset):
    raise ValueError(f"Length of y_means ({len(y_means)}) does not match number of rows in dataset ({len(dataset)})")

# Add cluster labels to the DataFrame
dataset['Cluster'] = y_means

# Save to a new Excel file (or overwrite the original)
output_path = r"D:\Education\Datascience\PYTHON_BIGINNER\Machine Learning\Clustering\Mall_Customers_with_Clusters.xlsx"
dataset.to_excel(output_path, index=False)

print(f"Updated dataset saved to {output_path}")