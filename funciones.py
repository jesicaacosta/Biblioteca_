from db import conectar
from flask import Flask, render_template, request, redirect, url_for, session

# Lista para almacenar los libros
biblioteca = []
libros=[]
#mostrar

''' 
def obtener_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    # Imprime la consulta para verificar
    consulta = "SELECT * FROM libros"
    print(consulta)
    cursor.execute(consulta)
    libros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return libros
'''

def obtener_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    # Imprime la consulta para verificar
    libros ="SELECT * libros"
    cursor.execute(libros)
    libros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return libros



# Agregar un libro a la base de datos
def agregar_libro(libro):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        # si fecha esta vacía, reemplazo por NULL
        # Manejo de fechas vacías: reemplazo con None para insertar NULL en la DB
        libro['comienzo_de_lectura'] = libro['comienzo_de_lectura'] or None
        libro['fin_de_lectura'] = libro['fin_de_lectura'] or None
        query = """
        INSERT INTO libros (titulo, autor, estrellas, comienzo_de_lectura, fin_de_lectura, descripcion)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (libro['titulo'], libro['autor'], libro['estrellas'], 
                libro['comienzo_de_lectura'], libro['fin_de_lectura'], libro['descripcion'])
        cursor.execute(query, valores)
        conexion.commit()
        conexion.close()

# actualizar 
def actualizar_libro(index, nuevo_libro):
    if 0 <= index < len(biblioteca):
        biblioteca[index] = nuevo_libro

#eliminar 
def eliminar_libro(index):
    if 0 <= index < len(biblioteca): #si el indice es menor que el tamaño de la biblioteca
        biblioteca.pop(index) #elimina el elemento en la posicion index
        
        
print(libros)
