import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Función para cargar los datos
def cargar_datos(ruta, sep, dec):
    return pd.read_csv(ruta, sep=sep, decimal=dec, index_col=0)

# Realizar PCA y calcular loadings
def realizar_pca(datos, ncp=5):
    pca = PCA(n_components=ncp)
    scores = pca.fit_transform(datos)
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
    return scores, loadings, pca

# Graficar plano principal
def graficar_plano_principal(scores, labels, componentes=(0, 1), color='red', titulo='Plano Principal'):
    plt.figure(figsize=(10, 8))
    plt.scatter(scores[:, componentes[0]], scores[:, componentes[1]], color=color)
    for i, label in enumerate(labels):
        plt.annotate(label, (scores[i, componentes[0]], scores[i, componentes[1]]))
    plt.title(titulo)
    plt.xlabel(f'Componente {componentes[0]+1}')
    plt.ylabel(f'Componente {componentes[1]+1}')
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    plt.grid(True)
    plt.show()

# Graficar círculo de correlaciones
def graficar_circulo_correlaciones(loadings, labels, componentes=(0, 1), color='blue', titulo='Círculo de Correlaciones'):
    fig, ax = plt.subplots(figsize=(10, 8))
    circle = Circle((0, 0), radius=1, color='blue', fill=False)
    ax.add_patch(circle)
    plt.scatter(loadings[:, componentes[0]], loadings[:, componentes[1]], color=color)
    for i, label in enumerate(labels):
        plt.annotate(label, (loadings[i, componentes[0]], loadings[i, componentes[1]]))
    plt.title(titulo)
    plt.xlabel(f'Componente {componentes[0]+1}')
    plt.ylabel(f'Componente {componentes[1]+1}')
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Función para el biplot
def graficar_biplot(scores, loadings, labels, componentes=(0, 1), titulo='Biplot'):
    plt.figure(figsize=(10, 8))
    plt.scatter(scores[:, componentes[0]], scores[:, componentes[1]], color='red', alpha=0.5)
    for i, (comp1, comp2) in enumerate(zip(loadings[:, componentes[0]], loadings[:, componentes[1]])):
        plt.arrow(0, 0, comp1 * max(abs(scores[:, componentes[0]])),
                  comp2 * max(abs(scores[:, componentes[1]])), color='blue', alpha=0.5)
        if labels is not None:
            plt.text(comp1, comp2, 'Var'+str(i+1), color='green', ha='center', va='center')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.title(titulo)
    plt.grid(True)
    plt.show()

# Datos y rutas
datasets = [
    ('/Users/fernandoleonfranco/app/EjemploEstudiantes.csv', ';', ','),
    ('/Users/fernandoleonfranco/app/EjemploClientes.csv', ',', '.'),
    ('/Users/fernandoleonfranco/app/EjemploAlgoritmosRecomendacion.csv', ',', '.')
]

# Procesar cada conjunto de datos
for ruta, sep, dec in datasets:
    datos = cargar_datos(ruta, sep, dec)
    scores, loadings, pca = realizar_pca(datos)
    graficar_plano_principal(scores, datos.index.tolist())
    graficar_circulo_correlaciones(loadings, datos.columns.tolist())
    graficar_biplot(scores, loadings, datos.columns.tolist())

