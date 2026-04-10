# Import the necessary libraries
# Data manipulation and numerical operations
import pandas as pd
import numpy as np

# Data visualization
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from  sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generate synthetic datapioints for clustering
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)           

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)    

# Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()     


# Evaluate the clustering performance using silhouette score
for i in range(2, 10):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    score = silhouette_score(X, y_kmeans)
    print(f'Number of Clusters: {i}, Silhouette Score: {score:.2f}')
 

