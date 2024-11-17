import cv2

# Cargar el clasificador Haar para la detección de caras
cara_haarcascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')

# Captura de video desde la cámara
captura = cv2.VideoCapture(0)

if not captura.isOpened():
    print("Error al acceder a la cámara.")
    exit()

while True:
    # Leer una imagen
    ret, imagen = captura.read()
    if not ret:
        print("Error al capturar imagen.")
        break

    # Convertir la imagen a escala de grises
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar caras en la imagen
    caras = cara_haarcascade.detectMultiScale(grises, scaleFactor=1.1, minNeighbors=5)

    # Dibujar un rectángulo alrededor de las caras detectadas
    for (x, y, w, h) in caras:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar la imagen con las caras detectadas
    cv2.imshow('Imagen', imagen)

    # Salir si se presiona la tecla 'ESC'
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

# Liberar los recursos
captura.release()
cv2.destroyAllWindows()