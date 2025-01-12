import math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Función principal
def main():
    print("Bienvenido al programa de cálculo de áreas de figuras geométricas")
    
    # Solicitar al usuario que elija una figura
    figura = input("Seleccione la figura (círculo, cuadrado, rectángulo): ").lower()

    if figura == "círculo":
        radio = float(input("Ingrese el radio del círculo: "))  # Solicitar radio al usuario
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f} unidades cuadradas.")
    
    elif figura == "cuadrado":
        lado = float(input("Ingrese el lado del cuadrado: "))  # Solicitar lado al usuario
        area = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area:.2f} unidades cuadradas.")
    
    elif figura == "rectángulo":
        base = float(input("Ingrese la base del rectángulo: "))  # Solicitar base al usuario
        altura = float(input("Ingrese la altura del rectángulo: "))  # Solicitar altura al usuario
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f} unidades cuadradas.")
    
    else:
        print("Error: La figura seleccionada no es válida.")

# Ejecutar la función principal
main()
