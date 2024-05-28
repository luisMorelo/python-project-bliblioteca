import os
from biblioteca import Biblioteca
import pickle

class Libro(Biblioteca):
    def __init__(self, libro, usuario, prestamo_libro, autor, datos_biblioteca):
        super().__init__(libro, usuario, prestamo_libro)
        self.autor = autor
        self.datos_biblioteca = {'libros': [], 'usuarios': [], 'prestamos': {}}



    #Verifica inicialmente si el archivo esta vacio o no, para luego cargar los datos existentes o unicializar el diccionario vacio
    def cargar_datos(self):
        if os.path.exists('datos_biblioteca.pkl'):
            if os.path.getsize('datos_biblioteca.pkl') > 0:  # Verificar si el archivo no está vacío
                with open('datos_biblioteca.pkl', 'rb') as file:
                    self.datos_biblioteca = pickle.load(file)
                
                # Asegurarse de que la clave 'prestamos' esté en el diccionario
                if 'prestamos' not in self.datos_biblioteca:
                    self.datos_biblioteca['prestamos'] = {}
            else:
                self.datos_biblioteca = {'libros': [], 'usuarios': [], 'prestamos': {}}
        else:
            self.datos_biblioteca = {'libros': [], 'usuarios': [], 'prestamos': {}}



    #Funcion para agregar un libro
    def agregar_libro(self):
        #Se llama a la funcion que se encarga de cargar los datos
        self.cargar_datos()
        print('-------------------------------------------------------------')
        self.libro = input('Digite el nombre del libro: ')
        self.autor = input('Digite el nombre del autor: ')

        # Agregar el nuevo libro a la lista de libros
        self.datos_biblioteca['libros'].append({'nombre_libro': self.libro, 'autor_libro': self.autor})

        # Guardar los datos actualizados de vuelta en el archivo
        with open('datos_biblioteca.pkl', 'wb') as file:
            pickle.dump(self.datos_biblioteca, file)



    #Muestra los libros de la biblioteca
    def mostrar_libros(self):
        #Se llama a la funcion que se encarga de cargar los datos 
        self.cargar_datos()
        #contar cuantos libros repetidos hay
        conteo_libros = {}
        for libro in self.datos_biblioteca['libros']:
            nombre_libro = libro['nombre_libro']
            autor_libro = libro['autor_libro']

            contador = (nombre_libro, autor_libro)

            if contador in conteo_libros:
                conteo_libros[contador] += 1
            else:
                conteo_libros[contador] = 1
        print('-------------------------------------------------')
        print("_____Cantidad de libros por nombre y autor____:")
        for (nombre_libro, autor_libro), conteo in conteo_libros.items():
            if conteo == 0:
                print(f"Libro: {nombre_libro}, Por: {autor_libro}, Cantidad: {conteo} -NO DISPONIBLE")
            else:
                print(f"Libro: {nombre_libro}, Por: {autor_libro}, Cantidad: {conteo} -DISPONIBLE")



    # Función para prestar un libro
    def prestar_libro(self):
        self.cargar_datos()
        nombre_libro = input('Digite el nombre del libro que desea prestar: ')
        nombre_usuario = input('Digite el nombre del usuario que desea el libro: ')

        # Verificar si el libro está disponible
        libro_encontrado = None
        for libro in self.datos_biblioteca['libros']:
            if libro['nombre_libro'] == nombre_libro:
                libro_encontrado = libro
                break

        if libro_encontrado is None:
            print(f'\nEl libro "{nombre_libro}" no está disponible en la biblioteca.')
            return

        # Verificar si el usuario está registrado
        usuario_registrado = False
        for usuario in self.datos_biblioteca['usuarios']:
            if usuario['nombre_usuario'] == nombre_usuario:
                usuario_registrado = True
                break

        if not usuario_registrado:
            print(f'\nEl usuario "{nombre_usuario}" no está registrado en el sistema.')
            return

        # Prestar el libro y actualizar la disponibilidad
        self.datos_biblioteca['libros'].remove(libro_encontrado)

        if nombre_usuario not in self.datos_biblioteca['prestamos']:
            self.datos_biblioteca['prestamos'][nombre_usuario] = []
        self.datos_biblioteca['prestamos'][nombre_usuario].append(libro_encontrado)

        with open('datos_biblioteca.pkl', 'wb') as file:
            pickle.dump(self.datos_biblioteca, file)

        print(f'\nEl libro "{nombre_libro}" ha sido prestado a "{nombre_usuario}".')




    #Función para registrar un usuario 
    def regisrar_usuario(self):
        #Se llama a la funcion que se encarga de cargar los datos 
        self.cargar_datos()
        print('-------------------------------------------------------------')
        self.usuario = input('Digite el nombre del usuario: ')
        # Agregar el nuevo usuario
        self.datos_biblioteca['usuarios'].append({'nombre_usuario': self.usuario})
        # Guardar los datos actualizados de vuelta en el archivo
        with open('datos_biblioteca.pkl', 'wb') as file:
            pickle.dump(self.datos_biblioteca, file)
        print('El nuevo usuario se ha registrado exitósamente!')



    #Muestra usuarios registrados
    def listar_usuarios(self):
        #Se llama a la funcion que se encarga de cargar los datos 
        self.cargar_datos()
       
        print('------------------------------------')
        print('Usuarios registrados: ')
        for usuario in self.datos_biblioteca['usuarios']:
            print(usuario['nombre_usuario'])



    # Función para listar libros prestados a un usuario específico
    def listar_libros_usuario(self):
        self.cargar_datos()
        nombre_usuario = input('Digite el nombre del usuario para listar sus libros prestados: ')

        if nombre_usuario in self.datos_biblioteca['prestamos']:
            libros_prestados = self.datos_biblioteca['prestamos'][nombre_usuario]
            print(f'Libros prestados a {nombre_usuario}:')
            for libro in libros_prestados:
                print(f"- {libro['nombre_libro']} por {libro['autor_libro']}")
        else:
            print(f'El usuario "{nombre_usuario}" no tiene libros prestados o no está registrado.')



    # Función para devolver un libro
    def devolver_libro(self):
        self.cargar_datos()
        nombre_libro = input('Digite el nombre del libro que desea devolver: ')
        nombre_usuario = input('Digite el nombre del usuario que devuelve el libro: ')

        # Verificar si el usuario tiene el libro prestado
        if nombre_usuario in self.datos_biblioteca['prestamos']:
            libros_prestados = self.datos_biblioteca['prestamos'][nombre_usuario]
            libro_a_devolver = None
            for libro in libros_prestados:
                if libro['nombre_libro'] == nombre_libro:
                    libro_a_devolver = libro
                    break

            if libro_a_devolver is not None:
                libros_prestados.remove(libro_a_devolver)
                self.datos_biblioteca['libros'].append(libro_a_devolver)

                with open('datos_biblioteca.pkl', 'wb') as file:
                    pickle.dump(self.datos_biblioteca, file)

                print(f'El libro "{nombre_libro}" ha sido devuelto por "{nombre_usuario}".')
            else:
                print(f'El usuario "{nombre_usuario}" no tiene el libro "{nombre_libro}" prestado.')
        else:
            print(f'El usuario "{nombre_usuario}" no tiene libros prestados o no está registrado.')