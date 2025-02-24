# Clase que representa un Producto en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre  # Atributo que guarda el nombre del producto
        self.precio = precio  # Atributo que guarda el precio del producto
        self.stock = stock    # Atributo que guarda la cantidad disponible del producto

    def vender(self, cantidad):
        """Método para vender una cierta cantidad de un producto"""
        if cantidad <= self.stock:
            self.stock -= cantidad
            return self.precio * cantidad  # Retorna el total de la venta
        else:
            print(f"No hay suficiente stock de {self.nombre}. Solo hay {self.stock} disponibles.")
            return 0

    def to_string(self):
        """Convierte el objeto Producto a una cadena para guardarlo en un archivo"""
        return f"{self.nombre},{self.precio},{self.stock}"

    @classmethod
    def from_string(cls, data):
        """Convierte una cadena de texto a un objeto Producto"""
        nombre, precio, stock = data.strip().split(',')
        return cls(nombre, float(precio), int(stock))


# Clase que representa la Tienda
class Tienda:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []  # Lista que almacena los productos disponibles en la tienda
        self.archivo = archivo  # Archivo donde se almacenarán los productos

        # Cargar productos desde el archivo al iniciar
        self.cargar_inventario()

    def agregar_producto(self, producto):
        """Método para agregar productos a la tienda y actualizar el archivo"""
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' agregado exitosamente al inventario.")

    def mostrar_productos(self):
        """Método para mostrar los productos disponibles en la tienda"""
        if not self.productos:
            print("No hay productos disponibles en la tienda.")
        else:
            print("Productos disponibles en la tienda:")
            for producto in self.productos:
                print(f"{producto.nombre} - Precio: {producto.precio} - Stock: {producto.stock}")

    def guardar_inventario(self):
        """Guarda los productos actuales en el archivo"""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(producto.to_string() + '\n')
            print("Inventario guardado exitosamente.")
        except (PermissionError, FileNotFoundError) as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self):
        """Carga los productos desde el archivo"""
        try:
            with open(self.archivo, 'r') as f:
                self.productos = [Producto.from_string(line) for line in f.readlines()]
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except PermissionError as e:
            print(f"Error al leer el archivo de inventario: {e}")
        except Exception as e:
            print(f"Se produjo un error inesperado al cargar el inventario: {e}")


# Clase que representa un Cliente
class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre  # Atributo que guarda el nombre del cliente
        self.saldo = saldo    # Atributo que guarda el saldo disponible del cliente

    def comprar(self, producto, cantidad):
        """Método para realizar la compra de un producto"""
        total = producto.vender(cantidad)
        if total > 0 and self.saldo >= total:
            self.saldo -= total  # Descontamos el dinero del saldo del cliente
            print(f"{self.nombre} ha comprado {cantidad} {producto.nombre}(s) por {total} unidades monetarias.")
        else:
            print(f"{self.nombre} no tiene suficiente saldo o no se puede realizar la compra.")


# Crear algunos productos
producto1 = Producto("Camiseta", 15, 10)
producto2 = Producto("Pantalón", 25, 5)
producto3 = Producto("Zapatos", 50, 2)

# Crear un cliente con un saldo inicial
cliente1 = Cliente("Juan", 100)

# Crear la tienda y agregar productos
tienda = Tienda()

# Mostrar los productos de la tienda
tienda.mostrar_productos()

# El cliente intenta comprar productos
cliente1.comprar(producto1, 2)  # Compra 2 camisetas
cliente1.comprar(producto2, 1)  # Compra 1 pantalón

# Mostrar el saldo del cliente después de las compras
print(f"Saldo restante de {cliente1.nombre}: {cliente1.saldo}")

# Agregar un nuevo producto a la tienda y guardar el inventario
nuevo_producto = Producto("Sombrero", 10, 15)
tienda.agregar_producto(nuevo_producto)

# Mostrar los productos de la tienda nuevamente después de agregar el nuevo producto
tienda.mostrar_productos()
