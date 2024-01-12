import os
import shutil
import pyodbc
import pandas as pd
import mysql.connector


# Método copy(), copia en Acces
def copy(ip):
#Ruta de ubicación genérica de Stammdaten.mdb
    rutaGen = r"\\IP_MAQUINA_ESPERA\Publica\Espera\export\rdb"
    # Reemplazar ip en la ruta generica para obtener la ruta específica
    rutaGen = rutaGen.replace("IP_MAQUINA_ESPERA", ip)
    nombre_archivo = "Stammdaten.mdb"

    listaDir = os.listdir(rutaGen)
    
    ruta = os.path.join(rutaGen,nombre_archivo)
    
    
    destinoEnRed = r"\\192.168.1.251\Publica\Espera\backup"  #La ruta se puede cambiar a la que desees
    
    if nombre_archivo not in  listaDir:
        error = 2
        return error 
        #2 significa no se encuentra copia de la BD para su ruta de red

  
    if not os.path.exists(destinoEnRed):
            os.makedirs(destinoEnRed)
            #Creamos carpeta en el destino si no existe ya
    try:
        shutil.copy2(ruta, destinoEnRed)  # Utilizamos la función copy de shutil para copiar el archivo

    except FileNotFoundError:
        error = 3
        return error
    
    acierto = 1
    return acierto
try:
    # Conexión a la base de datos de Access
    conexion_access = pyodbc.connect(r'DSN=hola;UID=a;PWD=a')
    cursor_access = conexion_access.cursor()

    # Obtener el nombre de todas las tablas en la base de datos de Access
    tablas_access = [tabla.table_name for tabla in cursor_access.tables(tableType='TABLE')]

    # Conexión a MySQL
    nombre_usuario = 'root'
    contraseña = '1910'
    nombre_host = '127.0.0.1'
    nombre_base_datos = 'final'

    conexion_mysql = mysql.connector.connect(user=nombre_usuario, password=contraseña, host=nombre_host, database=nombre_base_datos)
    cursor_mysql = conexion_mysql.cursor()

    try:
        # Iterar sobre cada tabla y transferir los datos de Access a MySQL
        for tabla in tablas_access:
            cursor_access.execute(f"SELECT * FROM {tabla}")
            columnas = [columna[0] for columna in cursor_access.description]

    # Obtener los nombres de las columnas que causan el error de tamaño de fila
            columnas_large = []
            for columna in columnas:
                cursor_access.execute(f"SELECT MAX(LEN({columna})) FROM {tabla}")
                max_length = cursor_access.fetchone()[0]
                if max_length is not None and max_length > 4000:  # Establecer tu límite según sea necesario
                    columnas_large.append(columna)
    # Crear la tabla en MySQL con las mismas columnas que en Access
            column_defs = [f'{col} TEXT' if col in columnas_large else f'{col} VARCHAR(255)' for col in columnas]
            columnas_mysql = ', '.join(column_defs)
            cursor_mysql.execute(f"CREATE TABLE IF NOT EXISTS {tabla} ({columnas_mysql})")

            # Insertar datos en la tabla de MySQL
            for fila in cursor_access:
                valores = []
                for valor in fila:
                    if isinstance(valor, str) and valor and valor[0] == "'":
                        valor = valor[1:-1]  # Remover comillas adicionales para evitar errores de formato
                    valores.append(f"'{str(valor)}'")

        conexion_mysql.commit()
        print("La base de datos se ha transferido de Access a MySQL.")
    except Exception as e:
        print(f"Error durante la transferencia de datos: {e}")
    finally:
        # Cerrar conexiones
        cursor_access.close()
        conexion_access.close()
        cursor_mysql.close()
        conexion_mysql.close()
except pyodbc.Error as e:
    print(f"Error de conexión a Access: {e}")

