A = [[2, -1,0],
    [1, 3, -1],
    [0, -1, 2]]


def VerificaDiagonal(A):
    sum = 0
    elemntoSumado = None
    diagonal = None
    for filas in range(len(A)):
        sum = 0
        
        for columnas in range(len(A)):

            if filas != columnas:
                sum += A[filas][columnas]
                elemntoSumado = sum
            else:
                diagonal = A[filas][columnas]
        if diagonal > elemntoSumado:
            continue
        else:
            return False
    return True


print(VerificaDiagonal(A))