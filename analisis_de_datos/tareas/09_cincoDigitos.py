# Invertir los digitos
def Invertir(val):
    nuevoDigito = ""
    for i in val[::-1]:
        nuevoDigito += f'{i}'
    
    return int(nuevoDigito)
digito = input("Introduce tu número: ")

digito_invertido = Invertir(digito)
print(f"Digito introducido {digito}, e invertido es: {digito_invertido}")