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


print(IfNumeroPrimo(9))


# 11) [FOR] Escribe un programa que indique cuantos años pares existen entre 1950 y 2010
def ContadorYearImpars(yearOne,yearTwo):
    quantityYear = abs(yearOne-yearTwo)+1
    listYearsImpars = []
    for year in range(0,quantityYear):
        if year%2!=0:
            listYearsImpars.append(year)
    return len(listYearsImpars)

# 12) Escribir un numero de 5 dígitos e indicar si se trata de una capicua
# 13) [FOR] Del listado (10,111,13,15,45,63,25,96) indicar cuantos numeros son impares
# 14) [FOR] Preguntar primero cuantos números, posterior solicitar cada uno de esos numeros y mostrar la sumatoria
# 15) [FOR] Programa que pida 4 calificaciones (0-10), posteriormente calcular el promedio e indicar su clasificacion: 
# 0.0-5.9: E
# 6.0-6.9: D
# 7.0-7.9: C
# 8.0-8.9: B
# 9.0-10: A

# Adicionales
# 16) Escribe un programa que dado un monto, indique los billetes a entregar: Denominaciones: 500, 200, 100, 50, 20, 10, 5, 1
# 17) Escribe un programa que pida un valor y calcule y muestre su factorial
# 18) Escribe un programa que pida 3 valores e indique cuando son iguales
# 19) Escribe un programa que pida un valor en Metros, y muestre su equivalencia en Pies y en Yardas
# 20) Escribe un programa que pida un número y diga si es multiplo de 5

# ESTRUCTURAS REPETITIVAS
# 21) Usando FOR y WHILE. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar cuantos números son pares
# 22) Usando FOR y WHILE. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar cuantos números están por encima de 15
# 23) Usando FOR y WHILE. De la siguiente lista [8,14,22,3,7,28,36,49,52], indicar la cantidad de valores, la sumatoria y su promedio
# 24) Usando FOR y WHILE. Del ejercicio anterior, calcular el La Varianza y Desviación Estándar Poblacional
# 25) Usando FOR y WHILE. Realiza un programa que pida 2 números enteros, e imprima los números impares que existen entre los 2 valores