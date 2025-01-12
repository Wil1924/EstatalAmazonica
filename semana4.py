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


# Clase que representa la Tienda
class Tienda:
    def __init__(self):
        self.productos = []  # Lista que almacena los productos disponibles en la tienda

    def agregar_producto(self, producto):
        """Método para agregar productos a la tienda"""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Método para mostrar los productos disponibles en la tienda"""
        print("Productos disponibles en la tienda:")
        for producto in self.productos:
            print(f"{producto.nombre} - Precio: {producto.precio} - Stock: {producto.stock}")


# Crear algunos productos
producto1 = Producto("Camiseta", 15, 10)
producto2 = Producto("Pantalón", 25, 5)
producto3 = Producto("Zapatos", 50, 2)

# Crear un cliente con un saldo inicial
cliente1 = Cliente("Juan", 100)

# Crear la tienda y agregar productos
tienda = Tienda()
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Mostrar los productos de la tienda
tienda.mostrar_productos()

# El cliente intenta comprar productos
cliente1.comprar(producto1, 2)  # Compra 2 camisetas
cliente1.comprar(producto2, 1)  # Compra 1 pantalón

# Mostrar el saldo del cliente después de las compras
print(f"Saldo restante de {cliente1.nombre}: {cliente1.saldo}")
