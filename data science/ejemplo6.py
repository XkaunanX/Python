import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Paso 1: Cargar el conjunto de datos Iris
data = load_iris()
X = data.data
y = data.target

# Paso 2: Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Paso 3: Visualización de los clusters
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.title("Agrupación con K-Means (Iris Dataset)")
plt.xlabel("Longitud del sépalo")
plt.ylabel("Ancho del sépalo")
plt.show()
