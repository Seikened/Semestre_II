# 1) Solicitar un valor en pesos y presentarlo en dolares y euros
def EurosDolares(pesos):
    pesos_a_euros = pesos*(.054)
    pesos_a_dolares = pesos*(.059)
    return pesos_a_dolares,pesos_a_euros
# 2) Pedir un importe y presentar el iva y el total general (Monto mas iva)
Iva = lambda subTotal:subTotal*1.16

# 3) Pedir un valor en segundos, y presentarlo en Horas:Minutos:Segundos  4000 s-->01:06:40 
def FormateadorHoras(segundos):
    segundos_restantes=0
    horas= segundos//3600
    segundos_restantes = segundos%3600
    minutos = segundos_restantes//60
    segundos_restantes = segundos_restantes%60
    return f"{horas}:{minutos}:{segundos_restantes}:"

# 4) [IF] Pedir 3 numeros y mostrarlos en forma ordenada descendente-----------------------------------------------
def OrdenadoDesendentre(listaNumeros):
    for i in range(len(listaNumeros)-1):
        for num in listaNumeros:
            if num < listaNumeros[i+1]:
                listaNumeros[i],listaNumeros[i+1] = listaNumeros[i+1],listaNumeros[i]
    return listaNumeros


# 5) [FUNCIONES TEXTO] Solicitar una frase de 3 palabras y mostrar las palabras separadas---------------------------------------------------------
def Frase(frase):
    listaPalabras = []
    palabra = ""
    for i,caracter in enumerate(frase):
        if caracter == " ":
            palabra = frase[0:i]
            listaPalabras.append(palabra)
    return listaPalabras


# 6) Calcular la hipotenusa (pidiendo ambos lados:opuesto y adyacente)
def Hipotenusa(ca,co):
    return ((ca**2)+(co**2))^(1/2)


# 7) [IF] Solicitar un numero e indicar si es impar
def Impar(numero):
    if numero%2==0:
        return f"Par"
    else:
        return f"Impar"


# 8) [ELIF] Pedir una calificacion (5 al 10), e indicar la leyenda:10-excelente, 9-muy bien, 8-Bien, 7-Regular, 6-Mal, 5-Reprobado
def CalculadorCalificaciones(calificacion):
    match calificacion:
        case 10:
            return "excelente"
        case 9:
            return "muy bien"
        case 8:
            return "bien"
        case 7:
            return "Regular"
        case 6:
            return "Mal"
        case 5:
            return "Reprobado"
        case _:
            return "Fuera del rango"



# 9) [FOR] Pedir 5 numeros, y presentar la suma, el conteo y el promedio

def NumerosSumados(listaNumeros):
    conteo = 0
    suma = 0
    for num in listaNumeros:
        suma += num
        conteo +=1
    promedio = suma/conteo
    return f"Suma: {suma} ,Conteo: {conteo}, Promedio: {promedio}"


# 10) [FOR] Pedir un numero e indicar si es un numero primo
def IfNumeroPrimo(numero):
    if numero < 2:
        primo="No es primo"
    else:
        raiz= int(numero**(0.5))+1
        primo=True
        for num in range(2,raiz):
            if numero%num == 0:
                primo=False
                break
        if primo:
            return f"Tu número {numero} es primo"
        else:
            return f"Tu número {numero} No es primo"



# 11) [FOR] Escribe un programa que indique cuantos años pares existen entre 1950 y 2010
def ContadorYearImpars(yearOne,yearTwo):
    quantityYear = abs(yearOne-yearTwo)+1
    listYearsImpars = []
    for year in range(0,quantityYear):
        if year%2!=0:
            listYearsImpars.append(year)
    return len(listYearsImpars)

# 12) Escribir un numero de 5 dígitos e indicar si se trata de una capicua
def Capicua(numero):
    #19,215
    primerNumero = numero // 10000
    resNum = numero%10000
    segundoNumero = resNum//1000
    resNum = resNum%1000
    tercerNumero = resNum//100
    resNum = resNum%100
    cuartoNumero = resNum//10
    resNum = resNum%10
    quintoNumero = resNum

    if (primerNumero==quintoNumero) and (segundoNumero==cuartoNumero):
        return f"{numero} ES UNA CAPICUA"
    else:
        print(f"El número {num} no es primo.")



#--------------------------------------------------
#09_cincoDigitos.py
# Invertir los digitos
def Invertir(val):
    nuevoDigito = ""
    for i in val[::-1]:
        nuevoDigito += f'{i}'
    
    return int(nuevoDigito)
digito = input("Introduce tu número: ")

digito_invertido = Invertir(digito)
print(f"Digito introducido {digito}, e invertido es: {digito_invertido}")
#--------------------------------------------------
#10_promedioMValMinVal.py
import random

def Max_min(lista):
    max = -9999999
    min = 9999999
    for num in lista:
        if num >= max:
            max = num
        if num <= min:
            min = num
    return min,max



def Promedio(lista):
    sum = 0
    for num in lista:
        sum += num
    return round(sum / (len(lista)),2)



#-------------#-------------#-------------#-------------#-------------

tam_lista = int(input("De que tamaño será tu lista de números: "))
lista_num = []
for i in range(tam_lista):
    #input(f"Dame el no. {i+1}: ")
    lista_num.append( round( random.uniform(1,10) , 2 ) )

prom = Promedio(lista_num)
min,max = Max_min(lista_num)

print(f"Tu lista es: {lista_num} y el valor máximo es: {max} y el mínimo es: {min} y el promedio de tu lista es: {prom}")





#--------------------------------------------------
#11_anoBisiesto.py
leap_years = []
years = list(range(1900,2025))

for year in years:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # es año bisiesto
                leap_years.append(year)
        else:
            # es año bisiesto
            leap_years.append(year)

print(f"Hay {len(leap_years)} años bisiestos desde 1900 hasta 2024 y son:")
for  leap_year in leap_years:
    print(f"-{leap_year}")
#--------------------------------------------------
#12_pares_while.py
# Ejercicio 1. De la siguiente lista , indicar cuantos números son pares

lista = [8,14,22,3,7,28,36,49,52]

c = 0
pares = 0
while c < len(lista):
    i = lista[c]
    if i % 2 == 0:
        pares += 1
    c += 1

print(f"Hay {pares} pares")
#--------------------------------------------------
#13_arriba_quince.py
# Ejercicio 2. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar cuantos números están por encima de 15

lista = [8,14,22,3,7,28,36,49,52]

c = 0
arribaQuince = 0
while c < len(lista):
    i = lista[c]
    if i > 15:
        arribaQuince += 1
    c += 1

print(f"Hay {arribaQuince} números arriba del 15")
#--------------------------------------------------
#14_promedio_sumatoria_valores.py
#Ejercicio 3. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar la cantidad de valores, la sumatoria y su promedio
lista = [8,14,22,3,7,28,36,49,52]

c = 0
sumatoria = 0
while c < len(lista):
    i = lista[c]
    sumatoria += i
    c += 1

promedio = sumatoria/c
print(f"""
El promedio es {promedio} 
La cantidad de valores es: {c}
La sumatoria es {sumatoria}""")
#--------------------------------------------------
#15_desvEstandar_varianza.py
#Ejercicio 3. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar la cantidad de valores, la sumatoria y su promedio
lista = [8,14,22,3,7,28,36,49,52]

c = 0
sumatoria = 0
while c < len(lista):
    i = lista[c]
    sumatoria += i
    c += 1
promedio = sumatoria/c

# Ejercicio 3.1. Del ejercicio anterior, calcular el La Varianza y Desviación Estándar Poblacional

c = 0
sumatoriaDesv = 0
while c < len(lista):
    sumatoriaDesv = (lista[c]-promedio)**2
    c+=1

varianza = (sumatoriaDesv/c)**(1/2)
desvEstandar = varianza**2

print(f"""
El promedio es {promedio} 
La cantidad de valores es: {c}
La sumatoria es {sumatoria}
La varianza es {varianza}
La desviación estándar es {desvEstandar}
""")
#--------------------------------------------------
#16_numeroImpares_while.py
# Ejercicio 4. Realiza un programa que pida 2 números enteros, e imprima los números impares que existen entre los 2 valores
uno = int(input("Dame tu primer número entero: "))
dos = int(input("Dame tu segundo número entero: "))
totalImpares = 0
c = uno
while c < dos:
    if c % 2 != 0:
        print(f"Número impar es: {c}")
        totalImpares += 1
    c+=1
print(f"Termine, hay {totalImpares} de números impares")



#--------------------------------------------------
#17_comparacion_lista.py
# Ejercicio 5. Realizar un programa que permita cargar dos listas de N valores cada una. 
# Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")


numLenLista1 = int(input("De que tamaño será tu lista 1: "))
c = 0
sumatoriaLista1 = 0
while c < numLenLista1:
    numUser1 = int(input(f"Cual es tu número {c+1} de tu lista 1: "))
    sumatoriaLista1 += numUser1
    c+=1

numLenLista2 = int(input("De que tamaño será tu lista 2: "))
c = 0
sumatoriaLista2 = 0
while c < numLenLista2:
    numUser2 = int(input(f"Cual es tu número {c+1} de tu lista 2: "))
    sumatoriaLista2 += numUser2
    c+=1

if sumatoriaLista1 > sumatoriaLista2:
    print(f"La lista uno es más grande con un valor total de {sumatoriaLista1}")
elif sumatoriaLista2 > sumatoriaLista1:
    print(f"La lista dos es más grande con un valor total de {sumatoriaLista2}")
else:
    print("Las dos listas son iguales")

#--------------------------------------------------
#18_imprimirLista.py
# Ejercicio 6. De la siguiente lista [16,25,16,99,48,67,37,10,42,56,29,79,34,55], 
# Mostrar para cada valor: El Valor, su valor al cuadrado, su raíz cuadrada y su recíproco.

lista = [16,25,16,99,48,67,37,10,42,56,29,79,34,55]

print(f"{'VALOR':<10} | {'CUADRADO':<10} | {'RAÍZ CUADRADA':<14} | {'RECÍPROCO':<10}")  
print("-" * 55)  

c = 0
while c < len(lista):
    n = lista[c]
    cuadrado = n**2
    raiz = n**(1/2)
    reciproco = 1/n
    print(f"{n:<10} | {cuadrado:<10.2f} | {raiz:<14.2f} | {reciproco:<10.2f}")
    c+=1
#--------------------------------------------------
#20_segundos.py
#Ejercicio No 1. Diseñar una función que calcule la cantidad de segundos en un tiempo dado en horas, minutos y segundos.

def ConversorSegundos(horas,min,seg):
    segundosTotales = ((horas*60)*60)+(min*60)+seg
    return segundosTotales


tiempo = [int(input("Dame tu tiempo en HORAS: ")),int(input("Dame tu tiempo en MINUTOS: ")),int(input("Dame tu tiempo en SEGUNDOS: "))]
segundos = ConversorSegundos(*tiempo)
print(f"Hay {segundos} segundos cuando tienes {tiempo[0]} horas con {tiempo[1]} minutos y con {tiempo[-1]} segundos")
#--------------------------------------------------
#21_bisiesto.py
# Ejercicio No 2. Función que pida como parámetro un año, y que regrese una leyenda que diga si es Bisiesto o no lo es.

ComprobadorBisiesto = lambda year: (year % 4) == 0

preguntaUser = int(input("Dame el año que deseas comprobar: "))
if ComprobadorBisiesto(preguntaUser):
    print(f"El año {preguntaUser} si es bisiesto")
else:
    print(f"El año {preguntaUser} no es bisiesto")

#--------------------------------------------------
#22_iva.py
#Ejercicio No 3. Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA

iva = lambda subTotal: subTotal*1.16

subTotalVenta = int(input("Dame el subtotal de tu venta: "))

total_con_iva = iva(subTotalVenta)
print(f"El total ya con iva es {total_con_iva}")
#--------------------------------------------------
#23_media.py
#Ejercicio No 4. Escribir una función que reciba una muestra de números en una lista y devuelva su media
import random
def Mediana(num_list):
    total_sum = 0
    for num in num_list:
        total_sum += num
    return total_sum/len(num_list)




lista_numeros = [(random.randint(1,100)) for i in range(10)]
promedio = Mediana(lista_numeros)

print(f"El promedio de {lista_numeros} \n es: {promedio}")
#--------------------------------------------------
#24_suma_cuadrados.py
#Ejercicio No 5. Escribir una función que reciba una muestra de números en una lista y devuelva la suma de sus cuadrados
import random

suma_cuadrados = lambda num_list: sum((num**2) for num in num_list) # Suma de la lista

listaNumeros = [random.randint(1,100) for i in range(10)] # Genera lista aleatoria

sumaTotal = suma_cuadrados(listaNumeros)
print(f"De tu lista {listaNumeros} la suma de todos al cuadrado es {sumaTotal}")
#--------------------------------------------------
#25_numeros_multiplos.py
#Ejercicio No 6. Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.

multiplo_num = lambda numOne,numTwo: f" {numOne} y {numTwo}  son multiplos" if (numOne%numTwo == 0) or (numTwo%numOne == 0) else f" {numOne} y {numTwo} no son multiplos"


numeroUno,numDos = int(input("Dame tu primer numero: ")),int(input("Dame tu segundo número: "))
print(multiplo_num(numeroUno,numDos))
#--------------------------------------------------
#26_menor_en_lista.py
#Ejercicio No 7. Escribir una función que reciba una nuestra de números en una lista y devuelva el número menor

import random

def menor_lista(lista):
    menor = 9999999
    for num in lista:
        menor = num if num < menor else menor
    return menor

lista = [random.randint(1,100) for i in range(20)]
menorLista = menor_lista(lista)
print(f"El menor de la lista {lista}\n es {menorLista}")

#--------------------------------------------------