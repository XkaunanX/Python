import sqlite3
import os

# 1. Crear una base de datos y una tabla
def crear_base_de_datos():
    # Conectar a la base de datos (si no existe, se crea automáticamente)
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    
    # Crear una tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            ciudad TEXT
        )
    ''')
    
    # Confirmar cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("Base de datos y tabla 'usuarios' creadas.")

# 2. Insertar datos en la tabla
def insertar_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    
    # Insertar datos en la tabla
    cursor.execute('''
        INSERT INTO usuarios (nombre, edad, ciudad)
        VALUES (?, ?, ?)
    ''', ("Juan", 30, "Madrid"))
    
    cursor.execute('''
        INSERT INTO usuarios (nombre, edad, ciudad)
        VALUES (?, ?, ?)
    ''', ("Ana", 25, "Barcelona"))
    
    cursor.execute('''
        INSERT INTO usuarios (nombre, edad, ciudad)
        VALUES (?, ?, ?)
    ''', ("Carlos", 40, "Valencia"))
    
    # Confirmar cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("Datos insertados en la tabla 'usuarios'.")

# 3. Leer datos desde la tabla
def leer_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    
    # Leer todos los datos de la tabla
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    
    # Mostrar los resultados
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}, Ciudad: {usuario[3]}")
    
    # Cerrar la conexión
    conexion.close()

# 4. Actualizar datos en la tabla
def actualizar_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    
    # Actualizar la edad de un usuario
    cursor.execute('''
        UPDATE usuarios
        SET edad = ?
        WHERE nombre = ?
    ''', (31, "Juan"))
    
    # Confirmar cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("Datos actualizados en la tabla 'usuarios'.")

# 5. Eliminar datos de la tabla
def eliminar_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    
    # Eliminar un usuario de la tabla
    cursor.execute('''
        DELETE FROM usuarios
        WHERE nombre = ?
    ''', ("Carlos",))
    
    # Confirmar cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("Datos eliminados de la tabla 'usuarios'.")

# 6. Eliminar la base de datos
def eliminar_base_de_datos():
    if os.path.exists("usuarios.db"):
        os.remove("usuarios.db")
        print("Base de datos 'usuarios.db' eliminada.")
    else:
        print("La base de datos no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_sqlite():
    crear_base_de_datos()     # Crear base de datos y tabla
    insertar_datos()           # Insertar datos
    leer_datos()               # Leer y mostrar los datos
    actualizar_datos()         # Actualizar datos
    leer_datos()               # Leer y mostrar los datos actualizados
    eliminar_datos()           # Eliminar datos
    leer_datos()               # Leer y mostrar los datos después de la eliminación
    eliminar_base_de_datos()   # Eliminar la base de datos

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_sqlite()
