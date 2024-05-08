# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import networkx as nx
import matplotlib.pyplot as plt

# Leer el conjunto de datos
datos = pd.read_csv('/Users/fernandoleonfranco/app/EjemploEstudiantes.csv', sep=';', decimal=',', index_col=0)

# Crear una columna para la variable objetivo (aprobado/reprobado)
datos['Aprobado'] = np.where(datos.mean(axis=1) >= 7.0, 1, 0)

# Normalizar los datos usando MinMaxScaler
scaler = MinMaxScaler()
datos_scaled = pd.DataFrame(scaler.fit_transform(datos), columns=datos.columns)

# Dividir el conjunto de datos en entrenamiento y prueba
X = datos_scaled.drop(columns=['Aprobado'])
y = datos_scaled['Aprobado']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Construir el modelo de red neuronal
modelo = Sequential([
    Dense(5, input_dim=X_train.shape[1], activation='relu'),  # Primera capa oculta con 5 neuronas
    Dense(3, activation='relu'),                             # Segunda capa oculta con 3 neuronas
    Dense(1, activation='sigmoid')                           # Capa de salida
])

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1, validation_data=(X_test, y_test))

# Definir la función para graficar la red neuronal con pesos
def plot_network_with_weights(modelo, layer_sizes):
    G = nx.DiGraph()
    layer_positions = {}

    # Crear nodos para cada capa con índices ordenados
    for layer_index, size in enumerate(layer_sizes):
        for node in range(size):
            node_label = f"{layer_index}_{node}"
            G.add_node(node_label, layer=layer_index)
            layer_positions[node_label] = (layer_index, -node)

    # Obtener los pesos de las capas del modelo
    weights = [layer.get_weights()[0] for layer in modelo.layers]

    # Conectar las capas con aristas y añadir los pesos
    for layer_index, weight_matrix in enumerate(weights):
        current_layer = [f"{layer_index}_{i}" for i in range(weight_matrix.shape[0])]
        next_layer = [f"{layer_index + 1}_{i}" for i in range(weight_matrix.shape[1])]

        for i, source_node in enumerate(current_layer):
            for j, target_node in enumerate(next_layer):
                weight = round(weight_matrix[i][j], 2)
                G.add_edge(source_node, target_node, weight=weight)

    # Configurar la posición de los nodos para visualizar
    pos = nx.multipartite_layout(G, subset_key="layer")

    # Dibujar los nodos y aristas con etiquetas de pesos
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1000)
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title('Red Neuronal con Pesos Visualizados')
    plt.show()

# Graficar la red neuronal con pesos (5, 3, 1 son las neuronas en cada capa)
plot_network_with_weights(modelo, [X_train.shape[1], 5, 3, 1])
