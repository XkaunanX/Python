import json
import os

# 1. Crear un archivo JSON y agregar datos
def crear_archivo_json():
    # Datos a escribir en el archivo JSON
    datos = {
        "usuarios": [
            {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"},
            {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"},
            {"nombre": "Carlos", "edad": 40, "ciudad": "Valencia"}
        ]
    }
    # Crear y escribir datos en el archivo JSON
    with open("archivo.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)  # Serializa el objeto y lo guarda con formato legible
    print("Archivo JSON creado y datos escritos.")

# 2. Leer datos desde un archivo JSON
def leer_archivo_json():
    if os.path.exists("archivo.json"):
        with open("archivo.json", "r") as archivo:
            datos = json.load(archivo)  # Deserializa el objeto del archivo
            print(json.dumps(datos, indent=4))  # Imprime el objeto de forma legible
    else:
        print("El archivo JSON no existe.")

# 3. Agregar nuevos datos a un archivo JSON
def agregar_datos_json():
    if os.path.exists("archivo.json"):
        with open("archivo.json", "r") as archivo:
            datos = json.load(archivo)  # Cargar datos actuales del archivo
        
        # Agregar nuevos usuarios
        nuevos_usuarios = [
            {"nombre": "Laura", "edad": 28, "ciudad": "Sevilla"},
            {"nombre": "David", "edad": 35, "ciudad": "Zaragoza"}
        ]
        datos["usuarios"].extend(nuevos_usuarios)  # Agregar nuevos usuarios a la lista

        # Guardar los cambios en el archivo JSON
        with open("archivo.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print("Nuevos datos agregados al archivo JSON.")
    else:
        print("El archivo JSON no existe.")

# 4. Modificar datos en un archivo JSON
def modificar_datos_json():
    if os.path.exists("archivo.json"):
        with open("archivo.json", "r") as archivo:
            datos = json.load(archivo)  # Cargar datos actuales del archivo
        
        # Modificar la edad del primer usuario
        datos["usuarios"][0]["edad"] = 31  # Cambiar edad de Juan
        
        # Guardar los cambios en el archivo JSON
        with open("archivo.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print("Datos modificados en el archivo JSON.")
    else:
        print("El archivo JSON no existe.")

# 5. Eliminar un archivo JSON
def eliminar_archivo_json():
    if os.path.exists("archivo.json"):
        os.remove("archivo.json")
        print("Archivo JSON eliminado.")
    else:
        print("El archivo JSON no existe para eliminar.")

# 6. Verificar si el archivo JSON existe
def verificar_existencia_json():
    if os.path.exists("archivo.json"):
        print("El archivo JSON existe.")
    else:
        print("El archivo JSON no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_json():
    crear_archivo_json()        # Crear y escribir datos en el archivo JSON
    leer_archivo_json()         # Leer y mostrar el contenido
    agregar_datos_json()        # Agregar nuevos datos
    leer_archivo_json()         # Leer y mostrar el nuevo contenido
    modificar_datos_json()      # Modificar datos en el archivo
    leer_archivo_json()         # Leer y mostrar el archivo modificado
    verificar_existencia_json() # Verificar si el archivo existe
    eliminar_archivo_json()     # Eliminar el archivo
    verificar_existencia_json() # Verificar si el archivo fue eliminado

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_json()
