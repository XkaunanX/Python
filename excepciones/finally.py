# finally.py

# Función que maneja un archivo y garantiza su cierre con finally
def leer_archivo():
    try:
        archivo = open("archivo.txt", "r")
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")
    finally:
        try:
            archivo.close()
            print("Archivo cerrado.")
        except NameError:
            # Si el archivo nunca se abrió, no intentamos cerrarlo
            print("No se abrió ningún archivo para cerrar.")

# Ejecutar la función
leer_archivo()
