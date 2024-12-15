class Clima:
    def __init__(self):
        # Atributo para almacenar las temperaturas de la semana
        self.temperaturas = []

    # Método para ingresar las temperaturas de los 7 días
    def ingresar_temperaturas(self):
        for dia in range(7):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingresa un valor numérico válido.")

    # Método para calcular el promedio de las temperaturas
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método para mostrar el resultado
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

# Función principal que orquesta el flujo
def main():
    print("Cálculo del Promedio Semanal de Temperaturas")
    # Crear un objeto de la clase Clima
    clima = Clima()
    # Ingresar temperaturas
    clima.ingresar_temperaturas()
    # Mostrar el promedio semanal
    clima.mostrar_promedio()

# Llamada a la función principal
if __name__ == "__main__":
    main()
