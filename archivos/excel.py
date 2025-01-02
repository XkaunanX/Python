import pandas as pd
import os

# 1. Leer un archivo Excel
def leer_excel():
    try:
        # Leer un archivo Excel (reemplaza con la ruta de tu archivo Excel)
        df = pd.read_excel("archivo_excel.xlsx")
        print("Contenido del archivo Excel:")
        print(df)
    except FileNotFoundError:
        print("El archivo Excel no fue encontrado.")

# 2. Crear un archivo Excel y agregar datos
def crear_excel():
    # Crear un DataFrame con datos de ejemplo
    data = {
        "Nombre": ["Juan", "Ana", "Carlos"],
        "Edad": [30, 25, 40],
        "Ciudad": ["Madrid", "Barcelona", "Valencia"]
    }
    df = pd.DataFrame(data)
    
    # Guardar el DataFrame en un archivo Excel
    df.to_excel("archivo_creado.xlsx", index=False)
    print("Archivo Excel creado como 'archivo_creado.xlsx'.")

# 3. Modificar datos en un archivo Excel existente
def modificar_excel():
    try:
        # Leer el archivo Excel existente
        df = pd.read_excel("archivo_excel.xlsx")
        
        # Modificar un valor en el DataFrame
        df.loc[df['Nombre'] == 'Juan', 'Edad'] = 35
        
        # Guardar los cambios en el mismo archivo
        df.to_excel("archivo_excel_modificado.xlsx", index=False)
        print("Archivo Excel modificado y guardado como 'archivo_excel_modificado.xlsx'.")
    except FileNotFoundError:
        print("El archivo Excel no fue encontrado.")

# 4. Guardar datos modificados en un archivo Excel
def guardar_excel_modificado():
    try:
        # Leer el archivo Excel existente
        df = pd.read_excel("archivo_excel_modificado.xlsx")
        
        # Modificar el contenido
        df['Ciudad'] = df['Ciudad'].str.upper()  # Convertir todas las ciudades a mayúsculas
        
        # Guardar los cambios
        df.to_excel("archivo_excel_guardado.xlsx", index=False)
        print("Archivo Excel modificado y guardado como 'archivo_excel_guardado.xlsx'.")
    except FileNotFoundError:
        print("El archivo Excel no fue encontrado.")

# 5. Eliminar un archivo Excel
def eliminar_excel():
    if os.path.exists("archivo_creado.xlsx"):
        os.remove("archivo_creado.xlsx")
        print("Archivo 'archivo_creado.xlsx' eliminado.")
    else:
        print("El archivo 'archivo_creado.xlsx' no existe para eliminar.")

# 6. Verificar la existencia de un archivo Excel
def verificar_existencia_excel():
    if os.path.exists("archivo_excel.xlsx"):
        print("El archivo 'archivo_excel.xlsx' existe.")
    else:
        print("El archivo 'archivo_excel.xlsx' no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_excel():
    crear_excel()               # Crear archivo Excel y agregar datos
    leer_excel()                # Leer archivo Excel
    modificar_excel()           # Modificar archivo Excel
    guardar_excel_modificado()  # Guardar archivo Excel con cambios
    eliminar_excel()            # Eliminar archivo Excel
    verificar_existencia_excel() # Verificar existencia de archivo Excel

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_excel()
