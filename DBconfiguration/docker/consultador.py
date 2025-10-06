import pyscopg2 

#conexión a la base de datos
conexion = pyscopg2.connect(
    host = "localhost",
    port = "5432",
    database = "credenciales",
    user = "Admin",
    password = "p4sw0rdDB",
    )

#Crear cursos
cursos = conexion.cursos()

# Ejecutar consola
cursos.execute("SELECT * FROM usuarios")
#fetchone() = una fila
#fetchmany(n) = hasta n filas
registros = cursos.fetchall() #Recuperar todas las filas devueltas
#registros almacena en tuplas

for fila in registros:
    print(fila)

#Cerrar la conexión
cursos.close()
conexion.close()
