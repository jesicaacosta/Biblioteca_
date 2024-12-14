# Biblioteca_


Flujo de agregar libro: 
El usuario llena un formulario en la interfaz de usuario.
Cuando el formulario se envía, la ruta en app.py que está asociada con ese formulario (en este caso, agregar_libro_route) se activa.
agregar_libro_route toma los datos del formulario, los organiza en un diccionario (por ejemplo, libro), y luego llama a la función agregar_libro (la que se conecta a la DB) de funciones.py.
La función agregar_libro toma ese diccionario con los datos y los guarda en la base de datos.
Luego, la función agregar_libro_route puede redirigir al usuario a otra página (por ejemplo, la página principal) para ver los cambios reflejados.


