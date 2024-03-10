def temperatura_promedio_ciudad(datos_temperaturas):
    """
    Calcula la temperatura promedio de una ciudad durante un período de tiempo.

    Args:
    - datos_temperaturas (list): Una lista que contiene los datos de temperaturas
                                 de múltiples ciudades y semanas.

    Returns:
    - dict: Un diccionario que contiene las temperaturas promedio de cada ciudad.
    """
    temperaturas_promedio = {}

    for ciudad in datos_temperaturas:
        nombre_ciudad = ciudad["ciudad"]
        total_temperaturas = 0
        cantidad_temperaturas = 0

        for semana in ciudad["semanas"]:
            temperaturas_semana = list(semana.values())[0].values()
            total_temperaturas += sum(temperaturas_semana)
            cantidad_temperaturas += len(temperaturas_semana)

        if cantidad_temperaturas > 0:
            temperatura_promedio = total_temperaturas / cantidad_temperaturas
            temperaturas_promedio[nombre_ciudad] = temperatura_promedio

    return temperaturas_promedio

# Datos de temperaturas diarias en varias ciudades
temperaturas = [
    {
        "ciudad": "Cuenca",
        "semanas": [
            {"Semana 1": {"Lunes": 10, "Martes": 12.06, "Miércoles": 14.12, "Jueves": 16.18, "Viernes": 18.24, "Sábado": 20.3, "Domingo": 22.36}},  # Semana 1
            {"Semana 2": {"Lunes": 10.6, "Martes": 12.5, "Miércoles": 14.4, "Jueves": 16.3, "Viernes": 18.2, "Sábado": 20.1, "Domingo": 22}},       # Semana 2
            {"Semana 3": {"Lunes": 10, "Martes": 12.14, "Miércoles": 14.28, "Jueves": 16.42, "Viernes": 18.56, "Sábado": 20.7, "Domingo": 22.84}},  # Semana 3
            {"Semana 4": {"Lunes": 10, "Martes": 12.06, "Miércoles": 14.12, "Jueves": 16.18, "Viernes": 18.24, "Sábado": 20.3, "Domingo": 22.36}}   # Semana 4
        ]
    },
    {
        "ciudad": "Quito",
        "semanas": [
            {"Semana 1": {"Lunes": 2.8, "Martes": 5.41, "Miércoles": 8.02, "Jueves": 10.63, "Viernes": 13.24, "Sábado": 15.85, "Domingo": 18.46}},  # Semana 1
            {"Semana 2": {"Lunes": 3.3, "Martes": 5.69, "Miércoles": 8.08, "Jueves": 10.47, "Viernes": 12.86, "Sábado": 15.25, "Domingo": 17.64}},  # Semana 2
            {"Semana 3": {"Lunes": 3.3, "Martes": 5.84, "Miércoles": 8.38, "Jueves": 10.92, "Viernes": 13.46, "Sábado": 16, "Domingo": 18.54}},      # Semana 3
            {"Semana 4": {"Lunes": 3.9, "Martes": 6.2, "Miércoles": 8.5, "Jueves": 10.8, "Viernes": 13.1, "Sábado": 15.4, "Domingo": 17.7}}          # Semana 4
        ]
    },
    {
        "ciudad": "Guayaquil",
        "semanas": [
            {"Semana 1": {"Lunes": 23.9, "Martes": 25.33, "Miércoles": 26.76, "Jueves": 28.19, "Viernes": 29.62, "Sábado": 31.05, "Domingo": 32.48}},  # Semana 1
            {"Semana 2": {"Lunes": 24.4, "Martes": 25.67, "Miércoles": 26.94, "Jueves": 28.21, "Viernes": 29.48, "Sábado": 30.75, "Domingo": 32.02}},  # Semana 2
            {"Semana 3": {"Lunes": 23.9, "Martes": 25.4, "Miércoles": 26.9, "Jueves": 28.4, "Viernes": 29.9, "Sábado": 31.4, "Domingo": 32.9}},         # Semana 3
            {"Semana 4": {"Lunes": 23.9, "Martes": 25.33, "Miércoles": 26.76, "Jueves": 28.19, "Viernes": 29.62, "Sábado": 31.05, "Domingo": 32.48}}   # Semana 4
        ]
    },
    {
        "ciudad": "El Puyo",
        "semanas": [
            {"Semana 1": {"Lunes": 2.8, "Martes": 7.24, "Miércoles": 11.68, "Jueves": 16.12, "Viernes": 20.56, "Sábado": 25, "Domingo": 29.44}},      # Semana 1
            {"Semana 2": {"Lunes": 3.3, "Martes": 7.59, "Miércoles": 11.88, "Jueves": 16.17, "Viernes": 20.46, "Sábado": 24.75, "Domingo": 29.04}},  # Semana 2
            {"Semana 3": {"Lunes": 3.3, "Martes": 7.74, "Miércoles": 12.18, "Jueves": 16.62, "Viernes": 21.06, "Sábado": 25.5, "Domingo": 29.94}},   # Semana 3
            {"Semana 4": {"Lunes": 3.9, "Martes": 8.19, "Miércoles": 12.48, "Jueves": 16.77, "Viernes": 21.06, "Sábado": 25.35, "Domingo": 29.64}}   # Semana 4
        ]
    }
]

# Función para calcular la temperatura promedio para cada ciudad
temperaturas_promedio = temperatura_promedio_ciudad(temperaturas)

# Imprimir temperaturas promedio por ciudad
print("Temperaturas promedio por ciudad:")
for ciudad, temperatura_promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {temperatura_promedio}")

# Agregar, confirmar y enviar cambios al repositorio en GitHub
import git

# Directorio de trabajo del repositorio
repo_dir = 'https://github.com/Wil1924/EstatalAmazonica.git'

# Inicializar el repositorio
repo = git.Repo(repo_dir)

# Añadir todos los archivos modificados
repo.git.add('--all')

# Confirmar los cambios
commit_message = "Agregada función temperatura_promedio_ciudad() para calcular la temperatura promedio de múltiples ciudades."
repo.index.commit(commit_message)

# Enviar los cambios al repositorio remoto en GitHub
origin = repo.remote(name='origin')
origin.push()

