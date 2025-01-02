from PIL import Image, ImageDraw, ImageFont
import os

# 1. Abrir una imagen existente
def abrir_imagen():
    try:
        # Abrir una imagen (reemplaza con la ruta de tu imagen)
        imagen = Image.open("imagen_original.jpg")
        imagen.show()
        print("Imagen abierta con éxito.")
    except FileNotFoundError:
        print("La imagen no fue encontrada.")

# 2. Crear una imagen nueva (en blanco)
def crear_imagen():
    # Crear una nueva imagen blanca de tamaño 400x400 píxeles
    imagen = Image.new("RGB", (400, 400), color="white")
    
    # Dibujar un texto en la imagen
    draw = ImageDraw.Draw(imagen)
    font = ImageFont.load_default()  # Fuente por defecto
    draw.text((50, 150), "Hola Mundo!", font=font, fill="black")
    
    # Guardar la imagen
    imagen.save("imagen_creada.jpg")
    imagen.show()
    print("Imagen creada y guardada como 'imagen_creada.jpg'.")

# 3. Modificar una imagen (como redimensionar)
def modificar_imagen():
    try:
        # Abrir la imagen existente
        imagen = Image.open("imagen_original.jpg")
        
        # Redimensionar la imagen a 200x200 píxeles
        imagen_redimensionada = imagen.resize((200, 200))
        
        # Guardar la imagen redimensionada
        imagen_redimensionada.save("imagen_redimensionada.jpg")
        imagen_redimensionada.show()
        print("Imagen redimensionada y guardada como 'imagen_redimensionada.jpg'.")
    except FileNotFoundError:
        print("La imagen no fue encontrada.")

# 4. Guardar una imagen en otro formato
def guardar_imagen_en_otro_formato():
    try:
        # Abrir la imagen existente
        imagen = Image.open("imagen_original.jpg")
        
        # Guardar la imagen en formato PNG
        imagen.save("imagen_convertida.png", "PNG")
        print("Imagen convertida y guardada como 'imagen_convertida.png'.")
    except FileNotFoundError:
        print("La imagen no fue encontrada.")

# 5. Eliminar una imagen
def eliminar_imagen():
    if os.path.exists("imagen_creada.jpg"):
        os.remove("imagen_creada.jpg")
        print("Imagen 'imagen_creada.jpg' eliminada.")
    else:
        print("La imagen 'imagen_creada.jpg' no existe para eliminar.")

# 6. Verificar la existencia de una imagen
def verificar_existencia_imagen():
    if os.path.exists("imagen_original.jpg"):
        print("La imagen 'imagen_original.jpg' existe.")
    else:
        print("La imagen 'imagen_original.jpg' no existe.")

# Ejecutar todas las operaciones en secuencia
def ejecutar_operaciones_imagen():
    abrir_imagen()               # Abrir imagen existente
    crear_imagen()               # Crear nueva imagen
    modificar_imagen()           # Redimensionar imagen existente
    guardar_imagen_en_otro_formato()  # Guardar imagen en otro formato
    eliminar_imagen()            # Eliminar imagen creada
    verificar_existencia_imagen()    # Verificar existencia de imagen

# Llamada a la función principal para ejecutar todas las operaciones
if __name__ == "__main__":
    ejecutar_operaciones_imagen()
