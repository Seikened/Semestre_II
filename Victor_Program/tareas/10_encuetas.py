import random

def Votante():
    votoRandom = random.uniform(0,100)
    salida = 0
    
    if 0<=  votoRandom  < 10:salida=1
    if 10<=  votoRandom  < 50:salida=2
    if 50<=  votoRandom  < 100:salida=3
    return salida