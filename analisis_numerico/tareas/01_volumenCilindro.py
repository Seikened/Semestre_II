# Completa el ejercicio aquí
import math as mt

# Para usar la constante pi en python usa: math.pi

#Define la función aquí

pi = mt.pi

def Calcular_volumen_cilindro(r,h):
    '''
    Esta función calcula el volumen de un cilindro.
    Requiere:
    - Valor de radio = r
    - Valor de altura = h
    Y devuelve el volumen
    NOTA: 
    Ten cuidado con tus medidas
    Procura que r y h sean los mismos 
    para que tus valores sean correctos
    '''
    return pi*(r**2)*h


if __name__ == "__main__":
    
    
    
    #Pide los valores del radio y la altura del cilindro por teclado.
    radio = float(input("Dame el radio del cilindro: "))
    altura = float(input("Dame la altura del cilindro: "))
    
    # Usa la función definida.
    volumen = Calcular_volumen_cilindro(radio,altura)
    
    
    print("""
████████████
████████████
████████████
█▀▀▀▀▀██████
█░░░░░██████
█░░░░░██████
█░░░░░██████
█░░░░░██████
█▄▄▄▄▄██████
████████████
████████████
████████████""")
    #Imprime a pantalla el valor del volumen usando .format: 
    print(f"El valor del volumen de cilindro de radio = {radio} y altura = {altura} es {volumen}")