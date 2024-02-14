#Vamos desde numpy a descomponer una matris por LU
import numpy as np
from scipy.linalg import lu

matriz = [
    [ 1 , 0 ,0],
    [-.5, 1 ,0],
    [2  ,-.8,1]
]

b1=0
b2=0
b3=0
vector_B = [b1,b2,b3]

vector_Y= [1,0,0]




vector_B[0] = (vector_Y[0] - (matriz[0][1])*b2 - (matriz[0][2])*b3) / matriz[0][0]

for fila in range(len(matriz)):
    for columna  in range(len(matriz[fila])):
        # valor = matriz[fila][columna]
        # print(f"Fila: [{fila}] | Columna [{columna}]")
        # print(valor)
        vector_B[fila] = ( vector_Y[fila] -( matriz[fila][columna+1] * vector_B[fila]) -( matriz[fila][columna+2]) ) / matriz[fila][fila]
    print(vector_B[fila])
