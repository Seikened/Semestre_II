# Crear población
import random

# Creamos la poblaicón binaria
def Poblacion(tamPoblacion, tamCadena):
    poblacion = []
    
    for _ in range(tamPoblacion):
        individuo = [random.randint(0,1) for _ in range(tamCadena)]
        poblacion.append(individuo)
    return poblacion


#La función de aptitud evalúa qué tan buena es una solución. 
# Por ejemplo, podríamos decir que queremos maximizar el número de 1s en la cadena de bits.
def aptitud(individuo):
    return sum(individuo)






#================ Test ====================
tamanoPoblacion = 10
tamanoCadena = 20

poblacionInicial = Poblacion(tamanoPoblacion,tamanoCadena)

print(poblacionInicial)
