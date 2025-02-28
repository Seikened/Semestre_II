import os
import pandas as pd
import matplotlib.pyplot as plt


#Establecer una ruta de trabajo
os.chdir('/Users/fernandoleonfranco/app/')

# Leer este archivo 'XLS - Datos Atipicos.csv'
datos = pd.read_csv('XLS - Datos Atipicos.csv')
print(datos)

#      Nombre  Velocidad Entrega  Precio  Valor Educativo
# 0      Adam               2.05    0.30              2.4
# 1      Anna               0.90    1.50              2.5
# 2   Bernard               1.70    2.60              4.3

# Vamos a gráficar diagrama de cajas y bigotes general y luego para cada columna

# Diagrama de cajas y bigotes general
datos.boxplot()
plt.show()

# Diagrama de cajas y bigotes para la columna 'Velocidad Entrega'
datos.boxplot(column='Velocidad Entrega')
plt.show()

# Diagrama de cajas y bigotes para la columna 'Precio'
datos.boxplot(column='Precio')
plt.show()

# Diagrama de cajas y bigotes para la columna 'Valor Educativo'
datos.boxplot(column='Valor Educativo')
plt.show()


# IDENTIFICAR LOS DATOS ATIPICOS
# por ejemplo en R es asi "atipicos = boxplot(datos$Valor.Educativo,plot=FALSE)$out"

atipicos = datos['Valor Educativo'].quantile(0.75) + 1.5 * (datos['Valor Educativo'].quantile(0.75) - datos['Valor Educativo'].quantile(0.25))
print(atipicos)

#Posicion en R
#which(datos$Valor.Educativo == atipicos)
#posicionAtipicos = which(datos$Valor.Educativo == atipicos)
# En python es
posicionAtipicos = datos[datos['Valor Educativo'] == atipicos].index


#Datos totales en R
#datos$Valor.Educativo
# en python es:
print(datos['Valor Educativo'])


# Datos sin atipicos R
#datos_sin_atipico <- datos$Valor.Educativo[-posicionAtipicos]
# en python es:
datos_sin_atipico = datos['Valor Educativo'].drop(posicionAtipicos)