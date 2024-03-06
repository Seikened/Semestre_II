# VECTORES
calificaciones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(calificaciones[1])
print(calificaciones[0:3])
print(calificaciones[(len(calificaciones)-1)])


# MATRICES
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][0])

# DATAFRAMES

nombre = ["Ana", "Beto", "Carmen", "Daniel", "Elena"]
edad = [20, 30, 40, 50, 60]
estatura = [1.60, 1.70, 1.80, 1.90, 2.00]
sexo = ["F", "M", "F", "M", "F"]

# Elementos de un diccionario el cual funciona como los encabezados de una tabla
elementos = {"nombre": nombre, "edad": edad, "estatura": estatura, "sexo": sexo}

import pandas as pd

data_frame = pd.DataFrame(elementos)
print(data_frame)

print(data_frame[0:3])

print(data_frame["nombre"])

print(data_frame.info())

print(data_frame.describe(include='all'))

# Conexiones a bases de datos PostgreSQL


import psycopg2

cadena_conexion = "dbname='FernandoDB' user='postgres' host='localhost' password='root' port='5432'"

try:

    conexion = psycopg2.connect(cadena_conexion)
    

    cursor = conexion.cursor()
    

    cursor.execute("CREATE TABLE IF NOT EXISTS alumno (id SERIAL PRIMARY KEY, nombre VARCHAR(50), edad INT)")
    cursor.execute("INSERT INTO alumno (nombre, edad) VALUES ('Juan', 20), ('Ana', 21), ('Pedro', 22), ('Maria', 23), ('Jose', 24), ('Luis', 25)")
    

    conexion.commit()


    cursor.execute("SELECT * FROM alumno")
    registros = cursor.fetchall()
    
    for registro in registros:
        print(registro)


    cursor.close()
    conexion.close()
except Exception as e:
    print(f"Ocurrió un error al conectar a PostgreSQL: {e}")

