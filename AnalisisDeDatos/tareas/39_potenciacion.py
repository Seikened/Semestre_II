import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos


file_path = "/Users/fernandoleonfranco/app/MuestraCredito_Completo.csv"
datos = pd.read_csv(file_path, sep=";", decimal=".")

# Convertir las columnas a categorías
columnas_categoricas = [
    'MontoCredito', 'IngresoNeto', 'CoefCreditoAvaluo',
    'MontoCuota', 'GradoAcademico', 'BuenPagador'
]
for columna in columnas_categoricas:
    datos[columna] = datos[columna].astype('category')

# Segmentar para entrenamiento y testing
train_data, test_data = train_test_split(datos, test_size=0.2, random_state=42)

# Definir características y etiquetas para el modelo
X_train = train_data.drop(columns='BuenPagador')
y_train = train_data['BuenPagador']
X_test = test_data.drop(columns='BuenPagador')
y_test = test_data['BuenPagador']

# Crear y entrenar el modelo de potenciación (AdaBoost)
modelo = AdaBoostClassifier(n_estimators=20, learning_rate=1, algorithm="SAMME", random_state=42)
modelo.fit(X_train, y_train)

# Predicción
prediccion = modelo.predict(X_test)

# Matriz de confusión
MC = confusion_matrix(y_test, prediccion)

# Porcentaje (precisión)
acierto = accuracy_score(y_test, prediccion)
error = 1 - acierto

print(f"Precisión: {acierto:.2f}")
print(f"Error: {error:.2f}")

# Graficar la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(MC, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicción")
plt.ylabel("Valor Real")
plt.title("Matriz de Confusión")
plt.show()
