import xml.etree.ElementTree as ET
import os

# 1. Crear un archivo XML y agregar datos
def crear_archivo_xml():
    # Crear el elemento raíz
    raiz = ET.Element("usuarios")
    
    # Crear subelementos (usuarios)
    usuario1 = ET.SubElement(raiz, "usuario", id="1")
    ET.SubElement(usuario1, "nombre").text = "Juan"
    ET.SubElement(usuario1, "edad").text = "30"
    ET.SubElement(usuario1, "ciudad").text = "Madrid"
    
    usuario2 = ET.SubElement(raiz, "usuario", id="2")
    ET.SubElement(usuario2, "nombre").text = "Ana"
    ET.SubElement(usuario2, "edad").text = "25"
    ET.SubElement(usuario2, "ciudad").text = "Barcelona"
    
    usuario3 = ET.SubElement(raiz, "usuario", id="3")
    ET.SubElement(usuario3, "nombre").text = "Carlos"
    ET.SubElement(usuario3, "edad").text = "40"
    ET.SubElement(usuario3, "ciudad").text = "Valencia"

    # Crear un objeto ElementTree y escribir el árbol en un archivo XML
    arbol = ET.ElementTree(raiz)
    arbol.write("archivo.xml", encoding="utf-8", xml_declaration=True)
    print("Archivo XML creado y datos escritos.")

# 2. Leer datos desde un archivo XML
def leer_archivo_xml():
    if os.path.exists("archivo.xml"):
        tree = ET.parse("archivo.xml")
        root = tree.getroot()
        
        # Mostrar los datos leídos
        for usuario in root.findall("usuario"):
            nombre = usuario.find("nombre").text
            edad = usuario.find("edad").text
            ciudad = usuario.find("ciudad").text
            print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
    else:
        print("El archivo XML no existe.")

# 3. Agregar nuevos datos a un archivo XML
def agregar_datos_xml():
    if os.path.exists("archivo.xml"):
        tree = ET.parse("archivo.xml")
        root = tree.getroot()
        
        # Agregar nuevos usuarios
        usuario4 = ET.SubElement(root, "usuario", id="4")
        ET.SubElement(usuario4, "nombre").text = "Laura"
        ET.SubElement(usuario4, "edad").text = "28"
        ET.SubElement(usuario4, "ciudad").text = "Sevilla"
        
        usuario5 = ET.SubElement(root, "usuario", id="5")
        ET.SubElement(usuario5, "nombre").text = "David"
        ET.SubElement(usuario5, "edad").text = "35"
        ET.SubElement(usuario5, "ciudad").text = "Zaragoza"
        
        # Guardar los cambios en el archivo XML
        tree.write("archivo.xml", encoding="utf-8", xml_declaration=True)
        print("Nuevos datos agregados al archivo XML.")
    else:
        print("El archivo XML no existe.")

# 4. Modificar datos en un archivo XML
def modificar_datos_xml():
    if os.path.exists("archivo.xml"):
        tree = ET.parse("archivo.xml")
        root = tree.getroot()
        
        # Modificar la edad del primer usuario (id="1")
        usuario1 = root.find(".//usuario[@id='1']")
        if usuario1 is not None:
            usuario1.find("edad").text = "31"
        
        # Guardar los cambios en el archivo XML
        tree.write("archivo.xml", encoding="utf-8", xml_declaration=True)
        print("Datos modificados en el archivo XML.")
    else:
        print("El archivo XML no existe.")

# 5. Eliminar un archivo XML
def eliminar_archivo_xml():
    if os.path.exists("archivo.xml"):
        os.remove("archivo.xml")
        print("Archivo XML eliminado.")
    else:
        print("El archivo XML no existe para eliminar.")

# 6. Verificar si el archivo XML existe
def verificar_existencia_xml():
    if os.path.exists("archivo.xml"):
        print("El archivo XML existe.")
    else:
        print("El archivo XML no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_xml():
    crear_archivo_xml()        # Crear y escribir datos en el archivo XML
    leer_archivo_xml()         # Leer y mostrar el contenido
    agregar_datos_xml()        # Agregar nuevos datos
    leer_archivo_xml()         # Leer y mostrar el nuevo contenido
    modificar_datos_xml()      # Modificar datos en el archivo
    leer_archivo_xml()         # Leer y mostrar el archivo modificado
    verificar_existencia_xml() # Verificar si el archivo existe
    eliminar_archivo_xml()     # Eliminar el archivo
    verificar_existencia_xml() # Verificar si el archivo fue eliminado

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_xml()
