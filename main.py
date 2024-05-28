
from biblioteca import Biblioteca
from libro import Libro

objeto = Libro(libro=[], usuario=[], prestamo_libro=[], autor=[], datos_biblioteca=[])

def menu():
        while True:
            print('_____________________________________________')
            print('\nMenú del sistema de gestión de biblioteca')
            print('1. Agregar un libro')
            print('2. Mostrar libros')
            print('3. Prestar libro')
            print('4. Registrar usuario')
            print('5. Listar usuarios')
            print('6. Listar libros de usuario')
            print('7. Devolver libro')
            print('8. Salir')
            opcion = int(input('Digite una opcion: '))

            if opcion == 1:
                objeto.agregar_libro()
            elif opcion == 2:
                objeto.mostrar_libros()
            elif opcion == 3:
                objeto.prestar_libro
            elif opcion == 4:
                objeto.regisrar_usuario()
            elif opcion == 5:
                objeto.listar_usuarios()
            elif opcion == 6:
                objeto.listar_libros_usuario()
            elif opcion == 7:
                objeto.devolver_libro()
            elif opcion == 8:
                print('\nGracias por usar nuestro sistema, hasta luego!\n')
                break
            else:
                print('Opción inválida. Inténtelo de nuevo.')

if __name__ == '__main__':
    menu()