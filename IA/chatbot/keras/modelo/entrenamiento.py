import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import os

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

# Inicializar lematizador
lematizador = WordNetLemmatizer()

# Cargar la base de datos JSON
with open('./base.json', 'r') as archivo:
    base_datos = json.load(archivo)

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Listas para almacenar datos
palabras = []
tags = []
documentos = []
simbolos_ignorados = ['?', '!', '¿', '¡', '.']

# Procesar cada intención en la base de datos
for intencion in base_datos['intenciones']:
    for patron in intencion['patron']:
        # Tokenizar cada frase del patrón
        palabras_tokenizadas = nltk.word_tokenize(patron)
        palabras.extend(palabras_tokenizadas)
        # Agregar a documentos (patrón, etiqueta)
        documentos.append((palabras_tokenizadas, intencion["tag"]))
        # Agregar la etiqueta si no está en la lista
        if intencion["tag"] not in tags:
            tags.append(intencion["tag"])

# Lematizar y eliminar símbolos ignorados
palabras = [lematizador.lemmatize(palabra) for palabra in palabras if palabra not in simbolos_ignorados]
# Ordenar y eliminar duplicados
palabras = sorted(set(palabras))
tags = sorted(set(tags))

# Crear la carpeta './binarios' si no existe
if not os.path.exists('../binarios'):
    os.makedirs('../binarios')

# Guardar palabras y etiquetas con pickle
pickle.dump(palabras, open('../binarios/palabras.pkl', 'wb'))
pickle.dump(tags, open('../binarios/tags.pkl', 'wb'))

# Preparar datos de entrenamiento
entrenamiento = []
output_vacio = [0] * len(tags)

# Crear bolsas de palabras para cada documento
for documento in documentos:
    bag = []
    palabras_patron = documento[0]
    # Lematizar cada palabra del patrón
    palabras_patron = [lematizador.lemmatize(palabra.lower()) for palabra in palabras_patron]
    # Crear bolsa de palabras
    for palabra in palabras:
        bag.append(1) if palabra in palabras_patron else bag.append(0)
    
    # Crear fila de salida (etiqueta)
    fila_salida = list(output_vacio)
    fila_salida[tags.index(documento[1])] = 1
    entrenamiento.append([bag, fila_salida])

# Mezclar datos y convertir a numpy arrays
random.shuffle(entrenamiento)
entrenamiento = np.array(entrenamiento, dtype=object)

# Separar datos de entrada (X) y salida (Y)
X = np.array(list(entrenamiento[:, 0]))
Y = np.array(list(entrenamiento[:, 1]))

# Definir el modelo de red neuronal
modelo = Sequential()
modelo.add(Dense(128, input_shape=(len(X[0]),), activation='relu'))
modelo.add(Dropout(0.5))
modelo.add(Dense(64, activation='relu'))
modelo.add(Dropout(0.5))
modelo.add(Dense(len(Y[0]), activation='softmax'))

# Definir el optimizador
s = SGD(learning_rate=0.001, decay=1e-6, momentum=0.9, nesterov=True)

# Compilar el modelo
modelo.compile(loss='categorical_crossentropy', optimizer=s, metrics=['accuracy'])

# Entrenar el modelo
proceso_entrenamiento = modelo.fit(X, Y, epochs=100, batch_size=5, verbose=1)

# Guardar el modelo entrenado
modelo.save("chatbot.h5")