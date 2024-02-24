import asyncio
import random
import time

async def TareaSuma(lista):
    tiempoInicial = time.time()
    suma = sum(lista)
    tiempoFinal = time.time() - tiempoInicial
    return suma, tiempoFinal

async def TareaSumaCuadrados(lista):
    tiempoInicial = time.time()
    sumaCudrados = sum( num**2 for num in lista)
    tiempoFinal = time.time() - tiempoInicial
    return sumaCudrados, tiempoFinal


async def main(lista):
    # Ejecutamos ambas tareas de forma concurrente y capturamos los resultados
    Tarea_Suma, TareaSuma_Cuadrados = await asyncio.gather(TareaSuma(lista), TareaSumaCuadrados(lista))
    return Tarea_Suma, TareaSuma_Cuadrados  # Devolvemos los resultados



# ===============================================================
tiempoInicial = time.time()
lista = [ random.randint(1,1000) for i in range(100000000)]


# Ejecutamos la función principal
Suma, SumaCuadrados = asyncio.run(main(lista))

# Quiero verificar que otras tareas no asincrónicas se ejecutan de forma concurrente e independiente

tiewmpoFinal = time.time() - tiempoInicial
# Vamos a imprimir los resultados de todos los tiempos involucrados y sus resultados
print(f"La suma de los números es: {Suma[0]} y se demoró {Suma[1]} segundos")
print(f"La suma de los cuadrados de los números es: {SumaCuadrados[0]} y se demoró {SumaCuadrados[1]} segundos")
print(f"El tiempo total de ejecución fue: {tiewmpoFinal} segundos")



# lista =[680,
#         216,
#         180,
#         180,
#         3500,
#         216,
#         180,
#         396,
#         3200,
#         4600,
#         220,
#         652,
#         100,
#         216
#         ]


# suma = sum(lista)
# print(suma)
