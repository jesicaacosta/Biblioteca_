import mysql.connector

#Conexion a la DB mysql

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  #datos de workbench
            password="root",  
            database="biblioteca-personal"
        )
        return conexion
    except mysql.connector.Error as e: #si ocurre un error 
        print(f"Error al conectar con la base de datos: {e}")
        return None

conectar()