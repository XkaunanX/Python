import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# Importar desde tensorflow.keras
from keras.models import load_model

# Inicializar el lematizador de palabras para reducirlas a su forma base
lematizador = WordNetLemmatizer()

# Cargar la base de datos JSON que contiene las intenciones y respuestas del chatbot
with open('./modelo/base.json', 'r') as archivo:
    base = json.load(archivo)

# Cargar las palabras y etiquetas (tags) que se han almacenado previamente
palabras = pickle.load(open('./binarios/palabras.pkl', 'rb'))
tags = pickle.load(open('./binarios/tags.pkl', 'rb'))

# Cargar el modelo entrenado de Keras que se usará para la predicción
modelo = load_model('./modelo/chatbot.h5')

# Función para limpiar una sentencia (oración) y devolver las palabras lematizadas
def limpiar_sentencia(sentencia):
    # Tokenizar la oración en palabras
    palabras_sentencia = nltk.word_tokenize(sentencia)
    
    # Lematizar cada palabra para convertirla a su raíz o forma base
    palabras_sentencia = [lematizador.lemmatize(palabra) for palabra in palabras_sentencia]
    
    return palabras_sentencia

# Función que convierte una sentencia en un vector de palabras
# (representación en el 'bag of words')
def bag_palabras(sentencia):
    # Limpiar y tokenizar la oración
    palabras_sentencia = limpiar_sentencia(sentencia)
    
    # Crear una lista de ceros con el tamaño de la lista de todas las palabras posibles
    bag = [0]*len(palabras)
    
    # Recorrer las palabras de la sentencia y marcar la posición de cada palabra en la lista de palabras
    for p in palabras_sentencia:
        for i, palabra in enumerate(palabras):
            if palabra == p:
                bag[i] = 1
    return np.array(bag)

# Función para predecir la etiqueta (tag) de la intención de una oración
def predecir_tag(sentencia):
    # Obtener el vector de características de la oración
    bow = bag_palabras(sentencia)
    
    # Hacer la predicción con el modelo cargado
    resultado = modelo.predict(np.array([bow]))[0]
    
    # Encontrar el índice de la etiqueta con el mayor valor de predicción
    max_index = np.where(resultado == np.max(resultado))[0][0]
    
    # Obtener la categoría (etiqueta) correspondiente
    categoria = tags[max_index]
    
    return categoria

# Función que devuelve una respuesta basada en el tag predicho
def get_respuesta(tags, base_json):
    # Obtener la lista de intenciones del JSON
    lista_intenciones = base_json['intenciones']
    
    # Inicializar la respuesta como vacía
    resultado = ""
    
    # Recorrer las intenciones para encontrar una que coincida con el tag
    for i in lista_intenciones:
        if i["tag"] == tags:
            # Seleccionar una respuesta aleatoria de las posibles respuestas
            resultado = random.choice(i['respuesta'])
            break
    return resultado

# Bucle principal para recibir y procesar mensajes del usuario
while True:
    # Solicitar un mensaje al usuario
    mensaje = input("Tu: ")
    
    # Predecir la intención del mensaje
    intencion = predecir_tag(mensaje)
    
    # Obtener la respuesta correspondiente según la intención
    respuesta = get_respuesta(intencion, base)
    
    # Imprimir la respuesta generada por el chatbot
    print("bot: " + respuesta)
