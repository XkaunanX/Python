import os
import pickle

# 1. Crear y serializar (guardar) datos en un archivo pickle
def crear_archivo_pickle():
    datos = [{"nombre": "Juan", "edad": 30}, {"nombre": "Ana", "edad": 25}]
    with open("datos.pickle", "wb") as archivo:
        pickle.dump(datos, archivo)  # Serializa y guarda los datos en el archivo
    print("Archivo pickle creado y datos serializados.")

# 2. Leer y deserializar datos de un archivo pickle
def leer_archivo_pickle():
    if os.path.exists("datos.pickle"):
        with open("datos.pickle", "rb") as archivo:
            datos_recuperados = pickle.load(archivo)  # Deserializa los datos
        print("Contenido del archivo pickle:", datos_recuperados)
    else:
        print("El archivo pickle no existe.")

# 3. Agregar datos a un archivo pickle existente
def agregar_datos_pickle():
    nuevos_datos = {"nombre": "Carlos", "edad": 40}
    # Leer los datos actuales
    with open("datos.pickle", "rb") as archivo:
        datos_recuperados = pickle.load(archivo)
    
    # Agregar nuevos datos
    datos_recuperados.append(nuevos_datos)
    
    # Volver a escribir los datos en el archivo pickle
    with open("datos.pickle", "wb") as archivo:
        pickle.dump(datos_recuperados, archivo)
    print("Nuevos datos agregados al archivo pickle.")

# 4. Eliminar un archivo pickle
def eliminar_archivo_pickle():
    if os.path.exists("datos.pickle"):
        os.remove("datos.pickle")
        print("Archivo pickle eliminado.")
    else:
        print("El archivo pickle no existe para eliminar.")

# 5. Verificar si el archivo pickle existe
def verificar_existencia_pickle():
    if os.path.exists("datos.pickle"):
        print("El archivo pickle existe.")
    else:
        print("El archivo pickle no existe.")

# 6. Manejo de excepciones al leer un archivo pickle
def manejar_excepcion_pickle():
    try:
        with open("datos.pickle", "rb") as archivo:
            datos_recuperados = pickle.load(archivo)
        print("Contenido del archivo pickle:", datos_recuperados)
    except (FileNotFoundError, pickle.UnpicklingError) as e:
        print(f"Ocurrió un error al leer el archivo pickle: {e}")

# 7. Leer un archivo pickle línea por línea (si fuera posible, aunque pickle almacena objetos completos)
def leer_pickle_linea_por_linea():
    if os.path.exists("datos.pickle"):
        with open("datos.pickle", "rb") as archivo:
            datos_recuperados = pickle.load(archivo)
            for item in datos_recuperados:
                print(item)
    else:
        print("El archivo pickle no existe.")

# Ejecutar todas las operaciones
def ejecutar_operaciones_pickle():
    crear_archivo_pickle()
    leer_archivo_pickle()
    agregar_datos_pickle()
    leer_archivo_pickle()
    verificar_existencia_pickle()
    manejar_excepcion_pickle()
    leer_pickle_linea_por_linea()
    eliminar_archivo_pickle()
    verificar_existencia_pickle()

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_pickle()
