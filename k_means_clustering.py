#IMPORTING THE LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#IMPORTING THE DATASET
dataset = pd.read_csv('Mall_customers.csv')
X = dataset.iloc[:,[3, 4]].values


#USING THE ELBOW METHOD TO FIND THE OPTIMAL NUMBER OF CLUSTERS
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
   kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
   kmeans.fit(X)
   wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
   
#TRAINING THE KMEANS MODEL ON THE DATASET
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
    
#VISUALISING THE CLUSTERS
plt.scatter(X[y_kmeans == 0 ,0], X[y_kmeans == 0 ,1], s = 100, c = 'red', label = 'cluster 1')
plt.scatter(X[y_kmeans == 1 ,0], X[y_kmeans == 1 ,1], s = 100, c = 'blue', label = 'cluster 2')
plt.scatter(X[y_kmeans == 2 ,0], X[y_kmeans == 2 ,1], s = 100, c = 'green', label = 'cluster 3')
plt.scatter(X[y_kmeans == 3 ,0], X[y_kmeans == 3 ,1], s = 100, c = 'cyan', label = 'cluster 4')
plt.scatter(X[y_kmeans == 4 ,0], X[y_kmeans == 4 ,1], s = 100, c = 'magenta', label = 'cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending score (1-100)')
plt.show()
