# Metodo montecarlo para contar piezas
# import random

# pesoPromedio = 200
# desviacion = pesoPromedio * 0.047

# piezasTotales = 0   

# for repetir in range(100):
#     pesoTotal = 0
#     pesoPieza = random.gauss(pesoPromedio, desviacion)
#     pesoTotal += pesoPieza
#     pesoPrimeraPieza = pesoPieza
#     for i in range(1, 19):
#         pesoPieza = random.gauss(pesoPromedio, desviacion)
#         pesoTotal += pesoPieza
    
#     numeroPieza = round(pesoTotal / pesoPrimeraPieza)
#     print(f"Peso total: {pesoTotal} Numero de piezas: {numeroPieza}")
#     piezasTotales += numeroPieza

# # Muestro el total de piezas
# print(f"Total de piezas: {piezasTotales}")


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random

# Configuración inicial
pesoPromedio = 200
desviacion = pesoPromedio * 0.047
num_muestras = 1000  # Número de muestras para el conjunto de datos

# Generar datos de entrenamiento
pesos_totales = []
num_piezas = []

for _ in range(num_muestras):
    num_piezas_simuladas = random.randint(10, 20)  # Número aleatorio de piezas entre 10 y 20
    peso_total = np.sum(np.random.normal(pesoPromedio, desviacion, num_piezas_simuladas))
    pesos_totales.append(peso_total)
    num_piezas.append(num_piezas_simuladas)

pesos_totales = np.array(pesos_totales, dtype=float)
num_piezas = np.array(num_piezas, dtype=float)

# Entrenamiento de la red neuronal
epocas = 500
tolerancia = 0.1

while True:
    tf.keras.backend.clear_session()  # Reiniciar la sesión para asegurarnos de que el modelo se inicializa de nuevo

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1,)),
        tf.keras.layers.Dense(units=1)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

    history = model.fit(pesos_totales, num_piezas, epochs=epocas, verbose=False)

    # Predecir valores con datos de entrenamiento
    predictions = model.predict(pesos_totales)

    # Comprobar si el modelo ha aprendido lo suficiente
    if np.all(np.abs(predictions.flatten() - num_piezas) < tolerancia):
        print(f"El modelo ha aprendido lo suficiente después de {epocas} épocas")
        break
    else:
        print(f"El modelo no ha aprendido lo suficiente después de {epocas} épocas, ajustando épocas...")
        epocas += 100
        if epocas > 1500:
            print(f"El modelo no ha aprendido lo suficiente después de {epocas} épocas")
            break

# Predecir el número de piezas para un nuevo peso total
nuevo_peso_total = np.array([4000])  # Puedes ajustar este valor según necesites
prediccion_num_piezas = model.predict(nuevo_peso_total)
print(f"Para un peso total de {nuevo_peso_total[0]}g, el modelo predice aproximadamente {prediccion_num_piezas[0][0]:.0f} piezas.")
