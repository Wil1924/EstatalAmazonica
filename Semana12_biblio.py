# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Se utiliza una tupla para título y autor ya que son inmutables
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

    def agregar_libro(self, libro):
        """Agregar un libro prestado al usuario"""
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        """Devolver un libro que el usuario había prestado"""
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar los libros por ISBN
        self.usuarios = set()  # Conjunto para almacenar los usuarios (ID único)
    
    def añadir_libro(self, libro):
        """Añadir un libro a la biblioteca"""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro {libro.titulo} añadido a la biblioteca.")
        else:
            print("El libro ya está en la biblioteca.")
    
    def quitar_libro(self, isbn):
        """Quitar un libro de la biblioteca por ISBN"""
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado.")
        else:
            print("El libro no existe en la biblioteca.")
    
    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario en la biblioteca"""
        if usuario.id_usuario not in {u.id_usuario for u in self.usuarios}:
            self.usuarios.add(usuario)
            print(f"Usuario {usuario.nombre} registrado correctamente.")
        else:
            print("Este usuario ya está registrado.")
    
    def dar_baja_usuario(self, id_usuario):
        """Dar de baja un usuario"""
        self.usuarios = {u for u in self.usuarios if u.id_usuario != id_usuario}
        print(f"Usuario con ID {id_usuario} dado de baja.")

    def prestar_libro(self, id_usuario, isbn):
        """Prestar un libro a un usuario"""
        # Buscar el libro en la biblioteca
        libro = self.libros.get(isbn)
        if libro:
            # Buscar el usuario
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if usuario:
                # Verificar si el libro ya está prestado
                if libro not in usuario.libros_prestados:
                    usuario.agregar_libro(libro)
                    print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
                else:
                    print(f"El libro '{libro.titulo}' ya está prestado a {usuario.nombre}.")
            else:
                print("Usuario no encontrado.")
        else:
            print("Libro no disponible.")
    
    def devolver_libro(self, id_usuario, isbn):
        """Devolver un libro prestado por un usuario"""
        # Buscar el libro en la biblioteca
        libro = self.libros.get(isbn)
        if libro:
            # Buscar el usuario
            usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
            if usuario:
                if libro in usuario.libros_prestados:
                    usuario.devolver_libro(libro)
                    print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
                else:
                    print(f"El libro '{libro.titulo}' no está prestado a {usuario.nombre}.")
            else:
                print("Usuario no encontrado.")
        else:
            print("Libro no disponible.")
    
    def buscar_libro(self, termino):
        """Buscar un libro por título, autor o categoría"""
        print(f"Resultados de búsqueda para '{termino}':")
        for libro in self.libros.values():
            if (termino.lower() in libro.titulo.lower() or
                termino.lower() in libro.autor.lower() or
                termino.lower() in libro.categoria.lower()):
                print(libro)

    def listar_libros_prestados(self, id_usuario):
        """Listar todos los libros prestados a un usuario"""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("Usuario no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear objetos de libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
    libro2 = Libro("1984", "George Orwell", "Distopía", "978-0-452-28423-4")

    # Crear un usuario
    usuario1 = Usuario("Juan Pérez", "U001")
    
    # Crear la biblioteca y registrar usuario
    biblioteca = Biblioteca()
    biblioteca.registrar_usuario(usuario1)
    
    # Añadir libros a la biblioteca
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    
    # Prestar un libro
    biblioteca.prestar_libro("U001", "978-3-16-148410-0")
    
    # Listar los libros prestados al usuario
    biblioteca.listar_libros_prestados("U001")
    
    # Buscar un libro por título
    biblioteca.buscar_libro("1984")
    
    # Devolver un libro
    biblioteca.devolver_libro("U001", "978-3-16-148410-0")
    
    # Quitar un libro de la biblioteca
    biblioteca.quitar_libro("978-0-452-28423-4")
