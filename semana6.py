# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca  # Atributo público
        self.año = año  # Atributo público

    def mover(self):
        # Método que simula el movimiento de un vehículo
        print(f"El vehículo {self.marca} del año {self.año} se está moviendo.")

    def detener(self):
        # Método para detener el vehículo
        print(f"El vehículo {self.marca} se ha detenido.")

# Definición de la clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)  # Llamada al constructor de la clase base
        self.__modelo = modelo  # Atributo encapsulado (privado)

    def obtener_modelo(self):
        # Método para acceder al modelo
        return self.__modelo

    def set_modelo(self, modelo):
        # Método para modificar el modelo
        self.__modelo = modelo

    def mover(self):
        # Sobrescritura del método 'mover' para Coche (polimorfismo)
        print(f"El coche {self.marca} modelo {self.__modelo} se está moviendo.")

    def mostrar_info(self):
        # Método para mostrar la información del coche
        print(f"Coche: {self.marca}, Año: {self.año}, Modelo: {self.__modelo}")

# Ejemplo de uso del código
def main():
    # Creación de instancias
    vehiculo = Vehiculo("Toyota", 2020)
    coche = Coche("Honda", 2022, "Civic")

    # Uso de métodos de la clase base
    vehiculo.mover()
    vehiculo.detener()

    # Uso de métodos de la clase derivada
    coche.mover()  # Polimorfismo, el método mover() es sobrescrito en Coche
    coche.mostrar_info()

    # Acceso al atributo encapsulado a través de los métodos
    print(f"El modelo del coche es: {coche.obtener_modelo()}")
    coche.set_modelo("Accord")  # Modificación del modelo
    print(f"El nuevo modelo del coche es: {coche.obtener_modelo()}")

if __name__ == "__main__":
    main()
