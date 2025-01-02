import yaml
import os

# 1. Crear un archivo YAML y agregar datos
def crear_archivo_yaml():
    # Datos a escribir en el archivo YAML
    datos = {
        "usuarios": [
            {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"},
            {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"},
            {"nombre": "Carlos", "edad": 40, "ciudad": "Valencia"}
        ]
    }
    # Crear y escribir datos en el archivo YAML
    with open("archivo.yaml", "w") as archivo:
        yaml.dump(datos, archivo, default_flow_style=False)  # Serializa el objeto y lo guarda
    print("Archivo YAML creado y datos escritos.")

# 2. Leer datos desde un archivo YAML
def leer_archivo_yaml():
    if os.path.exists("archivo.yaml"):
        with open("archivo.yaml", "r") as archivo:
            datos = yaml.load(archivo, Loader=yaml.FullLoader)  # Deserializa el objeto del archivo
            print(yaml.dump(datos, default_flow_style=False))  # Imprime el objeto de forma legible
    else:
        print("El archivo YAML no existe.")

# 3. Agregar nuevos datos a un archivo YAML
def agregar_datos_yaml():
    if os.path.exists("archivo.yaml"):
        with open("archivo.yaml", "r") as archivo:
            datos = yaml.load(archivo, Loader=yaml.FullLoader)  # Cargar datos actuales del archivo
        
        # Agregar nuevos usuarios
        nuevos_usuarios = [
            {"nombre": "Laura", "edad": 28, "ciudad": "Sevilla"},
            {"nombre": "David", "edad": 35, "ciudad": "Zaragoza"}
        ]
        datos["usuarios"].extend(nuevos_usuarios)  # Agregar nuevos usuarios a la lista

        # Guardar los cambios en el archivo YAML
        with open("archivo.yaml", "w") as archivo:
            yaml.dump(datos, archivo, default_flow_style=False)
        print("Nuevos datos agregados al archivo YAML.")
    else:
        print("El archivo YAML no existe.")

# 4. Modificar datos en un archivo YAML
def modificar_datos_yaml():
    if os.path.exists("archivo.yaml"):
        with open("archivo.yaml", "r") as archivo:
            datos = yaml.load(archivo, Loader=yaml.FullLoader)  # Cargar datos actuales del archivo
        
        # Modificar la edad del primer usuario
        datos["usuarios"][0]["edad"] = 31  # Cambiar edad de Juan
        
        # Guardar los cambios en el archivo YAML
        with open("archivo.yaml", "w") as archivo:
            yaml.dump(datos, archivo, default_flow_style=False)
        print("Datos modificados en el archivo YAML.")
    else:
        print("El archivo YAML no existe.")

# 5. Eliminar un archivo YAML
def eliminar_archivo_yaml():
    if os.path.exists("archivo.yaml"):
        os.remove("archivo.yaml")
        print("Archivo YAML eliminado.")
    else:
        print("El archivo YAML no existe para eliminar.")

# 6. Verificar si el archivo YAML existe
def verificar_existencia_yaml():
    if os.path.exists("archivo.yaml"):
        print("El archivo YAML existe.")
    else:
        print("El archivo YAML no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_yaml():
    crear_archivo_yaml()        # Crear y escribir datos en el archivo YAML
    leer_archivo_yaml()         # Leer y mostrar el contenido
    agregar_datos_yaml()        # Agregar nuevos datos
    leer_archivo_yaml()         # Leer y mostrar el nuevo contenido
    modificar_datos_yaml()      # Modificar datos en el archivo
    leer_archivo_yaml()         # Leer y mostrar el archivo modificado
    verificar_existencia_yaml() # Verificar si el archivo existe
    eliminar_archivo_yaml()     # Eliminar el archivo
    verificar_existencia_yaml() # Verificar si el archivo fue eliminado

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_yaml()
