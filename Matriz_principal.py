#Wilman Tasinchano
# Datos de temperaturas diarias en varias ciudades
temperaturas = [
    {
        "ciudad": "Cuenca",
        "semanas": [
            {"**Semana 1**": {"Lunes": 10, "Martes": 12.06, "Miércoles": 14.12, "Jueves": 16.18, "Viernes": 18.24, "Sábado": 20.3, "Domingo": 22.36}},  # Semana 1
            {"**Semana 2**": {"Lunes": 10.6, "Martes": 12.5, "Miércoles": 14.4, "Jueves": 16.3, "Viernes": 18.2, "Sábado": 20.1, "Domingo": 22}},       # Semana 2
            {"**Semana 3**": {"Lunes": 10, "Martes": 12.14, "Miércoles": 14.28, "Jueves": 16.42, "Viernes": 18.56, "Sábado": 20.7, "Domingo": 22.84}},  # Semana 3
            {"**Semana 4**": {"Lunes": 10, "Martes": 12.06, "Miércoles": 14.12, "Jueves": 16.18, "Viernes": 18.24, "Sábado": 20.3, "Domingo": 22.36}}   # Semana 4
        ]
    },
    {
        "ciudad": "Quito",
        "semanas": [
            {"**Semana 1**": {"Lunes": 2.8, "Martes": 5.41, "Miércoles": 8.02, "Jueves": 10.63, "Viernes": 13.24, "Sábado": 15.85, "Domingo": 18.46}},  # Semana 1
            {"**Semana 2**": {"Lunes": 3.3, "Martes": 5.69, "Miércoles": 8.08, "Jueves": 10.47, "Viernes": 12.86, "Sábado": 15.25, "Domingo": 17.64}},  # Semana 2
            {"**Semana 3**": {"Lunes": 3.3, "Martes": 5.84, "Miércoles": 8.38, "Jueves": 10.92, "Viernes": 13.46, "Sábado": 16, "Domingo": 18.54}},      # Semana 3
            {"**Semana 4**": {"Lunes": 3.9, "Martes": 6.2, "Miércoles": 8.5, "Jueves": 10.8, "Viernes": 13.1, "Sábado": 15.4, "Domingo": 17.7}}          # Semana 4
        ]
    },
    {
        "ciudad": "Guayaquil",
        "semanas": [
            {"**Semana 1**": {"Lunes": 23.9, "Martes": 25.33, "Miércoles": 26.76, "Jueves": 28.19, "Viernes": 29.62, "Sábado": 31.05, "Domingo": 32.48}},  # Semana 1
            {"**Semana 2**": {"Lunes": 24.4, "Martes": 25.67, "Miércoles": 26.94, "Jueves": 28.21, "Viernes": 29.48, "Sábado": 30.75, "Domingo": 32.02}},  # Semana 2
            {"**Semana 3**": {"Lunes": 23.9, "Martes": 25.4, "Miércoles": 26.9, "Jueves": 28.4, "Viernes": 29.9, "Sábado": 31.4, "Domingo": 32.9}},         # Semana 3
            {"**Semana 4**": {"Lunes": 23.9, "Martes": 25.33, "Miércoles": 26.76, "Jueves": 28.19, "Viernes": 29.62, "Sábado": 31.05, "Domingo": 32.48}}   # Semana 4
        ]
    },
    {
        "ciudad": "El Puyo",
        "semanas": [
            {"**Semana 1**": {"Lunes": 2.8, "Martes": 7.24, "Miércoles": 11.68, "Jueves": 16.12, "Viernes": 20.56, "Sábado": 25, "Domingo": 29.44}},      # Semana 1
            {"**Semana 2**": {"Lunes": 3.3, "Martes": 7.59, "Miércoles": 11.88, "Jueves": 16.17, "Viernes": 20.46, "Sábado": 24.75, "Domingo": 29.04}},  # Semana 2
            {"**Semana 3**": {"Lunes": 3.3, "Martes": 7.74, "Miércoles": 12.18, "Jueves": 16.62, "Viernes": 21.06, "Sábado": 25.5, "Domingo": 29.94}},   # Semana 3
            {"**Semana 4**": {"Lunes": 3.9, "Martes": 8.19, "Miércoles": 12.48, "Jueves": 16.77, "Viernes": 21.06, "Sábado": 25.35, "Domingo": 29.64}}   # Semana 4
        ]
    }
]

# Calcular promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    print("**Ciudad:", ciudad["ciudad"] + "**")  # Imprimir nombre de la ciudad en negrita
    for semana in ciudad["semanas"]:
        nombre_semana, datos_semana = list(semana.items())[0]
        dias = list(datos_semana.keys())
        temperaturas_semana = list(datos_semana.values())
        promedio_semana = sum(temperaturas_semana) / len(temperaturas_semana)
        print(nombre_semana)  # Imprimir nombre de la semana en negrita
        print("Promedio de temperatura para la semana:", promedio_semana)
        print("Temperaturas diarias:")
        for dia, temperatura in zip(dias, temperaturas_semana):
            print(dia + ":", temperatura)  # Imprimir temperatura por día
    print()  # Imprimir línea en blanco entre ciudades
