# MAQUINAS DE SOPORTE VECTORIAL

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
import os

# Cambiar el directorio de trabajo
os.chdir("/Users/fernandoleonfranco/app")  # Descomenta y ajusta la ruta según sea necesario

# Cargar datos
datos = pd.read_csv("iris.csv", sep=";", decimal=".")
print(datos.head())

# Revisar la estructura de los datos
print(datos.info())

# Cambiar la variable objetivo a categórica
datos['tipo'] = datos['tipo'].astype('category')
print(datos.info())

# Segmentar para entrenamiento y para testear
train_data, test_data = train_test_split(datos, test_size=0.33, random_state=42)

# Entrenamiento del modelo SVM
modelo = SVC(kernel='linear')
modelo.fit(train_data.drop('tipo', axis=1), train_data['tipo'])

# Predicción
prediccion = modelo.predict(test_data.drop('tipo', axis=1))
print(prediccion)

# Matriz de confusión y métricas de evaluación
matriz_de_confusion = confusion_matrix(test_data['tipo'], prediccion)
print(matriz_de_confusion)

# Precisión del modelo
acierto = accuracy_score(test_data['tipo'], prediccion)
print("Precisión:", acierto)

# Error
error = 1 - acierto
print("Error:", error)
