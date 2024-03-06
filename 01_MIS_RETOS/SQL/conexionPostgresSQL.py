import psycopg2

cadena_conexion = "dbname='FernandoDB' user='postgres' host='localhost' password='root' port='5432'"

try:
    # Conectarse a la base de datos
    conexion = psycopg2.connect(cadena_conexion)
    
    # Crear un cursor
    cursor = conexion.cursor()
    
    # Crear tabla y insertar datos
    cursor.execute("CREATE TABLE IF NOT EXISTS alumno (id SERIAL PRIMARY KEY, nombre VARCHAR(50), edad INT)")
    cursor.execute("INSERT INTO alumno (nombre, edad) VALUES ('Juan', 20), ('Ana', 21), ('Pedro', 22), ('Maria', 23), ('Jose', 24), ('Luis', 25)")
    
    # Hacer commit de las transacciones
    conexion.commit()

    # Seleccionar y mostrar todos los registros
    cursor.execute("SELECT * FROM alumno")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
except Exception as e:
    print(f"Ocurrió un error al conectar a PostgreSQL: {e}")
