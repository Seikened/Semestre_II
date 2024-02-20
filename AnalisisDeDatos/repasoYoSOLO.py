1. #17 - Calcular el factorial de un número: Este ejercicio es desafiante porque implica entender el concepto matemático de factorial y cómo implementar este cálculo mediante bucles o recursividad, lo cual puede ser complejo sin el uso de librerías.

def Factorial(numero=3):
    factorial = 1
    for num in range(1,numero+1):
        factorial *= num
    return factorial







2. #12 - Determinar si un número de 5 dígitos es capicúa: Requiere una lógica detallada para invertir el número o comparar sus dígitos sin utilizar métodos predefinidos, lo que puede ser bastante intrincado.
def Capicua(numero=52345):
    # 52 3 25
    primerNumero = numero //10000
    residuo = numero%10000
    segundoNumero = residuo//1000
    residuo= residuo%1000
    tercerNumero= residuo // 100
    residuo = residuo%100
    cuartoNumero = residuo//10
    residuo = residuo%10
    quintoNumero = residuo
    
    if (primerNumero == quintoNumero) and (segundoNumero == cuartoNumero):
        return "Si es capicua"
    else:
        return "No es capicua"




3. #10 - Determinar si un número es primo: Este ejercicio es desafiante por la necesidad de implementar una lógica para verificar si un número tiene divisores aparte de 1 y sí mismo.

numero = 6
raiz = int(numero**(1/2))

if numero <2:
    print("No es primo")

for num in range(2,raiz+1):
        if numero%num ==0:
            print(" No es primo")
            break
        else:
            print("Es primo")








4. #5 - [FUNCIONES TEXTO] Separar una frase de 3 palabras sin usar librerías: Asumiendo que este ejercicio es complicado por la restricción de no usar librerías, implica manipular cadenas y entender cómo iterar y reconocer separadores de palabras manualmente.



def SepararTexto(userText="Hola soy fernando"):
    texto= userText + " "
    listaPalabras = []
    puntoAnteriror = 0
    for pos,caracter in enumerate(texto):
        if caracter == " ":
            palabra = texto[puntoAnteriror:pos]
            puntoAnteriror = pos
            listaPalabras.append(palabra)
    return listaPalabras



5. #15 - Calcular el promedio de 4 calificaciones y clasificarlo: Aunque no es extremadamente complejo, combina la recopilación de datos, cálculo de promedios y la aplicación de múltiples condiciones para clasificar el resultado, lo que puede ser un buen desafío.

import random
listaCalificaciones = [random.randint(1,10) for _ in range(4) ]
califSumada = sum(listaCalificaciones)

promedio = califSumada/len(listaCalificaciones)

texto = ""
if 10>= promedio >=9:
    texto = "A"
elif 8.9>=promedio>=8:
    texto="B"
elif 7.9>=promedio>=7:
    texto="C"
elif 6.9>=promedio>=6:
    texto="D"
elif 5.9>=promedio>=0:
    texto="F"
else:
    texto = "El número esta fuera del rango"





6. #14 - Sumatoria de números ingresados por el usuario: Este ejercicio requiere recolectar una cantidad dinámica de entradas del usuario, sumarlas y manejar adecuadamente las variables, lo que introduce un nivel interesante de complejidad.

# cantidadNumeros = int(input("Dame total de tus números: "))
# listaNumeros = sum(float(input("Dame un número: ")) for i in range(cantidadNumeros))
# print(listaNumeros)


7. #9 - [FOR] Pedir 5 números, y presentar la suma, el conteo y el promedio: Implica la gestión de múltiples entradas y la realización de varias operaciones estadísticas básicas, lo que puede ser un buen ejercicio para practicar la iteración y el cálculo.
listaCalificaciones = [random.randint(1,10) for _ in range(5) ]
promedio = sum(listaCalificaciones)/len(listaCalificaciones)
#print(f"Lista de calificaciones:{listaCalificaciones} , cantidad de datos: {len(listaCalificaciones)} y promedio: {promedio}")



9. #4 - [IF] Ordenar 3 números de forma descendente: Requiere una comprensión de las estructuras condicionales para comparar y ordenar los números, lo que puede ser menos intuitivo sin el uso de funciones de ordenación.

# a= 2
# b = 3
# c = 6

# if a<b:
#     a,b = b,a
    
# if a<c:
#     a,c = c,a
    
# if  b<c:
#     b,c=c,b

# print(a,b,c)





10. #13 - [FOR] Contar números impares en una lista: Aunque más directo, este ejercicio introduce la iteración sobre una lista y la aplicación de condiciones, siendo un buen ejercicio para entender el flujo de control y las operaciones con listas.
