import os
from biblioteca import Biblioteca
import pickle

class Libro(Biblioteca):
    def __init__(self, libro, usuario, prestamo_libro, autor, datos_biblioteca):
        super().__init__(libro, usuario, prestamo_libro)
        self.autor = autor
        self.datos_biblioteca = {'libros': [], 'usuarios': []}

    #Funcion para agregar un libro
    def agregar_libro(self):
        # Cargar los datos existentes del archivo si existe
        if os.path.exists('datos_biblioteca.pkl'):
            with open('datos_biblioteca.pkl', 'rb') as file:
                self.datos_biblioteca = pickle.load(file)

        print('-------------------------------------------------------------')
        self.libro = input('Dijite el nombre del libro: ')
        self.autor = input('Dijite el nombre del autor: ')

        # Agregar el nuevo libro a la lista de libros
        self.datos_biblioteca['libros'].append({'nombre_libro': self.libro, 'autor_libro': self.autor})

        # Guardar los datos actualizados de vuelta en el archivo
        with open('datos_biblioteca.pkl', 'wb') as file:
            pickle.dump(self.datos_biblioteca, file)



    #Funcion que muestra los libros de la biblioteca
    def mostrar_libos(self):
        
        if os.path.exists('datos_biblioteca.pkl'):
            with open('datos_biblioteca.pkl', 'rb') as file:
                self.datos_biblioteca = pickle.load(file)

        #contar cuantos libros repetidos hay
        conteo_libros = {}
        for libro in self.datos_biblioteca['libros']:
            nombre_libro = libro['nombre_libro']
            autor_libro = libro['autor_libro']

            contador = (nombre_libro, autor_libro)

            if contador in conteo_libros:
                conteo_libros[contador] +=1
            else:
                conteo_libros[contador] = 0
        print('-------------------------------------------------')
        print("_____Cantidad de libros por nombre y autor____:")
        for (nombre_libro, autor_libro), conteo in conteo_libros.items():

            if conteo == 0:
                 print(f"Libro: {nombre_libro}, Por: {autor_libro}, Cantidad: {conteo} -NO DISPONIBLE")
            else:
                print(f"Libro: {nombre_libro}, Por: {autor_libro}, Cantidad: {conteo} -DISPONIBLE")
        


    #Función para registrar un usuario 
    def regisrar_usuario(self):
        # Cargar los datos existentes del archivo si existe
        if os.path.exists('datos_biblioteca.pkl'):
            with open('datos_biblioteca.pkl', 'rb') as file:
                self.datos_biblioteca = pickle.load(file)

        print('-------------------------------------------------------------')
        self.usuario = input('Dijite el nombre del usuario: ')
        # Agregar el nuevo usuario
        self.datos_biblioteca['usuarios'].append({'nombre_usuario': self.usuario})
        # Guardar los datos actualizados de vuelta en el archivo
        with open('datos_biblioteca.pkl', 'wb') as file:
            pickle.dump(self.datos_biblioteca, file)

        print('El nuevo usuario se ha registrado exitósamente!')




    def menu(self):

        while True:
            print('_____________________________________________')
            print('\nMenú del sistema de gestión de biblioteca')
            print('1. Agregar un libro')
            print('2. Mostrar libros')
            print('4. Registrar usuario')
            print('6. Salir')
            opcion = int(input('Dijite una opcion: '))

            if opcion == 1:
                objeto.agregar_libro()
            elif opcion == 2:
                objeto.mostrar_libos()
            elif opcion == 4:
                objeto.regisrar_usuario()
            elif opcion == 6:
                print('Gracias por usar nuestro sistema, hasta luego!')
                break
            else:
                print('Opción invalida. Intentelo de nuevo')












objeto = Libro(libro = [], usuario = [], prestamo_libro= [], autor= [], datos_biblioteca=[])

if __name__ == '__main__':
    objeto.menu()