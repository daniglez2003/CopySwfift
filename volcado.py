import pyodbc
import mysql.connector
import pandas as pd
import shutil 
import os 

def realizarVolcado(ipMnw): 
    try:
        nombre_usuario = 'root'             #completar con los datos de la base de datos que deseas
        contraseña = '1910'
        nombre_host = '127.0.0.1'
        nombre_base_datos = 'final'

        conexion_mysql = mysql.connector.connect(user=nombre_usuario, password=contraseña, host=nombre_host, database=nombre_base_datos)
        cursor_mysql = conexion_mysql.cursor()

         # Obtener el nombre de todas las tablas en la base de datos de MySQL
        cursor_mysql.execute("SHOW TABLES")
        tablas_mysql = [tabla[0] for tabla in cursor_mysql]

        # Conexión a la base de datos de Access
        conexion_access = pyodbc.connect(r'DSN=hola;UID=a;PWD=a')
        cursor_access = conexion_access.cursor()

        # Iterar sobre cada tabla y transferir los datos de MySQL a Access
        for tabla in tablas_mysql:
            cursor_mysql.execute(f"SELECT * FROM {tabla}")
            resultados = cursor_mysql.fetchall()

            # Obtener información sobre las columnas de MySQL
            cursor_mysql.execute(f"DESCRIBE {tabla}")
            columnas_mysql = [columna[0] for columna in cursor_mysql.fetchall()]

            # Crear la tabla en Access con las mismas columnas que en MySQL
            # Aquí necesitas construir la consulta de creación de tabla en Access
            # Utiliza la información de 'columnas_mysql' para generar la tabla en Access

            # Insertar datos en la tabla de Access
            for fila in resultados:
                valores = ', '.join(f"'{str(valor)}'" if valor is not None else 'NULL' for valor in fila)
                # Aquí necesitas construir y ejecutar una consulta de inserción en la tabla de Access

        conexion_access.commit()
        print("La base de datos se ha transferido de MySQL a Access.")
    except Exception as e:
        print(f"Error durante la transferencia de datos: {e}")
    finally:
    # Cerrar conexiones
        cursor_mysql.close()
        conexion_mysql.close()
        cursor_access.close()
        conexion_access.close()
    #Ruta de ubicación de backup de Stammdaten.mdb
    RutaDelAccess = r"\\192.168.1.251\Publica\Espera\backup"        #Cambiar a la ruta que deseas
    RutaDelAccess = os.path.join(RutaDelAccess,"Stammdaten.mdb")
    
    #Destino del volcado
    rutaDst = r"\\IP_MAQUINA_ESPERA\Publica\Espera\export\rdb"
    rutaDst = rutaDst.replace("IP_MAQUINA_ESPERA", ipMnw)

    try:
        shutil.copy2(RutaDelAccess,rutaDst)  # Utilizamos la función copy de shutil para copiar el archivo
        correcto = 1
        return correcto
    except FileNotFoundError:
        error = 2
        return error
