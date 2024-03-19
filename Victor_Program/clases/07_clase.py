# # Metodo montecarlo
# import random

# lista = [random.randint(1,17) for i in range(1700)]
# listaConteo = [ 0 for x in range(18)]

# for numero in lista:
#     listaConteo[numero] += 1

# for i in range(1,18):
#     print(f"El número {i} salio {listaConteo[i]} veces")




# # Generador de numeros distribucion normal
# import matplotlib.pyplot as plt
# import random


# lista = [random.gauss(100,15) for i in range(1700)]

# limiteInferior = list(range(40, 161, 10))
# conteo = [0 for x in range(13)]

# print(limiteInferior)

# for estaManzana in lista:
#     for i,limIf in enumerate(limiteInferior):
#         limSup = limIf + 10
#         if limIf <= estaManzana < limSup:
#             conteo[i] += 1
#             break

# for numero in conteo:
#     print(f"El número {numero} salio {conteo[numero]} veces")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random

# Generamos la lista de números con distribución normal
lista = [random.gauss(100, 15) for i in range(1700)]

# Definimos los límites inferiores de cada rango
limiteInferior = list(range(40, 161, 10))
conteo = [0 for x in range(len(limiteInferior))]

# Contamos cuántas veces cae cada número dentro de los rangos
for estaManzana in lista:
    for i, limIf in enumerate(limiteInferior):
        limSup = limIf + 10
        if limIf <= estaManzana < limSup:
            conteo[i] += 1
            break

# Creamos un DataFrame con los resultados
df = pd.DataFrame({
    'Rango': [f"{lim} - {lim + 10}" for lim in limiteInferior],
    'Frecuencia': conteo
})

# Graficamos usando Seaborn
sns.barplot(x='Rango', y='Frecuencia', data=df, palette='viridis', ci=None, estimator=sum)
plt.xticks(rotation=45)  # Rotamos las etiquetas del eje X para mejor lectura
plt.show()


