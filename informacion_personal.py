# Wilman Tasinchano
informacion_personal = {
    "nombre": "María",
    "edad": 25,
    "ciudad": "Cuenca",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
ciudad_anterior = informacion_personal["ciudad"]
nueva_ciudad = "Loja"
informacion_personal["ciudad"] = nueva_ciudad
print(f"La ciudad anterior era {ciudad_anterior}, se ha cambiado a {nueva_ciudad}.")

# Agregar una nueva clave-valor representando la profesión
profesion = "Abogada"
informacion_personal["profesion"] = profesion
print(f"Se ha agregado la profesión: {profesion}.")

# Verificar la existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    telefono = "0987654321"
    informacion_personal["telefono"] = telefono
    print(f"No se encontró la clave 'telefono', se agregó con el número {telefono}.")

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("La clave 'edad' ha sido eliminada del diccionario.")

# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)
