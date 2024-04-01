# run below commands in powershell in order
# cd to current folder
# python -m venv venv
# .\venv\Scripts\Activate.ps1
# pip install numpy matplotlib scikit-learn
# python ./clustering.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Generate synthetic data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Plot the original data
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title('Original Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# KMeans clustering
kmeans = KMeans(n_clusters=4)
kmeans_labels = kmeans.fit_predict(X)

# Plot KMeans clustering result
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, s=50, cmap='viridis')
plt.title('KMeans Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Agglomerative Clustering
agg_clustering = AgglomerativeClustering(n_clusters=4)
agg_labels = agg_clustering.fit_predict(X)

# Plot Agglomerative Clustering result
plt.scatter(X[:, 0], X[:, 1], c=agg_labels, s=50, cmap='viridis')
plt.title('Agglomerative Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Evaluate clustering using silhouette score
kmeans_silhouette = silhouette_score(X, kmeans_labels)
agg_silhouette = silhouette_score(X, agg_labels)

print("KMeans Silhouette Score:", kmeans_silhouette)
print("Agglomerative Clustering Silhouette Score:", agg_silhouette)
