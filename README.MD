'__init__(self, libro, usuario, prestamo_libro, autor, datos_biblioteca)'
Inicializa la clase Libro con los datos del libro, usuario, préstamo y autor. También inicializa los datos de la biblioteca.

libro: Nombre del libro

usuario: Nombre del usuario

prestamo_libro: Estado del préstamo del libro

autor: Nombre del autor del libro

datos_biblioteca: Diccionario con datos de la biblioteca

-cargar_datos(self)
Verifica si el archivo de datos de la biblioteca existe y no está vacío. Si el archivo existe y tiene datos, los carga. Si no, inicializa un diccionario vacío.

-agregar_libro(self)
Agrega un nuevo libro a la biblioteca. Solicita al usuario el nombre del libro y el autor, luego guarda los datos en el archivo.

-mostrar_libros(self)
Muestra todos los libros disponibles en la biblioteca y la cantidad de ejemplares por nombre y autor.

-prestar_libro(self)
Permite prestar un libro a un usuario. Solicita al usuario el nombre del libro y del usuario, verifica disponibilidad y actualiza los datos.

-regisrar_usuario(self)
Registra un nuevo usuario en la biblioteca. Solicita al usuario el nombre del nuevo usuario y guarda los datos en el archivo.

-listar_usuarios(self)
Muestra todos los usuarios registrados en la biblioteca.

-listar_libros_usuario(self)
Muestra todos los libros prestados a un usuario específico. Solicita al usuario el nombre del usuario y lista los libros prestados.

-devolver_libro(self)
Permite devolver un libro prestado a la biblioteca. Solicita al usuario el nombre del libro y del usuario, y actualiza los datos.


Funciones del Menú
Agregar un libro: Permite agregar un nuevo libro a la biblioteca.
Mostrar libros: Muestra todos los libros disponibles en la biblioteca.
Prestar libro: Permite prestar un libro a un usuario registrado.
Registrar usuario: Registra un nuevo usuario en el sistema.
Listar usuarios: Muestra todos los usuarios registrados en la biblioteca.
Listar libros de usuario: Muestra todos los libros prestados a un usuario específico.
Devolver libro: Permite devolver un libro prestado a la biblioteca.
Salir: Sale del sistema de gestión de biblioteca.