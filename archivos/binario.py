import pickle
import os

# 1. Crear un archivo binario y agregar datos
def crear_archivo_binario():
    # Datos a guardar en el archivo binario (puede ser cualquier tipo de objeto Python)
    datos = {
        "usuarios": [
            {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"},
            {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"},
            {"nombre": "Carlos", "edad": 40, "ciudad": "Valencia"}
        ]
    }
    # Crear y escribir datos en un archivo binario usando pickle
    with open("archivo.bin", "wb") as archivo:
        pickle.dump(datos, archivo)  # Serializa el objeto y lo guarda en el archivo
    print("Archivo binario creado y datos escritos.")

# 2. Leer datos desde un archivo binario
def leer_archivo_binario():
    if os.path.exists("archivo.bin"):
        with open("archivo.bin", "rb") as archivo:
            datos = pickle.load(archivo)  # Deserializa el objeto desde el archivo
            print(datos)
    else:
        print("El archivo binario no existe.")

# 3. Agregar nuevos datos a un archivo binario
def agregar_datos_binario():
    if os.path.exists("archivo.bin"):
        with open("archivo.bin", "rb") as archivo:
            datos = pickle.load(archivo)  # Cargar los datos actuales
        
        # Agregar nuevos usuarios
        nuevos_usuarios = [
            {"nombre": "Laura", "edad": 28, "ciudad": "Sevilla"},
            {"nombre": "David", "edad": 35, "ciudad": "Zaragoza"}
        ]
        datos["usuarios"].extend(nuevos_usuarios)  # Agregar los nuevos usuarios a la lista
        
        # Guardar los cambios en el archivo binario
        with open("archivo.bin", "wb") as archivo:
            pickle.dump(datos, archivo)
        print("Nuevos datos agregados al archivo binario.")
    else:
        print("El archivo binario no existe.")

# 4. Modificar datos en un archivo binario
def modificar_datos_binario():
    if os.path.exists("archivo.bin"):
        with open("archivo.bin", "rb") as archivo:
            datos = pickle.load(archivo)  # Cargar los datos actuales
        
        # Modificar la edad del primer usuario
        datos["usuarios"][0]["edad"] = 31  # Cambiar la edad de Juan
        
        # Guardar los cambios en el archivo binario
        with open("archivo.bin", "wb") as archivo:
            pickle.dump(datos, archivo)
        print("Datos modificados en el archivo binario.")
    else:
        print("El archivo binario no existe.")

# 5. Eliminar un archivo binario
def eliminar_archivo_binario():
    if os.path.exists("archivo.bin"):
        os.remove("archivo.bin")
        print("Archivo binario eliminado.")
    else:
        print("El archivo binario no existe para eliminar.")

# 6. Verificar si el archivo binario existe
def verificar_existencia_binario():
    if os.path.exists("archivo.bin"):
        print("El archivo binario existe.")
    else:
        print("El archivo binario no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_binario():
    crear_archivo_binario()        # Crear y escribir datos en el archivo binario
    leer_archivo_binario()         # Leer y mostrar el contenido
    agregar_datos_binario()        # Agregar nuevos datos
    leer_archivo_binario()         # Leer y mostrar el nuevo contenido
    modificar_datos_binario()      # Modificar datos en el archivo
    leer_archivo_binario()         # Leer y mostrar el archivo modificado
    verificar_existencia_binario() # Verificar si el archivo existe
    eliminar_archivo_binario()     # Eliminar el archivo
    verificar_existencia_binario() # Verificar si el archivo fue eliminado

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_binario()
