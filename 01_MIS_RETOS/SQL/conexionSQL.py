import pyodbc

# Define los parámetros de la conexión
server = r'TRAVELLAP\SQLEXPRESS'
database = 'Bd_RegistroPersonas'
driver = '{ODBC Driver 17 for SQL Server}'

# Establece la conexión utilizando la autenticación de Windows
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes')

# Crea un cursor
cursor = conn.cursor()

# Ejecuta una consulta
cursor.execute("""select Tabla.Mes,count(*) as Conteo from
(
select 
Fecha_Nacimiento,
Mes =case
		when MONTH(Fecha_Nacimiento) =  1 then '01Enero'
		when MONTH(Fecha_Nacimiento) =  2 then '02 Febrero'

		when MONTH(Fecha_Nacimiento) =  3 then '03 Marzo'
		when MONTH(Fecha_Nacimiento) =  4 then '04 Abril'

		when MONTH(Fecha_Nacimiento) =  5 then '05 Mayo'
		when MONTH(Fecha_Nacimiento) =  6 then '06 Junio'

		when MONTH(Fecha_Nacimiento) =  7 then '07 Julio'
		when MONTH(Fecha_Nacimiento) =  8 then '08 Agosto'

		when MONTH(Fecha_Nacimiento) =  9 then '09 Septiembre'
		when MONTH(Fecha_Nacimiento) =  10 then '10 Octubre'

		when MONTH(Fecha_Nacimiento) =  11 then '11 Noviembre'
		when MONTH(Fecha_Nacimiento) =  12 then '12 Diciembre'
		else 'Sin mes'
	end 
from personas
) as tabla group by Tabla.mes order by Tabla.Mes asc
""")

# Recupera los resultados
rows = cursor.fetchall()

# Imprime los resultados
for row in rows:
    print(row)
    
cursor.close()