#IMPORTO LA LIBRERIA
import pytesseract

#CONECTOR OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#FUNCIONES
def obtener_texto(image):
    return pytesseract.image_to_string(image)



