import os #se utiliza para construir rutas de archivos de manera compatible con cualquier so, me sirve para que
#al guardar imágenes en una ubicacion especifica del servidor
from flask import Flask, render_template, request, redirect, url_for, session
import requests
# request maneja solicitud que recibe tu servidor, requests es para cuando necesito enviar una solicitud a otro servidor o API para obtener datos.

from biblioteca import biblioteca, mostrar_libros, agregar_libro, actualizar_libro, eliminar_libro

app = Flask(__name__)

@app.route('/') #ruta principal del programa
def index(): 
    if len(biblioteca) == 0:
        # Si no hay libros, obtener recomendaciones
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=Mariana+Enriquez&maxResults=2&langRestrict=es&orderBy=relevance") #primer recomendacion 
        response2 = requests.get("https://www.googleapis.com/books/v1/volumes?q=Jennifer+Armentrout&maxResults=2&langRestrict=es&orderBy=relevance") #segunda recomend
        response3 = requests.get("https://www.googleapis.com/books/v1/volumes?q=García+Lorca&maxResults=2&langRestrict=es&orderBy=relevance") #tercer recomend
        recomendaciones = [] #creo lista 
        if response.status_code == 200:
            recomendaciones.extend(response.json().get("items", [])) # extends m,e permite agregar múltiples elementos a la lista recomendaciones desde las respuestas JSON obtenidas
        if response2.status_code == 200:
            recomendaciones.extend(response2.json().get("items", []))
        if response3.status_code == 200:
            recomendaciones.extend(response3.json().get("items", []))
        if not recomendaciones:
            print('No se obtuvo resultado.')
        return render_template("index.html", biblioteca=[], recomendaciones=recomendaciones)
    else:
        return render_template("index.html", biblioteca=biblioteca, recomendaciones=[])

@app.route('/agregar', methods=['POST'])
def agregar(): #defino la funcion agregar 
    libro = {
            'titulo': request.form['titulo'], #request es objeto qe tiene los datos del form q completo el user
            'autor': request.form['autor'],
            'estrellas': request.form['estrellas'],
            'comienzo_de_lectura': request.form['comienzo_de_lectura'],
            'fin_de_lectura': request.form['fin_de_lectura'],
            'descripcion': request.form['descripcion']
        }
    agregar_libro(libro)
    return redirect(url_for('index'))#redirige al user al menu principal


#----------- Funcion ELIMINAR
@app.route('/eliminar/<int:index>', methods=['POST'])
def eliminar(index): #eliminar es el manejador de la ruta que se invoca cuando un usuario quiere eliminar un libro, y se encarga de redirigir después de la eliminación.
    eliminar_libro(index) ## Llama a la fncion para realizar la eliminacion
    return redirect(url_for('index'))



#----------- FUNCION EDITAR 
@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar_libro(index):
    if request.method == 'POST':  # Actualiza los datos del libro en la lista biblioteca
        libro_actualizado = {
            'titulo': request.form['titulo'],
            'autor': request.form['autor'],
            'estrellas': request.form['estrellas'],
            'comienzo_de_lectura': request.form['comienzo_de_lectura'],
            'fin_de_lectura': request.form['fin_de_lectura'],
            'descripcion': request.form['descripcion']
        }
        actualizar_libro(index, libro_actualizado)# llama a la funcion de actaulizar libro 
        return redirect(url_for('index'))  #genera con flask la ruta para index y la retorna, retorna index
    
    # Si es un GET, muestra el libro a editar
    libro_a_editar = biblioteca[index]
    return render_template('editar.html', libro=libro_a_editar, index=index)


def actualizar_datos_libro(index, libro_actualizado):
    # Aquí implementas la lógica para actualizar el libro en la biblioteca
    biblioteca[index] = libro_actualizado



if __name__ == '__main__':
    app.run(debug=True)