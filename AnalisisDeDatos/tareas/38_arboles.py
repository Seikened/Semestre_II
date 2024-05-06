import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score

# Cambiamos el directorio de trabajo (opcional)
# os.chdir("/Users/fernandoleonfranco/app")

# Cargamos los datos
datos = pd.read_csv("/Users/fernandoleonfranco/app/iris.csv", sep=';', decimal='.')
print("Datos cargados:\n", datos.head())

# Estructura de los datos
print("\nEstructura de los datos:")
print(datos.info())

# Convertir columna 'tipo' a categórica
datos['tipo'] = datos['tipo'].astype('category')

# División en datos de entrenamiento y prueba
ttraining, ttesting = train_test_split(datos, test_size=0.2, random_state=42)

# Modelo de árbol de decisión
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(ttraining.drop('tipo', axis=1), ttraining['tipo'])

# Visualización del árbol
plt.figure(figsize=(20,10))
plot_tree(modelo, filled=True, feature_names=datos.columns.drop('tipo'), class_names=modelo.classes_)
plt.title("Visualización del Árbol de Decisión")
plt.show()

# Predicciones
prediccion = modelo.predict(ttesting.drop('tipo', axis=1))

# Matriz de confusión
MC = confusion_matrix(ttesting['tipo'], prediccion)
print("\nMatriz de Confusión:\n", MC)

# Cálculo de la precisión y error
acierto = accuracy_score(ttesting['tipo'], prediccion)
error = 1 - acierto

print('\nPrecisión:', acierto)
print('Error:', error)
