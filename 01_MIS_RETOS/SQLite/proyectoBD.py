import sqlite3 as sql





def printFormattedTable(datosTabla):
    stringMasLargo = 0
    for dato in datosTabla:
        for i in range(3):
            if len(str(dato[i])) > stringMasLargo:
                stringMasLargo = len(str(dato[i]))
    print(f"{'tipo_casa':<{stringMasLargo}} {'habitaciones':<{stringMasLargo}} {'precio':<{stringMasLargo}}")
    print("-"*(stringMasLargo*3))
    for dato in datosTabla:
        print(f"{dato[0]:<{stringMasLargo}} {dato[1]:<{stringMasLargo}} {dato[2]:<{stringMasLargo}}")
        print("-"*(stringMasLargo*3))
#---------------------------------------------------------------------------------------------

def createDB():
    conn = sql.connect("casas.db")
    conn.commit()
    conn.close()


def createTable():
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE casas(
            tipo_casa text,
            habitaciones integer,
            precio integer
        )"""
    )
    conn.commit()
    conn.close()


def insertRow(tipoCasa,numHabitaciones,precio):
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO casas VALUES ('{tipoCasa}',{numHabitaciones},{precio})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def readRows():
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM casas "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return printFormattedTable(datos)


def insertRows(listaCasas):
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO casas VALUES (?,?,?)"
    cursor.executemany(instruccion,listaCasas)
    conn.commit()
    conn.close()


def search():
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM casas WHERE tipo_casa LIKE 'M%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return printFormattedTable(datos)


def updateField():
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE casas SET precio = 10 WHERE tipo_casa = 'Molino'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def deleteRow():
    conn = sql.connect("casas.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM casas WHERE tipo_casa = 'Molino'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#-------------------------------

#Imprimir la tabla de forma ordenada desde el uso de readRows()
# Formateado de la tabla
# para el string mas largo dejemos el espacio para formatear y que se vea ordenado

# Crear una base de datos de casas
createDB()
# Crear una tabla de casas
createTable()
# Insertar una fila
insertRow("Casa",2,100)
# Leer todas las filas
readRows()
# Insertar muchas  filas
insertRows([("Molino",3,100),("Casa",2,200),("Mansion",5,300),("Molino",3,100),("Casa",2,200)])
# Buscar todas las casas que empiecen con M
search()
# Actualizar el precio de las casas que empiecen con M
updateField()
# Eliminar una fila
deleteRow()

readRows()




# CRUD (Create, Read, Update, Delete)