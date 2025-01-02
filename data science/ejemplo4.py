import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Paso 1: Cargar el conjunto de datos de imágenes
print("Cargando datos...")
# Usamos un conjunto de datos de ejemplo como el MNIST para la clasificación de dígitos
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Paso 2: Preprocesamiento de los datos
X_train = X_train / 255.0  # Normalización
X_test = X_test / 255.0

# Paso 3: Crear el modelo de red neuronal
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Aplanar las imágenes 28x28 a un vector de 784 elementos
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')  # 10 clases (dígitos del 0 al 9)
])

# Paso 4: Compilar el modelo
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# Paso 5: Entrenar el modelo
model.fit(X_train, y_train, epochs=5)

# Paso 6: Evaluar el modelo
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"\nPrecisión en los datos de prueba: {test_acc}")

# Paso 7: Predicciones
predictions = model.predict(X_test)
plt.imshow(X_test[0], cmap=plt.cm.binary)  # Visualizar la primera imagen de prueba
plt.title(f"Predicción: {np.argmax(predictions[0])}")
plt.show()
