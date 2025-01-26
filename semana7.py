class Producto:
    # Constructor de la clase, se activa cuando se crea un objeto de la clase
    def __init__(self, nombre, precio):
        self.nombre = nombre    # Atributo que almacena el nombre del producto
        self.precio = precio    # Atributo que almacena el precio del producto
        print(f"Producto '{self.nombre}' creado con precio: ${self.precio}")

    # Destructor de la clase, se activa cuando el objeto es destruido
    def __del__(self):
        print(f"El producto '{self.nombre}' ha sido eliminado. Limpiando recursos...")

    # Método para mostrar información del producto
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}")

# Creación de un objeto Producto
producto_1 = Producto("Laptop", 1200)

# Mostrar información del producto
producto_1.mostrar_info()

# El destructor se llama automáticamente cuando el objeto es eliminado (por ejemplo, cuando se sale del ámbito)
del producto_1  # Esto provoca que el destructor se active
