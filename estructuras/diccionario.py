# 04_diccionarios/diccionarios.py

# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a un valor por clave
print(persona["nombre"])  # Imprime Juan

# Modificar un valor
persona["edad"] = 31

# Agregar un nuevo par clave-valor
persona["ocupacion"] = "Ingeniero"

# Eliminar un par clave-valor
del persona["ciudad"]

# Iterar sobre las claves y valores
for clave, valor in persona.items():
    print(clave, valor)
