import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

# Step 1: Load the dataset
df = pd.read_csv(r"D:\Education\Datascience\PYTHON_BIGINNER\Machine Learning\Unsupervised Learning\Clustering\Hierarchial Clusters\Mall_Customers.csv")

# Step 2: (Optional) Display the first few rows
print(df.head())

# Step 3: Data Preprocessing
# Assuming you want to use all numerical columns
X = df.select_dtypes(include=['float64', 'int64'])  # Selecting only numeric columns
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Create linkage matrix for dendrogram
linked = linkage(X_scaled, method='ward')

# Step 5: Plot dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()

'''
# Step 6: Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  # You can change n_clusters
labels = model.fit_predict(X_scaled)
'''
# Step 6: Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')  # fixed: use 'metric' instead of 'affinity'
labels = model.fit_predict(X_scaled)

# Step 7: Attach cluster labels back to the dataframe
df['Cluster'] = labels

# Step 8: (Optional) View data with clusters
print(df.head())

# Step 9: (Optional) Save clustered data
df.to_csv(r'D:\Education\Datascience\PYTHON_BIGINNER\Machine Learning\Unsupervised Learning\Clustering\Hierarchial Clusters\clustered_output.csv', index=False)

