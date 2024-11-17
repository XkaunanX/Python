import pytesseract
import sys
import os
from PIL import Image

# CONECTOR OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# FUNCIONES
def obtener_texto(image, idioma):
    return pytesseract.image_to_string(image, lang=idioma)

# VALIDAR CANTIDAD DE ARGUMENTOS
if len(sys.argv) != 3:
    print("Uso: <imagen> <idioma>")
    exit()

# OBTENER ARGUMENTOS
imagen = sys.argv[1]
idioma = sys.argv[2]

# VALIDAR IMAGEN
if not os.path.isfile(imagen):
    print(f"Error: El archivo '{imagen}' no existe.")
    exit()

# VALIDAR IDIOMA
idiomas = pytesseract.get_languages(config='')
if idioma not in idiomas:
    print(f"Error: El idioma '{idioma}' no es válido. Idiomas disponibles: {', '.join(idiomas)}")
    exit()

# VALIDAR FORMATO
extensiones = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
if not any(imagen.lower().endswith(ext) for ext in extensiones):
    print("Error: El archivo no es una imagen válida (debe tener extensión .jpg, .jpeg, .png, .bmp, .tiff).")
    exit()

# PROCESAR  
try:
    image = Image.open(imagen)
except IOError:
    print(f"Error al abrir la imagen. Asegúrate de que sea un archivo de imagen válido.")
    exit()

# Intentar obtener el texto de la imagen
try:
    string = obtener_texto(image, idioma)
except Exception as e:
    print(f"Error al procesar la imagen con Tesseract: {e}")
    exit()

# Mostrar la salida
if string.strip():
    print("Salida: " + string)
else:
    print("Advertencia: No se pudo extraer texto de la imagen.")