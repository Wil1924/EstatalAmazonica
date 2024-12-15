# Función para ingresar las temperaturas diarias de la semana
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingresa un valor numérico válido.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal que orquesta el proceso
def main():
    print("Cálculo del Promedio Semanal de Temperaturas")
    # Ingresar temperaturas
    temperaturas = ingresar_temperaturas()
    # Calcular el promedio
    promedio = calcular_promedio(temperaturas)
    # Mostrar el resultado
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
