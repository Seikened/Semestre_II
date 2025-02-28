import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

# Carga de datos
datosCargados = pd.read_csv('/Users/fernandoleonfranco/app/EjemploAlgoritmosRecomendacion.csv', sep=',', decimal='.', index_col=0)

# Métodos de aglomeración
metodosAglomeracion = ['complete', 'single', 'average', 'ward']

# Realizar clustering jerárquico y visualizar dendrogramas
for metodo in metodosAglomeracion:
    # Enlace de la matriz de distancia
    modeloClustering = linkage(datosCargados, method=metodo)
    plt.figure(figsize=(10, 7))
    dendrogram(modeloClustering, labels=datosCargados.index, leaf_rotation=90, leaf_font_size=10)
    plt.title(f'Dendrograma de estudiantes método: {metodo}')
    plt.show()
    
    # Identificación de clusters
    clustersIdentificados = fcluster(modeloClustering, 3, criterion='maxclust')
    datosCargados[f'cluster_{metodo}'] = clustersIdentificados

# Guardar los datos con clusters asignados
datosCargados.to_csv("EjemploEstudiantesCluster.csv")

# Análisis de Componentes Principales (PCA)
escalador = StandardScaler()  # Esto es para estandarizar los datos
datosEstandarizados = escalador.fit_transform(datosCargados.iloc[:, :-4])  # Excluir columnas de cluster

analisisPCA = PCA(n_components=5) # Seleccionar 5 componentes principales
resultadosPCA = analisisPCA.fit_transform(datosEstandarizados) # Ajustar PCA

# Agglomerative Clustering sobre resultados de PCA
aglomerativo = AgglomerativeClustering(n_clusters=3) # Seleccionar 3 clusters
clustersIdentificados = aglomerativo.fit_predict(resultadosPCA) # Ajustar clustering jerárquico
dfPCA = pd.DataFrame(data=resultadosPCA, columns=[f'PC{i+1}' for i in range(5)]) # Crear DataFrame con resultados de PCA
dfPCA['cluster'] = clustersIdentificados # Agregar columna de clusters

# Visualización de los resultados de PCA con clusters
plt.figure(figsize=(10, 7))
dispersion = plt.scatter(dfPCA['PC1'], dfPCA['PC2'], c=dfPCA['cluster'], cmap='viridis')
plt.title('Mapa de PCA con Clusters')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(*dispersion.legend_elements(), title="Clusters")
plt.show()

# Guardar los datos de PCA con clusters
dfPCA.to_csv("PCA_Clusters.csv")
