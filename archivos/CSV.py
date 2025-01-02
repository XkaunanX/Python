import csv
import os

# 1. Crear un archivo CSV y agregar datos
def crear_archivo_csv():
    # Datos a escribir
    datos = [
        ["Nombre", "Edad", "Ciudad"],
        ["Juan", 30, "Madrid"],
        ["Ana", 25, "Barcelona"],
        ["Carlos", 40, "Valencia"]
    ]
    # Crear y escribir datos en el archivo CSV
    with open("archivo.csv", mode="w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)  # Escribe todas las filas a la vez
    print("Archivo CSV creado y datos escritos.")

# 2. Leer datos desde un archivo CSV
def leer_archivo_csv():
    if os.path.exists("archivo.csv"):
        with open("archivo.csv", mode="r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                print(fila)  # Imprime cada fila
    else:
        print("El archivo CSV no existe.")

# 3. Agregar nuevos datos a un archivo CSV existente
def agregar_datos_csv():
    nuevos_datos = [["Laura", 28, "Sevilla"], ["David", 35, "Zaragoza"]]
    # Abrir el archivo en modo de anexado
    with open("archivo.csv", mode="a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(nuevos_datos)  # Agrega nuevas filas
    print("Nuevos datos agregados al archivo CSV.")

# 4. Modificar un archivo CSV
def modificar_datos_csv():
    if os.path.exists("archivo.csv"):
        # Leer todo el contenido del archivo CSV
        with open("archivo.csv", mode="r") as archivo:
            lector = csv.reader(archivo)
            filas = list(lector)
        
        # Modificar la segunda fila (puedes modificar otros datos según sea necesario)
        filas[1][1] = 31  # Cambiar edad de Juan a 31
        
        # Escribir de nuevo todo el contenido modificado en el archivo CSV
        with open("archivo.csv", mode="w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(filas)  # Sobrescribe el archivo con los datos modificados
        print("Archivo CSV modificado.")
    else:
        print("El archivo CSV no existe.")

# 5. Eliminar un archivo CSV
def eliminar_archivo_csv():
    if os.path.exists("archivo.csv"):
        os.remove("archivo.csv")
        print("Archivo CSV eliminado.")
    else:
        print("El archivo CSV no existe para eliminar.")

# 6. Verificar si el archivo CSV existe
def verificar_existencia_csv():
    if os.path.exists("archivo.csv"):
        print("El archivo CSV existe.")
    else:
        print("El archivo CSV no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_csv():
    crear_archivo_csv()        # Crear y escribir datos en el archivo CSV
    leer_archivo_csv()         # Leer y mostrar el contenido
    agregar_datos_csv()        # Agregar nuevos datos
    leer_archivo_csv()         # Leer y mostrar el nuevo contenido
    modificar_datos_csv()      # Modificar datos en el archivo
    leer_archivo_csv()         # Leer y mostrar el archivo modificado
    verificar_existencia_csv() # Verificar si el archivo existe
    eliminar_archivo_csv()     # Eliminar el archivo
    verificar_existencia_csv() # Verificar si el archivo fue eliminado

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_csv()
