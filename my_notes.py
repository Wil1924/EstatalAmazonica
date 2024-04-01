#Wilman Tasinchano
# Leer el contenido del archivo y mostrarlo
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for i, line in enumerate(file, start=1):  # Enumeramos las líneas para mostrar el número de línea
        # Mostrar cada línea en la consola con su número correspondiente
        print(f"{i}. {line.strip()}")

# Permitir al usuario seleccionar una línea para modificar
selected_line = int(input("Seleccione la línea que desea modificar (1, 2 o 3): "))
if selected_line in [1, 2, 3]:  # Verificar si la selección del usuario es válida
    # Abrir el archivo en modo lectura y escritura
    with open('my_notes.txt', 'r+') as file:
        lines = file.readlines()  # Leer todas las líneas del archivo
        new_content = input("Ingrese el nuevo contenido: ")  # Solicitar al usuario el nuevo contenido
        lines[selected_line - 1] = f"{selected_line}. {new_content}\n"  # Modificar la línea seleccionada
        file.seek(0)  # Mover el cursor al principio del archivo
        file.writelines(lines)  # Escribir las líneas modificadas de vuelta al archivo
        file.truncate()  # Truncar el archivo para eliminar cualquier contenido restante
        print("Línea modificada exitosamente.")
else:
    print("Selección no válida. Debe seleccionar 1, 2 o 3.")

# Cerrar el archivo después de realizar las operaciones necesarias
file.close()
