# Importamos las librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.seasonal import STL
from statsmodels.graphics.tsaplots import plot_acf

# Cargamos los datos
datos = pd.read_csv('/Users/fernandoleonfranco/app/R_Series de Tiempo.csv')

# Convertimos la columna de Ventas en una serie de tiempo trimestral
datos_ts = pd.Series(datos['Ventas'].values, index=pd.period_range(start='2021Q1', periods=len(datos), freq='Q'))

# Gráfico de la serie de tiempo
datos_ts.to_timestamp().plot(title='Ventas por Trimestre', xlabel='Trimestres', ylabel='Ventas')
plt.show()

# Ejemplo de suavizados
plt.figure(figsize=(10, 6))
plt.plot(datos_ts.to_timestamp(), label='Original', color='blue')  # Convertimos a timestamp para la graficación
for ventana in [3, 5, 7]:
    datos_suavizados = datos_ts.rolling(window=ventana, center=True).mean()
    plt.plot(datos_suavizados.to_timestamp(), label=f'Suavizado {ventana}-puntos')  # Convertimos a timestamp para la graficación
plt.legend()
plt.title('Suavizados de la serie de tiempo')
plt.xlabel('Trimestres')
plt.ylabel('Ventas')
plt.show()

# Función de autocorrelación
plot_acf(datos_ts)
plt.show()

# Holt-Winters
modelo_hw = ExponentialSmoothing(datos_ts, seasonal='add', seasonal_periods=4).fit()
prediccion_hw = modelo_hw.forecast(4)
plt.plot(datos_ts.to_timestamp(), label='Datos Reales', color='blue')  # Convertimos a timestamp para la graficación
plt.plot(prediccion_hw.to_timestamp(), label='Predicción', color='red', linestyle='--')  # Convertimos a timestamp para la graficación
plt.legend()
plt.title('Predicción con Holt-Winters')
plt.xlabel('Trimestres')
plt.ylabel('Ventas')
plt.show()

# Para series anuales
datos_anuales = pd.read_csv('/Users/fernandoleonfranco/app/Serie_Anual.csv')
datos_ts_anuales = pd.Series(datos_anuales.iloc[:, 0].values, index=pd.date_range(start='2012-01', periods=len(datos_anuales), freq='M'))

# Gráfico de la serie anual
datos_ts_anuales.plot(title='Ventas Mensuales', xlabel='Meses', ylabel='Ventas')
plt.show()

# STL descomposición para series anuales
stl_result = STL(datos_ts_anuales, seasonal=13).fit()
stl_result.plot()
plt.show()

# Suavizado en series anuales
plt.figure(figsize=(10, 6))
plt.plot(datos_ts_anuales, label='Original', color='blue')
for ventana in [3, 5, 7]:
    datos_suavizados = datos_ts_anuales.rolling(window=ventana, center=True).mean()
    plt.plot(datos_suavizados, label=f'Suavizado {ventana}-puntos')
plt.legend()
plt.title('Suavizados de la serie anual')
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.show()

# Nota: El periodograma no tiene una implementación directa y simple en Python equivalente a R. Para análisis de frecuencias puedes explorar `scipy.signal.periodogram`.
