import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# Paso 1: Cargar el dataset
print("Cargando datos...")
data = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/twitter-data/master/Tweets.csv')

# Paso 2: Preparar datos de texto
print("\nLimpieza de texto...")
data['text'] = data['text'].str.replace('[^a-zA-Z0-9\s]', '')  # Eliminar caracteres especiales

# Convertir etiquetas (positivo/negativo) a valores binarios
data['sentiment'] = data['airline_sentiment'].apply(lambda x: 1 if x == 'positive' else 0)

# Paso 3: División de datos
X = data['text']
y = data['sentiment']

# Convertir el texto en características numéricas
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(X)

# División en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Modelo de clasificación
print("\nEntrenando el modelo...")
model = MultinomialNB()
model.fit(X_train, y_train)

# Paso 5: Evaluación del modelo
y_pred = model.predict(X_test)

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# Matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nMatriz de confusión:")
print(conf_matrix)
