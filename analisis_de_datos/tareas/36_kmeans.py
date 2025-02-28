# Importando librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

import os

# Imprimir el directorio actual
print("Directorio actual antes de cambiar:", os.getcwd())

# Cambiar el directorio de trabajo
os.chdir('/Users/fernandoleonfranco/app')

# Cargando el primer conjunto de datos
datos = pd.read_csv('EjemploEstudiantes.csv', sep=';', decimal=',', index_col=0)

# Aplicando K-Means
kmeans = KMeans(n_clusters=3, max_iter=100)
kmeans.fit(datos)

# Extracción de resultados del clustering
clusters = kmeans.labels_
centers = kmeans.cluster_centers_
total_inertia = kmeans.inertia_

# Tamaño de los grupos
sizes = np.bincount(clusters)

# Añadiendo la columna de clusters a los datos
datos['cluster'] = clusters

# Visualización de los clusters en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(datos.iloc[:, 0], datos.iloc[:, 1], datos.iloc[:, 2], c=clusters, marker='o')  # puntos de datos
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='blue', marker='o')  # centros
plt.show()

# Método del codo para determinar el número óptimo de clusters
inertias = []
for k in range(1, 9):
    kmeans = KMeans(n_clusters=k, max_iter=100)
    kmeans.fit(datos)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 9), inertias, marker='o', color='red')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.title('Método del Codo')
plt.show()
