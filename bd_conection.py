import mysql.connector
from mysql.connector import Error

try:
    # Establecer la conexión
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootsasa",
        database="reconocimiento_facial_bd"
    )

    if conexion.is_connected():
        print('Conectado a la base de datos')
        cursor  = conexion.cursor()

        cursor.execute("SELECT * FROM user")
        for row in cursor.fetchall():
            print(row)

except Error as e:
    print("Error al conectar a MySQL", e)

finally:
    if (conexion.is_connected()):
        cursor.close()
        conexion.close()
        print("La conexión a MySQL está cerrada")