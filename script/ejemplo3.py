import os

# Directorio de trabajo
directorio = "/home/usuario/documentos"

# Iterar sobre los archivos .txt en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".txt"):
        old_file = os.path.join(directorio, archivo)
        new_file = os.path.join(directorio, f"nuevo_{archivo}")
        os.rename(old_file, new_file)

print("Los archivos han sido renombrados con el prefijo 'nuevo_'")
