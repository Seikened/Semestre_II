import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Ruta de trabajo a establecer
ruta = os.chdir('/Users/fernandoleonfranco/app/')

clientesDatos = pd.read_csv('EjemploClientes.csv')

print(clientesDatos)

# Calculando la correlación entre 'Edad' y 'Antigüedad'
correlacion_edad_antiguedad = clientesDatos['Edad'].corr(clientesDatos['Antiguedad'])
print(f"Correlación entre Edad y Antigüedad: {correlacion_edad_antiguedad}")

datos_numericos = clientesDatos.select_dtypes(include=[np.number])
# Calculando la matriz de correlación para todo el DataFrame
datos_cor = datos_numericos.corr()

# Visualizando la matriz de correlación
plt.figure(figsize=(10, 8))  
sns.heatmap(datos_cor, annot=True, cmap='coolwarm', fmt=".2f", cbar=True, square=True)
plt.title('Matriz de Correlación')
plt.show()



print("-----------------------------Regresión lineal-----------------------------")
# Regresión lineal
ingresosVsEgresosDatos = pd.read_csv('R_Ejemplo Ingresos vs Egresos.csv')
x = sm.add_constant(ingresosVsEgresosDatos['Ingresos'])
y = ingresosVsEgresosDatos['Gastos']


# Ajustando el modelo de regresión lineal
modelo = sm.OLS(y, x).fit()

# Graficando la regresión lineal
plt.figure(figsize=(10, 8))
plt.scatter(ingresosVsEgresosDatos['Ingresos'], ingresosVsEgresosDatos['Gastos'], label='Datos')
plt.plot(ingresosVsEgresosDatos['Ingresos'], modelo.predict(x), color='red', label='Ajuste')
plt.title('Regresión lineal')
plt.xlabel('Ingresos')
plt.ylabel('Gastos')
plt.legend()
plt.show()


print("-----------------------------Intervalos de confianza-----------------------------")

# Intervalos de confianza
print(modelo.conf_int(alpha=0.05))


# Predicción
nuevos_ingresos = pd.DataFrame({'Ingresos': [12600,19000,16000]})
nuevos_ingresos_const = sm.add_constant(nuevos_ingresos)

predicciones = modelo.predict(nuevos_ingresos_const)

print("----------------------------Predicciones-----------------------------")
print(predicciones)


print("-----------------------------Regresión lineal múltiple-----------------------------")

datosContruccion = pd.read_csv('R_Ejemplo Construccion.csv')

# Ajustando el modelo de regresión lineal múltiple
X = sm.add_constant(datosContruccion[['Periodo', 'Superficie', 'ventanas', 'calzada']])
y = datosContruccion['Impuesto']
modelo_multiple = sm.OLS(y, X).fit()

# Nuevos datos para predecir
nuevos_datos_construccion = pd.DataFrame({
    'Periodo': [2014, 2016, 2015],
    'Superficie': [130, 215, 185],
    'ventanas': [5, 7, 3],
    'calzada': [22, 27, 16]
})

nuevos_datos_const = sm.add_constant(nuevos_datos_construccion)  # Fix: Replace "nuevos_datos" with "nuevos_datos_construccion"
predicciones = modelo_multiple.predict(nuevos_datos_const)

print("-----------------------------Predicciones-----------------------------")
# Mostrando las predicciones
print(predicciones)



# Calculando VIF
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
print("-----------------------------VIF-----------------------------")
print(vif_data)