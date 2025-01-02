import os

# 1. Crear y escribir datos en un archivo de texto
def crear_archivo():
    texto = "Hola, este es un archivo de texto.\nAquí escribimos algunas líneas."
    with open("archivo.txt", "w") as archivo:
        archivo.write(texto)  # Escribe 'texto' en el archivo
    print("Archivo creado y texto escrito.")

# 2. Leer datos de un archivo de texto
def leer_archivo():
    if os.path.exists("archivo.txt"):
        with open("archivo.txt", "r") as archivo:
            contenido = archivo.read()  # Lee todo el contenido del archivo
        print("Contenido del archivo:\n", contenido)
    else:
        print("El archivo no existe.")

# 3. Agregar contenido a un archivo de texto existente
def agregar_contenido():
    nuevas_lineas = "Este es un texto adicional.\nY otra línea."
    with open("archivo.txt", "a") as archivo:
        archivo.write(nuevas_lineas)  # Añade nuevas líneas al final del archivo
    print("Contenido agregado al archivo.")

# 4. Eliminar un archivo de texto
def eliminar_archivo():
    if os.path.exists("archivo.txt"):
        os.remove("archivo.txt")
        print("Archivo eliminado.")
    else:
        print("El archivo no existe para eliminar.")

# 5. Verificar si el archivo de texto existe
def verificar_existencia():
    if os.path.exists("archivo.txt"):
        print("El archivo existe.")
    else:
        print("El archivo no existe.")

# 6. Leer un archivo línea por línea
def leer_lineas():
    if os.path.exists("archivo.txt"):
        with open("archivo.txt", "r") as archivo:
            for linea in archivo:
                print(linea.strip())  # Imprime cada línea sin saltos de línea
    else:
        print("El archivo no existe.")

# 7. Leer todas las líneas de un archivo como lista
def leer_como_lista():
    if os.path.exists("archivo.txt"):
        with open("archivo.txt", "r") as archivo:
            lineas = archivo.readlines()  # Lee todas las líneas como una lista
        print("Contenido como lista:", lineas)
    else:
        print("El archivo no existe.")

# Ejecutar todas las operaciones
def ejecutar_operaciones():
    crear_archivo()
    leer_archivo()
    agregar_contenido()
    leer_archivo()
    verificar_existencia()
    leer_lineas()
    leer_como_lista()
    eliminar_archivo()
    verificar_existencia()

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones()
