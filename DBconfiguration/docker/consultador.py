import pyscopg2

#conexión a la base de datos
conexion = pyscopg2.connect(
    host = "localhost",
    port = "5432",
    database = "credenciales",
    user = "Admin",
    password = "p4sw0rdDB",
    )

#Crear cursor
cursor = conexion.cursor()

# Ejecutar consola
cursor.execute("SELECT * FROM usuarios")
#fetchone() = una fila
#fetchmany(n) = hasta n filas
registros = cursor.fetchall() #Recuperar todas las filas devueltas
#registros almacena en tuplas

for fila in registros:
    print(fila)

#Cerrar la conexión
cursor.close()
conexion.close()
